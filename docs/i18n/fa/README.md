# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · **فارسی** · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

یک ممیز گام نخست [شیوه‌نامه (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) برای مقاله‌های Wikipedia.

## چرا این ابزار وجود دارد

من در Wikipedia ویرایش می‌کنم. نه به‌طور مداوم، اما آن‌قدر که متوجه یک الگو شدم: هر بار که مقاله‌ای را برای مرتب‌سازی باز می‌کردم، همان چک‌لیست ذهنی همیشگی را مرور می‌کردم. آیا تاریخ‌ها یکدست هستند؟ عبارت‌های طفره‌آمیز وجود دارد؟ آیا کسی در منابع URLهای برهنه جا گذاشته است؟ آیا بخش «جستارهای وابسته» بیش از حد شلوغ شده است؟ آیا بخش‌های پایانی به ترتیب درست قرار دارند؟

بعد از سومین یا چهارمین بار که به‌صورت دستی دنبال همان دوازده مشکل تکراری گشتم، یک اسکریپت نوشتم. آن اسکریپت بزرگ‌تر شد. حالا بیش از ۳۰ موردی را که قبلاً با دست چک می‌کردم بررسی می‌کند و چیزهایی را می‌گیرد که در یک غروب خسته سه‌شنبه از دستم در می‌رفت.

این ابزار جایگزین قضاوت ویرایشی نیست. یک ابزار تریاژ و اولویت‌بندی است. به شما می‌گوید کجا را نگاه کنید، نه اینکه چه بنویسید.

## چه چیزهایی را بررسی می‌کند

**سبک و لحن**
- عبارت‌های طفره‌آمیز (MOS:WEASEL)، واژه‌های خودنمایی (MOS:PEACOCK)
- عبارت‌های زمانی نسبی («اخیراً»، «در حال حاضر») که به‌سرعت کهنه می‌شوند
- نشانه‌های محتوای تولیدشده با هوش مصنوعی: استناددهی بیش از حد در متن بدنه (WP:AISIGNS)، عبارت‌پردازی مقاله‌گونه (WP:NOTESSAY)
- هشدارهای اصطلاح‌شناسی MOS:INDIGENOUS
- قالب‌بندی نام‌گذاری MOS:AVIATION
- بیان‌های بدون منبع درباره تلفات در MOS:MILITARY

**ساختار**
- طول بخش آغازین (لید) و تعداد پاراگراف‌ها (MOS:LEAD)
- ترتیب بخش‌ها مطابق با MOS:LAYOUT
- بخش‌های کوتاه یا کم‌پرداخته
- بخش‌های بدون منبع (بیش از ۱۰۰ واژه، بدون `<ref>`)
- شلوغی و تورم بخش «جستارهای وابسته»
- URLهای خارجی برهنه در بدنه مقاله
- تراکم الگوهای نقل‌قول

**منابع و ارجاع‌ها**
- URLهای برهنه درون برچسب‌های `<ref>` (بدون الگوی یادکرد)
- اعتبارسنجی رقم کنترلی شابک (ISBN)
- URLهای بدشکل در الگوهای یادکرد
- پیوندهای خارجی مرده (اختیاری، کند)

**رده‌ها و پیوندها**
- رده‌های جاافتاده
- کیفیت رده‌بندی (کم‌رده، بیش از حد کلی)
- تشخیص پیوند قرمز (ویکی‌لینک به مقاله‌های ناموجود)
- رده‌های با پیوند قرمز
- پیوند به صفحه‌های ابهام‌زدایی
- پیونددهی بیش از حد (MOS:OVERLINK)

**جعبه اطلاعات (Infobox)**
- تعداد پارامترها و تراکم فهرست‌ها (تشخیص شلوغی)
- پارامترهای مرسوم جاافتاده
- نشانه‌های جعبه اطلاعات MOS:MILHIST

**سایر**
- کیفیت توضیح کوتاه (نبودن، بیش از حد طولانی بودن، یکسان بودن با عنوان)
- فهرست الگوهای نگهداری
- بهداشت پیوندهای پروژه‌های خواهر (MOS:SISTER)
- تشخیص مقاله یتیم (بدون ویکی‌لینک ورودی)
- کشف پیوندهای برگشتی احتمالی
- الگوهای سرخط گاه‌شمار/لایوبلاگ

هر بررسی یک مشکل با سطح شدت رتبه‌بندی‌شده (کم/متوسط/زیاد) و کسر امتیاز تولید می‌کند. یک مقاله تمیز امتیاز ۱۰۰ می‌گیرد.

## نصب

```
pip install .
```

کتابخانه mwparserfromhell یک وابستگی الزامی است. این کتابخانه تجزیه مبتنی بر AST ویکی‌متن را برای تشخیص دقیق الگوها، سرخط‌ها و ویکی‌لینک‌ها فراهم می‌کند. اگر امکان کامپایل آن وجود نداشته باشد (کامپایلر C در دسترس نباشد)، ابزار به‌طور خودکار به تجزیه مبتنی بر regex برمی‌گردد.

برای توسعه:

```
pip install -e '.[dev]'
```

## نحوه استفاده

ممیزی یک مقاله زنده در Wikipedia:

```
wiki-mos-audit "Gettysburg Address"
```

ممیزی از روی یک URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

ممیزی یک فایل ویکی‌متن محلی:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

ممیزی دسته‌ای یک پوشه از فایل‌های ویکی‌متن:

```
wiki-mos-audit --dir ./articles/
```

رد کردن بررسی‌های API (حالت آفلاین):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### قالب‌های خروجی

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### بررسی‌های اختیاری

این موارد به‌طور پیش‌فرض خاموش هستند چون کندند یا به دسترسی شبکه نیاز دارند:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### اصلاح خودکار

اصلاح‌های مکانیکی ایمن (فاصله‌ها، قالب‌بندی) می‌توانند به‌طور خودکار اعمال شوند:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

پیش‌نمایش بدون نوشتن فایل:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### حالت مقایسه (Diff)

مقایسه ویکی‌متن محلی با نسخه زنده:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### پیکربندی

یک فایل `.wiki-mos-audit.toml` بسازید تا آستانه‌ها را تنظیم یا بررسی‌های خاص را غیرفعال کنید:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

ارسال صریح آن:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### بومی‌سازی

راهنمای خط فرمان، پیام‌های تشخیصی و پوسته گزارش‌های متنی/HTML از ۴۵ زبان و منطقه (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) بدون نیاز به وابستگی اضافه پشتیبانی می‌کنند. تشخیص زبان ابتدا `--lang` (متمایز از `--language` که نسخه زبانی Wikipedia را انتخاب می‌کند) و سپس `LC_ALL`، `LC_MESSAGES` و `LANG` را بررسی می‌کند و در نهایت به `en` بازمی‌گردد. کلیدهای خروجی JSON و الگوهای ویکی‌متن بدون تغییر باقی می‌مانند.

```
wiki-mos-audit "Article" --lang de --wikitext-file article.txt
LANG=fr_FR.UTF-8 wiki-mos-audit --help
```

## API پایتون

```python
from wiki_mos_audit import audit_mos

report = audit_mos("Article Title", wikitext)
print(f"Score: {report.score}/100")
for issue in report.issues:
    print(f"[{issue.severity}] {issue.check_id}: {issue.message}")
```

## توسعه

اجرای آزمون‌ها:

```
python -m pytest tests/ -x -q
```

لینت:

```
ruff check src/ tests/
```

## پیش‌نیازها

- Python 3.12+
- mwparserfromhell

## مجوز

MIT
