# 快速启动指南

## 第一步：创建模型权重链接

**以管理员权限打开PowerShell**，然后执行：

```powershell
cd d:\File\Programming\Tooth_VLM\ToothVLM-App
.\setup_weights.ps1
```

如果成功，你会看到：
```
✓ 符号链接创建成功!
✓ 检测模型权重: 找到
✓ 分类模型权重: 找到
```

## 第二步：启动应用

```powershell
# 激活环境
conda activate dino_VLM

# 启动
cd d:\File\Programming\Tooth_VLM\ToothVLM-App
tooth_vlm
```

浏览器会自动打开 http://localhost:5173

## 常见问题

### Q: setup_weights.ps1 报错 "需要管理员权限"
**A**: 右键点击PowerShell图标，选择"以管理员身份运行"

### Q: 找不到 tooth_vlm 命令
**A**: 在应用仓库目录运行：
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\app\scripts\install_active_conda_command.ps1
```

### Q: 模型加载失败
**A**: 检查 `res_checkpoints/` 目录是否存在：
```powershell
Test-Path res_checkpoints
```
如果返回 False，需要重新运行 setup_weights.ps1

### Q: 不想用符号链接怎么办？
**A**: 直接复制权重文件：
```powershell
# 创建目录
New-Item -ItemType Directory -Force -Path "res_checkpoints\multi_disease_Sonata_expt_v3_1"

# 复制检测模型
Copy-Item "d:\File\Programming\Tooth_VLM\dinoV3_ToothVLM\res_checkpoints\multi_disease_Sonata_expt_v3_1\best_map.pth" `
          "res_checkpoints\multi_disease_Sonata_expt_v3_1\"

# 复制分类模型
Copy-Item "d:\File\Programming\Tooth_VLM\dinoV3_ToothVLM\res_checkpoints\best_val_acc.pth" `
          "res_checkpoints\"
```

---

详细文档见 [README.md](README.md) 和 [MIGRATION.md](MIGRATION.md)
