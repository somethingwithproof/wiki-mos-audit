# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · **العربية** · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

مدقّق أولي لمدى التزام مقالات Wikipedia بـ [دليل الأسلوب (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style).

## سبب وجود هذه الأداة

أقوم بتحرير Wikipedia. ليس باستمرار، ولكن بالقدر الكافي الذي جعلني ألاحظ نمطاً متكرراً: في كل مرة أفتح فيها مقالة لتنقيحها، كنت أراجع القائمة الذهنية نفسها. هل التواريخ متسقة؟ هل توجد ألفاظ مبهمة (weasel words)؟ هل ترك أحدهم روابط URL مجردة في المراجع؟ هل قسم «انظر أيضاً» متضخم؟ هل الأقسام الختامية مرتبة بالشكل الصحيح؟

بعد المرة الثالثة أو الرابعة من الفحص اليدوي للمشكلات العشر نفسها على التوالي، كتبت نصاً برمجياً. ثم نما هذا النص البرمجي. والآن يفحص أكثر من 30 أمراً كنت أتحقق منها يدوياً، ويلتقط أشياء قد تفوتني في مساء ثلاثاء متعب.

هذه الأداة ليست بديلاً عن التقدير التحريري، بل هي أداة فرز أولي. تخبرك أين تنظر، لا ماذا تكتب.

## ما الذي تفحصه الأداة

**الأسلوب والنبرة**
- الألفاظ المبهمة (MOS:WEASEL) وعبارات التمجيد غير المبررة (MOS:PEACOCK)
- تعبيرات الزمن النسبية (مثل "recently" و"currently") التي تتقادم سريعاً
- مؤشرات المحتوى المولّد بالذكاء الاصطناعي: الإفراط في الإسناد داخل متن المقالة (WP:AISIGNS)، والصياغة الإنشائية الشبيهة بمقالات الرأي (WP:NOTESSAY)
- تنبيهات مصطلحات MOS:INDIGENOUS
- تنسيق تسميات الطيران وفق MOS:AVIATION
- بيانات الخسائر البشرية غير الموثقة بمصادر وفق MOS:MILITARY

**البنية**
- طول المقدمة وعدد فقراتها (MOS:LEAD)
- ترتيب الأقسام وفق MOS:LAYOUT
- الأقسام القصيرة أو غير المكتملة
- الأقسام الخالية من المراجع (أكثر من 100 كلمة دون `<ref>`)
- تضخم قسم «انظر أيضاً»
- روابط URL الخارجية المجردة في متن المقالة
- كثافة قوالب الاقتباس

**المراجع والاستشهادات**
- روابط URL المجردة داخل وسوم `<ref>` (دون قالب استشهاد)
- التحقق من رقم التدقيق لمعرّفات ISBN
- روابط URL المشوّهة داخل قوالب الاستشهاد
- الروابط الخارجية المعطلة (اختياري، بطيء)

**التصنيفات والوصلات**
- التصنيفات المفقودة
- جودة التصنيفات (تصنيف ناقص أو واسع أكثر من اللازم)
- اكتشاف الوصلات الحمراء (وصلات ويكي إلى مقالات غير موجودة)
- تصنيفات الوصلات الحمراء
- وصلات صفحات التوضيح
- الإفراط في وضع الوصلات (MOS:OVERLINK)

**صندوق المعلومات (Infobox)**
- عدد الوسائط وكثافة القوائم (اكتشاف التضخم)
- الوسائط الشائعة المتوقعة والمفقودة
- مؤشرات صندوق معلومات MOS:MILHIST

**أخرى**
- جودة الوصف المختصر (مفقود، أو طويل جداً، أو مطابق للعنوان)
- حصر قوالب الصيانة
- سلامة وصلات المشاريع الشقيقة (MOS:SISTER)
- اكتشاف المقالات اليتيمة (لا توجد وصلات ويكي واردة إليها)
- اكتشاف الوصلات الخلفية المحتملة
- أنماط عناوين الخطوط الزمنية والمدونات الحية

يُنتج كل فحص مشكلة مصنّفة حسب الخطورة (منخفضة/متوسطة/عالية) مع خصم من الدرجة. وتحصل المقالة السليمة على 100 نقطة.

## التثبيت

```
pip install .
```

تُعد حزمة mwparserfromhell اعتمادية مطلوبة؛ فهي توفّر تحليلاً نحوياً لنص الويكي قائماً على شجرة البنية المجردة (AST) لاكتشاف القوالب والعناوين ووصلات الويكي بدقة. وإذا تعذر تصريفها (لعدم توفر مترجم C)، تتحول الأداة تلقائياً إلى التحليل المعتمد على التعابير النمطية.

للتطوير:

```
pip install -e '.[dev]'
```

## الاستخدام

تدقيق مقالة Wikipedia حية:

```
wiki-mos-audit "Gettysburg Address"
```

التدقيق انطلاقاً من عنوان URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

تدقيق ملف نص ويكي محلي:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

تدقيق دفعي لمجلد يحتوي على ملفات نص ويكي:

```
wiki-mos-audit --dir ./articles/
```

تخطي فحوصات واجهة برمجة التطبيقات (وضع عدم الاتصال):

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

تكون هذه الفحوصات معطلة افتراضياً لأنها بطيئة أو تتطلب اتصالاً بالشبكة:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### الإصلاح التلقائي

يمكن تطبيق الإصلاحات الآلية الآمنة (المسافات البيضاء والتنسيق) تلقائياً:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

المعاينة دون كتابة التغييرات:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### وضع الفروقات (Diff)

مقارنة نص الويكي المحلي بالنسخة الحية:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### الإعداد

أنشئ ملف `.wiki-mos-audit.toml` لضبط العتبات أو تعطيل فحوصات محددة:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

مرّره صراحةً:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### التوطين

تدعم مساعدة سطر الأوامر والرسائل التشخيصية وإطار تقارير النص وHTML نحو 45 لغة محلية (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) دون أي اعتماديات إضافية. يتحقق تحديد اللغة المحلية من `--lang` (وهو يختلف عن `--language` الذي يحدد نسخة Wikipedia)، ثم `LC_ALL` و`LC_MESSAGES` و`LANG`، مع الرجوع إلى `en`. وتبقى مفاتيح مخرجات JSON وقوالب نص الويكي دون تغيير.

```
wiki-mos-audit "Article" --lang de --wikitext-file article.txt
LANG=fr_FR.UTF-8 wiki-mos-audit --help
```

## واجهة برمجة تطبيقات Python

```python
from wiki_mos_audit import audit_mos

report = audit_mos("Article Title", wikitext)
print(f"Score: {report.score}/100")
for issue in report.issues:
    print(f"[{issue.severity}] {issue.check_id}: {issue.message}")
```

## التطوير

تشغيل الاختبارات:

```
python -m pytest tests/ -x -q
```

فحص الأسلوب (Lint):

```
ruff check src/ tests/
```

## المتطلبات

- Python 3.12+
- mwparserfromhell

## الترخيص

MIT
