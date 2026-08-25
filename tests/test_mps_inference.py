"""MPS 推理冒烟测试：验证检测器与牙周炎分类器在 MPS 设备上正常工作。

在无 MPS（非 Apple Silicon）的环境下自动跳过模型推理部分，仅验证设备解析。
用法：
    python tests/test_mps_inference.py
"""
import sys
from pathlib import Path

import torch
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from models.utils.device import resolve_device

print("=" * 60)
print("设备解析测试")
print("=" * 60)
device = resolve_device()
print(f"auto 解析结果: {device}")
print(f"  cuda available: {torch.cuda.is_available()}")
print(f"  mps available : {torch.backends.mps.is_available()}")
print(f"  mps built     : {torch.backends.mps.is_built()}")
assert str(resolve_device("cpu")) == "cpu"
assert str(resolve_device("mps")) == "mps"
if torch.cuda.is_available():
    assert device.type == "cuda"
elif torch.backends.mps.is_available():
    assert device.type == "mps", f"期望 MPS 设备，实际为 {device}"
else:
    assert device.type == "cpu"
print(f"✅ 设备解析正确 (auto -> {device.type})\n")

if not torch.backends.mps.is_available():
    print("MPS 不可用（非 Apple Silicon），跳过模型推理测试。")
    sys.exit(0)

# 生成测试图片
test_image = Image.new("RGB", (800, 600), (200, 180, 160))
test_image_path = PROJECT_ROOT / "test_mps_dummy.jpg"
test_image.save(test_image_path)

print("=" * 60)
print("测试 1: 牙周炎分类器 (MPS)")
print("=" * 60)
try:
    from services.periodontal_classifier_tool import classify_periodontal_disease

    result = classify_periodontal_disease(str(test_image_path))
    print(f"✅ 分类成功: {result.get('prediction')} "
          f"({result.get('confidence', 0):.2%})")
except Exception as exc:
    import traceback
    traceback.print_exc()
    print(f"❌ 分类器失败: {exc}")

print()
print("=" * 60)
print("测试 2: 牙齿疾病检测器 (MPS)")
print("=" * 60)
try:
    from services.tooth_detector_tool import SimpleToothDetector

    detector_ckpt = PROJECT_ROOT / "res_checkpoints" / "multi_disease_Sonata_expt_v3_1" / "best_map.pth"
    detector = SimpleToothDetector(detector_ckpt, device="auto")  # 默认 auto
    print(f"检测器实际设备: {detector.device}")
    assert detector.device.type == "mps", f"期望 MPS，实际 {detector.device}"

    result = detector.process_image(test_image_path, save_annotated=False)
    print(f"✅ 检测成功: 检测到 {result['total_count']} 个目标")
    print(f"   报告: {result['report'][:80]}...")
except Exception as exc:
    import traceback
    traceback.print_exc()
    print(f"❌ 检测器失败: {exc}")

print()
print("=" * 60)
print("测试 3: Web 服务层 (MPS)")
print("=" * 60)
try:
    from app.backend.services.periodontal import periodontal_service
    from app.backend.services.detector import detector_service

    print(f"PeriodontalService 设备: {periodontal_service._device}")
    assert periodontal_service._device.type == "mps"

    analysis = detector_service.analyze(test_image_path)
    print(f"✅ Web 服务检测成功: {analysis['total_count']} 个目标")
    print(f"   牙周炎: {analysis['periodontal']['prediction']} "
          f"({analysis['periodontal']['confidence']:.2%})")
    print(f"   标注图: {analysis['annotated_image']}")
except Exception as exc:
    import traceback
    traceback.print_exc()
    print(f"❌ Web 服务层失败: {exc}")

test_image_path.unlink(missing_ok=True)
print()
print("冒烟测试完成")
