# 口腔健康知识库 (Oral Health Knowledge Base)

用于「根据口腔图片生成诊疗建议」的 LLM RAG 检索增强的知识库。
全部内容来自公开、合法的官方与学术来源，共 **486 篇 Markdown 文档，约 9.7MB**。

## 目录结构

```
kb/
├── manifest.json          # 全库索引（file / source / bytes）
├── cjdr/                  # 《中华口腔医学研究杂志》CJDR 期刊论文全文 222 篇（2017–2025 各期，期刊官网免费 PDF）
├── pmc/                   # PubMed Central 开放获取综述 61 篇（MeSH 主题检索，含龋病/牙周/口腔癌/种植/正畸等）
├── web/                   # 英文官方机构网页内容（173 篇）
│   ├── ada.org/           # 美国牙科协会：口腔健康主题 + 循证临床指南
│   ├── nidcr.nih.gov/     # 美国国家牙科与颅面研究所：疾病科普
│   ├── msdmanuals.com/    # MSD 诊疗手册：牙科专业+患者章节（含操作步骤）
│   ├── who.int/           # 世界卫生组织：口腔健康主题 + 事实清单
│   └── nhs.uk/            # 英国 NHS：牙齿与牙龈护理指南
├── nidcr_pubs/            # NIDCR 官方出版物手册 25 本（公有领域 PDF 转文本）
├── gov_cn/                # 中国政府公开文件：《中国居民口腔健康指南》《健康口腔行动方案》
└── cndent/                # 中华口腔医学会：专业科普（精选 3 篇）
```

## 内容覆盖

| 类别 | 代表内容 |
|---|---|
| 期刊论文（学术证据） | CJDR 224 篇全文（牙周-正畸联合治疗、龋病、种植、干细胞、口腔癌等）；PMC 61 篇系统综述/Meta 分析 |
| 临床指南与规范 | ADA 循证指南（疼痛管理、抗生素、心内膜炎预防、龋病管理）；中华口腔医学会团标（根管内器械取出、纤维桩粘接、正畸疗效评价）；《中国居民口腔健康指南》 |
| 常见疾病 | 龋齿、牙周病、牙髓炎、口腔癌及癌前病变、口腔黏膜病、颞下颌关节病、磨牙症、口干症、种植体周围炎 |
| 治疗与操作 | 根管治疗、微创拔牙、种植、正畸、麻醉、脓肿引流、牙外伤处理、义齿修复 |
| 日常护理 | 刷牙、牙线、漱口水、氟化物、窝沟封闭、儿童/老年/特殊人群护理 |
| 公共卫生 | WHO 口腔健康战略、健康口腔行动方案、NIDCR 手册 |

## 文件格式

每个 .md 文件带 frontmatter：

```markdown
---
title: "标题"
source: 来源（cjdr / pmc / ada.org / nidcr.nih.gov / msdmanuals.com / who.int / nhs.uk / nidcr (publication) / gov.cn / cndent）
url: 原始链接
topic: 主题分类（pmc 专有，如 caries/periodontal/implant）
---

正文内容（Markdown）
```

- `cjdr/`：期刊 PDF 全文经 pdftotext 流式提取，文件名为 `序号-英文标题`
- `pmc/`：JATS XML 结构化转换，含摘要、章节、表格
- 其余：trafilatura 从 HTML 提取的干净 Markdown

## RAG 使用建议

- **chunk 策略**：正文按 800–1200 token、重叠 100–150 token 切块；frontmatter 的 `title/source/url` 作为元数据随 chunk 入库，便于溯源。
- **检索提示**：查询「图片所见 + 症状」时建议混合检索：
  - 学术证据 → `pmc/`（综述）+ `cjdr/`（原始研究）
  - 临床规范 → `web/`（MSD/ADA 章节与指南）
  - 中文查询 → `cndent/`（学会专业科普）+ `gov_cn/`（官方指南）
- **免责声明**：本库内容仅供辅助参考，诊疗建议必须由持证口腔医师确认。

## 数据来源与合规

- 全部为官方公开内容：CJDR（cjdr.cndent.com 期刊官网免费全文）、PMC（NCBI 开放获取）、ADA、NIDCR（美国政府公有领域）、MSD Manual、WHO、NHS、中华口腔医学会、中国政府公开文件。
- 仅用于个人/研究用途的检索增强，不用于再分发或商业出版；引用时注明来源 URL。
- 未从任何盗版书库（如 Z-Library）获取内容。

## 重新爬取

```bash
# CJDR 期刊 PDF（需系统 poppler pdftotext）
/opt/anaconda3/envs/scrape/bin/python scripts/crawl_cjdr.py kb/cjdr

# PMC 综述（MeSH 检索，60 篇）
.venv/bin/python scripts/crawl_pmc.py kb/pmc 60

# 网页内容（断点续爬）
.venv/bin/python scripts/crawl_web.py scripts/urls/*.txt kb/web

# NIDCR 出版物 / 中华口腔医学会专业内容 / 政府文件
.venv/bin/python scripts/crawl_nidcr_pubs.py kb/nidcr_pubs
.venv/bin/python scripts/crawl_cndent.py kb/cndent_pro && .venv/bin/python scripts/filter_cndent_pro.py
```

## 统计（manifest.json）

- 文件总数：486；总体积：约 9.7MB
- 按来源：cjdr 222 篇（6.4MB）/ pmc 61 篇（1.7MB）/ msdmanuals.com 70 篇 / ada.org 66 篇 / nidcr 53 篇 / cndent 3 篇 / nhs.uk 5 篇 / who.int 4 篇 / gov.cn 2 篇
