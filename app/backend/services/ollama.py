from __future__ import annotations

from openai import OpenAI

from ..settings import settings
from .rag import retrieve, results_to_markdown


SYSTEM_PROMPT = """你是 Tooth VLM 口腔健康对话助手。请用中文回答，表达清晰、克制。
当上下文中存在"检测工具结果"时，结合它解释结果，但必须说明这只是辅助筛查，不替代牙科医生诊断。
当上下文中存在"知识库参考"时，优先使用其中的专业知识回答用户问题，确保信息准确性。
不要捏造未提供的检测发现。用户可以继续追问同一张图或此前结果。"""


def _truncate_rag_context(rag_text: str, max_chars: int = 1500) -> str:
    """
    裁剪 RAG 知识库内容，避免上下文过长。
    保留标题和前 max_chars 字符，确保每条参考都有内容。
    """
    if len(rag_text) <= max_chars:
        return rag_text

    lines = rag_text.split("\n\n")
    result = [lines[0]]  # 保留 "[知识库参考]" 标题
    current_len = len(lines[0])

    for line in lines[1:]:
        # 每条参考至少保留标题和前 200 字符
        if "[" in line and "]" in line:  # 是新的参考条目
            if current_len + 200 > max_chars:
                break
            truncated = line[:400] + "..." if len(line) > 400 else line
            result.append(truncated)
            current_len += len(truncated)
        elif current_len + len(line) <= max_chars:
            result.append(line)
            current_len += len(line)

    return "\n\n".join(result)


class OllamaService:
    def __init__(self) -> None:
        self.client = OpenAI(base_url=settings.ollama_url, api_key="ollama")

    def list_models(self) -> list[str]:
        return [model.id for model in self.client.models.list().data]

    def selected_model(self) -> str:
        models = self.list_models()
        if settings.model:
            if settings.model not in models:
                raise RuntimeError(f"配置的模型 {settings.model} 未安装到 Ollama。")
            return settings.model
        if not models:
            raise RuntimeError("Ollama 中没有本地模型。请先运行 ollama pull qwen3:8b。")
        return models[0]

    def respond(self, history: list[dict], use_rag: bool = True) -> tuple[str, str]:
        """
        生成对话响应，可选地使用 RAG 增强。

        Args:
            history: 对话历史
            use_rag: 是否启用 RAG 知识库检索

        Returns:
            (响应内容, 模型名称)
        """
        model = self.selected_model()
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        # RAG 增强：检索相关知识并注入上下文
        if use_rag and history:
            try:
                # 获取最后一条用户消息作为查询
                last_user_msg = next(
                    (msg for msg in reversed(history) if msg["role"] == "user"),
                    None
                )
                if last_user_msg:
                    query = last_user_msg["content"]
                    # 提取检测报告(如果存在)
                    detector_report = ""
                    if "[检测工具结果]" in query:
                        parts = query.split("[检测工具结果]")
                        query = parts[0].strip()
                        detector_report = parts[1].strip() if len(parts) > 1 else ""

                    # 检索相关知识
                    results = retrieve(
                        query=query,
                        top_k=3,  # 减少到 3 条，避免上下文过长
                        detector_report=detector_report,
                        cross_lingual=True
                    )

                    # 如果检索到相关知识，注入到历史中
                    if results and results[0]["score"] > 0.3:  # 相似度阈值
                        rag_context = results_to_markdown(results)
                        # 裁剪过长的知识库内容（每条最多 400 字符）
                        rag_context = _truncate_rag_context(rag_context, max_chars=1500)
                        # 在用户最后一条消息后插入知识库上下文
                        enhanced_history = history[:-1] + [
                            {
                                "role": "user",
                                "content": f"{last_user_msg['content']}\n\n{rag_context}"
                            }
                        ]
                        messages.extend(enhanced_history)
                    else:
                        messages.extend(history)
                else:
                    messages.extend(history)
            except Exception as e:
                # RAG 失败时降级到普通对话
                print(f"RAG 检索失败: {e}")
                messages.extend(history)
        else:
            messages.extend(history)

        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.4,
            max_tokens=8192,  # 增加最大生成长度
        )
        content = response.choices[0].message.content
        finish_reason = response.choices[0].finish_reason

        # 调试信息：检查为什么停止生成
        if finish_reason == "length":
            print(f"[警告] 模型达到 max_tokens 限制，输出可能被截断")
        elif finish_reason != "stop":
            print(f"[警告] 模型异常停止: {finish_reason}")

        return (content or "模型没有返回文本。", model)


ollama_service = OllamaService()
