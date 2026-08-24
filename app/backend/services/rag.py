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

def _add_bilingual_terms(query: str) -> str:
    """
    为查询添加双语关键词，提升跨语言检索效果。

    策略：检测查询语言，添加对应语言的常见术语翻译。
    """
    # 简单的中英文术语对照表
    cn_to_en = {
        "龋齿": "caries dental decay",
        "龋病": "caries",
        "牙周炎": "periodontitis",
        "牙龈炎": "gingivitis",
        "牙结石": "calculus tartar",
        "牙菌斑": "plaque",
        "牙龈出血": "gingival bleeding",
        "牙龈红肿": "gingival inflammation swelling",
        "牙龈退缩": "gingival recession",
        "预防": "prevention prevent",
        "治疗": "treatment therapy",
        "窝沟封闭": "sealants pit fissure sealant",
        "氟化物": "fluoride",
        "根管治疗": "root canal endodontic",
        "种植牙": "implant dental implant",
    }

    en_to_cn = {
        "caries": "龋齿 龋病",
        "decay": "龋坏 腐蚀",
        "periodontitis": "牙周炎",
        "gingivitis": "牙龈炎",
        "calculus": "牙结石",
        "tartar": "牙结石",
        "plaque": "牙菌斑",
        "bleeding": "出血",
        "recession": "退缩",
        "prevention": "预防",
        "prevent": "预防",
        "treatment": "治疗",
        "therapy": "治疗",
        "sealant": "窝沟封闭",
        "fluoride": "氟化物 氟",
        "implant": "种植体 植入",
    }

    query_lower = query.lower()
    added_terms = []

    # 检测是否为中文查询
    has_chinese = any("一" <= c <= "鿿" for c in query)

    if has_chinese:
        # 中文查询，添加英文术语
        for cn, en in cn_to_en.items():
            if cn in query:
                added_terms.append(en)
    else:
        # 英文查询，添加中文术语
        for en, cn in en_to_cn.items():
            if en in query_lower:
                added_terms.append(cn)

    if added_terms:
        return query + " " + " ".join(added_terms)
    return query

def _merge_results(result1: dict, result2: dict) -> dict:
    """
    合并两个 chromadb 查询结果，去重并保留最高分。

    返回格式与 chromadb query 结果相同。
    """
    # 使用 ID 去重（通过文本内容作为唯一标识）
    seen = {}

    for doc, meta, dist in zip(result1["documents"][0],
                               result1["metadatas"][0],
                               result1["distances"][0]):
        key = doc[:100]  # 用前100字符作为唯一标识
        if key not in seen or dist < seen[key][2]:
            seen[key] = (doc, meta, dist)

    for doc, meta, dist in zip(result2["documents"][0],
                               result2["metadatas"][0],
                               result2["distances"][0]):
        key = doc[:100]
        if key not in seen or dist < seen[key][2]:
            seen[key] = (doc, meta, dist)

    # 按距离排序（距离越小越相关）
    sorted_results = sorted(seen.values(), key=lambda x: x[2])

    # 重新组装成 chromadb 格式
    return {
        "documents": [[r[0] for r in sorted_results]],
        "metadatas": [[r[1] for r in sorted_results]],
        "distances": [[r[2] for r in sorted_results]],
    }

def retrieve(query: str, top_k: int = 8, detector_report: str = "", cross_lingual: bool = True) -> list[dict]:
    """
    返回 [{text, score, metadata}, ...]，score 为余弦相似度（越高越相关）。

    Params:
        query: string, 检索词
        top_k: int, 需返回的最近匹配数量
        detector_report: str, 检测器返回结果
        cross_lingual: bool, 是否启用跨语言检索（混合中英文结果）

    Returns:
        一个由字典组成的list, 包含文本，匹配分数，文件数据
    """
    search_text = build_search_query(query, detector_report)

    if cross_lingual:
        # 跨语言检索：使用双语查询策略
        # 1. 原始查询检索 top_k 条
        qvec = _embed(search_text)
        result1 = _get_collection().query(
            query_embeddings=[qvec],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )

        # 2. 添加双语关键词再检索 top_k 条
        bilingual_terms = _add_bilingual_terms(search_text)
        qvec2 = _embed(bilingual_terms)
        result2 = _get_collection().query(
            query_embeddings=[qvec2],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )

        # 3. 合并去重，保留最高分
        merged = _merge_results(result1, result2)

        # 4. 重新排序并返回 top_k
        out = []
        for doc, meta, dist in zip(merged["documents"][0][:top_k],
                                   merged["metadatas"][0][:top_k],
                                   merged["distances"][0][:top_k]):
            out.append({
                "text": doc,
                "score": round(1.0 - dist, 4),
                "metadata": meta,
            })
        return out
    else:
        # 单语言检索（原始逻辑）
        qvec = _embed(search_text)
        result = _get_collection().query(
            query_embeddings=[qvec],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )

        out = []
        for doc, meta, dist in zip(result["documents"][0],
                                   result["metadatas"][0],
                                   result["distances"][0]):
            out.append({
                "text": doc,
                "score": round(1.0 - dist, 4),
                "metadata": meta,
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