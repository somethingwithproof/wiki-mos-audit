# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · **العربية (مصر)** · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

أداة مراجعة أولية لـ [دليل الأسلوب (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) لمقالات Wikipedia.

## ليه الأداة دي موجودة

أنا بعدل في Wikipedia. مش طول الوقت، بس كفاية إني أبدأ ألاحظ نمط بيتكرر: كل مرة أفتح مقال عشان أنضفه وأظبطه، بلاقي نفسي ماشي على نفس قايمة المراجعة في دماغي. هل التواريخ متسقة؟ في كلمات مراوغة (weasel words)؟ حد ساب روابط عريانة (bare URLs) في المراجع؟ هل قسم "شوف كمان" (See also) منفوخ بزيادة؟ هل الأقسام اللي في آخر المقال مترتبة صح؟

بعد تالت أو رابع مرة أدور فيها بإيدي على نفس العشر مشاكل ورا بعض، كتبت سكريبت. والسكريبت ده كبر. دلوقتي بيفحص أكتر من 30 حاجة كنت بعملها بإيدي، وبيلقط حاجات كانت ممكن تعدي عليا في يوم تلات بالليل وأنا تعبان.

دي مش بديل لحكم المحرر. دي أداة فرز أولي (triage). بتقولك تبص فين، مش تكتب إيه.

## إيه اللي بتفحصه

**الأسلوب والنبرة**
- الكلمات المراوغة (MOS:WEASEL)، وعبارات التضخيم والتفخيم (MOS:PEACOCK)
- تعبيرات الوقت النسبية ("مؤخراً"، "حالياً") اللي بتقدم بسرعة
- مؤشرات المحتوى المولّد بالذكاء الاصطناعي: الإسناد المبالغ فيه جوه نص المقال (WP:AISIGNS)، والصياغة اللي شبه المقالات الإنشائية (WP:NOTESSAY)
- تنبيهات مصطلحات MOS:INDIGENOUS
- تنسيق تسميات MOS:AVIATION
- عبارات الخسائر غير الموثقة بمصادر في MOS:MILITARY

**الهيكل والتنظيم**
- طول المقدمة وعدد فقراتها (MOS:LEAD)
- ترتيب الأقسام قدام قواعد MOS:LAYOUT
- الأقسام القصيرة أو اللي مش مكتملة
- الأقسام اللي من غير مراجع (أكتر من 100 كلمة ومفيش `<ref>`)
- تضخم قسم See also
- الروابط الخارجية العريانة جوه متن المقال
- كثافة قوالب الاقتباس

**المراجع والاستشهادات**
- الروابط العريانة جوه وسوم `<ref>` (من غير قالب استشهاد)
- التحقق من رقم الفحص (check digit) بتاع ISBN
- الروابط الغلط في قوالب الاستشهاد
- الروابط الخارجية الميتة (اختياري، وبطيء)

**التصنيفات والروابط**
- التصنيفات الناقصة
- جودة التصنيفات (تصنيفات قليلة أو عامة بزيادة)
- اكتشاف الروابط الحمراء (روابط ويكي لمقالات مش موجودة)
- تصنيفات الروابط الحمراء
- روابط صفحات التوضيح (Disambiguation)
- كثرة الروابط بزيادة (MOS:OVERLINK)

**صندوق المعلومات (Infobox)**
- عدد المعاملات وكثافة القوايم (اكتشاف التضخم)
- المعاملات المعتادة اللي ناقصة
- مؤشرات صندوق المعلومات بتاعة MOS:MILHIST

**حاجات تانية**
- جودة الوصف القصير (ناقص، طويل بزيادة، أو مطابق للعنوان)
- جرد قوالب الصيانة
- نظافة روابط المشاريع الشقيقة (MOS:SISTER)
- اكتشاف المقالات اليتيمة (مفيش روابط ويكي داخلة ليها)
- اكتشاف الروابط الخلفية المحتملة (backlinks)
- أنماط عناوين الخط الزمني أو التغطية الحية (timeline/liveblog)

كل فحص بيطلع مشكلة بدرجة خطورة (منخفضة/متوسطة/عالية) مع خصم من الدرجة. المقال النضيف بياخد 100.

## التثبيت

```
pip install .
```

مكتبة mwparserfromhell اعتمادية أساسية. بتوفر تحليل للـ wikitext مبني على AST عشان تلقط القوالب والعناوين وروابط الويكي بدقة. لو مقدرتش تتبني (مفيش مترجم C متاح)، الأداة بتحول لوحدها تلقائياً للتحليل بـ regex.

للتطوير:

```
pip install -e '.[dev]'
```

## الاستخدام

راجع مقال Wikipedia مباشر أونلاين:

```
wiki-mos-audit "Gettysburg Address"
```

راجع من رابط URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

راجع ملف wikitext محلي:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

راجع مجلد كامل فيه ملفات wikitext مرة واحدة:

```
wiki-mos-audit --dir ./articles/
```

اتخطى فحوصات الـ API (وضع الأوفلاين):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### صيغ الإخراج

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### الفحوصات الاختيارية

دول مقفولين بشكل افتراضي عشان بطاء أو محتاجين اتصال بالنت:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### الإصلاح التلقائي

الإصلاحات الميكانيكية الآمنة (المسافات، التنسيق) ممكن تتطبق تلقائياً:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

معاينة من غير كتابة التغييرات:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### وضع المقارنة (Diff mode)

قارن ملف wikitext محلي بالنسخة المباشرة:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### الإعدادات

اعمل ملف `.wiki-mos-audit.toml` عشان تعدل الحدود أو تقفل فحوصات معينة:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

مرره بشكل صريح:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### الترجمة واللغات (Localization)

مساعدة سطر الأوامر، رسائل التشخيص، وواجهة التقارير النصية والـ HTML بتدعم 45 لغة ومحلية (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) من غير أي اعتماديات إضافية. تحديد اللغة بيدور الأول في `--lang` (وده مختلف عن `--language` اللي بيختار نسخة Wikipedia)، بعد كده `LC_ALL` و`LC_MESSAGES` و`LANG`، وبيرجع لـ `en` لو مفيش. مفاتيح مخرجات JSON وقوالب الـ wikitext بتفضل زي ما هي.

```
wiki-mos-audit "Article" --lang de --wikitext-file article.txt
LANG=fr_FR.UTF-8 wiki-mos-audit --help
```

## واجهة Python (Python API)

```python
from wiki_mos_audit import audit_mos

report = audit_mos("Article Title", wikitext)
print(f"Score: {report.score}/100")
for issue in report.issues:
    print(f"[{issue.severity}] {issue.check_id}: {issue.message}")
```

## التطوير

شغل الاختبارات:

```
python -m pytest tests/ -x -q
```

فحص الكود (Lint):

```
ruff check src/ tests/
```

## المتطلبات

- Python 3.12+
- mwparserfromhell

## الرخصة

MIT
