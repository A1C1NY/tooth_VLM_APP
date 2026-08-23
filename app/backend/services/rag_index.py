from __future__ import annotations

import os
import re
from pathlib import Path
import sys
import yaml

# 必须在导入 chromadb 之前禁用 telemetry
os.environ["ANONYMIZED_TELEMETRY"] = "False"

import chromadb
import argparse

from openai import OpenAI

# ---------------------------------------------------------------------------
# 路径与默认配置
# ---------------------------------------------------------------------------

BACKEND_DIR = Path(__file__).resolve().parents[1]            # app/backend
APP_DIR = BACKEND_DIR.parent                                  # app
KB_DIR = APP_DIR / "Oral-Health-Knowledge"
INDEX_DIR = BACKEND_DIR / "runtime" / "rag_index"

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/v1/")
DEFAULT_EMBED_MODEL = os.getenv("TOOTH_VLM_EMBED_MODEL", "bge-m3")
COLLECTION_NAME = "oral_health"

# 可能需要根据实际情况调整切块参数（token 为估计值）
# bge-m3 理论上下文长度：8192 tokens
# 但 Ollama 实现中实际限制约 512 tokens，需保守设置
DEFAULT_MIN_TOKENS = 200
DEFAULT_MAX_TOKENS = 400  # 留 20% 安全余量
DEFAULT_OVERLAP_TOKENS = 80


_CJK_RE = re.compile(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]")# 主要汉字-标点符号-全角字符
_LATIN_RE = re.compile(r"[A-Za-z0-9]+") # 大写-小写-数字（标点不单独算）

_CJK_MULTIPLIER = 1
_LATIN_RE_MULTIPLIER = 1.3


def estimate_tokens(text:str) -> int:
    """
    估计text语段的token数量
    
    Params:
        text: 输入的text语段

    Returns:
        int, 估计的token数
    
    """
    cjk = len(_CJK_RE.findall(text))
    latin = len(_LATIN_RE.findall(text))

    return cjk * _CJK_MULTIPLIER + int(latin * _LATIN_RE_MULTIPLIER) + 10

