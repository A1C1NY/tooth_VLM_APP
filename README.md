# ToothVLM Application

口腔健康检测应用 - 生产级Web应用

## 项目结构

```
ToothVLM-App/
├── app/                          # Web应用
│   ├── backend/                  # FastAPI后端
│   ├── frontend/                 # Vue前端
│   ├── scripts/                  # 启动脚本
│   └── runtime/                  # 运行时数据（上传图片、结果等）
├── services/                     # 推理服务工具
│   ├── tooth_detector_tool.py    # 牙齿疾病检测
│   ├── periodontal_classifier_tool.py  # 牙周炎分类
│   └── function_definitions.py   # LLM Function Calling定义
├── models/                       # 模型定义和配置
│   ├── definitions/              # 模型架构定义
│   ├── config/                   # 模型配置
│   └── infer_classifier_periodontal.py  # 牙周炎推理
├── knowledge/                    # RAG知识库
├── dinov3/                       # DINOv3 Backbone
├── res_checkpoints/              # 模型权重（需要从训练仓库链接/复制）
└── lm_studio_integration.py      # LM Studio集成示例
```

## 快速开始

### 前置要求

1. **Conda环境**: 使用训练仓库的 `dino_VLM` 环境
2. **模型权重**: 从训练仓库获取（见下方说明）
3. **Ollama**: 用于LLM对话功能

### 1. 设置模型权重

**方案A: 符号链接（推荐）**

在 PowerShell（管理员权限）中执行：

```powershell
cd d:\File\Programming\Tooth_VLM\ToothVLM-App
New-Item -ItemType SymbolicLink -Path "res_checkpoints" -Target "d:\File\Programming\Tooth_VLM\dinoV3_ToothVLM\res_checkpoints"
```

**方案B: 复制文件**

详见 [models/weights/README.md](models/weights/README.md)

### 2. 激活环境并安装依赖

```powershell
# 激活conda环境
conda activate dino_VLM

# 安装后端依赖
python -m pip install -r app/backend/requirements.txt

# 安装前端依赖
npm --prefix app/frontend install
```

### 3. 安装启动命令

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\app\scripts\install_active_conda_command.ps1
```

### 4. 启动应用

```powershell
# 确保在dino_VLM环境中
tooth_vlm
```

应用会自动：
- 启动FastAPI后端（端口8000）
- 启动Vue开发服务器（端口5173）
- 打开浏览器访问应用

按 `Ctrl+C` 停止所有服务。

## 配置

### 选择Ollama模型

```powershell
$env:TOOTH_VLM_MODEL = "qwen3:8b"
tooth_vlm
```

如果未设置，应用使用第一个可用的本地模型。

### LM Studio集成

如果想使用LM Studio而不是Ollama：

```powershell
python lm_studio_integration.py
```

确保：
1. LM Studio已启动
2. 已加载模型
3. Server已启动（http://localhost:1234）

## 开发说明

### 仓库分离

- **训练仓库**: `dinoV3_ToothVLM` - 包含所有训练代码、数据处理、模型研究
- **应用仓库**: `ToothVLM-App` (本仓库) - 只包含推理和Web应用

### 依赖更新

应用仓库的依赖已精简，只包含推理和Web服务所需：

- PyTorch（推理）
- FastAPI、Uvicorn（后端）
- Ollama SDK（LLM对话）
- Pillow（图像处理）

训练依赖（数据增强、可视化工具等）已从应用仓库移除。

### 修改模型

如果训练了新模型：

1. 在训练仓库训练并保存checkpoint
2. 更新应用仓库中的权重路径（在 `app/backend/services/detector.py` 或 `periodontal.py`）
3. 如果模型架构改变，同步更新 `models/definitions/` 中的定义

## 故障排除

### 模型加载失败

```
FileNotFoundError: 模型权重不存在
```

检查 `res_checkpoints/` 目录是否正确链接或复制。

### 导入错误

```
ModuleNotFoundError: No module named 'new_dinoyolo_src'
```

所有导入路径已更新为应用仓库结构。如果出现此错误，说明有文件未正确迁移。

### CUDA内存不足

在 `app/backend/services/detector.py` 中修改设备：

```python
self._detector = SimpleToothDetector(checkpoint, device="cpu")
```

## 相关链接

- **训练仓库**: `d:\File\Programming\Tooth_VLM\dinoV3_ToothVLM`
- **Ollama**: https://ollama.com/
- **LM Studio**: https://lmstudio.ai/

## License

MIT License（继承自训练仓库）
