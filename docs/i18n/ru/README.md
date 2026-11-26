# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · **Русский** · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Инструмент первичной проверки статей Wikipedia на соответствие [Руководству по стилю (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style).

## Зачем это нужно

Я редактирую Wikipedia. Не постоянно, но достаточно часто, чтобы заметить закономерность: каждый раз, открывая статью для вычитки, я мысленно проходился по одному и тому же чек-листу. Согласованы ли даты? Есть ли обтекаемые формулировки? Не оставил ли кто-то голые URL в примечаниях? Не раздут ли раздел "См. также"? В правильном ли порядке расположены заключительные разделы?

После третьего или четвертого раза, когда мне пришлось вручную искать один и тот же десяток проблем подряд, я написал скрипт. Скрипт разросся. Теперь он проверяет более 30 вещей, которые я раньше делал вручную, и находит то, что я бы пропустил уставшим вечером во вторник.

Это не замена редакторскому суждению. Это инструмент первичной сортировки проблем. Он подсказывает, куда посмотреть, а не что написать.

## Что проверяется

**Стиль и тон**
- Обтекаемые формулировки (MOS:WEASEL), напыщенные выражения (MOS:PEACOCK)
- Относительные выражения времени ("recently", "currently"), которые быстро устаревают
- Признаки текста, сгенерированного ИИ: избыточная атрибуция в основном тексте (WP:AISIGNS), эссеистские формулировки (WP:NOTESSAY)
- Замечания по терминологии MOS:INDIGENOUS
- Форматирование обозначений по MOS:AVIATION
- Неподтвержденные источниками сведения о потерях (MOS:MILITARY)

**Структура**
- Длина преамбулы и количество абзацев (MOS:LEAD)
- Порядок разделов согласно MOS:LAYOUT
- Короткие или недостаточно раскрытые разделы
- Разделы без ссылок на источники (более 100 слов без `<ref>`)
- Перегруженность раздела "См. также"
- Голые внешние URL в основном тексте статьи
- Плотность шаблонов цитирования

**Примечания и ссылки на источники**
- Голые URL внутри тегов `<ref>` (без шаблона цитирования)
- Проверка контрольной цифры ISBN
- Некорректные URL в шаблонах цитирования
- Неработающие внешние ссылки (включается отдельно, работает медленно)

**Категории и ссылки**
- Отсутствующие категории
- Качество категоризации (недостаточная категоризация, слишком широкие категории)
- Обнаружение красных ссылок (вики-ссылки на несуществующие статьи)
- Категории с красными ссылками
- Ссылки на страницы неоднозначностей
- Избыточная викификация (MOS:OVERLINK)

**Карточка**
- Количество параметров и плотность списков (выявление перегруженности)
- Отсутствующие стандартно ожидаемые параметры
- Сигналы карточек по MOS:MILHIST

**Прочее**
- Качество краткого описания (отсутствует, слишком длинное, совпадает с заголовком)
- Инвентаризация служебных шаблонов
- Корректность ссылок на родственные проекты (MOS:SISTER)
- Выявление статей-сирот (отсутствие входящих вики-ссылок)
- Поиск потенциальных обратных ссылок
- Шаблоны заголовков в стиле хронологии или онлайн-трансляции

Каждая проверка формирует замечание с уровнем серьезности (low/medium/high) и вычитает баллы. Чистая статья получает оценку 100.

## Установка

```
pip install .
```

mwparserfromhell является обязательной зависимостью. Библиотека обеспечивает разбор викитекста на основе AST для точного распознавания шаблонов, заголовков и вики-ссылок. Если ее не удается скомпилировать (отсутствует компилятор C), инструмент автоматически переключается на разбор с помощью регулярных выражений.

Для разработки:

```
pip install -e '.[dev]'
```

## Использование

Проверка актуальной статьи Wikipedia:

```
wiki-mos-audit "Gettysburg Address"
```

Проверка по URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Проверка локального файла с викитекстом:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Пакетная проверка каталога файлов с викитекстом:

```
wiki-mos-audit --dir ./articles/
```

Пропуск проверок через API (автономный режим):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Форматы вывода

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Необязательные проверки

Они отключены по умолчанию, поскольку выполняются медленно или требуют доступа к сети:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Автоисправление

Безопасные механические исправления (пробелы, форматирование) могут применяться автоматически:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Предварительный просмотр без записи в файл:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Режим сравнения

Сравнение локального викитекста с актуальной версией:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Конфигурация

Создайте файл `.wiki-mos-audit.toml` для настройки пороговых значений или отключения отдельных проверок:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Явная передача файла конфигурации:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Локализация

Справка CLI, диагностика и элементы оформления текстовых и HTML-отчетов поддерживают 45 локалей (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) без дополнительных зависимостей. Определение локали проверяет `--lang` (в отличие от `--language`, который выбирает языковой раздел Wikipedia), затем `LC_ALL`, `LC_MESSAGES` и `LANG`, с резервным переходом на `en`. Ключи вывода JSON и шаблоны викитекста остаются неизменными.

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

## Разработка

Запуск тестов:

```
python -m pytest tests/ -x -q
```

Линтинг:

```
ruff check src/ tests/
```

## Требования

- Python 3.12+
- mwparserfromhell

## Лицензия

MIT
