# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · **தமிழ்** · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Wikipedia கட்டுரைகளுக்கான முதற்கட்ட [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) தணிக்கையாளர்.

## இது ஏன் உள்ளது

நான் Wikipedia வில் தொகுக்கிறேன். தொடர்ந்து அல்ல, ஆனால் ஒரு வடிவத்தைக் கவனிக்கத் தொடங்கும் அளவுக்குப் போதுமான அளவு: ஒவ்வொரு முறையும் ஒரு கட்டுரையைச் சுத்தம் செய்யத் திறக்கும்போது, அதே மனப் பட்டியலைச் சரிபார்த்துக் கொண்டிருந்தேன். தேதிகள் சீராக உள்ளனவா? மழுப்பலான சொற்கள் ஏதேனும் உள்ளனவா? மேற்கோள்களில் வெறும் URL களை யாராவது விட்டுவிட்டார்களா? மேலும் காண்க பகுதி வீங்கியுள்ளதா? கீழ்-பகுதி பிரிவுகள் சரியான வரிசையில் உள்ளனவா?

மூன்றாவது அல்லது நான்காவது முறையாக வரிசையாக அதே டஜன் சிக்கல்களைக் கைமுறையாகத் தேடிய பிறகு, நான் ஒரு ஸ்கிரிப்டை எழுதினேன். அந்த ஸ்கிரிப்ட் வளர்ந்தது. இப்போது நான் கையால் செய்து கொண்டிருந்த 30+ விஷயங்களை இது சரிபார்க்கிறது, மேலும் சோர்வான செவ்வாய் மாலையில் நான் தவறவிடக்கூடிய விஷயங்களையும் இது பிடிக்கிறது.

இது ஆசிரியர் தீர்ப்புக்கு மாற்றல்ல. இது ஒரு முன்னுரிமைப்படுத்தும் கருவி. எதை எழுத வேண்டும் என்பதை அல்ல, எங்கே பார்க்க வேண்டும் என்பதை இது உங்களுக்குச் சொல்கிறது.

## இது என்ன சரிபார்க்கிறது

**நடை மற்றும் தொனி**
- மழுப்பலான சொற்கள் (MOS:WEASEL), மிகைப்படுத்தும் சொற்கள் (MOS:PEACOCK)
- காலாவதியாகும் ஒப்பீட்டு நேர வெளிப்பாடுகள் ("recently", "currently")
- AI-உருவாக்கிய உள்ளடக்கச் சமிக்ஞைகள்: உடல் உரையில் அதிகப்படியான பண்புக்கூறு (WP:AISIGNS), கட்டுரை போன்ற சொற்றொடர் (WP:NOTESSAY)
- MOS:INDIGENOUS கலைச்சொல் குறிப்புகள்
- MOS:AVIATION பதவி வடிவமைப்பு
- MOS:MILITARY சான்றற்ற உயிரிழப்பு அறிக்கைகள்

**கட்டமைப்பு**
- முன்னுரை நீளம் மற்றும் பத்தி எண்ணிக்கை (MOS:LEAD)
- MOS:LAYOUT உடன் ஒப்பிட்டுப் பிரிவு வரிசைப்படுத்தல்
- குறுகிய அல்லது முழுமையடையாத பிரிவுகள்
- மேற்கோளற்ற பிரிவுகள் (100+ சொற்கள், `<ref>` இல்லை)
- மேலும் காண்க பிரிவு வீக்கம்
- கட்டுரை உடலில் வெறும் வெளிப்புற URL கள்
- மேற்கோள் வார்ப்புரு அடர்த்தி

**குறிப்புகள் மற்றும் சான்றுகள்**
- `<ref>` குறிச்சொற்களுக்குள் வெறும் URL கள் (cite வார்ப்புரு இல்லை)
- ISBN சரிபார்ப்பு இலக்கச் சரிபார்ப்பு
- சான்று வார்ப்புருக்களில் தவறாக வடிவமைக்கப்பட்ட URL கள்
- செயல்படாத வெளிப்புற இணைப்புகள் (விருப்பத் தேர்வு, மெதுவானது)

**பகுப்புகள் மற்றும் இணைப்புகள்**
- விடுபட்ட பகுப்புகள்
- பகுப்புத் தரம் (குறைவான பகுப்புகள், மிகவும் பரந்தவை)
- சிவப்பு-இணைப்புக் கண்டறிதல் (இல்லாத கட்டுரைகளுக்கான விக்கி இணைப்புகள்)
- சிவப்பு-இணைப்புப் பகுப்புகள்
- பக்கவழி நெறிப்படுத்தல் பக்க இணைப்புகள்
- அதிகப்படியான இணைப்பிடுதல் (MOS:OVERLINK)

