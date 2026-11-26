# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · **日本語** · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Wikipedia 記事向けの一次スクリーニング用 [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) 監査ツールです。

## 開発の背景

私は Wikipedia を編集しています。常に編集しているわけではありませんが、記事を整理するために開くたびに、毎回頭の中で同じチェックリストをなぞっていることに気づく程度には編集しています。日付の表記は統一されているか？ぼかし言葉（weasel words）はないか？出典に裸の URL を残したままにしていないか？「関連項目」セクションが肥大化していないか？末尾のセクションは正しい順序になっているか？

同じ十数個の問題を 3 回目か 4 回目かに連続して手作業で探したあと、スクリプトを書きました。そのスクリプトが成長し、今では手作業で行っていた 30 以上の項目をチェックするようになり、火曜日の夜に疲れているときに見落としがちな点も検出してくれます。

これは編集者の判断を代替するものではありません。トリアージ用のツールです。何を書くべきかではなく、どこを見るべきかを教えてくれます。

## チェック項目

**文体とトーン**
- ぼかし言葉（MOS:WEASEL）、大言壮語（MOS:PEACOCK）
- 時間経過で古びやすい相対的な時間表現（「最近」「現在」など）
- AI 生成コンテンツのシグナル: 本文中の過剰な帰属表現（WP:AISIGNS）、エッセイ調の表現（WP:NOTESSAY）
- MOS:INDIGENOUS 用語フラグ
- MOS:AVIATION 形式指定の書式
- MOS:MILITARY 出典のない死傷者数の記述

**構造**
- 導入部の長さと段落数（MOS:LEAD）
- MOS:LAYOUT に照らしたセクション順序
- 短すぎる、または未発達なセクション
- 出典のないセクション（100 語以上で `<ref>` がない）
- 関連項目セクションの肥大化
- 記事本文中の裸の外部 URL
- 引用テンプレートの密度

**出典と引用**
- `<ref>` タグ内の裸の URL（引用テンプレートなし）
- ISBN チェックディジット検証
- 引用テンプレート内の不正な URL
- リンク切れの外部リンク（オプトイン、低速）

**カテゴリとリンク**
- カテゴリの欠落
- カテゴリの品質（カテゴリ不足、広範すぎるカテゴリ）
- 赤リンクの検出（存在しない記事へのウィキリンク）
- 赤リンクカテゴリ
- 曖昧さ回避ページへのリンク
- 過剰な内部リンク（MOS:OVERLINK）

**インフォボックス**
- パラメーター数とリスト密度（肥大化の検出）
- 一般的に期待されるパラメーターの欠落
- MOS:MILHIST インフォボックスのシグナル

**その他**
- ショートデスクリプションの品質（欠落、長すぎる、記事名と一致）
- メンテナンス用テンプレートの一覧
- 姉妹プロジェクトリンクの衛生状態（MOS:SISTER）
- 孤立記事の検出（被ウィキリンクなし）
- バックリンク候補の発見
- 年表・ライブブログ風の見出しパターン

各チェックでは重要度ランク付き（low/medium/high）の問題が生成され、スコアが減点されます。問題のない記事のスコアは 100 になります。

## インストール

```
pip install .
```

mwparserfromhell は必須の依存関係です。テンプレート、見出し、ウィキリンクを正確に検出するための AST ベースのウィキテキスト解析を提供します。コンパイルできない場合（C コンパイラが利用できない場合）、ツールは自動的に正規表現ベースの解析にフォールバックします。

開発用インストール:

```
pip install -e '.[dev]'
```

## 使い方

公開中の Wikipedia 記事を監査する:

```
wiki-mos-audit "Gettysburg Address"
```

URL から監査する:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

ローカルのウィキテキストファイルを監査する:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

ウィキテキストファイルのディレクトリを一括監査する:

```
wiki-mos-audit --dir ./articles/
```

API チェックをスキップする（オフラインモード）:

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### 出力形式

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### オプションチェック

以下は低速であるかネットワークアクセスが必要なため、デフォルトではオフになっています:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### 自動修正

安全な機械的修正（空白や書式設定）は自動的に適用できます:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

書き込まずにプレビューする:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### 差分モード

ローカルのウィキテキストを公開版と比較する:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### 設定

しきい値の調整や特定のチェックの無効化を行うには `.wiki-mos-audit.toml` ファイルを作成します:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

明示的に指定して渡す場合:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### ローカライズ

CLI のヘルプ、診断メッセージ、およびテキスト/HTML レポートの表示枠は、追加の依存関係なしで 45 ロケール（`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`）に対応しています。解決時は `--lang`（Wikipedia の言語版を選択する `--language` とは別です）、次に `LC_ALL`、`LC_MESSAGES`、`LANG` の順に確認し、`en` にフォールバックします。JSON の出力キーおよびウィキテキストのテンプレートは変更されません。

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

## 開発

テストを実行する:

```
python -m pytest tests/ -x -q
```

リントを実行する:

```
ruff check src/ tests/
```

## 動作要件

- Python 3.12+
- mwparserfromhell

## ライセンス

MIT
