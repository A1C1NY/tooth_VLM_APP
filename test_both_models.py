"""测试两个模型能否正常加载"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

print("=" * 60)
print("测试 1: 检测器模型 (Detector)")
print("=" * 60)

detector_checkpoint = PROJECT_ROOT / "res_checkpoints" / "multi_disease_Sonata_expt_v3_1" / "best_map.pth"
print(f"权重路径: {detector_checkpoint}")
print(f"权重存在: {detector_checkpoint.exists()}")
print()

try:
    from services.tooth_detector_tool import SimpleToothDetector
    detector = SimpleToothDetector(detector_checkpoint, device="cpu")
    print("✅ 检测器模型加载成功！\n")
except Exception as e:
    print("❌ 检测器模型加载失败")
    import traceback
    traceback.print_exc()
    print()

print("=" * 60)
print("测试 2: 牙周炎分类器 (Periodontal Classifier)")
print("=" * 60)

classifier_checkpoint = PROJECT_ROOT / "res_checkpoints" / "best_val_acc.pth"
print(f"权重路径: {classifier_checkpoint}")
print(f"权重存在: {classifier_checkpoint.exists()}")
print()

try:
    from models.infer_classifier_periodontal import load_checkpoint
    model, class_names, img_size = load_checkpoint(classifier_checkpoint)
    print(f"✅ 分类器模型加载成功！")
    print(f"   类别: {class_names}")
    print(f"   图像尺寸: {img_size}\n")
except Exception as e:
    print("❌ 分类器模型加载失败")
    import traceback
    traceback.print_exc()
    print()

print("=" * 60)
print("测试完成")
print("=" * 60)
