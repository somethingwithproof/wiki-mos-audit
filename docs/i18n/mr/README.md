# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · **मराठी** · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Wikipedia लेखांसाठी प्रथम-टप्पा [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) ऑडिटर.

## हे का अस्तित्वात आहे

मी Wikipedia संपादित करतो. सतत नाही, पण इतके की मला एक पॅटर्न जाणवू लागला: प्रत्येक वेळी जेव्हा मी लेख स्वच्छ करण्यासाठी उघडत असे, तेव्हा मी तीच मानसिक चेकलिस्ट चालवत असे. तारखा सुसंगत आहेत का? काही मोघम शब्द (weasel words) आहेत का? कोणी संदर्भांमध्ये नुसत्या URL सोडल्या आहेत का? See also विभाग अवाजवी मोठा झाला आहे का? तळाशी असलेले विभाग योग्य क्रमाने आहेत का?

सलग तिसऱ्या किंवा चौथ्यांदा एकाच डझनभर समस्या हाताने शोधल्यानंतर, मी एक स्क्रिप्ट लिहिली. ती स्क्रिप्ट वाढत गेली. आता ती 30+ गोष्टी तपासते ज्या मी हाताने करत होतो, आणि थकलेल्या मंगळवारी संध्याकाळी माझ्याकडून सुटू शकणाऱ्या गोष्टी ती पकडते.

हा संपादकीय निर्णयाला पर्याय नाही. हे एक वर्गीकरण (triage) साधन आहे. हे तुम्हाला काय लिहायचे ते नाही, तर कुठे पाहायचे ते सांगते.

## हे काय तपासते

**शैली आणि सूर**
- मोघम शब्द (MOS:WEASEL), भपकेदार शब्द (MOS:PEACOCK)
- सापेक्ष काळाचे उल्लेख ("recently", "currently") जे कालांतराने कालबाह्य होतात
- AI-निर्मित सामग्रीची चिन्हे: मुख्य मजकुरातील अति-अवलंबन (WP:AISIGNS), निबंधसदृश वाक्यरचना (WP:NOTESSAY)
- MOS:INDIGENOUS परिभाषा चिन्हे
- MOS:AVIATION पदनाम फॉरमॅटिंग
- MOS:MILITARY विनासंदर्भ जीवितहानीची विधाने

**रचना**
- प्रास्ताविकाची (Lead) लांबी आणि परिच्छेद संख्या (MOS:LEAD)
- MOS:LAYOUT नुसार विभागांचा क्रम
- लहान किंवा अपूर्ण विकसित विभाग
- संदर्भ नसलेले विभाग (100+ शब्द, `<ref>` नाही)
- See also विभागाचा अवाजवी विस्तार
- लेखाच्या मुख्य भागातील नुसत्या बाह्य URL
- अवतरण टेम्पलेट घनता

**संदर्भ आणि उद्धरणे**
- `<ref>` टॅगच्या आत नुसत्या URL (cite टेम्पलेट नाही)
- ISBN तपासणी अंक पडताळणी
- उद्धरण टेम्पलेट्समधील सदोष URL
- मृत बाह्य दुवे (ऐच्छिक, संथ)

**श्रेण्या आणि दुवे**
- गहाळ श्रेण्या
- श्रेणी गुणवत्ता (कमी श्रेण्या, अतिव्यापक)
- रेड-लिंक शोध (अस्तित्वात नसलेल्या लेखांसाठी विकिलिंक्स)
- रेड-लिंक श्रेण्या
- निःसंदिग्धीकरण (Disambiguation) पृष्ठ दुवे
- अति-दुवे जोडणे (MOS:OVERLINK)

**माहितीचौकट (Infobox)**
- पॅरामीटर संख्या आणि सूची घनता (अवाजवी विस्तार शोध)
- सामान्यतः अपेक्षित असलेले गहाळ पॅरामीटर्स
- MOS:MILHIST माहितीचौकट चिन्हे

**इतर**
- लघु वर्णन गुणवत्ता (गहाळ, खूप मोठे, शीर्षकाशी जुळणारे)
- देखभाल टेम्पलेट सूची
- भगिनी प्रकल्प दुवा स्वच्छता (MOS:SISTER)
- अनाथ पृष्ठ शोध (कोणतेही येणारे विकिलिंक्स नाहीत)
- संभाव्य बॅकलिंक शोध
- टाइमलाइन/लाइव्हब्लॉग शीर्षक पॅटर्न

प्रत्येक तपासणी गुण वजावटीसह तीव्रता-श्रेणीबद्ध समस्या (low/medium/high) तयार करते. स्वच्छ लेखाला 100 गुण मिळतात.

## इंस्टॉलेशन

```
pip install .
```

mwparserfromhell हे एक आवश्यक अवलंबित्व आहे. हे अचूक टेम्पलेट, शीर्षक आणि विकिलिंक शोधासाठी AST-आधारित विकिटेक्स्ट पार्सिंग प्रदान करते. जर ते कंपाईल होऊ शकत नसेल (C कंपाइलर उपलब्ध नसल्यास), तर हे साधन आपोआप regex-आधारित पार्सिंगवर परत जाते.

विकासासाठी:

```
pip install -e '.[dev]'
```

## वापर

थेट Wikipedia लेखाचे ऑडिट करा:

```
wiki-mos-audit "Gettysburg Address"
```

URL वरून ऑडिट करा:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

स्थानिक विकिटेक्स्ट फाइलचे ऑडिट करा:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

विकिटेक्स्ट फाइल्सच्या डिरेक्टरीचे बॅच ऑडिट करा:

```
wiki-mos-audit --dir ./articles/
```

API तपासण्या वगळा (ऑफलाइन मोड):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### आउटपुट फॉरमॅट्स

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### ऐच्छिक तपासण्या

या डीफॉल्टनुसार बंद असतात कारण त्या संथ आहेत किंवा त्यांना नेटवर्क प्रवेश आवश्यक असतो:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### स्वयं-दुरुस्ती (Auto-fix)

सुरक्षित यांत्रिक दुरुस्त्या (व्हाइटस्पेस, फॉरमॅटिंग) आपोआप लागू केल्या जाऊ शकतात:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

न लिहिता पूर्वावलोकन पहा:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### फरक मोड (Diff mode)

स्थानिक विकिटेक्स्टची थेट आवृत्तीशी तुलना करा:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### कॉन्फिगरेशन

मर्यादा समायोजित करण्यासाठी किंवा विशिष्ट तपासण्या अक्षम करण्यासाठी `.wiki-mos-audit.toml` फाइल तयार करा:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

ती स्पष्टपणे पास करा:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### स्थानिकीकरण

CLI मदत, निदान आणि मजकूर/HTML अहवाल क्रोम कोणत्याही अतिरिक्त अवलंबित्वाशिवाय 45 लोकेल्स (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ला समर्थन देतात. रिझोल्यूशन `--lang` (Wikipedia आवृत्ती निवडणाऱ्या `--language` पेक्षा वेगळे), नंतर `LC_ALL`, `LC_MESSAGES`, आणि `LANG` तपासते आणि शेवटी `en` वर परत येते. JSON आउटपुट की आणि विकिटेक्स्ट टेम्पलेट्स अपरिवर्तित राहतात.

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

चाचण्या चालवा:

```
python -m pytest tests/ -x -q
```

लिंट:

```
ruff check src/ tests/
```

## आवश्यकता

- Python 3.12+
- mwparserfromhell

## परवाना

MIT
