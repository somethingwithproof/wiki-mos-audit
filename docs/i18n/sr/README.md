# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (28 locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [Bosanski](../bs/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Hrvatski](../hr/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · **Српски** · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Првостепени ревизор усклађености чланака Википедије са [Приручником за стил (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style).

## Зашто ово постоји

Уређујем Википедију. Не стално, али довољно често да сам почео да примећујем образац: сваки пут када бих отворио чланак да га средим, пролазио сам кроз исту менталну контролну листу. Да ли су датуми доследни? Има ли неодређених израза (weasel words)? Да ли је неко оставио голе URL-ове у референцама? Да ли је одељак "See also" пренатрпан? Да ли су завршни одељци у исправном редоследу?

После трећег или четвртог пута ручног претраживања истих десетак проблема заредом, написао сам скрипту. Та скрипта је порасла. Сада проверава преко 30 ствари које сам радио ручно и хвата ситнице које бих пропустио једног уморног уторка увече.

Ово није замена за уредничку процену. Ово је алат за тријажу. Показује кориснику где да погледа, а не шта да напише.

## Шта проверава

**Стил и тон**
- Неодређени, избегавајући изрази (MOS:WEASEL), хвалисави термини (MOS:PEACOCK)
- Релативни временски изрази ("недавно", "тренутно") који брзо застаревају
- Сигнали садржаја генерисаног вештачком интелигенцијом: прекомерно приписивање у главном тексту (WP:AISIGNS), есејистичко изражавање (WP:NOTESSAY)
- Ознаке терминологије MOS:INDIGENOUS
- Форматирање ваздухопловних ознака (MOS:AVIATION)
- Нецитирани наводи о жртвама (MOS:MILITARY)

**Структура**
- Дужина увода и број пасуса (MOS:LEAD)
- Редослед одељака према MOS:LAYOUT
- Кратки или недовољно разрађени одељци
- Одељци без референци (100+ речи, без `<ref>`)
- Пренатрпаност одељка "See also"
- Голи спољашњи URL-ови у телу чланка
- Густина шаблона за цитирање

**Референце и цитати**
- Голи URL-ови унутар `<ref>` ознака (без шаблона за цитирање)
- Валидација контролне цифре ISBN-а
- Неисправно формирани URL-ови у шаблонима за цитирање
- Неисправне спољашње везе (опционо, споро)

**Категорије и везе**
- Категорије које недостају
- Квалитет категорија (недовољна категоризација, прешироке категорије)
- Откривање црвених веза (викивезе ка непостојећим чланцима)
- Црвене везе категорија
- Везе ка вишезначним одредницама
- Прекомерно повезивање (MOS:OVERLINK)

**Инфокутија**
- Број параметара и густина листа (откривање пренатрпаности)
- Уобичајено очекивани параметри који недостају
- Сигнали инфокутије MOS:MILHIST

**Остало**
- Квалитет кратког описа (недостаје, предугачак, поклапа се са насловом)
- Попис шаблона за одржавање
- Уредност веза ка сестринским пројектима (MOS:SISTER)
- Откривање чланака сирочади (без долазних викивеза)
- Проналажење потенцијалних повратних веза
- Обрасци наслова у стилу хронологије или преноса уживо (liveblog)

Свака провера даје налаз са оценом озбиљности (low/medium/high) и одузимањем бодова. Уредан чланак добија 100 бодова.

## Инсталација

```
pip install .
```

mwparserfromhell је обавезна зависност. Омогућава парсирање викитекста засновано на AST-у ради прецизног откривања шаблона, наслова и викивеза. Ако се не може компајлирати (на рачунару нема доступног C компајлера), алат се аутоматски пребацује на парсирање помоћу регуларних израза.

За развој:

```
pip install -e '.[dev]'
```

## Употреба

Ревизија објављеног чланка на Википедији:

```
wiki-mos-audit "Gettysburg Address"
```

Ревизија преко URL-а:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Ревизија локалне датотеке викитекста:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Групна ревизија директоријума са датотекама викитекста:

```
wiki-mos-audit --dir ./articles/
```

Прескакање API провера (ванмрежни режим):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Формати излаза

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Опционе провере

Ове провере су подразумевано искључене јер су споре или захтевају приступ мрежи и серверима:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Аутоматско исправљање

Безбедне механичке исправке (размаци, форматирање) могу се применити аутоматски:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Преглед без уписивања у датотеку:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Режим поређења (Diff)

Упоређивање локалног викитекста са објављеном верзијом:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Подешавања

Направите датотеку `.wiki-mos-audit.toml` да бисте прилагодили прагове или онемогућили појединачне провере:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Проследите је експлицитно:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Локализација

Помоћ за CLI, дијагностичке поруке и елементи текстуалних и HTML извештаја подржавају 48 локалитета (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`) без додатних зависности. Одређивање локалитета проверава `--lang` (различито од `--language`, које бира језичко издање Википедије), затим `LC_ALL`, `LC_MESSAGES` и `LANG`, уз повратак на `en`. Кључеви JSON излаза и шаблони викитекста остају непромењени.

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

## Развој

Покретање тестова:

```
python -m pytest tests/ -x -q
```

Провера линтером:

```
ruff check src/ tests/
```

## Захтеви

- Python 3.12+
- mwparserfromhell

## Лиценца

MIT
