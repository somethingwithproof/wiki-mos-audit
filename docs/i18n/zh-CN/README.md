# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · **简体中文** · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

一款面向 Wikipedia 条目的初筛[格式手册](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style)（MOS）审查工具。

## 开发初衷

我平时会编辑 Wikipedia。虽然算不上高频贡献者，但次数多到让我发现了一个规律：每次打开一个条目准备清理规范时，我脑子里都在重复同一份检查清单。日期格式是否统一？有没有含糊其辞的表述？是不是有人在参考文献里直接留了裸露 URL？“参见”章节是否过于臃肿？文末各章节的排列顺序是否正确？

在连续三四次手动排查这十来个相同的问题之后，我写了一个脚本。后来脚本不断演进，现在它能自动检查我以前手工核对的 30 多项内容，还能抓出我在周二晚上犯困时容易漏掉的细节。

它并不能替代编者的专业判断，而是一个初筛分流工具。它告诉你该重点看哪里，而不是替你决定怎么写。

## 检查内容

**风格与语气**
- 含糊其辞的表述（MOS:WEASEL）、浮夸用语（MOS:PEACOCK）
- 容易随时间过时的相对时间表述（“recently”、“currently”）
- AI 生成内容信号：正文中过度归因（WP:AISIGNS）、散文式或随笔化措辞（WP:NOTESSAY）
- MOS:INDIGENOUS 术语标记
- MOS:AVIATION 机型编号与名称格式
- MOS:MILITARY 未附来源的伤亡表述

**结构**
- 导言长度与段落数量（MOS:LEAD）
- 对照 MOS:LAYOUT 的章节排序
- 过短或内容单薄的章节
- 缺乏参考文献的章节（超过 100 词且无 `<ref>`）
- “参见”章节臃肿检查
- 条目正文中的裸露外部 URL
- 引用模板密度

**参考文献与引文**
- `<ref>` 标签内的裸露 URL（未使用 cite 模板）
- ISBN 校验位验证
- 引文模板中格式错误的 URL
- 失效外部链接（需主动启用，速度较慢）

**分类与链接**
- 缺失分类
- 分类质量（分类不足、过于宽泛）
- 红链检测（指向不存在条目的维基内链）
- 红链分类
- 消歧义页面链接
- 过度链接（MOS:OVERLINK）

**信息框**
- 参数数量与列表密度（臃肿检测）
- 缺失常见预期参数
- MOS:MILHIST 信息框信号

**其他**
- 简短描述质量（缺失、过长、与标题重复）
- 维护模板清单
- 姊妹项目链接规范（MOS:SISTER）
- 孤立条目检测（无入站维基内链）
- 潜在反向链接发现
- 时间线/实时播报类标题模式

每项检查都会生成一个带严重程度分级（low/medium/high）的问题条目，并相应扣分。完全合规的条目得分为 100。

## 安装

```
pip install .
```

mwparserfromhell 是必需依赖。它提供基于 AST 的 wikitext 解析，用于准确识别模板、标题和维基内链。如果因缺少 C 编译器而无法编译安装，工具会自动回退到基于正则表达式的解析方式。

用于开发环境：

```
pip install -e '.[dev]'
```

## 用法

审查在线 Wikipedia 条目：

```
wiki-mos-audit "Gettysburg Address"
```

通过 URL 审查：

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

审查本地 wikitext 文件：

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

批量审查目录下的 wikitext 文件：

```
wiki-mos-audit --dir ./articles/
```

跳过 API 检查（离线模式）：

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### 输出格式

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### 可选检查

以下检查默认关闭，因为它们耗时较长或需要网络访问：

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### 自动修复

可以自动应用安全的机械性修复（空白字符、格式排版等）：

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

仅预览而不写入文件：

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### 差异对比模式

将本地 wikitext 与在线版本进行对比：

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### 配置

创建 `.wiki-mos-audit.toml` 文件以调整阈值或禁用特定检查：

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

显式指定配置文件路径：

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### 本地化

CLI 帮助、诊断信息和文本/HTML 报告界面框架支持 45 种语言区域（`en`、`de`、`es`、`fr`、`it`、`pt-BR`、`nl`、`ru`、`uk`、`ja`、`ko`、`zh-CN`、`zh-TW`、`ar`、`hi`、`pl`、`tr`、`sv`、`vi`、`id`、`af-ZA`、`am-ET`、`ar-EG`、`ar-MA`、`fr-MA`、`fr-SN`、`ha-NG`、`ig-NG`、`mg-MG`、`rw-RW`、`so-SO`、`sw-KE`、`xh-ZA`、`yo-NG`、`zu-ZA`、`bn`、`fa`、`he`、`mr`、`ta`、`te`、`th`、`ur`、`ms`、`fil`），无需额外依赖。语言区域解析依次检查 `--lang`（与用于选择 Wikipedia 语言版本的 `--language` 不同）、`LC_ALL`、`LC_MESSAGES` 和 `LANG`，最后回退到 `en`。JSON 输出键名和 wikitext 模板保持不变。

```
wiki-mos-audit "Article" --lang de --wikitext-file article.txt
LANG=fr_FR.UTF-8 wiki-mos-audit --help
```

## Python API

```python
from wiki_mos_audit import audit_mos

report = audit_mos("Article Title", wikitext)
print(f"Score: {report.score}/100")
for issue in report.issues:
    print(f"[{issue.severity}] {issue.check_id}: {issue.message}")
```

## 开发

运行测试：

```
python -m pytest tests/ -x -q
```

代码检查：

```
ruff check src/ tests/
```

## 环境要求

- Python 3.12+
- mwparserfromhell

## 许可证

MIT
