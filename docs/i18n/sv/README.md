# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · **Svenska** · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Ett verktyg för en första granskning av Wikipedia-artiklar mot [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style).

## Varför detta finns

Jag redigerar Wikipedia. Inte konstant, men tillräckligt ofta för att börja märka ett mönster: varje gång jag öppnade en artikel för att städa upp i den gick jag igenom samma mentala checklista. Är datumen konsekventa? Några vaga formuleringar (weasel words)? Lämnade någon bara råa URL:er i referenserna? Är avsnittet Se även överbelastat? Ligger de avslutande avsnitten i rätt ordning?

Efter tredje eller fjärde gången jag manuellt skannade efter samma dussin problem i rad skrev jag ett skript. Det skriptet växte. Nu kontrollerar det över 30 saker som jag brukade göra för hand, och det fångar sådant jag skulle missa en trött tisdagskväll.

Detta ersätter inte redaktionellt omdöme. Det är ett sållningsverktyg. Det talar om var du ska titta, inte vad du ska skriva.

## Vad verktyget kontrollerar

**Stil och ton**
- Vaga uttryck (MOS:WEASEL), skrytord (MOS:PEACOCK)
- Relativa tidsuttryck ("nyligen", "för närvarande") som åldras dåligt
- Signaler på AI-genererat innehåll: överdriven attribuering i brödtext (WP:AISIGNS), essäliknande formuleringar (WP:NOTESSAY)
- Flaggning av terminologi enligt MOS:INDIGENOUS
- Beteckningsformatering enligt MOS:AVIATION
- Obestyrkta uppgifter om förluster enligt MOS:MILITARY

**Struktur**
- Inledningens längd och antal stycken (MOS:LEAD)
- Avsnittsordning enligt MOS:LAYOUT
- Korta eller underutvecklade avsnitt
- Avsnitt utan källor (100+ ord, inga `<ref>`)
- Överlastade Se även-avsnitt
- Råa externa URL:er i artikeltexten
- Täthet av citatmallar

**Referenser och källor**
- Råa URL:er inuti `<ref>`-taggar (ingen källmall)
- Validering av kontrollsiffra i ISBN
- Felformaterade URL:er i källmallar
- Döda externa länkar (valbart, långsamt)

**Kategorier och länkar**
- Saknade kategorier
- Kategorikvalitet (underkategoriserad, alltför bred)
- Upptäckt av röda länkar (wikilänkar till artiklar som inte finns)
- Röda länkar till kategorier
- Länkar till förgreningssidor
- Överlänkning (MOS:OVERLINK)

**Infobox**
- Antal parametrar och listtäthet (upptäckt av överlastning)
- Saknade vanligen förväntade parametrar
- Signaler för MOS:MILHIST-infoboxar

**Övrigt**
- Kvalitet på kort beskrivning (saknas, för lång, matchar titeln)
- Inventering av underhållsmallar
- Länkhygien för systerprojekt (MOS:SISTER)
- Upptäckt av föräldralösa artiklar (inga inkommande wikilänkar)
- Upptäckt av potentiella bakåtlänkar
- Rubrikmönster för tidslinjer/livebloggar

Varje kontroll genererar ett ärende med allvarlighetsgrad (låg/medel/hög) och ett poängavdrag. En felfri artikel får 100 poäng.

## Installation

```
pip install .
```

mwparserfromhell är ett obligatoriskt beroende. Det tillhandahåller AST-baserad wikitext-parsning för exakt upptäckt av mallar, rubriker och wikilänkar. Om det inte kan kompileras (ingen C-kompilator tillgänglig) faller verktyget automatiskt tillbaka till regex-baserad parsning.

För utveckling:

```
pip install -e '.[dev]'
```

## Användning

Granska en publicerad Wikipedia-artikel:

```
wiki-mos-audit "Gettysburg Address"
```

Granska från en URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Granska en lokal wikitext-fil:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Batchgranska en katalog med wikitext-filer:

```
wiki-mos-audit --dir ./articles/
```

Hoppa över API-kontroller (offlineläge):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Utdataformat

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Valfria kontroller

Dessa är avstängda som standard eftersom de är långsamma eller kräver nätverksåtkomst:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Automatisk korrigering

Säkra mekaniska korrigeringar (blanksteg, formatering) kan tillämpas automatiskt:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Förhandsgranska utan att skriva:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Diff-läge

Jämför lokal wikitext mot den publicerade versionen:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Konfiguration

Skapa filen `.wiki-mos-audit.toml` för att justera tröskelvärden eller inaktivera specifika kontroller:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Skicka in den explicit:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Lokalisering

CLI-hjälp, diagnostik samt text- och HTML-rapportens ramverk stöder 45 språkversioner (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) utan extra beroenden. Upplösningen kontrollerar `--lang` (skilt från `--language`, som väljer Wikipedia-upplaga), sedan `LC_ALL`, `LC_MESSAGES` och `LANG`, och faller tillbaka till `en`. JSON-utdatanycklar och wikitext-mallar förblir oförändrade.

```
wiki-mos-audit "Article" --lang de --wikitext-file article.txt
LANG=fr_FR.UTF-8 wiki-mos-audit --help
```

## Python-API

```python
from wiki_mos_audit import audit_mos

report = audit_mos("Article Title", wikitext)
print(f"Score: {report.score}/100")
for issue in report.issues:
    print(f"[{issue.severity}] {issue.check_id}: {issue.message}")
```

## Utveckling

Kör tester:

```
python -m pytest tests/ -x -q
```

Lintning:

```
ruff check src/ tests/
```

## Krav

- Python 3.12+
- mwparserfromhell

## Licens

MIT
