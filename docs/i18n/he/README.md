# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · **עברית** · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

כלי ביקורת ראשוני לפי [מדריך הסגנון (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) עבור ערכי Wikipedia.

## למה הכלי הזה קיים

אני עורך ב-Wikipedia. לא באופן קבוע, אבל מספיק כדי להתחיל לשים לב לדפוס: בכל פעם שפתחתי ערך כדי לסדר אותו, הרצתי את אותו צ'ק-ליסט בראש. האם התאריכים עקביים? יש מילות התחמקות (weasel words)? מישהו השאיר כתובות URL חשופות בהערות השוליים? האם פסקת "ראו גם" מנופחת? האם פסקאות הסיום מסודרות בסדר הנכון?

אחרי הפעם השלישית או הרביעית שסרקתי ידנית את אותן תריסר בעיות ברצף, כתבתי סקריפט. הסקריפט הזה גדל. עכשיו הוא בודק יותר מ-30 דברים שהייתי עושה ידנית, והוא תופס דברים שהייתי מפספס בערב שלישי עייף.

זה אינו תחליף לשיקול דעת עריכתי. זה כלי מיון ראשוני. הוא אומר לכם איפה לחפש, לא מה לכתוב.

## מה הכלי בודק

**סגנון וטון**
- מילות התחמקות (MOS:WEASEL), ביטויים מליציים (MOS:PEACOCK)
- ביטויי זמן יחסיים ("recently", "currently") שמתיישנים מהר
- סימנים לתוכן שנוצר על ידי AI: ייחוס יתר בגוף הטקסט (WP:AISIGNS), ניסוח דמוי מסה (WP:NOTESSAY)
- דגלי מינוח של MOS:INDIGENOUS
- עיצוב כינויים לפי MOS:AVIATION
- הצהרות נפגעים ללא מקור לפי MOS:MILITARY

**מבנה**
- אורך הפתיח ומספר הפסקאות (MOS:LEAD)
- סדר הפרקים מול MOS:LAYOUT
- פרקים קצרים או לא מפותחים
- פרקים ללא מקורות (100+ מילים, ללא `<ref>`)
- התנפחות של פרק "ראו גם"
- כתובות URL חיצוניות חשופות בגוף הערך
- צפיפות תבניות ציטוט

**הפניות ומקורות**
- כתובות URL חשופות בתוך תגי `<ref>` (ללא תבנית ציטוט)
- אימות ספרת ביקורת של ISBN
- כתובות URL פגומות בתבניות ציטוט
- קישורים חיצוניים מתים (אופציונלי, איטי)

**קטגוריות וקישורים**
- קטגוריות חסרות
- איכות קטגוריות (מיעוט קטגוריות, רחבות מדי)
- זיהוי קישורים אדומים (קישורי ויקי לערכים שאינם קיימים)
- קטגוריות עם קישורים אדומים
- קישורים לדפי פירושונים
- קישור יתר (MOS:OVERLINK)

**תבנית מידע (Infobox)**
- ספירת פרמטרים וצפיפות רשימות (זיהוי ניפוח)
- פרמטרים חסרים שמצופה שיופיעו
- סימנים לתבנית מידע של MOS:MILHIST

**אחר**
- איכות תיאור קצר (חסר, ארוך מדי, זהה לכותרת)
- מלאי תבניות תחזוקה
- היגיינת קישורים למיזמי אחות (MOS:SISTER)
- זיהוי ערכים יתומים (ללא קישורי ויקי נכנסים)
- גילוי קישורים נכנסים פוטנציאליים
- דפוסי כותרות של ציר זמן או בלוג חי (liveblog)

כל בדיקה מפיקה ממצא מדורג לפי חומרה (נמוכה/בינונית/גבוהה) עם הפחתת ציון. ערך נקי מקבל ציון 100.

## התקנה

```
pip install .
```

`mwparserfromhell` היא תלות נדרשת. היא מספקת ניתוח wikitext מבוסס AST לזיהוי מדויק של תבניות, כותרות וקישורי ויקי. אם לא ניתן להדר אותה (אין מהדר C זמין), הכלי חוזר אוטומטית לניתוח מבוסס ביטויים רגולריים (regex).

לפיתוח:

```
pip install -e '.[dev]'
```

## שימוש

ביקורת של ערך חי ב-Wikipedia:

```
wiki-mos-audit "Gettysburg Address"
```

ביקורת מתוך כתובת URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

ביקורת של קובץ wikitext מקומי:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

ביקורת אצווה של תיקיית קובצי wikitext:

```
wiki-mos-audit --dir ./articles/
```

דילוג על בדיקות API (מצב לא מקוון):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### פורמטי פלט

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### בדיקות אופציונליות

בדיקות אלו כבויות כברירת מחדל משום שהן איטיות או דורשות גישה לרשת:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### תיקון אוטומטי

ניתן להחיל אוטומטית תיקונים מכניים בטוחים (רווחים, עיצוב):

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

תצוגה מקדימה ללא כתיבה:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### מצב השוואה (Diff)

השוואת wikitext מקומי מול הגרסה החיה:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### תצורה

צרו קובץ `.wiki-mos-audit.toml` כדי להתאים ערכי סף או להשבית בדיקות מסוימות:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

העברה מפורשת של הקובץ:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### לוקליזציה

עזרת ה-CLI, כלי האבחון ומעטפת דוחות הטקסט וה-HTML תומכים ב-45 לוקאלים (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ללא תלויות נוספות. הזיהוי בודק את `--lang` (נפרד מ-`--language`, הבוחר את מהדורת Wikipedia), לאחר מכן `LC_ALL`, `LC_MESSAGES`, ו-`LANG`, וחוזר לברירת המחדל `en`. מפתחות פלט ה-JSON ותבניות ה-wikitext נותרים ללא שינוי.

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

## פיתוח

הרצת בדיקות:

```
python -m pytest tests/ -x -q
```

Lint:

```
ruff check src/ tests/
```

## דרישות

- Python 3.12+
- mwparserfromhell

## רישיון

MIT