**தகவல் பெட்டி**
- அளவுரு எண்ணிக்கை மற்றும் பட்டியல் அடர்த்தி (வீக்கக் கண்டறிதல்)
- பொதுவாக எதிர்பார்க்கப்படும் விடுபட்ட அளவுருக்கள்
- MOS:MILHIST தகவல் பெட்டிச் சமிக்ஞைகள்

**மற்றவை**
- குறுகிய விளக்கத் தரம் (இல்லாதது, மிக நீளமானது, தலைப்புடன் பொருந்துவது)
- பராமரிப்பு வார்ப்புருப் பட்டியல்
- சகோதரத் திட்ட இணைப்புத் தூய்மை (MOS:SISTER)
- அனாதைப் பக்கக் கண்டறிதல் (உள்வரும் விக்கி இணைப்புகள் இல்லை)
- சாத்தியமான பின்னிணைப்புக் கண்டறிதல்
- காலவரிசை/நேரலை வலைப்பதிவுத் தலைப்பு வடிவங்கள்

ஒவ்வொரு சோதனையும் மதிப்பெண் கழிப்புடன் கூடிய தீவிரத்தன்மை-மதிப்பிடப்பட்ட சிக்கலை (குறைவு/நடுத்தரம்/உயர்வு) உருவாக்குகிறது. ஒரு தூய்மையான கட்டுரை 100 மதிப்பெண்கள் பெறும்.

## நிறுவல்

```
pip install .
```

mwparserfromhell என்பது ஒரு தேவையான சார்பு ஆகும். துல்லியமான வார்ப்புரு, தலைப்பு மற்றும் விக்கி இணைப்புக் கண்டறிதலுக்காக இது AST-அடிப்படையிலான wikitext பாகுபடுத்தலை வழங்குகிறது. அதைத் தொகுக்க முடியாவிட்டால் (C தொகுப்பி இல்லையெனில்), கருவி தானாகவே regex-அடிப்படையிலான பாகுபடுத்தலுக்கு மாறும்.

வளர்ச்சிக்கு:

```
pip install -e '.[dev]'
```

## பயன்பாடு

நேரடி Wikipedia கட்டுரையைத் தணிக்கை செய்ய:

```
wiki-mos-audit "Gettysburg Address"
```

ஒரு URL இலிருந்து தணிக்கை செய்ய:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

உள்ளூர் wikitext கோப்பைத் தணிக்கை செய்ய:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

wikitext கோப்புகளின் கோப்பகத்தைத் தொகுப்பாகத் தணிக்கை செய்ய:

```
wiki-mos-audit --dir ./articles/
```

API சோதனைகளைத் தவிர்க்க (ஆஃப்லைன் பயன்முறை):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### வெளியீட்டு வடிவங்கள்

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### விருப்பச் சோதனைகள்

இவை மெதுவாக இருப்பதால் அல்லது பிணைய அணுகல் தேவைப்படுவதால் இயல்புநிலையில் முடக்கப்பட்டிருக்கும்:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### தானியங்கிச் சரிசெய்தல்

பாதுகாப்பான இயந்திரத் திருத்தங்களை (இடைவெளி, வடிவமைப்பு) தானாகவே பயன்படுத்தலாம்:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

எழுதாமல் முன்னோட்டமிட:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### வேறுபாடு (Diff) பயன்முறை

உள்ளூர் wikitext ஐ நேரடிப் பதிப்புடன் ஒப்பிட:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### உள்ளமைவு

வரம்புகளைச் சரிசெய்ய அல்லது குறிப்பிட்ட சோதனைகளை முடக்க `.wiki-mos-audit.toml` கோப்பை உருவாக்கவும்:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

அதை வெளிப்படையாக அனுப்ப:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### உள்ளூர்மயமாக்கல்

CLI உதவி, நோயறிதல்கள் மற்றும் உரை/HTML அறிக்கை முகப்பு ஆகியவை எந்தக் கூடுதல் சார்புகளும் இல்லாமல் 45 மொழிகளை (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ஆதரிக்கின்றன. தீர்மானம் முதலில் `--lang` (Wikipedia பதிப்பைத் தேர்ந்தெடுக்கும் `--language` இலிருந்து வேறுபட்டது), பின்னர் `LC_ALL`, `LC_MESSAGES` மற்றும் `LANG` ஆகியவற்றைச் சரிபார்த்து, இறுதியில் `en` க்குத் திரும்புகிறது. JSON வெளியீட்டு விசைகளும் wikitext வார்ப்புருக்களும் மாறாமல் இருக்கும்.

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

## வளர்ச்சி

சோதனைகளை இயக்க:

```
python -m pytest tests/ -x -q
```

Lint செய்ய:

```
ruff check src/ tests/
```

## தேவைகள்

- Python 3.12+
- mwparserfromhell

## உரிமம்

MIT
