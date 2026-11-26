# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** **English** · [Deutsch](docs/i18n/de/README.md) · [Español](docs/i18n/es/README.md) · [Français](docs/i18n/fr/README.md) · [Italiano](docs/i18n/it/README.md) · [Português (BR)](docs/i18n/pt-BR/README.md) · [Nederlands](docs/i18n/nl/README.md) · [Русский](docs/i18n/ru/README.md) · [Українська](docs/i18n/uk/README.md) · [日本語](docs/i18n/ja/README.md) · [한국어](docs/i18n/ko/README.md) · [简体中文](docs/i18n/zh-CN/README.md) · [繁體中文](docs/i18n/zh-TW/README.md) · [العربية](docs/i18n/ar/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [Polski](docs/i18n/pl/README.md) · [Türkçe](docs/i18n/tr/README.md) · [Svenska](docs/i18n/sv/README.md) · [Tiếng Việt](docs/i18n/vi/README.md) · [Bahasa Indonesia](docs/i18n/id/README.md)

<details><summary>More languages (28 locales)</summary>

[Afrikaans](docs/i18n/af-ZA/README.md) · [አማርኛ](docs/i18n/am-ET/README.md) · [العربية (مصر)](docs/i18n/ar-EG/README.md) · [العربية (المغرب)](docs/i18n/ar-MA/README.md) · [বাংলা](docs/i18n/bn/README.md) · [Bosanski](docs/i18n/bs/README.md) · [فارسی](docs/i18n/fa/README.md) · [Filipino](docs/i18n/fil/README.md) · [Français (Maroc)](docs/i18n/fr-MA/README.md) · [Français (Sénégal)](docs/i18n/fr-SN/README.md) · [Hausa](docs/i18n/ha-NG/README.md) · [עברית](docs/i18n/he/README.md) · [Hrvatski](docs/i18n/hr/README.md) · [Igbo](docs/i18n/ig-NG/README.md) · [Malagasy](docs/i18n/mg-MG/README.md) · [मराठी](docs/i18n/mr/README.md) · [Bahasa Melayu](docs/i18n/ms/README.md) · [Kinyarwanda](docs/i18n/rw-RW/README.md) · [Soomaali](docs/i18n/so-SO/README.md) · [Српски](docs/i18n/sr/README.md) · [Kiswahili](docs/i18n/sw-KE/README.md) · [தமிழ்](docs/i18n/ta/README.md) · [తెలుగు](docs/i18n/te/README.md) · [ไทย](docs/i18n/th/README.md) · [اردو](docs/i18n/ur/README.md) · [isiXhosa](docs/i18n/xh-ZA/README.md) · [Yorùbá](docs/i18n/yo-NG/README.md) · [isiZulu](docs/i18n/zu-ZA/README.md)

</details>

A first-pass [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) auditor for Wikipedia articles.

## Why this exists

I edit Wikipedia. Not constantly, but enough that I started noticing a pattern: every time I opened an article to clean up, I was running the same mental checklist. Are the dates consistent? Any weasel words? Did someone leave bare URLs in the refs? Is the See also section bloated? Are the bottom-matter sections in the right order?

After the third or fourth time manually scanning for the same dozen problems in a row, I wrote a script. That script grew. Now it checks 30+ things I was doing by hand, and it catches stuff I'd miss on a tired Tuesday evening.

This is not a replacement for editorial judgment. It is a triage tool. It tells you where to look, not what to write.

## What it checks

**Style and tone**
- Weasel words (MOS:WEASEL), peacock terms (MOS:PEACOCK)
- Relative time expressions ("recently", "currently") that age poorly
- AI-generated content signals: over-attribution in body text (WP:AISIGNS), essay-like phrasing (WP:NOTESSAY)
- MOS:INDIGENOUS terminology flags
- MOS:AVIATION designation formatting
- MOS:MILITARY uncited casualty statements

**Structure**
- Lead length and paragraph count (MOS:LEAD)
- Section ordering against MOS:LAYOUT
- Short or underdeveloped sections
- Unreferenced sections (100+ words, no `<ref>`)
- See also section bloat
- Bare external URLs in article body
- Quote template density

**References and citations**
- Bare URLs inside `<ref>` tags (no cite template)
- ISBN check digit validation
- Malformed URLs in citation templates
- Dead external links (opt-in, slow)

**Categories and links**
- Missing categories
- Category quality (undercategorized, overly broad)
- Red-link detection (wikilinks to nonexistent articles)
- Red-link categories
- Disambiguation page links
- Overlinking (MOS:OVERLINK)

**Infobox**
- Parameter count and list density (bloat detection)
- Missing commonly expected parameters
- MOS:MILHIST infobox signals

**Other**
- Short description quality (missing, too long, matches title)
- Maintenance template inventory
- Sister project link hygiene (MOS:SISTER)
- Orphan detection (no incoming wikilinks)
- Potential backlink discovery
- Timeline/liveblog heading patterns

Each check produces a severity-rated issue (low/medium/high) with a score deduction. A clean article scores 100.

## Installation

```
pip install .
```

mwparserfromhell is a required dependency. It provides AST-based wikitext parsing for accurate template, heading, and wikilink detection. If it cannot be compiled (no C compiler available), the tool falls back to regex-based parsing automatically.

For development:

```
pip install -e '.[dev]'
```

## Usage

Audit a live Wikipedia article:

```
wiki-mos-audit "Gettysburg Address"
```

Audit from a URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Audit a local wikitext file:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Batch audit a directory of wikitext files:

```
wiki-mos-audit --dir ./articles/
```

Skip API checks (offline mode):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Output formats

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Optional checks

These are off by default because they're slow or need network access:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Auto-fix

Safe mechanical fixes (whitespace, formatting) can be applied automatically:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Preview without writing:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Diff mode

Compare local wikitext against the live version:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Configuration

Create a `.wiki-mos-audit.toml` file to adjust thresholds or disable specific checks:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Pass it explicitly:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Localization

CLI help, diagnostics, and text/HTML report chrome support 48 locales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`) with zero extra dependencies. Resolution checks `--lang` (distinct from `--language`, which selects the Wikipedia edition), then `LC_ALL`, `LC_MESSAGES`, and `LANG`, falling back to `en`. JSON output keys and wikitext templates remain unchanged.

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

## Development

Run tests:

```
python -m pytest tests/ -x -q
```

Lint:

```
ruff check src/ tests/
```

## Requirements

- Python 3.12+
- mwparserfromhell

## License

MIT
