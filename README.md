# ToothVLM Application

口腔健康检测应用 - 集成 DINOv3 视觉识别、LLM 对话和知识库检索。

训练仓库：https://github.com/A1C1NY/dinoV3_ToothVLM  

权重： https://huggingface.co/Kellection/dinoV3-ToothVLM-Sonata

训练使用数据集：https://huggingface.co/datasets/Kellection/sonata-dental-dataset
## 项目结构

```
ToothVLM-App/
├── app/                                    # Web应用
│   ├── backend/                            # FastAPI 后端服务
│   │   ├── main.py                         # 应用入口，API 端点定义
│   │   ├── settings.py                     # 环境变量配置
│   │   ├── database.py                     # SQLite 对话历史存储
│   │   ├── services/
│   │   │   ├── detector.py                 # 牙齿检测推理
│   │   │   ├── periodontal.py              # 牙周炎分类推理
│   │   │   ├── ollama.py                   # Ollama LLM 和 RAG 集成
│   │   │   ├── rag.py                      # RAG 检索和知识库引擎
│   │   │   └── rag_index.py                # RAG 向量索引构建工具
│   │   ├── requirements.txt                # Python 依赖
│   │   └── runtime/                        # 运行时目录（自动创建）
│   │       ├── uploads/                    # 用户上传的图片
│   │       ├── results/                    # 检测结果和标注图像
│   │       ├── rag_index/                  # ChromaDB 向量索引
│   │       └── conversations.sqlite3       # 对话历史数据库
│   ├── frontend/                           # Vue 3 前端应用
│   │   ├── src/                            # 源代码
│   │   ├── package.json                    # npm 依赖
│   │   └── vite.config.js                  # Vite 构建配置
│   ├── scripts/
│   │   ├── launch.py                       # 启动脚本（检查依赖、启动服务）
│   │   └── install_active_conda_command.ps1 # PowerShell 命令安装脚本
│   ├── Oral-Health-Knowledge/              # RAG 知识库（Markdown 文件）
│   └── src/
├── models/                                 # 模型定义和推理代码
│   ├── definitions/
│   │   └── model/
│   │       ├── dinov3_backbone.py          # DINOv3 骨干网络
│   │       └── yolov10_dinov3.py           # YOLOv10 + DINOv3 检测头
│   ├── infer_classifier_periodontal.py    # 牙周炎分类推理
│   ├── train_classifier_periodontal.py    # 牙周炎分类训练
│   ├── config/                             # 模型配置文件
│   └── utils/                              # 工具函数
├── dinov3/                                 # DINOv3 骨干网络源代码（Meta 开源）
├── services/                               # 独立推理服务工具
├── res_checkpoints/                        # 模型权重（需要从训练仓库链接或复制）
├── knowledge/                              # 额外知识库资源
└── lm_studio_integration.py                # LM Studio 集成示例（可选）
```

## 系统要求

- **操作系统**: Windows 11 / macOS / Linux
- **Python**: 3.9+
- **Node.js**: 16+
- **CUDA**: 11.8+（推荐用于 GPU 加速；CPU 模式需修改配置）
- **内存**: 16GB+ RAM（带 GPU）或 32GB+（CPU 模式）
- **磁盘**: 20GB+ 自由空间

## 前置依赖

### 1. Conda 环境

使用训练仓库 https://github.com/A1C1NY/dinoV3_ToothVLM 的 `dino_VLM` 环境。如果没有，可从训练仓库复制或基于 CUDA 版本创建：

```bash
# 查看现有环境
conda env list

# 激活环境
conda activate dino_VLM
```

### 2. 模型权重

模型权重需要从训练仓库获取。  

可以从 https://huggingface.co/Kellection/dinoV3-ToothVLM-Sonata 直接下载已经训练的权重，也可以使用 https://github.com/A1C1NY/dinoV3_ToothVLM 自主训练

在 PowerShell（**管理员权限**）执行：

```powershell
New-Item -ItemType SymbolicLink -Path "res_checkpoints" -Target "YOUR_PATH"
```

也可以直接下载到本仓库 `res_checkpoints/`位置下 。

### 3. Ollama（LLM 和文本嵌入）

**Ollama** 提供本地 LLM 推理和文本向量化服务。

#### 安装 Ollama

下载并安装：https://ollama.com/

#### 下载所需模型

打开终端执行以下命令：

```bash
# 对话 LLM 模型（可选择不同型号）
ollama pull qwen3.5:9b      # 默认，平衡性能和质量（约 5GB）
# 或其他选项：
# ollama pull qwen3.8:27b   # 更强大但更慢（约 16GB）
# ollama pull llama3:8b     # 开源替代方案（约 4GB）
# ollama pull mistral       # 更快但精度略低（约 4GB）

# 文本嵌入模型（用于 RAG 知识库检索）
ollama pull bge-m3          # 多语言向量化模型（推荐，约 2GB）
# 或其他选项：
# ollama pull nomic-embed-text  # 英文优化（约 900MB）
```

