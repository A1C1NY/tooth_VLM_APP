# 模型权重目录

此目录用于存放推理所需的模型权重文件。

## 需要的权重文件

应用需要以下两个模型权重：

### 1. 牙齿疾病检测模型
- **路径**: `../res_checkpoints/multi_disease_Sonata_expt_v3_1/best_map.pth`
- **用途**: 检测龋齿、牙结石、口腔溃疡、牙齿变色等疾病


### 2. 牙周炎分类模型
- **路径**: `../res_checkpoints/best_val_acc.pth`
- **用途**: 分类图像是否存在牙周炎


## 验证

权重文件正确放置后，应有以下结构：

```
ToothVLM-App/
├── res_checkpoints/
│   ├── multi_disease_Sonata_expt_v3_1/
│   │   └── best_map.pth          # 检测模型权重
│   └── best_val_acc.pth          # 分类模型权重
```
