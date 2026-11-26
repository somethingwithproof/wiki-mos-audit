# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · **اردو** · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Wikipedia مضامین کے لیے ابتدائی مرحلے کا [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) آڈیٹر۔

## یہ کیوں موجود ہے

میں Wikipedia میں ترمیم کرتا ہوں۔ مسلسل نہیں، لیکن اتنا ضرور کہ مجھے ایک پیٹرن نظر آنے لگا: ہر بار جب میں صفائی کے لیے کوئی مضمون کھولتا تھا، تو میں ذہن میں وہی چیک لسٹ دہرا رہا ہوتا تھا۔ کیا تاریخیں یکساں ہیں؟ کیا کوئی مبہم یا جانبدار الفاظ (weasel words) موجود ہیں؟ کیا کسی نے حوالوں میں سادہ URLs چھوڑ دیے ہیں؟ کیا "مزید دیکھیے" (See also) سیکشن غیر ضروری طور پر پھیل گیا ہے؟ کیا نچلے حصے کے سیکشنز صحیح ترتیب میں ہیں؟

لگاتار تیسری یا چوتھی بار دستی طور پر انہی درجن بھر مسائل کو تلاش کرنے کے بعد، میں نے ایک اسکرپٹ لکھا۔ وہ اسکرپٹ بڑھتا گیا۔ اب یہ 30 سے زیادہ ایسی چیزیں چیک کرتا ہے جو میں ہاتھ سے کرتا تھا، اور یہ ان چیزوں کو بھی پکڑ لیتا ہے جو منگل کی تھکی ہوئی شام کو مجھ سے چھوٹ جاتیں۔

یہ ادارتی فیصلے کا متبادل نہیں ہے۔ یہ ایک درجہ بندی (triage) کا ٹول ہے۔ یہ آپ کو بتاتا ہے کہ کہاں دیکھنا ہے، یہ نہیں کہ کیا لکھنا ہے۔

## یہ کیا چیک کرتا ہے

**اسلوب اور لہجہ**
- مبہم الفاظ (MOS:WEASEL)، مبالغہ آمیز اصطلاحات (MOS:PEACOCK)
- نسبتی وقت کے حوالے ("حال ہی میں"، "فی الحال") جو وقت کے ساتھ پرانے ہو جاتے ہیں
- AI سے تیار کردہ مواد کے اشارے: مرکزی متن میں حد سے زیادہ حوالہ کاری (WP:AISIGNS)، مضمون نما اندازِ تحریر (WP:NOTESSAY)
- MOS:INDIGENOUS اصطلاحات کے نشانات
- MOS:AVIATION عہدے یا نام کی فارمیٹنگ
- MOS:MILITARY غیر حوالہ شدہ جانی نقصان کے بیانات

**ساخت**
- تمہید (Lead) کی لمبائی اور پیراگراف کی تعداد (MOS:LEAD)
- MOS:LAYOUT کے مطابق سیکشنز کی ترتیب
- مختصر یا نامکمل سیکشنز
- بغیر حوالے کے سیکشنز (100+ الفاظ، کوئی `<ref>` نہیں)
- See also سیکشن کی غیر ضروری طوالت
- مضمون کے متن میں سادہ بیرونی URLs
- اقتباس (Quote) ٹیمپلیٹ کی کثرت

**حوالہ جات اور اقتباسات**
- `<ref>` ٹیگز کے اندر سادہ URLs (بغیر cite ٹیمپلیٹ کے)
- ISBN چیک ڈیجٹ کی توثیق
- حوالہ جاتی ٹیمپلیٹس میں خراب فارمیٹ شدہ URLs
- مردہ بیرونی لنکس (اختیاری، سست)

**زمرہ جات اور لنکس**
- غائب زمرہ جات
- زمرے کا معیار (کم زمرہ بندی، حد سے زیادہ عمومی)
- سرخ لنک کی شناخت (غیر موجود مضامین کے وکی لنکس)
- سرخ لنک زمرہ جات
- ضد ابہام (Disambiguation) صفحات کے لنکس
- حد سے زیادہ لنکنگ (MOS:OVERLINK)