验证模型已加载：

```bash
ollama list
```

预期输出类似：
```
NAME                  ID              SIZE     MODIFIED
qwen3.5:9b           ...             5.1 GB   2 hours ago
bge-m3               ...             2.3 GB   1 hour ago
```

### 4. Node.js（前端）

下载并安装最新 LTS：https://nodejs.org/

验证安装：

```bash
node --version
npm --version
```

## 安装步骤

### 1. 克隆/获取仓库

```bash
git clone <repository-url>
cd ToothVLM-App
```

### 2. 激活 Conda 环境

```bash
conda activate dino_VLM
```

验证当前环境：

```bash
python --version
which python  # Linux/macOS
# 或 where python  # Windows
```

### 3. 安装 Python 依赖

```bash
python -m pip install -r app/backend/requirements.txt
```

依赖包括：

- **fastapi** (≥0.115) - 高性能 Web 框架
- **uvicorn** (≥0.30) - ASGI 应用服务器
- **python-multipart** - 文件上传支持
- **openai** (≥1.0) - Ollama 兼容 SDK
- **chromadb** - 向量数据库（RAG 存储）
- **PyYAML** - 知识库元数据解析

### 4. 安装前端依赖

```bash
npm --prefix app/frontend install
```

### 5. 构建 RAG 知识库索引（可选但推荐）

首先确保 Ollama 已启动并加载了 `bge-m3` 模型。

```bash
python -m app.backend.services.rag_index \
  --kb app/Oral-Health-Knowledge \
  --index-dir app/backend/runtime/rag_index \
  --model bge-m3 \
  --ollama-url http://127.0.0.1:11434/v1/
```

输出示例：
```
共生成 147 个 chunk（来自 12 个文件），开始嵌入…
  16/147
  32/147
  ...
完成。集合 oral_health 共 147 条。
索引持久化在：app/backend/runtime/rag_index
嵌入模型：bge-m3
```

如果跳过此步骤，RAG 功能将自动禁用（应用会正常运行，但无法检索知识库）。

## 启动应用

### 方式 1：使用启动脚本（推荐）

在 PowerShell 中执行一次性设置（如果未做过）：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\app\scripts\install_active_conda_command.ps1
```

然后启动应用：

```powershell
tooth_vlm
```

应用会自动：
1. 检查 Python 和 npm 依赖
2. 验证 Ollama 连接和模型可用性
3. 启动 FastAPI 后端（端口 8000）
4. 启动 Vue 前端开发服务器（端口 5173）
5. 在浏览器打开 http://127.0.0.1:5173

### 方式 2：手动启动（开发/调试）

#### 启动后端

在项目根目录开启一个终端：

```bash
conda activate dino_VLM
python -m uvicorn app.backend.main:app --host 127.0.0.1 --port 8000 --reload
```

#### 启动前端

在另一个终端：

```bash
cd app/frontend
npm run dev -- --host 127.0.0.1
```

然后访问 http://127.0.0.1:5173

## 配置

### 环境变量

在启动前设置以下环境变量来自定义应用行为：

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `TOOTH_VLM_MODEL` | `qwen3.5:9b` | 对话 LLM 模型名（Ollama 中的模型）|
| `TOOTH_VLM_EMBED_MODEL` | `bge-m3` | 文本嵌入模型名（用于 RAG）|
| `TOOTH_VLM_MAX_HISTORY` | `30` | 对话历史消息数（越多越消耗内存）|
| `TOOTH_VLM_DEVICE` | `auto` | 推理设备：`auto`（自动选择 cuda → mps → cpu）/ `cuda` / `mps` / `cpu`（Apple Silicon 上自动使用 MPS 加速）|
| `OLLAMA_URL` | `http://127.0.0.1:11434/v1/` | Ollama 服务地址 |

#### 示例：选择不同的 LLM 模型

```powershell
# Windows PowerShell
$env:TOOTH_VLM_MODEL = "llama3:8b"
tooth_vlm

# Linux/macOS bash
export TOOTH_VLM_MODEL="llama3:8b"
tooth_vlm
```

#### 示例：使用远程 Ollama 服务

```bash
export OLLAMA_URL="http://192.168.1.100:11434/v1/"
tooth_vlm
```

### 模型选择建议

#### 对话 LLM（TOOTH_VLM_MODEL）

| 模型 | 大小 | 速度 | 质量 | 推荐场景 |
|------|------|------|------|---------|
| `qwen3.5:9b` | ~5GB | ⚡⚡ | ⭐⭐⭐⭐ | **默认选择**，中文优化 |
| `qwen3.8:27b` | ~16GB | ⚡ | ⭐⭐⭐⭐⭐ | 高精度需求，需要好的 GPU |
| `llama3:8b` | ~4GB | ⚡⚡⚡ | ⭐⭐⭐ | 资源受限，开源首选 |
| `mistral` | ~4GB | ⚡⚡⚡ | ⭐⭐⭐ | 速度优先 |

