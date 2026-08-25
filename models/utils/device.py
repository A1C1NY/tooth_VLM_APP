"""跨平台推理设备选择工具。

在 NVIDIA GPU (CUDA)、Apple Silicon (MPS) 与纯 CPU 环境之间自动选择最合适的
推理设备，也支持通过参数显式指定。所有推理入口（检测器、分类器、Web 服务）
统一从这里解析设备，避免各文件各自判断导致不一致。
"""

from __future__ import annotations

import torch


def resolve_device(device: str = "auto") -> torch.device:
    """解析推理设备。

    Args:
        device: "auto"（默认，按 cuda -> mps -> cpu 顺序自动选择）或显式的
            "cuda" / "mps" / "cpu"（等价于 torch.device 的合法取值）。

    Returns:
        选定的 torch.device。

    Examples:
        >>> resolve_device()              # 在 Apple Silicon 上返回 mps
        >>> resolve_device("auto")        # 同上
        >>> resolve_device("cpu")         # 强制使用 CPU
    """
    if device != "auto":
        return torch.device(device)
    if torch.cuda.is_available():
        return torch.device("cuda")
    if getattr(torch.backends, "mps", None) is not None and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")
