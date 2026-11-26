# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · **Deutsch** · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Ein Erstprüfungs-Auditor für den [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) bei Wikipedia-Artikeln.

## Warum es das gibt

Ich bearbeite Wikipedia. Nicht ständig, aber oft genug, dass mir ein Muster auffiel: Jedes Mal, wenn ich einen Artikel zum Aufräumen öffnete, ging ich im Kopf dieselbe Checkliste durch. Sind die Datumsformate konsistent? Gibt es Wieselwörter? Hat jemand nackte URLs in den Einzelnachweisen gelassen? Ist der Abschnitt „Siehe auch“ aufgebläht? Stehen die Schlussabschnitte in der richtigen Reihenfolge?

Nachdem ich zum dritten oder vierten Mal hintereinander manuell nach demselben Dutzend Problemen gesucht hatte, schrieb ich ein Skript. Dieses Skript wuchs. Jetzt prüft es über 30 Dinge, die ich früher von Hand erledigt habe, und findet Sachen, die ich an einem müden Dienstagabend übersehen würde.

Dies ist kein Ersatz für redaktionelles Urteilsvermögen. Es ist ein Triage-Werkzeug. Es zeigt Ihnen, wo Sie hinschauen sollten, nicht, was Sie schreiben sollen.

## Was geprüft wird

**Stil und Ton**
- Wieselwörter (MOS:WEASEL), schmückende/wertende Ausdrücke (MOS:PEACOCK)
- Relative Zeitangaben („recently“, „currently“), die schlecht altern
- Signale für KI-generierte Inhalte: Überattribution im Fließtext (WP:AISIGNS), essayartige Formulierungen (WP:NOTESSAY)
- Hinweise zur Terminologie nach MOS:INDIGENOUS
- Formatierung von Bezeichnungen nach MOS:AVIATION
- Unbelegte Opferzahlen nach MOS:MILITARY

**Struktur**
- Länge und Absatzanzahl der Einleitung (MOS:LEAD)
- Reihenfolge der Abschnitte gemäß MOS:LAYOUT
- Kurze oder unterentwickelte Abschnitte
- Unbelegte Abschnitte (100+ Wörter, kein `<ref>`)
- Aufblähung des Abschnitts „Siehe auch“
- Nackte externe URLs im Artikeltext
- Dichte von Zitat-Vorlagen

**Einzelnachweise und Belege**
- Nackte URLs innerhalb von `<ref>`-Tags (ohne Zitationsvorlage)
- Validierung der ISBN-Prüfziffer
- Fehlerhafte URLs in Zitationsvorlagen
- Tote externe Links (Opt-in, langsam)

**Kategorien und Links**
- Fehlende Kategorien
- Kategoriequalität (unterkategorisiert, zu allgemein)
- Erkennung roter Links (Wikilinks auf nicht existierende Artikel)
- Kategorien mit roten Links
- Links auf Begriffsklärungsseiten
- Überverlinkung (MOS:OVERLINK)

**Infobox**
- Parameteranzahl und Listendichte (Erkennung von Aufblähung)
- Fehlende häufig erwartete Parameter
- MOS:MILHIST-Infobox-Signale

**Sonstiges**
- Qualität der Kurzbeschreibung (fehlt, zu lang, entspricht dem Titel)
- Bestandsaufnahme von Wartungsbausteinen
- Hygiene bei Schwesterprojekt-Links (MOS:SISTER)
- Erkennung verwaister Artikel (keine eingehenden Wikilinks)
- Ermittlung potenzieller Backlinks
- Überschriftsmuster für Zeitleisten/Liveblogs

Jede Prüfung erzeugt ein nach Schweregrad eingestuftes Problem (niedrig/mittel/hoch) mit einem Punktabzug. Ein sauberer Artikel erreicht 100 Punkte.

## Installation

```
pip install .
```

mwparserfromhell ist eine erforderliche Abhängigkeit. Es stellt AST-basiertes Wikitext-Parsing für eine präzise Erkennung von Vorlagen, Überschriften und Wikilinks bereit. Kann es nicht kompiliert werden (kein C-Compiler verfügbar), greift das Werkzeug automatisch auf Regex-basiertes Parsing zurück.

Für die Entwicklung:

```
pip install -e '.[dev]'
```

## Verwendung

Einen Live-Wikipedia-Artikel prüfen:

```
wiki-mos-audit "Gettysburg Address"
```

Anhand einer URL prüfen:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Eine lokale Wikitext-Datei prüfen:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Ein Verzeichnis von Wikitext-Dateien im Stapel prüfen:

```
wiki-mos-audit --dir ./articles/
```

API-Prüfungen überspringen (Offline-Modus):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Ausgabeformate

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Optionale Prüfungen

Diese sind standardmäßig deaktiviert, da sie langsam sind oder Netzwerkzugriff benötigen:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Automatische Korrektur

Sichere mechanische Korrekturen (Leerzeichen, Formatierung) können automatisch angewendet werden:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Vorschau ohne Schreiben:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Diff-Modus

Lokalen Wikitext mit der Live-Version vergleichen:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Konfiguration

Erstellen Sie eine Datei `.wiki-mos-audit.toml`, um Schwellenwerte anzupassen oder bestimmte Prüfungen zu deaktivieren:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Explizit übergeben:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Lokalisierung

CLI-Hilfe, Diagnosemeldungen sowie Text- und HTML-Berichtsrahmen unterstützen 45 Locales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ohne zusätzliche Abhängigkeiten. Die Auflösung prüft `--lang` (unterschiedlich zu `--language`, das die Wikipedia-Sprachausgabe wählt), dann `LC_ALL`, `LC_MESSAGES` und `LANG` und fällt auf `en` zurück. JSON-Ausgabeschlüssel und Wikitext-Vorlagen bleiben unverändert.

```
wiki-mos-audit "Article" --lang de --wikitext-file article.txt
LANG=fr_FR.UTF-8 wiki-mos-audit --help
```

## Python-API

```python
from wiki_mos_audit import audit_mos

report = audit_mos("Article Title", wikitext)
print(f"Score: {report.score}/100")
for issue in report.issues:
    print(f"[{issue.severity}] {issue.check_id}: {issue.message}")
```

## Entwicklung

Tests ausführen:

```
python -m pytest tests/ -x -q
```

Linting:

```
ruff check src/ tests/
```

## Voraussetzungen

- Python 3.12+
- mwparserfromhell

## Lizenz

MIT
