# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · **తెలుగు** · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Wikipedia వ్యాసాల కోసం మొదటి-దశ [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) ఆడిటర్.

## ఇది ఎందుకు రూపొందించబడింది

నేను Wikipediaను దిద్దుబాటు చేస్తుంటాను. నిరంతరం కాకపోయినా, ఒక సరళిని గమనించేంతగా చేస్తాను: నేను శుభ్రం చేయడానికి ఒక వ్యాసాన్ని తెరిచిన ప్రతిసారీ, నా మనసులో అదే చెక్‌లిస్ట్‌ను అమలు చేస్తున్నాను. తేదీలు స్థిరంగా ఉన్నాయా? ఏవైనా అస్పష్టమైన పదాలు ఉన్నాయా? ఎవరైనా మూలాలలో నేరుగా URLలను వదిలేశారా? ఇవి కూడా చూడండి విభాగం అనవసరంగా పెరిగిందా? దిగువ విభాగాలు సరైన క్రమంలో ఉన్నాయా?

వరుసగా మూడు లేదా నాలుగు సార్లు అవే డజను సమస్యల కోసం చేతితో వెతికిన తర్వాత, నేను ఒక స్క్రిప్ట్ రాశాను. ఆ స్క్రిప్ట్ క్రమంగా పెరిగింది. ఇప్పుడు ఇది నేను చేతితో చేసే 30కి పైగా అంశాలను తనిఖీ చేస్తుంది మరియు అలసిపోయిన మంగళవారం సాయంత్రం నేను గమనించలేని వాటిని కూడా పట్టుకుంటుంది.

ఇది సంపాదకీయ విచక్షణకు ప్రత్యామ్నాయం కాదు. ఇది కేవలం సమస్యలను గుర్తించే టూల్ మాత్రమే. ఇది ఏమి రాయాలో కాదు, ఎక్కడ చూడాలో చెబుతుంది.

## ఇది ఏమి తనిఖీ చేస్తుంది

**శైలి మరియు ధోరణి**
- అస్పష్టమైన పదాలు (MOS:WEASEL), అతిశయోక్తి పదాలు (MOS:PEACOCK)
- కాలక్రమేణా పాతబడిపోయే సాపేక్ష కాల వ్యక్తీకరణలు ("recently", "currently")
- AI ద్వారా రూపొందించబడిన కంటెంట్ సంకేతాలు: వ్యాస పాఠ్యంలో అతిగా ఆపాదించడం (WP:AISIGNS), వ్యాసరచన లాంటి శైలి (WP:NOTESSAY)
- MOS:INDIGENOUS పదజాల హెచ్చరికలు
- MOS:AVIATION హోదా ఫార్మాటింగ్
- MOS:MILITARY ఆధారం లేని ప్రాణనష్ట ప్రకటనలు

**నిర్మాణం**
- ఉపోద్ఘాతం పొడవు మరియు పేరాల సంఖ్య (MOS:LEAD)
- MOS:LAYOUT ప్రకారం విభాగాల క్రమం
- చిన్న లేదా తగినంతగా అభివృద్ధి చెందని విభాగాలు
- మూలాలు లేని విభాగాలు (100+ పదాలు, `<ref>` లేకపోవడం)
- ఇవి కూడా చూడండి విభాగం విస్తరణ
- వ్యాస పాఠ్యంలో నేరుగా ఉన్న బాహ్య URLలు
- కోట్ టెంప్లేట్ సాంద్రత

**మూలాలు మరియు ఉల్లేఖనాలు**
- `<ref>` ట్యాగ్‌ల లోపల నేరుగా ఉన్న URLలు (ఉల్లేఖన టెంప్లేట్ లేదు)
- ISBN చెక్ డిజిట్ ధృవీకరణ
- ఉల్లేఖన టెంప్లేట్‌లలో లోపభూయిష్ట URLలు
- పనిచేయని బాహ్య లింకులు (ఐచ్ఛికం, నెమ్మదిగా ఉంటుంది)

**వర్గాలు మరియు లింకులు**
- లోపించిన వర్గాలు
- వర్గాల నాణ్యత (తగినన్ని వర్గాలు లేకపోవడం, మరీ విస్తృతంగా ఉండటం)
- రెడ్-లింక్ గుర్తింపు (లేని వ్యాసాలకు వికీలింకులు)
- రెడ్-లింక్ వర్గాలు
- అయోమయ నివృత్తి పేజీ లింకులు
- అధిక లింకింగ్ (MOS:OVERLINK)

**ఇన్ఫోబాక్స్**
- పారామీటర్ల సంఖ్య మరియు జాబితా సాంద్రత (అధిక విస్తరణ గుర్తింపు)
- సాధారణంగా ఆశించే పారామీటర్లు లేకపోవడం
- MOS:MILHIST ఇన్ఫోబాక్స్ సంకేతాలు

