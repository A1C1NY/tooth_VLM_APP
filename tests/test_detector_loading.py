"""测试检测器能否正常加载"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from services.tooth_detector_tool import SimpleToothDetector

checkpoint_path = PROJECT_ROOT / "res_checkpoints" / "multi_disease_Sonata_expt_v3_1" / "best_map.pth"

print("=" * 60)
print("开始测试模型加载")
print("=" * 60)
print(f"权重路径: {checkpoint_path}")
print(f"权重存在: {checkpoint_path.exists()}")
print()

try:
    detector = SimpleToothDetector(checkpoint_path, device="cpu")
    print("=" * 60)
    print("✅ 模型加载成功！")
    print("=" * 60)
except Exception as e:
    print("=" * 60)
    print("❌ 模型加载失败")
    print("=" * 60)
    import traceback
    traceback.print_exc()
