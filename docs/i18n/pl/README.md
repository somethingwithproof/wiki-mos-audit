# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · **Polski** · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Audytor pierwszego przejścia do sprawdzania artykułów Wikipedia pod kątem zgodności z [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style).

## Dlaczego powstało

Edytuję Wikipedia. Nie nieustannie, ale wystarczająco często, by zauważyć pewien schemat: za każdym razem, gdy otwierałem artykuł do uporządkowania, w myślach przechodziłem przez tę samą listę kontrolną. Czy daty są spójne? Czy są słowa-wytrychy (weasel words)? Czy ktoś zostawił gołe adresy URL w przypisach? Czy sekcja „Zobacz też” nie jest nadmiernie rozbudowana? Czy końcowe sekcje są we właściwej kolejności?

Po trzecim lub czwartym ręcznym przeglądaniu pod kątem tego samego tuzina problemów z rzędu napisałem skrypt. Ten skrypt się rozrósł. Teraz sprawdza ponad 30 rzeczy, które wcześniej robiłem ręcznie, i wyłapuje błędy, które przeoczyłbym w zmęczony wtorkowy wieczór.

To nie jest zamiennik oceny redakcyjnej. To narzędzie do wstępnej selekcji (triage). Pokazuje, gdzie szukać, a nie co napisać.

## Co sprawdza

**Styl i ton**
- Słowa-wytrychy (MOS:WEASEL), wyrażenia emfatyczne (MOS:PEACOCK)
- Wyrażenia określające czas względny ("niedawno", "obecnie"), które źle się starzeją
- Sygnały treści wygenerowanych przez AI: nadmierne przypisywanie źródeł w treści głównej (WP:AISIGNS), sformułowania o charakterze eseistycznym (WP:NOTESSAY)
- Flagi terminologii MOS:INDIGENOUS
- Formatowanie oznaczeń MOS:AVIATION
- Niepoparte źródłami stwierdzenia o ofiarach (MOS:MILITARY)

**Struktura**
- Długość sekcji wstępnej i liczba akapitów (MOS:LEAD)
- Kolejność sekcji względem MOS:LAYOUT
- Krótkie lub słabo rozwinięte sekcje
- Sekcje bez przypisów (ponad 100 słów, brak `<ref>`)
- Nadmierna objętość sekcji „Zobacz też”
- Gołe zewnętrzne adresy URL w treści artykułu
- Zagęszczenie szablonów cytatów

**Przypisy i cytowania**
- Gołe adresy URL wewnątrz znaczników `<ref>` (bez szablonu cytowania)
- Walidacja cyfry kontrolnej ISBN
- Nieprawidłowo sformułowane adresy URL w szablonach cytowań
- Martwe linki zewnętrzne (opcjonalne, powolne)

**Kategorie i linki**
- Brakujące kategorie
- Jakość kategorii (zbyt mało kategorii, zbyt ogólne)
- Wykrywanie czerwonych linków (linki wiki do nieistniejących artykułów)
- Kategorie będące czerwonymi linkami
- Linki do stron ujednoznaczniających
- Nadmierne linkowanie (MOS:OVERLINK)

**Infobox**
- Liczba parametrów i zagęszczenie list (wykrywanie nadmiernego rozrostu)
- Brakujące powszechnie oczekiwane parametry
- Sygnały szablonów infobox z MOS:MILHIST

**Inne**
- Jakość krótkiego opisu (brakujący, zbyt długi, identyczny z tytułem)
- Inwentaryzacja szablonów konserwacyjnych
- Higiena linków do projektów siostrzanych (MOS:SISTER)
- Wykrywanie stron osieroconych (brak przychodzących linków wiki)
- Odkrywanie potencjalnych linków zwrotnych
- Wzorce nagłówków typu oś czasu / relacja na żywo

Każde sprawdzenie generuje problem z oceną ważności (niska/średnia/wysoka) oraz odjęciem punktów. Czysty artykuł otrzymuje wynik 100.

## Instalacja

```
pip install .
```

mwparserfromhell jest wymaganą zależnością. Zapewnia parsowanie wikitekstu oparte na AST w celu dokładnego wykrywania szablonów, nagłówków i linków wiki. Jeśli nie można go skompilować (brak dostępnego kompilatora C), narzędzie automatycznie przełącza się na parsowanie oparte na wyrażeniach regularnych.

Do celów programistycznych:

```
pip install -e '.[dev]'
```

## Użycie

Audyt opublikowanego artykułu Wikipedia:

```
wiki-mos-audit "Gettysburg Address"
```

Audyt na podstawie adresu URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Audyt lokalnego pliku wikitekstu:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Audyt wsadowy katalogu plików wikitekstu:

```
wiki-mos-audit --dir ./articles/
```

Pominięcie sprawdzeń API (tryb offline):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Formaty wyjściowe

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Opcjonalne sprawdzenia

Domyślnie są wyłączone, ponieważ są powolne lub wymagają dostępu do sieci:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Automatyczne poprawki

Bezpieczne poprawki mechaniczne (białe znaki, formatowanie) można zastosować automatycznie:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Podgląd bez zapisywania:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Tryb różnic (diff)

Porównanie lokalnego wikitekstu z wersją opublikowaną:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Konfiguracja

Utwórz plik `.wiki-mos-audit.toml`, aby dostosować progi lub wyłączyć wybrane sprawdzenia:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Przekaż go jawnie:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Lokalizacja

Pomoc CLI, komunikaty diagnostyczne oraz interfejs raportów tekstowych i HTML obsługują 45 języków (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) bez dodatkowych zależności. Rozpoznawanie języka sprawdza `--lang` (odróżniane od `--language`, które wybiera edycję Wikipedia), następnie `LC_ALL`, `LC_MESSAGES` i `LANG`, z powrotem do `en`. Klucze wyjściowe JSON oraz szablony wikitekstu pozostają niezmienione.

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

## Rozwój

Uruchomienie testów:

```
python -m pytest tests/ -x -q
```

Linting:

```
ruff check src/ tests/
```

## Wymagania

- Python 3.12+
- mwparserfromhell

## Licencja

MIT
