# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (28 locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [Bosanski](../bs/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · **Hrvatski** · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Српски](../sr/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Alat za brzu prvu provjeru usklađenosti članaka Wikipedije s [Priručnikom za stil (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style).

## Zašto ovo postoji

Uređujem Wikipediju. Ne neprekidno, ali dovoljno često da sam počeo uočavati obrazac: svaki put kad bih otvorio članak za uređivanje, u mislima sam prolazio kroz isti popis za provjeru. Jesu li nadnevci usklađeni? Ima li neodređenih, izmotavajućih izraza (weasel words)? Je li netko ostavio gole URL-ove u bilješkama? Je li odjeljak "See also" prenatrpan? Jesu li završni odjeljci u ispravnom redoslijedu?

Nakon trećeg ili četvrtog puta što sam ručno pretraživao istih desetak problema zaredom, napisao sam skriptu. Ta je skripta narasla. Sada provjerava više od 30 stavki koje sam nekoć provjeravao ručno i otkriva propuste koji bi mi promakli jedne umorne večeri utorkom.

Ovo nije zamjena za uredničku prosudbu. Riječ je o alatu za početno razvrstavanje. Pokazuje vam kamo pogledati, a ne što napisati.

## Što provjerava

**Stil i ton**
- Neodređene formulacije (MOS:WEASEL), kićeni i hvalisavi izrazi (MOS:PEACOCK)
- Relativni vremenski izrazi ("nedavno", "trenutačno") koji brzo zastarijevaju
- Znakovi sadržaja generiranog umjetnom inteligencijom: prekomjerno navođenje izvora u glavnom tekstu (WP:AISIGNS), esejističko izražavanje (WP:NOTESSAY)
- Oznake terminologije MOS:INDIGENOUS
- Oblikovanje zrakoplovnih oznaka (MOS:AVIATION)
- Navodi o žrtvama bez izvora (MOS:MILITARY)

**Struktura**
- Duljina uvodnog dijela i broj odlomaka (MOS:LEAD)
- Redoslijed odjeljaka u odnosu na MOS:LAYOUT
- Kratki ili nedovoljno razrađeni odjeljci
- Odjeljci bez referenci (100+ riječi, bez `<ref>`)
- Prenatrpanost odjeljka "See also"
- Goli vanjski URL-ovi u tijelu članka
- Gustoća predložaka za citiranje

**Reference i izvori**
- Goli URL-ovi unutar oznaka `<ref>` (bez predloška za citiranje)
- Provjera kontrolne znamenke ISBN-a
- Neispravno oblikovani URL-ovi u predlošcima za citiranje
- Neispravne vanjske poveznice (izborno, sporo)

**Kategorije i poveznice**
- Kategorije koje nedostaju
- Kvaliteta kategorija (nedovoljna kategorizacija, preopćenite kategorije)
- Otkrivanje crvenih poveznica (wikipoveznice na nepostojeće članke)
- Crvene poveznice kategorija
- Poveznice na razdvojbene stranice
- Prekomjerno povezivanje (MOS:OVERLINK)

**Infookvir**
- Broj parametara i gustoća popisa (otkrivanje prenatrpanosti)
- Nedostajući uobičajeno očekivani parametri
- Znakovi infookvira MOS:MILHIST

**Ostalo**
- Kvaliteta kratkog opisa (nedostaje, predugačak, podudara se s naslovom)
- Popis predložaka za održavanje
- Urednost poveznica na sestrinske projekte (MOS:SISTER)
- Otkrivanje članaka siročadi (nema dolaznih wikipoveznica)
- Otkrivanje mogućih povratnih poveznica
- Obrasci naslova u stilu vremenske crte ili prijenosa uživo (liveblog)

Svaka provjera daje nalaz s razinom ozbiljnosti (low/medium/high) i oduzimanjem bodova. Uredan članak ostvaruje 100 bodova.

## Instalacija

```
pip install .
```

mwparserfromhell je obvezna ovisnost. Osigurava raščlambu wikiteksta temeljenu na AST-u radi točnog prepoznavanja predložaka, naslova i wikipoveznica. Ako se ne može prevesti (na računalu nema C prevoditelja), alat se automatski prebacuje na raščlambu pomoću regularnih izraza.

Za razvoj:

```
pip install -e '.[dev]'
```

## Uporaba

Provjera objavljenog članka Wikipedije:

```
wiki-mos-audit "Gettysburg Address"
```

Provjera putem URL-a:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Provjera lokalne datoteke wikiteksta:

```
wiki-mos-audit "Article" --wikitext-file article_corrected.txt
```

Skupna provjera mape s datotekama wikiteksta:

```
wiki-mos-audit --dir ./articles/
```

Preskakanje API provjera (izvanmrežni način rada):

```
wiki-mos-audit "Article" --wikitext-file article.txt --offline
```

### Formati izlaza

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Izborne provjere

Ove su provjere zadano isključene jer su spore ili zahtijevaju mrežni pristup poslužiteljima:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Automatski popravak

Sigurni mehanički popravci (razmaci, oblikovanje) mogu se primijeniti automatski:

```
wiki-mos-audit "Article" --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Predpregled opisa popravaka bez pohrane u datoteku:

```
wiki-mos-audit "Article" --wikitext-file article.txt --fix --dry-run --verbose
```

### Način usporedbe (Diff)

Usporedba lokalnoga wikiteksta s objavljenom inačicom:

```
wiki-mos-audit "Article" --wikitext-file article_corrected.txt --diff
```

### Postavke

Stvorite datoteku `.wiki-mos-audit.toml` za prilagodbu pragova ili onemogućivanje pojedinih provjera:

```toml
[audit]
min_severity = "low"
disabled_checks = ["mos-aviation-style"]

[thresholds]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Proslijedite je izričito:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Lokalizacija

Pomoć za CLI, dijagnostičke poruke te okvir tekstnih i HTML izvješća podržavaju 48 lokaliteta (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`) bez ikakvih dodatnih ovisnosti. Određivanje jezika provjerava `--lang` (različito od `--language`, koje odabire jezično izdanje Wikipedije), zatim `LC_ALL`, `LC_MESSAGES` i `LANG`, s pričuvnim povratkom na `en`. Ključevi JSON izlaza i predlošci wikiteksta ostaju nepromijenjeni.

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

## Razvoj

Pokretanje testova:

```
python -m pytest tests/ -x -q
```

Provjera linterom:

```
ruff check src/ tests/
```

## Zahtjevi

- Python 3.12+
- mwparserfromhell

## Licencija

MIT
