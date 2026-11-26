# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

**Afrikaans** · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

'n Eerstefase-ouditeur volgens die [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) vir Wikipedia-artikels.

## Hoekom dit bestaan

Ek redigeer Wikipedia. Nie voortdurend nie, maar genoeg dat ek 'n patroon begin opmerk het: elke keer as ek 'n artikel oopgemaak het om dit op te ruim, het ek deur dieselfde geestelike kontrolelys gegaan. Is die datums konsekwent? Enige ontwykende woorde? Het iemand kaal URL's in die verwysings gelos? Is die See also-afdeling opgeblaas? Is die onderaan-afdelings in die regte volgorde?

Na die derde of vierde keer wat ek handmatig vir dieselfde dosyn probleme na mekaar geskandeer het, het ek 'n skrip geskryf. Daardie skrip het gegroei. Nou kontroleer dit 30+ dinge wat ek met die hand gedoen het, en dit vang goed raak wat ek op 'n moeë Dinsdagaand sou mis.

Dit is nie 'n plaasvervanger vir redaksionele oordeel nie. Dit is 'n sifnutsmiddel. Dit sê vir jou waar om te kyk, nie wat om te skryf nie.

## Wat dit kontroleer

**Styl en toon**
- Ontwykende woorde (MOS:WEASEL), pronkterme (MOS:PEACOCK)
- Relatiewe tydsuitdrukkings ("onlangs", "tans") wat swak verouder
- Seine van KI-gegenereerde inhoud: oor-toeskrywing in hoofteks (WP:AISIGNS), opstelagtige frasering (WP:NOTESSAY)
- MOS:INDIGENOUS-terminologievlae
- MOS:AVIATION-benamingsformatering
- MOS:MILITARY-ongevalleverklarings sonder bronverwysing

**Struktuur**
- Inleidingslengte en paragraaftelling (MOS:LEAD)
- Afdelingsvolgorde teenoor MOS:LAYOUT
- Kort of onderontwikkelde afdelings
- Afdelings sonder verwysings (100+ woorde, geen `<ref>`)
- Opgeblase See also-afdeling
- Kaal eksterne URL's in artikelliggaam
- Digtheid van aanhalingsjablone

**Verwysings en aanhalings**
- Kaal URL's binne `<ref>`-etikette (geen aanhalingsjabloon nie)
- ISBN-kontrolesyfervalidering
- Wangevormde URL's in aanhalingsjablone
- Dooie eksterne skakels (opsioneel, stadig)

**Kategorieë en skakels**
- Ontbrekende kategorieë
- Kategoriegehalte (ondergekategoriseer, te breed)
- Rooiskakel-opsporing (wikiskakels na nie-bestaande artikels)
- Rooiskakel-kategorieë
- Dubbelsinnigheidsbladsy-skakels
- Oormaat skakels (MOS:OVERLINK)

**Inligtingskas**
- Parametertelling en lysdigtheid (opblaas-opsporing)
- Ontbrekende algemeen verwagte parameters
- MOS:MILHIST-inligtingskasseine

**Ander**
- Kortbeskrywing-gehalte (ontbreek, te lank, stem ooreen met titel)
- Onderhoudsjabloon-inventaris
- Susterprojek-skakelhigiëne (MOS:SISTER)
- Weesbladsy-opsporing (geen inkomende wikiskakels nie)
- Potensiële terugskakel-ontdekking
- Tydlyn-/lewendige blog-opskrifpatrone

Elke kontrole lewer 'n erns-gegradeerde probleem (laag/medium/hoog) met 'n tellingaftrekking op. 'n Skoon artikel behaal 100.

## Installasie

```
pip install .
```

mwparserfromhell is 'n vereiste afhanklikheid. Dit verskaf AST-gebaseerde wikiteks-ontleding vir akkurate sjabloon-, opskrif- en wikiskakelopsporing. As dit nie gekompileer kan word nie (geen C-kompileerder beskikbaar nie), val die nutsmiddel outomaties terug na regex-gebaseerde ontleding.

Vir ontwikkeling:

```
pip install -e '.[dev]'
```

## Gebruik

Ouditeer 'n lewendige Wikipedia-artikel:

```
wiki-mos-audit "Gettysburg Address"
```

Ouditeer vanaf 'n URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Ouditeer 'n plaaslike wikitekslêer:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Bondelouditeer 'n gids met wikitekslêers:

```
wiki-mos-audit --dir ./articles/
```

Slaan API-kontroles oor (vanlynmodus):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Afvoerformate

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Opsionele kontroles

Hierdie is by verstek afgeskakel omdat dit stadig is of netwerktoegang benodig:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Outo-herstel

Veilige meganiese regstellings (witspasie, formatering) kan outomaties toegepas word:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Voorskou sonder om te skryf:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Diff-modus

Vergelyk plaaslike wikiteks teen die lewendige weergawe:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Konfigurasie

Skep 'n `.wiki-mos-audit.toml`-lêer om drempels aan te pas of spesifieke kontroles te deaktiveer:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Gee dit eksplisiet deur:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Lokalisering

CLI-hulp, diagnostiek en teks-/HTML-verslagraamwerk ondersteun 45 lokale (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) sonder ekstra afhanklikhede. Oplossing kontroleer `--lang` (onderskei van `--language`, wat die Wikipedia-uitgawe kies), dan `LC_ALL`, `LC_MESSAGES`, en `LANG`, en val terug na `en`. JSON-afvoersleutels en wikitekssjablone bly onveranderd.

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

## Ontwikkeling

Voer toetse uit:

```
python -m pytest tests/ -x -q
```

Lint:

```
ruff check src/ tests/
```

## Vereistes

- Python 3.12+
- mwparserfromhell

## Lisensie

MIT
