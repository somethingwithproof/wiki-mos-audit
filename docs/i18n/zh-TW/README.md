# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · **繁體中文** · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

一款針對 Wikipedia 條目進行初篩的 [格式手冊（Manual of Style）](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) 稽核工具。

## 開發緣由

我平時會編輯 Wikipedia。雖然不是無時無刻在編，但頻率高到讓我注意到一個規律：每次打開一篇條目準備整理時，腦中總會跑過同一份檢查清單。日期格式一致嗎？有沒有模糊修飾詞？參考文獻裡是不是有人留了裸露網址？「參見」章節會不會太冗長？文末各章節的順序對不對？

連續三、四次手動掃描同樣這十幾種問題之後，我寫了一支腳本。那支腳本一路擴充到現在，能自動檢查 30 多項我過去靠人工核對的項目，甚至能抓出我在週二晚上精神不濟時容易漏掉的細節。

這套工具無法取代編者的判斷力，它是一個初步篩檢工具：它告訴您該往哪裡看，而不是替您決定要寫什麼。

## 檢查項目

**風格與語氣**
- 模糊修飾詞（MOS:WEASEL）、浮誇詞彙（MOS:PEACOCK）
- 容易隨時間過時的相對時間用語（「最近」、「目前」）
- AI 生成內容訊號：正文中的過度歸因（WP:AISIGNS）、散文式寫法（WP:NOTESSAY）
- MOS:INDIGENOUS 用語標記
- MOS:AVIATION 型號格式規範
- MOS:MILITARY 未附來源的傷亡人數陳述

**結構**
- 導言長度與段落數（MOS:LEAD）
- 依據 MOS:LAYOUT 檢查章節順序
- 過短或內容不足的章節
- 缺乏來源的章節（超過 100 字且無 `<ref>`）
- 「參見」章節過於冗長
- 條目正文中的裸露外部網址
- 引文模板密度

**參考文獻與引用**
- `<ref>` 標籤內的裸露網址（未使用引用模板）
- ISBN 檢查碼驗證
- 引用模板中格式錯誤的網址
- 失效外部連結（選用項目，速度較慢）

**分類與連結**
- 缺少分類
- 分類品質（分類過少、過於寬泛）
- 紅字連結偵測（指向不存在條目的維基連結）
- 紅字分類
- 連往消歧義頁面的連結
- 過度連結（MOS:OVERLINK）

**資訊框（Infobox）**
- 參數數量與清單密度（冗餘膨脹偵測）
- 缺少常見的預期參數
- MOS:MILHIST 資訊框訊號

**其他**
- 簡短描述品質（缺少、過長、與標題重複）
- 維護模板清查
- 姊妹計畫連結規範（MOS:SISTER）
- 孤立條目偵測（沒有連入的維基連結）
- 潛在反向連結探索
- 時間軸／即時報導式標題樣式

每項檢查都會產生附帶嚴重程度分級（低／中／高）的問題項目並扣分。一篇乾淨無誤的條目得分為 100 分。

## 安裝

```
pip install .
```

mwparserfromhell 為必要相依套件，提供基於 AST 的 Wikitext 解析功能，以精確偵測模板、標題與維基連結。若無法編譯（例如缺少 C 編譯器），工具會自動退回使用正規表示式進行解析。

開發環境安裝：

```
pip install -e '.[dev]'
```

## 使用方式

稽核線上的 Wikipedia 條目：

```
wiki-mos-audit "Gettysburg Address"
```

透過 URL 進行稽核：

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

稽核本機 Wikitext 檔案：

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

批次稽核目錄中的 Wikitext 檔案：

```
wiki-mos-audit --dir ./articles/
```

略過 API 檢查（離線模式）：

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### 輸出格式

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### 選用檢查

以下檢查因執行較慢或需要網路連線，預設為關閉狀態：

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### 自動修復

可自動套用安全的機械式修正（空白字元、格式調整）：

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

預覽修正結果而不寫入檔案：

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### 差異比對模式

將本機 Wikitext 與線上版本進行比對：

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### 設定

建立 `.wiki-mos-audit.toml` 設定檔以調整閾值或停用特定檢查：

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

明確指定設定檔路徑：

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### 在地化

CLI 說明、診斷資訊與純文字／HTML 報告介面支援 45 種語系（`en`、`de`、`es`、`fr`、`it`、`pt-BR`、`nl`、`ru`、`uk`、`ja`、`ko`、`zh-CN`、`zh-TW`、`ar`、`hi`、`pl`、`tr`、`sv`、`vi`、`id`、`af-ZA`、`am-ET`、`ar-EG`、`ar-MA`、`fr-MA`、`fr-SN`、`ha-NG`、`ig-NG`、`mg-MG`、`rw-RW`、`so-SO`、`sw-KE`、`xh-ZA`、`yo-NG`、`zu-ZA`、`bn`、`fa`、`he`、`mr`、`ta`、`te`、`th`、`ur`、`ms`、`fil`），無須額外相依套件。解析順序為檢查 `--lang`（不同於用於選擇 Wikipedia 語言版本的 `--language`），接著是 `LC_ALL`、`LC_MESSAGES` 與 `LANG`，最後備援至 `en`。JSON 輸出鍵值與 Wikitext 模板皆保持不變。

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

## 開發

執行測試：

```
python -m pytest tests/ -x -q
```

程式碼檢查：

```
ruff check src/ tests/
```

## 系統需求

- Python 3.12+
- mwparserfromhell

## 授權條款

MIT
