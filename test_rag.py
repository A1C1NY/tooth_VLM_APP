"""测试 app/backend/services/rag.py 的检索功能（Phase 2）。

运行（需已激活 dino_VLM 环境，且已完成 Phase 1 建索引）：
    python test_rag.py
"""
import sys
from pathlib import Path

# 让 Python 能找到 app/backend/services 包
BACKEND_DIR = Path(__file__).resolve().parent / "app" / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from services import rag


def has_cjk(text: str) -> bool:
    """粗略判断文本是否含中文。"""
    return any("\u4e00" <= c <= "\u9fff" for c in text)


def cross_lingual_demo() -> None:
    """演示跨语言检索：中文查询能否命中英文文档、英文查询能否命中中文文档。"""
    queries = [
        ("中文查询 → 应能命中英文预防内容", "龋齿如何预防？窝沟封闭和氟化物有用吗？", ""),
        ("英文查询", "How to prevent dental caries? Are fluoride and sealants effective?", ""),
        ("中文查询（牙周炎）", "牙龈出血和牙周炎的关系，怎么治疗？", ""),
    ]
    for label, q, rep in queries:
        results = rag.retrieve(q, top_k=5, detector_report=rep)
        langs = ["中" if has_cjk(r["text"]) else "英" for r in results]
        print(f"\n=== {label} ===")
        print(f"查询: {q}")
        print(f"命中语言分布(top5): {langs}")
        for i, r in enumerate(results, 1):
            m = r["metadata"]
            title = (m.get("title") or "")[:34]
            print(f"   [{i}] {m.get('source','?'):<14} {r['score']:<8} {title}")


def main() -> None:
    # 1) 关键词抽取
    report = "检测到：牙结石沉积、牙龈退缩、疑似牙周炎，建议进一步检查。"
    print("1) extract_keywords ->", rag.extract_keywords(report))

    # 2) 查询构造（用户文字 + 检报告关键词）
    query = "图片里看到牙结石和牙龈红肿，是牙周炎吗？该怎么处理？"
    search = rag.build_search_query(query, report)
    print("2) build_search_query ->", search)

    # 3) 检索
    results = rag.retrieve(query, top_k=3, detector_report=report)
    print(f"\n3) retrieve -> {len(results)} 条命中")
    for i, r in enumerate(results, 1):
        m = r["metadata"]
        print(f"   [{i}] score = {r['score']}")
        print(f"       title  = {m.get('title')}")
        print(f"       source = {m.get('source')}")
        print(f"       url    = {m.get('url')}")
        print(f"       text   = {r['text'][:80]} ...")

    # 4) 拼 LLM 上下文（Phase 3 会用到）
    md = rag.results_to_markdown(results)
    print("\n4) results_to_markdown 前 300 字符:")
    print(md[:300])

    # 5) 跨语言检索演示
    cross_lingual_demo()


if __name__ == "__main__":
    main()
