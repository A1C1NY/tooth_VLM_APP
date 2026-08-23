from __future__ import annotations

import os
os.environ["ANONYMIZED_TELEMETRY"] = "False"

from pathlib import Path

import chromadb
from openai import OpenAI

BACKEND_DIR = Path(__file__).resolve().parents[1]
INDEX_DIR = BACKEND_DIR / "runtime" / "rag_index"

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/v1/")
EMBED_MODEL = os.getenv("TOOTH_VLM_EMBED_MODEL", "bge-m3")
COLLECTION_NAME = "oral_health"

_collection = None   # 懒加载缓存

KEYWORDS = [
    "龋齿", "龋病", "牙髓炎", "根尖周炎", "牙周炎", "牙周病", "牙龈炎",
    "牙结石", "牙菌斑", "牙龈退缩", "牙龈出血", "牙龈红肿", "牙槽骨吸收",
    "口腔癌", "口腔溃疡", "扁平苔藓", "种植体周围炎", "颞下颌关节", "磨牙症",
    "口臭", "口干", "caries", "periodontitis", "gingivitis", "pulpitis",
    "calculus", "plaque", "recession", "implant", "tmd", "xerostomia",
    "halitosis", "cancer", "mucosa", "abscess",
]

def _get_collection():
    global _collection
    if _collection is not None:
        return _collection

    if not INDEX_DIR.exists():
        raise FileNotFoundError(
            f"索引不存在：{INDEX_DIR}，请先运行 app/backend/services/rag_index.py"
        )
    client = chromadb.PersistentClient(path=str(INDEX_DIR))
    try:
        _collection = client.get_collection(COLLECTION_NAME)
    except Exception as Ec:
        raise RuntimeError(
            f"无法打开集合{COLLECTION_NAME}: {Ec}"
        )

    return _collection

def _embed(text: str) -> list[float]:
    """
    用与建索引相同的模型生成查询向量。
    """
    client = OpenAI(base_url=OLLAMA_URL, api_key="ollama")
    resp = client.embeddings.create(model=EMBED_MODEL, input=[text])
    return resp.data[0].embedding

def extract_keywords(report: str) -> list[str]:
    """从检测报告中抽出词表里命中的关键词，用于拼进检索查询。"""
    lowered = (report or "").lower()
    return [kw for kw in KEYWORDS if kw.lower() in lowered]

def build_search_query(user_prompt: str, detector_report: str = "") -> str:
    """
    检索查询 = 用户文字 + 检测报告关键词。

    Params:
        user_prompt: 用户提示词
        detector_report: 检测器返回结果，可以为空

    Returns:
        out: 查询所用索引
    
    """
    parts = [user_prompt.strip()]
    keywords = extract_keywords(detector_report)
    if keywords:
        parts.append(" ".join(keywords))
    return " ".join(p for p in parts if p)

def retrieve(query: str, top_k: int = 8, detector_report: str = "" ) -> list[dict]:
    """
    返回 [{text, score, metadata}, ...]，score 为余弦相似度（越高越相关）。

    Params:
        query: string, 检索词
        top_k: int, 需返回的最近匹配数量
        detector_report: str, 检测器返回结果

    Returns:
        一个由字典组成的list, 包含文本，匹配分数，文件数据
    """
    search_text = build_search_query(query, detector_report)
    qvec = _embed(search_text)

    result = _get_collection().query(
        query_embeddings=[qvec],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    # chromadb cosine 距离 = 1 - 余弦相似度 → 转成相似度
    out = []
    for doc, meta, dist in zip(result["documents"][0],
                               result["metadatas"][0],
                               result["distances"][0]):
        out.append({
            "text": doc,
            "score": round(1.0 - dist, 4),
            "metadata": meta,          # 含 file/title/source/url/topic/section
        })
    return out

def results_to_markdown(results: list[dict]) -> str:
    """
    把检索结果拼成给 LLM 的 '[知识库参考]' 上下文（带来源，便于溯源）。
    
    Params:
        results: 字典列表，检索出来的结果

    Returns:
        string, markdown的文本
    """
    lines = ["[知识库参考]"]
    for i, r in enumerate(results, 1):
        m = r["metadata"]
        lines.append(
            f"[{i}] 来源: {m.get('title', '')} ({m.get('source', '')})\n"
            f"链接: {m.get('url', '')}\n"
            f"{r['text']}"
        )
    return "\n\n".join(lines)