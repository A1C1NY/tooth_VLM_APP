"""端到端测试：加载模型 + 实际推理"""
import sys
from pathlib import Path
from PIL import Image
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

# 创建一个测试图片（随机噪声）
print("生成测试图片...")
test_image = Image.fromarray(np.random.randint(0, 255, (800, 600, 3), dtype=np.uint8))
test_image_path = PROJECT_ROOT / "test_image_dummy.jpg"
test_image.save(test_image_path)
print(f"测试图片已保存: {test_image_path}\n")

print("=" * 60)
print("测试 1: 检测器完整流程（加载 + 推理）")
print("=" * 60)

try:
    from services.tooth_detector_tool import SimpleToothDetector

    detector_checkpoint = PROJECT_ROOT / "res_checkpoints" / "multi_disease_Sonata_expt_v3_1" / "best_map.pth"
    print(f"加载检测器: {detector_checkpoint.name}")
    detector = SimpleToothDetector(detector_checkpoint, device="cpu")
    print("✅ 检测器加载成功\n")

    print("开始推理...")
    result = detector.process_image(test_image_path, save_annotated=False)
    print("✅ 推理成功")
    print(f"   检测到 {result['total_count']} 个目标")
    print(f"   报告: {result['report'][:100]}...\n")

except Exception as e:
    print("❌ 检测器流程失败")
    import traceback
    traceback.print_exc()
    print()

print("=" * 60)
print("测试 2: 分类器完整流程（加载 + 推理）")
print("=" * 60)

try:
    from services.periodontal_classifier_tool import classify_periodontal_disease

    print("开始分类...")
    result = classify_periodontal_disease(str(test_image_path))

    if result['status'] == 'success':
        print("✅ 分类成功")
        print(f"   预测类别: {result['prediction']}")
        print(f"   置信度: {result['confidence']:.2%}\n")
    else:
        print("❌ 分类失败")
        print(f"   错误: {result.get('error_message')}\n")

except Exception as e:
    print("❌ 分类器流程失败")
    import traceback
    traceback.print_exc()
    print()

# 清理测试图片
test_image_path.unlink(missing_ok=True)
print("=" * 60)
print("测试完成（已清理测试图片）")
print("=" * 60)
