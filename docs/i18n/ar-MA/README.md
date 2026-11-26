# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · **العربية (المغرب)** · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

أداة تدقيق للمرور اللول وفق [دليل الأسلوب (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) لمقالات Wikipedia.

## علاش هاد المشروع كاين

كنعدل مقالات فـ Wikipedia. ماشي ديما، ولكن بالقدر اللي خلاني نبدا نلاحظ واحد النمط: كل مرة كنحل فيها شي مقال باش ننقيه، كنلقى راسي كندوز نفس الليستة الذهنية. واش التواريخ متناسقة؟ واش كاين شي كلام مراوغ (weasel words)؟ واش شي واحد خلى روابط عريانة فالمراجع؟ واش قسم «شوف حتى» (See also) عامر بزاف؟ واش الأقسام اللي فتحت المقال مرتبين بالترتيب الصحيح؟

مورا المرة الثالثة ولا الرابعة اللي قلبت فيها بيدي على نفس الدزينة ديال المشاكل واحد مورا واحد، كتبت سكربت. داك السكربت كبر. دابا كيقلب على كثر من 30 حاجة كنت كنديرها بيدي، وكيلقط حوايج كنت غنفلتهم فشي عشية ديال التلات وأنا عيان.

هاد الأداة ماشي بديل على الحكم التحريري. هي أداة فرز وتوجيه (triage). كتقول ليك فين تشوف، ماشي شنو تكتب.

## شنو كيفحص

**الأسلوب والنبرة**
- الكلام المراوغ (MOS:WEASEL)، وعبارات التضخيم والمبالغة (MOS:PEACOCK)
- تعابير الوقت النسبية ("مؤخرا"، "حاليا") اللي كتقدم دغيا وما كتبقاش صالحة
- إشارات المحتوى المولد بالذكاء الاصطناعي: الإفراط فالعزو داخل نص المقال (WP:AISIGNS)، والصياغة اللي بحال المقالات الإنشائية (WP:NOTESSAY)
- تنبيهات مصطلحات MOS:INDIGENOUS
- تنسيق تسميات الطيران وفق MOS:AVIATION
- تصريحات الخسائر اللي بلا مصادر وفق MOS:MILITARY

**البنية**
- طول المقدمة وعدد الفقرات (MOS:LEAD)
- ترتيب الأقسام مقابل MOS:LAYOUT
- الأقسام القصيرة ولا اللي ما مطوراش مزيان
- الأقسام اللي بلا مراجع (100+ كلمة، بلا `<ref>`)
- تضخم قسم «شوف حتى» (See also)
- الروابط الخارجية العريانة داخل نص المقال
- كثافة قوالب الاقتباس

**المراجع والاستشهادات**
- الروابط العريانة وسط وسوم `<ref>` (بلا قالب استشهاد)
- التحقق من رقم الفحص ديال ISBN
- الروابط الخاسرة فقوالب الاستشهاد
- الروابط الخارجية الميتة (اختياري، تقيل شوية)

**التصنيفات والروابط**
- التصنيفات اللي ناقصة
- جودة التصنيفات (تصنيفات قليلة بزاف، ولا عامة بزاف)
- اكتشاف الروابط الحمراء (روابط ويكي لمقالات ما كاينينش)
- تصنيفات الروابط الحمراء
- روابط صفحات التوضيح (Disambiguation)
- الإفراط فالربط (MOS:OVERLINK)

**صندوق المعلومات (Infobox)**
- عدد المعاملات وكثافة اللوائح (اكتشاف التضخم)
- المعاملات اللي فالعادة كتكون متوقعة وناقصة
- إشارات صندوق المعلومات ديال MOS:MILHIST

**حوايج أخرى**
- جودة الوصف القصير (ناقص، طويل بزاف، ولا مطابق للعنوان)
- جرد قوالب الصيانة
- نظافة روابط المشاريع الشقيقة (MOS:SISTER)
- اكتشاف المقالات اليتيمة (بلا روابط ويكي داخلة ليها)
- اكتشاف الروابط الخلفية المحتملة
- أنماط عناوين الخط الزمني / التغطية المباشرة

كل فحص كيعطي مشكل مصنف على حساب الخطورة (خفيف/متوسط/عالي) مع نقصان فالنقطة. المقال النقي كيجيب 100.

## التثبيت

```
pip install .
```

مكتبة mwparserfromhell اعتمادية ضرورية. كتوفر تحليل wikitext مبني على AST باش تلقط القوالب، العناوين، وروابط الويكي بدقة. إلا ما قدراتش تتكومبيلا (ما كاينش مترجم C متوفر)، الأداة كترجع أوتوماتيكيا للتحليل المبني على regex.

للتطوير:

```
pip install -e '.[dev]'
```

## الاستعمال

دقق مقال حي فـ Wikipedia:

```
wiki-mos-audit "Gettysburg Address"
```

دقق انطلاقا من رابط URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

دقق ملف wikitext محلي:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

دقق دفعة وحدة مجلد فيه ملفات wikitext:

```
wiki-mos-audit --dir ./articles/
```

نقز فحوصات الـ API (وضع أوفلاين):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### صيغ المخرجات

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### الفحوصات الاختيارية

هادو طافيين افتراضيا حيت تقال ولا كيحتاجو اتصال بالشبكة:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### الإصلاح التلقائي

الإصلاحات الميكانيكية الآمنة (المسافات، التنسيق) يمكن تطبق أوتوماتيكيا:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

معاينة بلا كتابة:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### وضع المقارنة (Diff mode)

قارن ملف wikitext محلي مع النسخة الحية:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### الإعدادات

صاوب ملف `.wiki-mos-audit.toml` باش تضبط العتبات ولا تعطل فحوصات معينة:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

دوزو بشكل صريح:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### التوطين واللغات

مساعدة سطر الأوامر، التشخيصات، وواجهة تقارير النص وHTML كيدعمو 45 لغة محلية (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) بلا حتى شي اعتماديات زائدة. اختيار اللغة كيقلب فـ `--lang` (مختلف على `--language`، اللي كيختار نسخة Wikipedia)، من بعد فـ `LC_ALL`، و`LC_MESSAGES`، و`LANG`، وكيرجع لـ `en` إلا ما لقاش. مفاتيح مخرجات JSON وقوالب wikitext كيبقاو بلا تغيير.

```
wiki-mos-audit "Article" --lang de --wikitext-file article.txt
LANG=fr_FR.UTF-8 wiki-mos-audit --help
```

## واجهة Python البرمجية (Python API)

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

تدقيق الكود (Lint):

```
ruff check src/ tests/
```

## المتطلبات

- Python 3.12+
- mwparserfromhell

## الرخصة

MIT