def _overlap_tail(text: str, overlap_tokens: int) -> str:
    """
    取 text 尾部约 overlap_tokens 的内容，尽量断在句末，用作下一个 chunk 的开头。

    Params:
        text: 输入的text语段
        overlap_tokens: 重合部分

    Returns:
        int, 估计的token数
    """
    if estimate_tokens(text) <= overlap_tokens:
        return text
    # 混合文本粗略按 3.5 字符/token 估算长度
    tail = text[-int(overlap_tokens * 3.5):]
    m = re.search(r"[.!?。！？]\s", tail)
    if m:
        tail = tail[m.end():]
    return tail.lstrip()

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """拆分 frontmatter 与正文，返回 (元数据 dict, 正文 str)。

    知识库格式：
        ---
        title: "..."
        source: ...
        url: ...
        topic: ...
        ---
        正文...
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close = i
            break
    if close is None:
        return {}, text
    try:
        meta = yaml.safe_load("\n".join(lines[1:close])) or {}
    except yaml.YAMLError:
        meta = {}
    body = "\n".join(lines[close + 1:]).strip()
    return (meta if isinstance(meta, dict) else {}), body

def split_by_sections(body: str) -> list[tuple[str, str]]:
    """按 "## " 标题把正文切成 [(标题, 内容)]；无标题的归入 ("", 内容)。"""
    sections: list[tuple[str, str]] = []
    heading, buf = "", []

    def flush() -> None:
        content = "\n".join(buf).strip()
        if content:
            sections.append((heading, content))

    for line in body.splitlines():
        if line.startswith("## "):
            flush()
            heading, buf = line, [line]
        else:
            buf.append(line)
    flush()
    return sections

def _split_long(text: str, max_tokens: int, overlap_tokens: int) -> list[str]:
    """
    把超过 max_tokens 的单个段落按句子继续切，带重叠。
    如果单个句子仍然超长，则强制按字符切分。

    Params:
        text: 输入的text语段
        max_tokens: 最长token数
        overlap_tokens: 允许的最大重叠tokens

    Returns:
        chunks: 一个list,返回语段区块
    """
    sentences = re.split(r"(?<=[.!?。！？])\s+", text)
    chunks: list[str] = []
    curr = ""

    for sentence in sentences:
        sent_tokens = estimate_tokens(sentence)

        # 如果单个句子就超过 max_tokens，强制按字符切分
        if sent_tokens > max_tokens:
            if curr:
                chunks.append(curr)
                curr = ""
            # 按字符强制切分超长句子
            # 粗略估算：每个 token 约 2-3 个字符（中英混合）
            chars_per_chunk = int(max_tokens * 2.5)
            for i in range(0, len(sentence), chars_per_chunk):
                chunk = sentence[i:i + chars_per_chunk]
                if chunk:
                    chunks.append(chunk)
            continue

        if not curr:
            curr = sentence
        elif estimate_tokens(curr) + sent_tokens <= max_tokens:
            curr += " " + sentence
        else:
            chunks.append(curr)
            curr = _overlap_tail(curr, overlap_tokens) + " " + sentence

    if curr:
        chunks.append(curr)

    return chunks

def chunk_section(section: str, min_tokens: int, max_tokens: int, overlap_tokens: int) -> list[str]:
    """
    对单个章节分块，先聚落到到 max_tokens，超长段落再按句子切。

    Params:
        section: 章节分块、
        min_tokens: 
        max_tokens:
        overlap_tokens:

    Returns:
        out: 一份list
    """

    if estimate_tokens(section) <= max_tokens:
        return [section]

    chunks: list[str] = []
    curr = ""
    for para in re.split(r"\n\s*\n", section):
        para = para.strip()
        if not para:
            continue
        if estimate_tokens(para) > max_tokens:
            if curr: # 单段落就超长，先把当前结束，再强制切割
                chunks.append(curr)
                curr = ""
            chunks.extend(_split_long(para, max_tokens, overlap_tokens))
            continue
        if not curr:
            curr = para
        elif estimate_tokens(curr) + estimate_tokens(para) <= max_tokens:
            curr += "\n\n" + para
        else:
            chunks.append(curr)
            curr = _overlap_tail(curr, overlap_tokens) + "\n\n" + para
    if curr:
        chunks.append(curr)
    return chunks

def embed_batch(client: OpenAI, texts: list[str], model: str) -> list[list[float]]:
    """用 Ollama 的 OpenAI 兼容 /v1/embeddings 批量生成向量。"""
    resp = client.embeddings.create(model=model, input=texts)
    ordered = sorted(resp.data, key=lambda item: item.index)
    return [item.embedding for item in ordered]


def build_index(args: argparse.Namespace) -> None:
    """


    """
    index_dir = Path(args.index_dir)
    index_dir.mkdir(parents=True, exist_ok=True)

    os.environ["CHROMA_TELEMETRY_DISABLED"] = "true"
    client = chromadb.PersistentClient(path=str(index_dir))
    try:
        client.delete_collection(args.collection)
    except Exception:
        pass
    collection = client.create_collection(
        name=args.collection,
        metadata={"hnsw:space": "cosine"},
    )

    llm = OpenAI(base_url=args.ollama_url, api_key="ollama")

    kb_dir = Path(args.kb)
    md_files = sorted(kb_dir.rglob("*.md"))
    if not md_files:
        print(f"[Warning] 在 {kb_dir} 下没有找到 .md 文件")
        return

    all_docs: list[dict] = []
    global_chunk_id = 0  # 全局唯一的 chunk ID

    for path in md_files:
        rel = path.relative_to(kb_dir).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        meta, body = parse_frontmatter(text)
        if not body:
            continue
        title = meta.get("title") or path.stem
        source = meta.get("source", "")
        url = meta.get("url", "")
        topic = meta.get("topic", "")

        for heading, section in split_by_sections(body):
            for chunk in chunk_section(section, args.min_tokens, args.max_tokens, args.overlap_tokens):
                all_docs.append({
                    "id": f"{rel}::{global_chunk_id}",
                    "text": chunk,
                    "metadata": {
                        "file": rel,
                        "title": str(title),
                        "source": str(source),
                        "url": str(url),
                        "topic": str(topic),
                        "section": heading,
                    },
                })
                global_chunk_id += 1

    total = len(all_docs)
    print(f"共生成 {total} 个 chunk（来自 {len(md_files)} 个文件），开始嵌入…")

    # 检查是否有超长的 chunk
    max_safe_tokens = 512  # bge-m3 理论上 8192，但保守设置 512
    long_chunks = [(i, d, estimate_tokens(d["text"])) for i, d in enumerate(all_docs) if estimate_tokens(d["text"]) > max_safe_tokens]
    if long_chunks:
        print(f"\n[警告] 发现 {len(long_chunks)} 个可能超长的 chunk（估计 >{max_safe_tokens} tokens）：")
        for idx, doc, est_tokens in long_chunks[:5]:  # 只显示前 5 个
            print(f"  #{idx}: {doc['id']} - 估计 {est_tokens} tokens, 实际字符数 {len(doc['text'])}")
        print(f"  继续处理中...\n")

    batch_size = args.batch_size
    for i in range(0, total, batch_size):
        batch = all_docs[i:i + batch_size]
        try:
            embeddings = embed_batch(llm, [dict["text"] for dict in batch], args.model)
        except Exception as e:
            print(f"\n[错误] 批次 {i}-{i+len(batch)} 失败: {e}")
            print(f"问题 chunk:")
            for idx, d in enumerate(batch):
                est = estimate_tokens(d["text"])
                print(f"  {i+idx}: {d['id']} - 估计 {est} tokens, 字符数 {len(d['text'])}")
            raise

        collection.add(
            ids=[d["id"] for d in batch],
            documents=[d["text"] for d in batch],
            embeddings=embeddings,
            metadatas=[d["metadata"] for d in batch],
        )

        done = min(i + batch_size, total)

        print(f"  {done}/{total}")

    print(f"\n完成。集合 {args.collection} 共 {collection.count()} 条。")
    print(f"索引持久化在：{index_dir}")
    print(f"嵌入模型：{args.model}")

def main() -> int:
    parser = argparse.ArgumentParser(description="构建口腔知识库 RAG 向量索引")
    parser.add_argument("--kb", default=str(KB_DIR), help="知识库目录")
    parser.add_argument("--index-dir", default=str(INDEX_DIR), help="chromadb 持久化目录")
    parser.add_argument("--model", default=DEFAULT_EMBED_MODEL, help="Ollama 嵌入模型名")
    parser.add_argument("--collection", default=COLLECTION_NAME, help="chromadb 集合名")
    parser.add_argument("--ollama-url", default=OLLAMA_URL, help="Ollama 地址")
    parser.add_argument("--min-tokens", type=int, default=DEFAULT_MIN_TOKENS)
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    parser.add_argument("--overlap-tokens", type=int, default=DEFAULT_OVERLAP_TOKENS)
    parser.add_argument("--batch-size", type=int, default=16, help="每次嵌入的文本数")
    args = parser.parse_args()

    try:
        build_index(args)
    except Exception as exc:  # noqa: BLE001 —— 脚本入口，统一兜底报错
        print(f"[错误] {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())