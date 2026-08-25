"""
简单的牙齿疾病检测工具，供 LLM 调用。

功能：
1. 加载训练好的模型
2. 对输入图片进行推理
3. 在图片上绘制检测框和标签
4. 返回标注图片 + 文字诊断结果
"""

import json
import torch
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from torchvision.transforms.functional import pil_to_tensor
import sys

# 添加项目根目录到路径
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from models.definitions.model.yolov10_dinov3 import build_model
from models.config.config import Config
from models.utils.device import resolve_device


class SimpleToothDetector:
    """简单的牙齿疾病检测器"""

    # 疾病类别配置（与训练时保持一致）
    CATEGORIES = {
        1: {"name": "caries", "display": "龋齿", "color": (0, 255, 0)},
        2: {"name": "calculus", "display": "牙结石", "color": (0, 0, 255)},
        3: {"name": "mouth_ulcer", "display": "口腔溃疡", "color": (255, 165, 0)},
        4: {"name": "tooth_discoloration", "display": "牙齿变色", "color": (0, 255, 255)},
    }

    # 健康建议
    HEALTH_ADVICE = {
        "caries": "建议尽快就诊进行充填治疗，防止龋洞扩大。",
        "calculus": "建议进行专业洗牙，清除牙结石，预防牙周疾病。",
        "mouth_ulcer": "注意口腔卫生，避免刺激性食物，如持续不愈请就医。",
        "tooth_discoloration": "可考虑牙齿美白治疗，建议咨询牙科医生。",
    }

    def __init__(self, checkpoint_path, device="auto"):
        """
        初始化检测器

        Args:
            checkpoint_path: 模型权重路径
            device: 运行设备 (auto/cuda/mps/cpu)，auto 自动选择 cuda -> mps -> cpu
        """
        self.device = resolve_device(device)
        self.checkpoint_path = Path(checkpoint_path)

        if not self.checkpoint_path.exists():
            raise FileNotFoundError(f"模型权重不存在: {checkpoint_path}")

        print(f"🔧 正在加载模型: {self.checkpoint_path.name}")
        print(f"   设备: {self.device}")

        # 加载配置（推理用的固定配置）
        class InferenceConfig(Config):
            REPO_DIR = "."
            IMAGE_DIR = "../Sonata/image"
            TRAIN_JSON = "coco/All_Diseases_Sonata/train.json"
            VAL_JSON = "coco/All_Diseases_Sonata/val.json"
            SINGLE_CAT_ID = None
            OUTPUT_DIR = "inference_output"
            WEIGHTS = "pretrained_checkpoints/dinov3_vitb16_pretrain_lvd1689m-73cec8be.pth"

            DROP_EMPTY = True
            AUG_HFLIP = 0.5
            AUG_AFFINE = 0.7
            AUG_SCALE = 0.25
            AUG_TRANSLATE = 0.10
            AUG_ROTATE = 7.0
            AUG_MIN_BOX_SIZE = 4.0
            AUG_MIN_BOX_KEEP = 0.25
            PAD_VALUE = 114

            MOSAIC_PROB = 0.35
            MOSAIC_CENTER_RANGE = (0.45, 0.55)
            COPY_PASTE_PROB = 0.30
            COPY_PASTE_MAX_BOX_AREA_RATIO = 0.02
            COPY_PASTE_MAX_OBJECTS = 2
            COPY_PASTE_CONTEXT_RATIO = 0.20
            COPY_PASTE_MAX_IOU = 0.10
            OVERSAMPLE_CATEGORY_ID = 3
            OVERSAMPLE_FACTOR = 1.75

            CLIP_GRAD_NORM = 200.0
            BATCH_SIZE = 1
            EPOCHS = 70
            LR = 0.001
            BACKBONE_LR = 0.0001
            WARMUP_EPOCHS = 5
            UNFREEZE_BLOCKS = 6
            DEVICE = str(resolve_device())

            BACKBONE_OUT_INDICES = (5, 8, 11)
            RESUME_CHECKPOINT = None
            START_EPOCH = 1

            IOU_THRESHOLD = 0.5
            SCORE_THRESHOLD = 0.5
            MIN_SIZE = 1200
            MAX_SIZE = 1200
            NUM_CLASSES = 4
            CONF_THRESHOLD = 0.001

            VAL_CLASS_THRESHOLDS = {0: 0.30, 1: 0.30, 2: 0.30, 3: 0.30}
            VAL_CONF_THRESHOLD_DEFAULT = 0.3
            CLASS_WEIGHTS = [1.2, 1.3, 2.5, 1.1]

            DINO_MEAN = (0.485, 0.456, 0.406)
            DINO_STD = (0.229, 0.224, 0.225)
            IMG_SIZE = 768
            NUM_WORKERS = 0
            SEED = 42

        self.cfg = InferenceConfig

        # 构建模型
        self.model = build_model(num_classes=4, config=InferenceConfig)
        self.model.to(self.device)

        # 加载权重
        checkpoint = torch.load(checkpoint_path, map_location=self.device, weights_only=False)
        self.model.load_state_dict(checkpoint['model_state_dict'], strict=False)
        self.model.eval()

        print("✅ 模型加载完成\n")

    def _preprocess_image(self, image_path):
        """预处理图像"""
        image = Image.open(image_path).convert("RGB")
        original_size = image.size

        # Letterbox resize (保持宽高比)
        target_size = 768
        ratio = min(target_size / image.width, target_size / image.height)
        new_width = int(image.width * ratio)
        new_height = int(image.height * ratio)

        image_resized = image.resize((new_width, new_height), Image.BILINEAR)

        # 创建填充画布
        canvas = Image.new("RGB", (target_size, target_size), (114, 114, 114))
        pad_x = (target_size - new_width) // 2
        pad_y = (target_size - new_height) // 2
        canvas.paste(image_resized, (pad_x, pad_y))

        # 转换为张量
        tensor = pil_to_tensor(canvas).float() / 255.0

        return tensor.unsqueeze(0), ratio, pad_x, pad_y, original_size

    @torch.no_grad()
    def detect(self, image_path, confidence_threshold=0.3):
        """
        对图片进行疾病检测

        Args:
            image_path: 图片路径
            confidence_threshold: 置信度阈值

        Returns:
            dict: 包含检测结果的字典
        """
        image_path = Path(image_path)
        if not image_path.exists():
            raise FileNotFoundError(f"图片不存在: {image_path}")

        # 预处理
        tensor, ratio, pad_x, pad_y, original_size = self._preprocess_image(image_path)
        tensor = tensor.to(self.device)

        # 推理
        predictions = self.model(tensor, conf_threshold=confidence_threshold)

        # 解析结果
        detections = []
        if len(predictions) > 0 and len(predictions[0]) > 0:
            for pred in predictions[0].cpu().numpy():
                x1, y1, x2, y2, conf, cls = pred

                # 转换回原图坐标
                x1_orig = (x1 - pad_x) / ratio
                y1_orig = (y1 - pad_y) / ratio
                x2_orig = (x2 - pad_x) / ratio
                y2_orig = (y2 - pad_y) / ratio

                category_id = int(cls) + 1
                category_info = self.CATEGORIES.get(category_id, {})

                detections.append({
                    "disease": category_info.get("name", "unknown"),
                    "display_name": category_info.get("display", "未知"),
                    "confidence": float(conf),
                    "bbox": [float(x1_orig), float(y1_orig), float(x2_orig), float(y2_orig)],
                    "color": category_info.get("color", (128, 128, 128)),
                })

        return {
            "image_path": str(image_path),
            "detections": detections,
            "total_count": len(detections),
        }

    def draw_detections(self, image_path, detections):
        """
        在图片上绘制检测框

        Args:
            image_path: 原始图片路径
            detections: detect() 返回的 detections 列表

        Returns:
            PIL Image (已标注)
        """
        image = Image.open(image_path).convert("RGB")
        draw = ImageDraw.Draw(image)

        # 尝试加载中文字体
        try:
            font = ImageFont.truetype("msyh.ttc", 24)  # Windows 微软雅黑
        except:
            try:
                font = ImageFont.truetype("Arial Unicode.ttf", 24)  # macOS
            except:
                font = ImageFont.load_default()

        for det in detections:
            x1, y1, x2, y2 = det['bbox']
            color = det['color']

            # 绘制边框
            draw.rectangle([x1, y1, x2, y2], outline=color, width=3)

            # 绘制标签
            label_text = f"{det['display_name']} {det['confidence']:.2f}"
            text_bbox = draw.textbbox((x1, y1), label_text, font=font)
            draw.rectangle(
                [text_bbox[0] - 2, text_bbox[1] - 2, text_bbox[2] + 2, text_bbox[3] + 2],
                fill=color
            )
            draw.text((x1, y1), label_text, fill=(255, 255, 255), font=font)

        return image

    def generate_report(self, detections):
        """
        生成诊断报告

        Args:
            detections: detect() 返回的 detections 列表

        Returns:
            str: 文字报告
        """
        if not detections:
            return "✅ 未检测到明显的口腔疾病，口腔状态良好。建议保持定期口腔检查。"

        # 统计各类别数量
        from collections import Counter
        disease_counts = Counter(det['disease'] for det in detections)

        report_lines = ["🦷 口腔健康检测报告", "=" * 50, ""]
        report_lines.append(f"检测到 {len(detections)} 处异常区域:\n")

        for disease_name, count in disease_counts.items():
            # 找到对应的显示名称
            display_name = next(
                (det['display_name'] for det in detections if det['disease'] == disease_name),
                "未知"
            )
            advice = self.HEALTH_ADVICE.get(disease_name, "建议咨询牙科医生。")

            report_lines.append(f"📌 {display_name} (x{count})")
            report_lines.append(f"   {advice}\n")

        report_lines.append("=" * 50)
        report_lines.append("⚠️  本报告仅供参考，请以专业牙医诊断为准。")

        return "\n".join(report_lines)

    def process_image(self, image_path, output_dir=None, save_annotated=True):
        """
        完整的处理流程：加载图片 -> 检测 -> 标注 -> 生成报告

        Args:
            image_path: 输入图片路径
            output_dir: 输出目录（可选）
            save_annotated: 是否保存标注图片

        Returns:
            dict: {
                'detections': {...},
                'annotated_image': '标注图片路径',
                'report': '文字报告',
                'total_count': 检测数量
            }
        """
        image_path = Path(image_path)
        if not image_path.exists():
            raise FileNotFoundError(f"图片不存在: {image_path}")

        # 加载图片
        image = Image.open(image_path).convert('RGB')

        # 检测
        result = self.detect(image_path)
        detections = result['detections']

        # 标注
        annotated_image = self.draw_detections(image_path, detections)

        # 保存
        result = {
            'detections': detections,
            'total_count': result['total_count'],
            'report': self.generate_report(detections)
        }

        if save_annotated:
            if output_dir is None:
                output_dir = image_path.parent / "detection_results"
            else:
                output_dir = Path(output_dir)

            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"{image_path.stem}_annotated.jpg"
            annotated_image.save(output_path, quality=95)
            result['annotated_image'] = str(output_path)
        else:
            result['annotated_image'] = None

        return result