#### 文本嵌入模型（TOOTH_VLM_EMBED_MODEL）

| 模型 | 大小 | 支持语言 | 推荐 |
|------|------|---------|------|
| `bge-m3` | ~2GB | 中文/英文/100+ 语言 | ✅ **推荐**，多语言最强 |
| `nomic-embed-text` | ~900MB | 英文为主 | 英文数据集优先 |

## API 文档

### 健康检查

```http
GET /api/health
```

返回 Ollama 连接状态和可用模型列表。

### 创建对话

```http
POST /api/conversations
Content-Type: application/json

{
  "title": "我的对话"
}
```

### 发送消息（支持图片上传）

```http
POST /api/conversations/{conversation_id}/messages
Content-Type: multipart/form-data

prompt=请分析我的牙齿&images=<file1>&images=<file2>
```

工作流程：
1. 上传图片 → 自动检测牙齿并生成注解图像和检测报告
2. 检测报告 + 用户提示 → RAG 检索相关知识
3. 知识库 + 对话历史 → LLM 生成对话响应

## 故障排除

### Ollama 连接失败

```
无法连接 Ollama 服务
```

**解决方案**：

```bash
# 1. 确保 Ollama 已启动
ollama serve  # 在另一个终端运行

# 2. 验证连接
curl http://127.0.0.1:11434/api/tags

# 3. 如果使用远程 Ollama，检查 URL 和网络连通性
```

### 模型未加载

```
Ollama 中没有本地模型。请先运行 ollama pull qwen3:8b。
```

**解决方案**：

```bash
# 下载默认模型
ollama pull qwen3.5:9b

# 或手动指定
export TOOTH_VLM_MODEL="llama3:8b"
ollama pull llama3:8b
tooth_vlm
```

### RAG 知识库检索失败

```
RAG 检索失败: ...
```

**解决方案**：

```bash
# 1. 检查知识库文件是否存在
ls app/Oral-Health-Knowledge/*.md

# 2. 重建索引
python -m app.backend.services.rag_index

# 3. 如果仍然失败，应用会自动禁用 RAG（无影响）
```

### 前端无法连接后端

```
GET http://127.0.0.1:8000/api/health 404
```

**解决方案**：

```bash
# 1. 检查后端是否启动
curl http://127.0.0.1:8000/api/health

# 2. 检查 CORS 配置（检查后端 main.py 的 CORSMiddleware）

# 3. 确保前端访问的是正确的 URL（应该是 127.0.0.1:5173）
```

### CUDA 内存不足 / 显存不足

**解决方案**：设置 `TOOTH_VLM_DEVICE` 切换到 CPU（或 Apple Silicon 上改用 MPS）：

```bash
# 强制使用 CPU
export TOOTH_VLM_DEVICE="cpu"

# Apple Silicon 上使用 MPS（默认 auto 已自动选择）
export TOOTH_VLM_DEVICE="mps"
```

## 开发说明

### 仓库分离

- **训练仓库** `dinoV3_ToothVLM` - 模型训练、数据处理、研究代码
- **应用仓库** `ToothVLM-App` (本仓库) - 推理和 Web 应用

### 修改检测模型

如果在训练仓库训练了新模型：

1. 在训练仓库保存 checkpoint
2. 更新应用仓库权重路径（见 [app/backend/services/detector.py](app/backend/services/detector.py)）
3. 如果架构改变，同步更新 [models/definitions/](models/definitions/)

### 更新知识库

1. 在 `app/Oral-Health-Knowledge/` 中添加 Markdown 文件（支持 YAML frontmatter）
2. 重建索引：`python -m app.backend.services.rag_index`
3. 重启后端使索引生效

### 本地测试

```bash
# 运行后端单元测试（如果有）
pytest app/backend/

# 运行前端检查
npm --prefix app/frontend run build
```

## 相关链接

- **训练仓库**: d:\File\Programming\Tooth_VLM\dinoV3_ToothVLM
- **Ollama**: https://ollama.com/
- **FastAPI 文档**: https://fastapi.tiangolo.com/
- **Vue 3 文档**: https://vuejs.org/
- **ChromaDB 文档**: https://docs.trychroma.com/

## License

本项目使用 [DINOv3](https://github.com/facebookresearch/dinov3) 视觉骨干网络（由 Meta 开源），许可证见 [LICENSE.md](LICENSE.md)。

应用代码和衍生作品遵循 MIT 许可证，但必须遵守 DINOv3 的许可条款。详见 [LICENSE.md](LICENSE.md)。

## 致谢

本项目基于 [DINOv3](https://github.com/facebookresearch/dinov3)（Meta Platforms, Inc.）构建，感谢 Meta 开源的优秀视觉模型。
