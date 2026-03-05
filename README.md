# wiki-mos-audit

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