def detect_tooth_diseases(
    image_path: str,
    checkpoint_path: str = None,
    save_output: bool = True
) -> dict:
    """
    Function-calling 接口：检测牙齿疾病

    Args:
        image_path: 图片路径
        checkpoint_path: 模型权重路径（可选，使用默认值）
        save_output: 是否保存标注图片

    Returns:
        dict: {
            'status': 'success' | 'error',
            'detections_count': int,
            'disease_categories': [str, ...],
            'annotated_image_path': str,
            'diagnosis_report': str
        }
    """
    try:
        # 默认权重路径
        if checkpoint_path is None:
            checkpoint_path = (
                PROJECT_ROOT / "res_checkpoints" / "multi_disease_Sonata_expt_v3_1" / "best_map.pth"
            )

        # 初始化检测器（首次调用会加载模型）
        if not hasattr(detect_tooth_diseases, '_detector'):
            detect_tooth_diseases._detector = SimpleToothDetector(checkpoint_path)

        detector = detect_tooth_diseases._detector

        # 处理图片
        result = detector.process_image(image_path, save_annotated=save_output)

        # 提取疾病类别
        disease_categories = [
            detector.CATEGORIES.get(label, {"display": "未知"})['display']
            for label in set(result['detections']['labels'])
        ]

        return {
            'status': 'success',
            'detections_count': result['total_count'],
            'disease_categories': disease_categories,
            'annotated_image_path': result['annotated_image'],
            'diagnosis_report': result['report']
        }

    except Exception as e:
        import traceback
        return {
            'status': 'error',
            'error_message': str(e),
            'traceback': traceback.format_exc()
        }
