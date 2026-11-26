# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · **Українська** · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Інструмент первинного аудиту статей Wikipedia на відповідність [Посібнику зі стилю (MOS)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style).

## Навіщо це потрібно

Я редагую Wikipedia. Не постійно, але достатньо часто, щоб помітити закономірність: щоразу, відкриваючи статтю для вичитки й упорядкування, я подумки проходив той самий контрольний список. Чи узгоджені дати? Чи є слова-паразити та ухильні формулювання (weasel words)? Чи не залишив хтось голі URL у примітках? Чи не роздутий розділ «Див. також» (See also)? Чи в правильному порядку розташовані прикінцеві розділи?

Після третього чи четвертого разу, коли довелося вручну шукати той самий десяток проблем поспіль, я написав скрипт. Скрипт розрісся. Тепер він перевіряє понад 30 речей, які я робив вручну, і знаходить те, що я міг би пропустити втомленим вечором вівторка.

Це не заміна редакторському судженню. Це інструмент первинного сортування (тріажу). Він підказує, на що звернути увагу, а не що саме писати.

## Що перевіряється

**Стиль і тон**
- Слова-лазівки (MOS:WEASEL), пишномовні терміни (MOS:PEACOCK)
- Відносні часові вирази («нещодавно», «наразі»), які швидко застарівають
- Ознаки згенерованого ШІ тексту: надмірна атрибуція в основному тексті (WP:AISIGNS), есеїстичні звороти (WP:NOTESSAY)
- Позначення термінології MOS:INDIGENOUS
- Форматування позначень авіаційної техніки (MOS:AVIATION)
- Непідкріплені джерелами згадки про втрати (MOS:MILITARY)

**Структура**
- Довжина преамбули та кількість абзаців (MOS:LEAD)
- Порядок розділів відповідно до MOS:LAYOUT
- Короткі або недостатньо розкриті розділи
- Розділи без посилань на джерела (понад 100 слів, без `<ref>`)
- Роздутість розділу «Див. також» (See also)
- Голі зовнішні URL в тексті статті
- Щільність шаблонів цитування

**Примітки та посилання на джерела**
- Голі URL усередині тегів `<ref>` (без шаблону цитування)
- Перевірка контрольної цифри ISBN
- Некоректні URL у шаблонах цитування
- Непрацюючі зовнішні посилання (опційно, повільно)

**Категорії та посилання**
- Відсутні категорії
- Якість категорій (недостатня категоризація, надмірно широкі категорії)
- Виявлення червоних посилань (вікіпосилання на неіснуючі статті)
- Червоні посилання на категорії
- Посилання на сторінки неоднозначності
- Надмірне вікіфікування (MOS:OVERLINK)

**Інфобокс**
- Кількість параметрів і щільність списків (виявлення роздутості)
- Відсутні зазвичай очікувані параметри
- Сигнали інфобоксу MOS:MILHIST

**Інше**
- Якість короткого опису (відсутній, занадто довгий, збігається з назвою)
- Перелік шаблонів обслуговування
- Гігієна посилань на сестринські проєкти (MOS:SISTER)
- Виявлення статей-сиріт (відсутні вхідні вікіпосилання)
- Пошук потенційних зворотних посилань
- Шаблони заголовків у стилі хроніки або онлайн-трансляції (liveblog)

Кожна перевірка формує зауваження з рівнем серйозності (low/medium/high) та зняттям балів. Стаття без зауважень отримує 100 балів.

## Встановлення

```
pip install .
```

mwparserfromhell є обов'язковою залежністю. Вона забезпечує розбір вікітексту на основі AST для точного виявлення шаблонів, заголовків і вікіпосилань. Якщо її не вдається скомпілювати (немає компілятора C), інструмент автоматично переходить на розбір за допомогою регулярних виразів.

Для розробки:

```
pip install -e '.[dev]'
```

## Використання

Аудит опублікованої статті Wikipedia:

```
wiki-mos-audit "Gettysburg Address"
```

Аудит за URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Аудит локального файлу вікітексту:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Пакетний аудит каталогу з файлами вікітексту:

```
wiki-mos-audit --dir ./articles/
```

Пропуск перевірок через API (автономний режим):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Формати виводу

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Додаткові перевірки

Вони вимкнені за замовчуванням, оскільки працюють повільно або потребують доступу до мережі:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Автовиправлення

Безпечні механічні виправлення (пробіли, форматування) можна застосувати автоматично:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Попередній перегляд без запису у файл:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Режим порівняння (Diff)

Порівняння локального вікітексту з поточною версією у Wikipedia:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Конфігурація

Створіть файл `.wiki-mos-audit.toml`, щоб налаштувати порогові значення або вимкнути окремі перевірки:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Або передайте його явно:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Локалізація

Довідка CLI, діагностичні повідомлення та інтерфейсні елементи текстових і HTML-звітів підтримують 45 мов (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) без жодних додаткових залежностей. Визначення локалі перевіряє `--lang` (на відміну від `--language`, який вибирає мовний розділ Wikipedia), далі `LC_ALL`, `LC_MESSAGES` і `LANG`, із переходом до `en` за замовчуванням. Ключі JSON-виводу та шаблони вікітексту залишаються незмінними.

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

## Розробка

Запуск тестів:

```
python -m pytest tests/ -x -q
```

Перевірка лінтером:

```
ruff check src/ tests/
```

## Вимоги

- Python 3.12+
- mwparserfromhell

## Ліцензія

MIT
