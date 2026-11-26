# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · **Nederlands** · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Een eerste-ronde [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style)-auditor voor Wikipedia-artikelen.

## Waarom dit bestaat

Ik bewerk Wikipedia. Niet voortdurend, maar genoeg dat me een patroon begon op te vallen: elke keer als ik een artikel opende om het op te schonen, liep ik dezelfde mentale checklist af. Zijn de datums consistent? Zitten er vage formuleringen (weasel words) in? Heeft iemand kale URL's in de referenties laten staan? Is de sectie 'See also' opgeblazen? Staan de onderste secties in de juiste volgorde?

Na de derde of vierde keer handmatig scannen op steeds hetzelfde dozijn problemen achter elkaar, heb ik een script geschreven. Dat script groeide. Nu controleert het meer dan 30 zaken die ik eerst met de hand deed, en het vangt dingen op die ik op een vermoeide dinsdagavond over het hoofd zou zien.

Dit is geen vervanging voor redactioneel oordeel. Het is een triage-tool. Het wijst je waar je moet kijken, niet wat je moet schrijven.

## Wat het controleert

**Stijl en toon**
- Vage formuleringen (MOS:WEASEL), ophemelende termen (MOS:PEACOCK)
- Relatieve tijdsaanduidingen ("recently", "currently") die slecht verouderen
- Signalen van door AI gegenereerde inhoud: overmatige attributie in de hoofdtekst (WP:AISIGNS), essay-achtige formulering (WP:NOTESSAY)
- Signalering van MOS:INDIGENOUS-terminologie
- MOS:AVIATION-aanduidingsopmaak
- MOS:MILITARY niet-onderbouwde slachtoffervermeldingen

**Structuur**
- Lengte van de inleiding en aantal alinea's (MOS:LEAD)
- Sectievolgorde volgens MOS:LAYOUT
- Korte of onderontwikkelde secties
- Secties zonder referenties (100+ woorden, geen `<ref>`)
- Opgeblazen 'See also'-sectie
- Kale externe URL's in de hoofdtekst van het artikel
- Dichtheid van citaatsjablonen

**Referenties en bronvermeldingen**
- Kale URL's binnen `<ref>`-tags (geen cite-sjabloon)
- Validatie van het controlecijfer van ISBN's
- Misvormde URL's in bronvermeldingssjablonen
- Dode externe links (opt-in, traag)

**Categorieën en links**
- Ontbrekende categorieën
- Categoriekwaliteit (ondergecategoriseerd, te breed)
- Detectie van rode links (wikilinks naar niet-bestaande artikelen)
- Rode-linkcategorieën
- Links naar doorverwijspagina's
- Overmatig linken (MOS:OVERLINK)

**Infobox**
- Aantal parameters en lijstdichtheid (detectie van opgeblazen infoboxen)
- Ontbrekende veelverwachte parameters
- MOS:MILHIST-infoboxsignalen

**Overig**
- Kwaliteit van de korte beschrijving (ontbrekend, te lang, gelijk aan titel)
- Inventarisatie van onderhoudssjablonen
- Hygiëne van links naar zusterprojecten (MOS:SISTER)
- Detectie van weesartikelen (geen inkomende wikilinks)
- Ontdekking van potentiële backlinks
- Koppatronen voor tijdlijnen en liveblogs

Elke controle levert een bevinding op met een ernstniveau (low/medium/high) en een puntenaftrek. Een foutloos artikel scoort 100.

## Installatie

```
pip install .
```

mwparserfromhell is een vereiste afhankelijkheid. Het biedt op een AST gebaseerde wikitext-parsing voor nauwkeurige detectie van sjablonen, koppen en wikilinks. Als het niet kan worden gecompileerd (geen C-compiler beschikbaar), valt de tool automatisch terug op parsing met reguliere expressies.

Voor ontwikkeling:

```
pip install -e '.[dev]'
```

## Gebruik

Auditeer een live Wikipedia-artikel:

```
wiki-mos-audit "Gettysburg Address"
```

Auditeer vanaf een URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Auditeer een lokaal wikitext-bestand:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Voer een batch-audit uit op een map met wikitext-bestanden:

```
wiki-mos-audit --dir ./articles/
```

Sla API-controles over (offline modus):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Uitvoerformaten

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Optionele controles

Deze staan standaard uit omdat ze traag zijn of netwerktoegang vereisen:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Automatisch corrigeren

Veilige mechanische correcties (witruimte, opmaak) kunnen automatisch worden toegepast:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Voorvertoning zonder weg te schrijven:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Diff-modus

Vergelijk lokale wikitext met de live versie:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Configuratie

Maak een `.wiki-mos-audit.toml`-bestand aan om drempelwaarden aan te passen of specifieke controles uit te schakelen:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Geef het expliciet mee:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Lokalisatie

CLI-help, diagnostiek en de opmaak van tekst- en HTML-rapporten ondersteunen 45 locales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) zonder extra afhankelijkheden. De bepaling controleert `--lang` (onderscheiden van `--language`, waarmee de Wikipedia-editie wordt gekozen), daarna `LC_ALL`, `LC_MESSAGES` en `LANG`, met `en` als terugvaloptie. JSON-uitvoersleutels en wikitext-sjablonen blijven ongewijzigd.

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

## Ontwikkeling

Tests uitvoeren:

```
python -m pytest tests/ -x -q
```

Linten:

```
ruff check src/ tests/
```

## Vereisten

- Python 3.12+
- mwparserfromhell

## Licentie

MIT