**انفوباکس**
- پیرامیٹرز کی تعداد اور فہرست کی کثرت (پھیلاؤ کی شناخت)
- عام طور پر متوقع پیرامیٹرز کی عدم موجودگی
- MOS:MILHIST انفوباکس اشارے

**دیگر**
- مختصر تفصیل (Short description) کا معیار (غائب، بہت طویل، عنوان سے مماثل)
- دیکھ بھال (Maintenance) ٹیمپلیٹس کی فہرست
- برادر پروجیکٹ لنک کی صفائی (MOS:SISTER)
- یتیم صفحے کی شناخت (کوئی آنے والا وکی لنک نہیں)
- ممکنہ بیک لنکس کی دریافت
- ٹائم لائن/لائیو بلاگ سرخیوں کے پیٹرنز

ہر چیک شدت کے درجے (کم/درمیانہ/زیادہ) کے ساتھ ایک مسئلہ اور اسکور میں کٹوتی پیدا کرتا ہے۔ ایک صاف ستھرا مضمون 100 اسکور حاصل کرتا ہے۔

## تنصیب

```
pip install .
```

mwparserfromhell ایک لازمی انحصار ہے۔ یہ درست ٹیمپلیٹ، سرخی، اور وکی لنک کی شناخت کے لیے AST پر مبنی وکی ٹیکسٹ پارسنگ فراہم کرتا ہے۔ اگر اسے کمپائل نہ کیا جا سکے (کوئی C کمپائلر دستیاب نہ ہو)، تو ٹول خودکار طور پر regex پر مبنی پارسنگ پر منتقل ہو جاتا ہے۔

ترقی کے لیے:

```
pip install -e '.[dev]'
```

## استعمال

ایک لائیو Wikipedia مضمون کا آڈٹ کریں:

```
wiki-mos-audit "Gettysburg Address"
```

URL سے آڈٹ کریں:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

ایک مقامی وکی ٹیکسٹ فائل کا آڈٹ کریں:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

وکی ٹیکسٹ فائلوں کی ایک ڈائریکٹری کا بیچ آڈٹ کریں:

```
wiki-mos-audit --dir ./articles/
```

API چیکس نظر انداز کریں (آف لائن موڈ):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### آؤٹ پٹ فارمیٹس

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### اختیاری چیکس

یہ بطورِ ڈیفالٹ بند ہوتے ہیں کیونکہ یہ سست ہیں یا انہیں نیٹ ورک تک رسائی کی ضرورت ہوتی ہے:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### خودکار اصلاح

محفوظ میکانکی اصلاحات (خالی جگہیں، فارمیٹنگ) خودکار طور پر لاگو کی جا سکتی ہیں:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

لکھے بغیر پیش نظارہ دیکھیں:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### موازنہ موڈ (Diff mode)

لائیو ورژن کے خلاف مقامی وکی ٹیکسٹ کا موازنہ کریں:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### کنفیگریشن

حدود کو ایڈجسٹ کرنے یا مخصوص چیکس کو غیر فعال کرنے کے لیے `.wiki-mos-audit.toml` فائل بنائیں:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

اسے واضح طور پر پاس کریں:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### لوکلائزیشن

CLI مدد، تشخیصات، اور ٹیکسٹ/HTML رپورٹ کے ظاہری عناصر (chrome) بغیر کسی اضافی انحصار کے 45 لوکیلز (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) کی معاونت کرتے ہیں۔ لوکیل کی شناخت پہلے `--lang` (جو `--language` سے مختلف ہے، جو Wikipedia ایڈیشن منتخب کرتا ہے)، پھر `LC_ALL`، `LC_MESSAGES`، اور `LANG` کو چیک کرتی ہے، اور آخر میں `en` پر واپس آتی ہے۔ JSON آؤٹ پٹ کیز اور وکی ٹیکسٹ ٹیمپلیٹس غیر متبدل رہتے ہیں۔

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

## ترقی

ٹیسٹس چلائیں:

```
python -m pytest tests/ -x -q
```

لنٹ:

```
ruff check src/ tests/
```

## تقاضے

- Python 3.12+
- mwparserfromhell

## لائسنس

MIT
