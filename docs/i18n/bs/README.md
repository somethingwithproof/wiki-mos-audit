# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (28 locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · **Bosanski** · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Hrvatski](../hr/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Српски](../sr/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Prvostepeni auditor prema [Priručniku za stil (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) za članke na Wikipediji.

## Zašto ovo postoji

Uređujem Wikipediju. Ne stalno, ali dovoljno često da sam počeo primjećivati obrazac: svaki put kad bih otvorio članak za sređivanje, prolazio sam kroz istu mentalnu kontrolnu listu. Jesu li datumi dosljedni? Ima li neodređenih, izbjegavajućih izraza (weasel words)? Je li neko ostavio gole URL-ove u referencama? Je li odjeljak "See also" prenatrpan? Jesu li završni odjeljci u ispravnom redoslijedu?

Nakon trećeg ili četvrtog puta kada sam ručno pretraživao istih desetak problema zaredom, napisao sam skriptu. Ta skripta je rasla. Sada provjerava više od 30 stvari koje sam ranije radio ručno i uočava detalje koje bih propustio jednog umornog utorka navečer.

Ovo nije zamjena za uredničku prosudbu. Ovo je alat za trijažu. Pokazuje vam gdje da pogledate, a ne šta da napišete.

## Šta provjerava

**Stil i ton**
- Izbjegavajući izrazi (MOS:WEASEL), hvalisavi termini (MOS:PEACOCK)
- Relativni vremenski izrazi ("nedavno", "trenutno") koji brzo zastarijevaju
- Signali sadržaja generisanog vještačkom inteligencijom: prekomjerno pripisivanje u glavnom tekstu (WP:AISIGNS), esejističko izražavanje (WP:NOTESSAY)
- Oznake terminologije MOS:INDIGENOUS
- Formatiranje oznaka u zrakoplovstvu (MOS:AVIATION)
- Necitirani navodi o žrtvama (MOS:MILITARY)

**Struktura**
- Dužina uvoda i broj pasusa (MOS:LEAD)
- Redoslijed odjeljaka prema MOS:LAYOUT
- Kratki ili nedovoljno razrađeni odjeljci
- Odjeljci bez referenci (100+ riječi, bez `<ref>`)
- Prenatrpanost odjeljka "See also"
- Goli vanjski URL-ovi u tijelu članka
- Gustoća šablona za citiranje

**Reference i citati**
- Goli URL-ovi unutar `<ref>` oznaka (bez šablona za citiranje)
- Validacija kontrolne cifre ISBN-a
- Neispravno formirani URL-ovi u šablonima za citiranje
- Neispravni vanjski linkovi (opcionalno, sporo)

**Kategorije i linkovi**
- Nedostajuće kategorije
- Kvalitet kategorija (nedovoljna kategorizacija, preširoke kategorije)
- Otkrivanje crvenih linkova (vikilinkovi na nepostojeće članke)
- Crveni linkovi kategorija
- Linkovi na stranice za višeznačnost
- Prekomjerno linkovanje (MOS:OVERLINK)

**Infokutija**
- Broj parametara i gustoća lista (otkrivanje prenatrpanosti)
- Nedostajući uobičajeno očekivani parametri
- Signali infokutije MOS:MILHIST

**Ostalo**
- Kvalitet kratkog opisa (nedostaje, predugačak, poklapa se s naslovom)
- Popis šablona za održavanje
- Higijena linkova prema sestrinskim projektima (MOS:SISTER)
- Otkrivanje članaka siročadi (nema dolaznih vikilinkova)
- Pronalaženje potencijalnih povratnih linkova
- Obrasci naslova u stilu hronologije ili prijenosa uživo (liveblog)

Svaka provjera generiše nalaz s ocjenom ozbiljnosti (low/medium/high) i odbitkom bodova. Čist članak dobija 100 bodova.

## Instalacija

```
pip install .
```

mwparserfromhell je obavezna zavisnost. Omogućava parsiranje vikiteksta zasnovano na AST-u radi tačnog prepoznavanja šablona, naslova i vikilinkova. Ako se ne može kompajlirati (nema dostupnog C kompajlera), alat se automatski prebacuje na parsiranje zasnovano na regularnim izrazima.

Za razvoj:

```
pip install -e '.[dev]'
```

## Korištenje

Analiziraj objavljeni članak na Wikipediji:

```
wiki-mos-audit "Gettysburg Address"
```

Analiziraj putem URL-a:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Analiziraj lokalnu datoteku vikiteksta:

```
wiki-mos-audit "Article" --wikitext-file article_corrected.txt
```

Paketna analiza direktorija s datotekama vikiteksta:

```
wiki-mos-audit --dir ./articles/
```

Preskoči API provjere (vanmrežni način rada):

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

### Opcionalne provjere

Ove provjere su podrazumijevano isključene jer su spore ili zahtijevaju pristup mreži:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Automatsko ispravljanje

Sigurne mehaničke ispravke (razmaci, formatiranje) mogu se primijeniti automatski:

```
wiki-mos-audit "Article" --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Pregled opisa ispravki bez upisivanja u datoteku:

```
wiki-mos-audit "Article" --wikitext-file article.txt --fix --dry-run --verbose
```

### Način poređenja (Diff)

Uporedi lokalni vikitekst s objavljenom verzijom:

```
wiki-mos-audit "Article" --wikitext-file article_corrected.txt --diff
```

### Postavke i konfiguracija

Kreirajte datoteku `.wiki-mos-audit.toml` da prilagodite pragove ili onemogućite pojedinačne provjere:

```toml
[audit]
min_severity = "low"
disabled_checks = ["mos-aviation-style"]

[thresholds]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Proslijedite je eksplicitno:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Lokalizacija

Pomoć za CLI, dijagnostičke poruke i elementi tekstualnih i HTML izvještaja podržavaju 48 lokala (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`) bez ikakvih dodatnih zavisnosti. Razrješavanje prvo provjerava `--lang` (različito od `--language`, koje bira jezičko izdanje Wikipedije), zatim `LC_ALL`, `LC_MESSAGES` i `LANG`, uz povratak na `en`. Ključevi JSON izlaza i šabloni vikiteksta ostaju nepromijenjeni.

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

## Licenca

MIT
