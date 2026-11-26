# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · **Filipino** · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Isang unang-hakbang na auditor ng [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) para sa mga artikulo sa Wikipedia.

## Bakit ito umiiral

Nag-e-edit ako sa Wikipedia. Hindi palagi, pero sapat na para mapansin ang isang pattern: tuwing magbubukas ako ng artikulo para linisin, parehong mental checklist ang sinusundan ko. Magkakatugma ba ang mga petsa? May mga weasel word ba? May nakaiwan ba ng mga bare URL sa mga ref? Masyado na bang mahaba ang seksyong See also? Nasa tamang pagkakasunod-sunod ba ang mga seksyon sa ibaba?

Pagkatapos ng pangatlo o pang-apat na beses na manu-manong paghahanap sa parehong dosenang problema nang sunod-sunod, gumawa ako ng script. Lumaki ang script na iyon. Ngayon, sinusuri na nito ang mahigit 30 bagay na dati kong ginagawa nang mano-mano, at nahuhuli nito ang mga bagay na makakaligtaan ko sa isang nakakapagod na Martes ng gabi.

Hindi ito kapalit ng pagpapasya ng editor. Ito ay isang triage tool. Sinasabi nito kung saan titingin, hindi kung ano ang isusulat.

## Mga sinusuri nito

**Estilo at tono**
- Mga weasel word (MOS:WEASEL), mga peacock term (MOS:PEACOCK)
- Mga ekspresyon ng relatibong oras ("recently", "currently") na hindi tumatanda nang maayos
- Mga senyales ng nilalamang gawa ng AI: labis na attribution sa teksto ng katawan (WP:AISIGNS), pananalitang parang sanaysay (WP:NOTESSAY)
- Mga flag ng terminolohiyang MOS:INDIGENOUS
- Pag-format ng designasyon ng MOS:AVIATION
- Mga pahayag ng nasawi na walang sanggunian ayon sa MOS:MILITARY

**Estruktura**
- Haba ng lead at bilang ng talata (MOS:LEAD)
- Pagkakasunod-sunod ng mga seksyon laban sa MOS:LAYOUT
- Maiikli o kulang sa laman na mga seksyon
- Mga seksyong walang sanggunian (100+ na salita, walang `<ref>`)
- Sobrang dami ng laman sa seksyong See also
- Mga bare external URL sa katawan ng artikulo
- Dalas ng mga quote template

**Mga sanggunian at pagsipi**
- Mga bare URL sa loob ng mga `<ref>` tag (walang cite template)
- Pag-validate ng ISBN check digit
- Mga sirang URL sa mga citation template
- Mga sirang external link (opt-in, mabagal)

**Mga kategorya at link**
- Mga nawawalang kategorya
- Kalidad ng kategorya (kulang sa kategorya, masyadong malawak)
- Pagtukoy ng red-link (mga wikilink patungo sa hindi umiiral na mga artikulo)
- Mga red-link na kategorya
- Mga link sa pahina ng disambiguation
- Sobrang pag-link (MOS:OVERLINK)

**Infobox**
- Bilang ng parameter at dalas ng listahan (pagtukoy ng sobrang dami)
- Mga nawawalang karaniwang inaasahang parameter
- Mga senyales ng infobox ng MOS:MILHIST

**Iba pa**
- Kalidad ng maikling paglalarawan (nawawala, masyadong mahaba, kapareho ng pamagat)
- Imbentaryo ng maintenance template
- Kaayusan ng link ng sister project (MOS:SISTER)
- Pagtukoy ng orphan (walang pumapasok na wikilink)
- Pagtuklas ng mga potensyal na backlink
- Mga pattern ng heading ng timeline/liveblog

Ang bawat pagsusuri ay nagbubunga ng isyung may antas ng kalubhaan (low/medium/high) na may bawas sa score. Ang isang malinis na artikulo ay may score na 100.

## Pag-install

```
pip install .
```

Kinakailangang dependency ang mwparserfromhell. Nagbibigay ito ng pag-parse ng wikitext na nakabatay sa AST para sa tumpak na pagtukoy ng template, heading, at wikilink. Kung hindi ito ma-compile (walang available na C compiler), awtomatikong bumabalik ang tool sa pag-parse na nakabatay sa regex.

Para sa pag-develop:

```
pip install -e '.[dev]'
```

## Paggamit

I-audit ang isang live na artikulo sa Wikipedia:

```
wiki-mos-audit "Gettysburg Address"
```

I-audit mula sa isang URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

I-audit ang isang lokal na wikitext file:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Sabay-sabay na i-audit ang isang direktoryo ng mga wikitext file:

```
wiki-mos-audit --dir ./articles/
```

Laktawan ang mga pagsusuri sa API (offline mode):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Mga format ng output

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Mga opsyonal na pagsusuri

Naka-off ang mga ito bilang default dahil mabagal ang mga ito o nangangailangan ng access sa network:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Awtomatikong pag-ayos

Maaaring awtomatikong ilapat ang mga ligtas na mekanikal na pag-aayos (whitespace, pag-format):

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

I-preview nang hindi nagsusulat:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Diff mode

Ihambing ang lokal na wikitext laban sa live na bersyon:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Configuration

Gumawa ng `.wiki-mos-audit.toml` file upang isaayos ang mga threshold o i-disable ang mga partikular na pagsusuri:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Ipasa ito nang tahasan:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Localization

Sinusuportahan ng tulong sa CLI, mga diagnostic, at teksto/HTML na report chrome ang 45 locale (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) nang walang dagdag na dependency. Sinusuri ng pagresolba ang `--lang` (iba sa `--language`, na pumipili ng edisyon ng Wikipedia), pagkatapos ay `LC_ALL`, `LC_MESSAGES`, at `LANG`, at bumabalik sa `en`. Nananatiling hindi nagbabago ang mga JSON output key at wikitext template.

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

## Pag-develop

Patakbuhin ang mga test:

```
python -m pytest tests/ -x -q
```

I-lint:

```
ruff check src/ tests/
```

## Mga Kinakailangan

- Python 3.12+
- mwparserfromhell

## Lisensya

MIT
