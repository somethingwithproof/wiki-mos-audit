# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · **हिन्दी** · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Wikipedia लेखों के लिए एक प्रथम-चरणीय [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) ऑडिटर।

## यह क्यों मौजूद है

मैं Wikipedia संपादित करता हूँ। लगातार नहीं, लेकिन इतना कि मुझे एक पैटर्न दिखने लगा: जब भी मैं किसी लेख को सुधारने के लिए खोलता था, मैं वही मानसिक चेकलिस्ट चला रहा होता था। क्या तिथियां सुसंगत हैं? क्या कोई अस्पष्ट पक्षपाती शब्द हैं? क्या किसी ने संदर्भों में केवल खाली URL छोड़ दिए हैं? क्या See also अनुभाग अत्यधिक लंबा है? क्या नीचे के अनुभाग सही क्रम में हैं?

लगातार तीसरी या चौथी बार मैनुअल रूप से उन्हीं दर्जन भर समस्याओं को खोजने के बाद, मैंने एक स्क्रिप्ट लिखी। वह स्क्रिप्ट बढ़ती गई। अब यह 30 से अधिक चीजों की जांच करती है जो मैं हाथ से करता था, और यह उन गलतियों को भी पकड़ती है जो मैं किसी थके हुए मंगलवार की शाम को चूक जाता।

यह संपादकीय निर्णय का विकल्प नहीं है। यह एक ट्रायएज टूल है। यह आपको बताता है कि कहां देखना है, न कि क्या लिखना है।

## यह क्या जांचता है

**शैली और लहजा**
- अस्पष्ट पक्षपाती शब्द (MOS:WEASEL), अतिशयोक्तिपूर्ण शब्द (MOS:PEACOCK)
- सापेक्ष समय अभिव्यक्तियाँ ("हाल ही में", "वर्तमान में") जो समय के साथ पुरानी पड़ जाती हैं
- AI-जनित सामग्री के संकेत: मुख्य पाठ में अत्यधिक श्रेय देना (WP:AISIGNS), निबंध जैसा वाक्यांश (WP:NOTESSAY)
- MOS:INDIGENOUS शब्दावली ध्वज
- MOS:AVIATION पदनाम प्रारूपण
- MOS:MILITARY बिना संदर्भ वाले हताहत विवरण

**संरचना**
- परिचय की लंबाई और अनुच्छेद संख्या (MOS:LEAD)
- MOS:LAYOUT के अनुसार अनुभाग क्रम
- छोटे या अविकसित अनुभाग
- बिना संदर्भ वाले अनुभाग (100+ शब्द, कोई `<ref>` नहीं)
- See also अनुभाग का अनावश्यक विस्तार
- लेख के मुख्य भाग में खाली बाहरी URL
- उद्धरण टेम्पलेट घनत्व

**संदर्भ और उद्धरण**
- `<ref>` टैग के अंदर खाली URL (कोई cite टेम्पलेट नहीं)
- ISBN चेक अंक सत्यापन
- उद्धरण टेम्पलेट्स में विकृत URL
- मृत बाहरी लिंक (ऑप्ट-इन, धीमा)

**श्रेणियां और लिंक**
- अनुपलब्ध श्रेणियां
- श्रेणी गुणवत्ता (अपर्याप्त श्रेणीबद्ध, अत्यधिक व्यापक)
- रेड-लिंक पहचान (गैर-मौजूद लेखों के विकिलिंक)
- रेड-लिंक श्रेणियां
- बहुविकल्पी पृष्ठ लिंक
- अत्यधिक लिंकिंग (MOS:OVERLINK)

**इन्फोबॉक्स**
- पैरामीटर संख्या और सूची घनत्व (अत्यधिक विस्तार का पता लगाना)
- सामान्यतः अपेक्षित पैरामीटरों का न होना
- MOS:MILHIST इन्फोबॉक्स संकेत

**अन्य**
- संक्षिप्त विवरण गुणवत्ता (अनुपलब्ध, बहुत लंबा, शीर्षक से मेल खाता हुआ)
- रखरखाव टेम्पलेट सूची
- सहयोगी परियोजना लिंक स्वच्छता (MOS:SISTER)
- अनाथ पृष्ठ पहचान (कोई आवक विकिलिंक नहीं)
- संभावित बैकलिंग खोज
- समयरेखा/लाइवब्लॉग शीर्षक पैटर्न

प्रत्येक जांच अंक कटौती के साथ गंभीरता-रेटेड समस्या (निम्न/मध्यम/उच्च) उत्पन्न करती है। एक स्वच्छ लेख को 100 अंक मिलते हैं।

## स्थापना

```
pip install .
```

mwparserfromhell एक आवश्यक निर्भरता है। यह सटीक टेम्पलेट, शीर्षक और विकिलिंक पहचान के लिए AST-आधारित विकिटेक्स्ट पार्सिंग प्रदान करता है। यदि इसे संकलित नहीं किया जा सकता (कोई C कंपाइलर उपलब्ध नहीं है), तो टूल स्वचालित रूप से regex-आधारित पार्सिंग पर वापस आ जाता है।

विकास के लिए:

```
pip install -e '.[dev]'
```

## उपयोग

एक लाइव Wikipedia लेख का ऑडिट करें:

```
wiki-mos-audit "Gettysburg Address"
```

एक URL से ऑडिट करें:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

एक स्थानीय विकिटेक्स्ट फ़ाइल का ऑडिट करें:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

विकिटेक्स्ट फ़ाइलों की एक निर्देशिका का बैच ऑडिट करें:

```
wiki-mos-audit --dir ./articles/
```

API जांच छोड़ें (ऑफ़लाइन मोड):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### आउटपुट प्रारूप

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### वैकल्पिक जांच

ये डिफ़ॉल्ट रूप से बंद हैं क्योंकि ये धीमे हैं या इन्हें नेटवर्क एक्सेस की आवश्यकता होती है:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### स्वतः-सुधार

सुरक्षित यांत्रिक सुधार (व्हाइटस्पेस, प्रारूपण) स्वचालित रूप से लागू किए जा सकते हैं:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

लिखे बिना पूर्वावलोकन करें:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### अंतर मोड

लाइव संस्करण से स्थानीय विकिटेक्स्ट की तुलना करें:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### कॉन्फ़िगरेशन

सीमा मान समायोजित करने या विशिष्ट जांच अक्षम करने के लिए `.wiki-mos-audit.toml` फ़ाइल बनाएं:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

इसे स्पष्ट रूप से पास करें:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### स्थानीयकरण

CLI सहायता, डायग्नोस्टिक्स और पाठ/HTML रिपोर्ट क्रोम बिना किसी अतिरिक्त निर्भरता के 45 लोकेल (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) का समर्थन करते हैं। रिज़ॉल्यूशन `--lang` (`--language` से अलग, जो Wikipedia संस्करण का चयन करता है), फिर `LC_ALL`, `LC_MESSAGES`, और `LANG` की जांच करता है, और कुछ न मिलने पर `en` पर वापस आ जाता है। JSON आउटपुट कुंजियाँ और विकिटेक्स्ट टेम्पलेट अपरिवर्तित रहते हैं।

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

## विकास

परीक्षण चलाएं:

```
python -m pytest tests/ -x -q
```

लिंट:

```
ruff check src/ tests/
```

## आवश्यकताएं

- Python 3.12+
- mwparserfromhell

## लाइसेंस

MIT