**ఇతర అంశాలు**
- సంక్షిప్త వివరణ నాణ్యత (లేకపోవడం, మరీ పొడవుగా ఉండటం, శీర్షికతో సరిపోలడం)
- నిర్వహణ టెంప్లేట్ జాబితా
- సోదర ప్రాజెక్ట్ లింక్ శుభ్రత (MOS:SISTER)
- అనాథ వ్యాస గుర్తింపు (వచ్చే వికీలింకులు లేకపోవడం)
- సంభావ్య బ్యాక్‌లింక్ ఆవిష్కరణ
- టైమ్‌లైన్/లైవ్‌బ్లాగ్ శీర్షిక నమూనాలు

ప్రతి తనిఖీ తీవ్రత-రేటెడ్ సమస్యను (తక్కువ/మధ్యస్థం/అధికం) స్కోరు తగ్గింపుతో అందిస్తుంది. లోపాలు లేని స్వచ్ఛమైన వ్యాసానికి 100 స్కోరు వస్తుంది.

## ఇన్‌స్టాలేషన్

```
pip install .
```

mwparserfromhell ఒక తప్పనిసరి డిపెండెన్సీ. ఖచ్చితమైన టెంప్లేట్, శీర్షిక మరియు వికీలింక్ గుర్తింపు కోసం ఇది AST-ఆధారిత వికీటెక్స్ట్ పార్సింగ్‌ను అందిస్తుంది. దానిని కంపైల్ చేయలేకపోతే (C కంపైలర్ అందుబాటులో లేకపోతే), ఈ టూల్ స్వయంచాలకంగా regex-ఆధారిత పార్సింగ్‌కు మారుతుంది.

అభివృద్ధి కోసం:

```
pip install -e '.[dev]'
```

## వినియోగం

లైవ్ Wikipedia వ్యాసాన్ని ఆడిట్ చేయండి:

```
wiki-mos-audit "Gettysburg Address"
```

URL నుండి ఆడిట్ చేయండి:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

స్థానిక వికీటెక్స్ట్ ఫైల్‌ను ఆడిట్ చేయండి:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

వికీటెక్స్ట్ ఫైల్‌ల డైరెక్టరీని బ్యాచ్ ఆడిట్ చేయండి:

```
wiki-mos-audit --dir ./articles/
```

API తనిఖీలను దాటవేయండి (ఆఫ్‌లైన్ మోడ్):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### అవుట్‌పుట్ ఫార్మాట్‌లు

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### ఐచ్ఛిక తనిఖీలు

ఇవి నెమ్మదిగా ఉంటాయి లేదా వీటికి నెట్‌వర్క్ యాక్సెస్ అవసరం కనుక డిఫాల్ట్‌గా ఆఫ్ చేసి ఉంటాయి:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### ఆటో-ఫిక్స్

సురక్షితమైన యాంత్రిక సవరణలు (ఖాళీలు, ఫార్మాటింగ్) స్వయంచాలకంగా వర్తింపజేయబడతాయి:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

రాయకుండానే ముందస్తుగా చూడండి:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### డిఫ్ మోడ్

స్థానిక వికీటెక్స్ట్‌ను లైవ్ వెర్షన్‌తో పోల్చండి:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### కాన్ఫిగరేషన్

పరిమితులను సర్దుబాటు చేయడానికి లేదా నిర్దిష్ట తనిఖీలను నిలిపివేయడానికి `.wiki-mos-audit.toml` ఫైల్‌ను సృష్టించండి:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

దానిని స్పష్టంగా అందించండి:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### స్థానికీకరణ

CLI సహాయం, డయాగ్నస్టిక్స్ మరియు టెక్స్ట్/HTML నివేదిక క్రోమ్ ఎటువంటి అదనపు డిపెండెన్సీలు లేకుండా 45 లోకేల్స్‌కు (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) మద్దతు ఇస్తాయి. నిర్ధారణ `--lang` (ఇది Wikipedia ఎడిషన్‌ను ఎంచుకునే `--language` కంటే భిన్నమైనది), ఆపై `LC_ALL`, `LC_MESSAGES`, మరియు `LANG`లను తనిఖీ చేసి, చివరకు `en`కు తిరిగి వస్తుంది. JSON అవుట్‌పుట్ కీలు మరియు వికీటెక్స్ట్ టెంప్లేట్‌లు మారకుండా అలాగే ఉంటాయి.

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

## అభివృద్ధి

పరీక్షలను అమలు చేయండి:

```
python -m pytest tests/ -x -q
```

లింట్:

```
ruff check src/ tests/
```

## అవసరాలు

- Python 3.12+
- mwparserfromhell

## లైసెన్స్

MIT
