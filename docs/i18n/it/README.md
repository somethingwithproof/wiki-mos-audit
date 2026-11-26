# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · **Italiano** · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Uno strumento di verifica preliminare secondo il [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) per le voci di Wikipedia.

## Perché esiste

Modifico voci su Wikipedia. Non costantemente, ma abbastanza da aver iniziato a notare uno schema ricorrente: ogni volta che aprivo una voce per ripulirla, eseguivo mentalmente la stessa lista di controlli. Le date sono coerenti? Ci sono espressioni evasive? Qualcuno ha lasciato URL nudi nei riferimenti? La sezione Voci correlate è eccessivamente lunga? Le sezioni finali sono nell'ordine giusto?

Dopo la terza o quarta volta che cercavo manualmente la stessa dozzina di problemi uno dopo l'altro, ho scritto uno script. Quello script è cresciuto. Ora controlla più di 30 aspetti che verificavo a mano e intercetta dettagli che mi sfuggirebbero in una sera stanca di martedì.

Non sostituisce il giudizio editoriale. È uno strumento di triage: ti indica dove guardare, non cosa scrivere.

## Cosa controlla

**Stile e tono**
- Espressioni evasive (MOS:WEASEL), termini enfatici (MOS:PEACOCK)
- Espressioni temporali relative ("di recente", "attualmente") che invecchiano male
- Segnali di contenuto generato dall'IA: eccessiva attribuzione nel corpo del testo (WP:AISIGNS), formulazioni in stile saggio (WP:NOTESSAY)
- Segnalazioni terminologiche MOS:INDIGENOUS
- Formattazione delle designazioni MOS:AVIATION
- Affermazioni non supportate da fonti sulle vittime secondo MOS:MILITARY

**Struttura**
- Lunghezza dell'incipit e numero di paragrafi (MOS:LEAD)
- Ordinamento delle sezioni rispetto a MOS:LAYOUT
- Sezioni brevi o poco sviluppate
- Sezioni prive di fonti (oltre 100 parole, nessun `<ref>`)
- Gonfiamento della sezione Voci correlate
- URL esterni nudi nel corpo della voce
- Densità dei template di citazione testuale

**Riferimenti e note**
- URL nudi all'interno dei tag `<ref>` (senza template di citazione)
- Validazione della cifra di controllo ISBN
- URL malformati nei template di citazione
- Collegamenti esterni interrotti (opt-in, lento)

**Categorie e collegamenti**
- Categorie mancanti
- Qualità delle categorie (sottocategorizzazione, categorie troppo ampie)
- Rilevamento di link rossi (wikilink a voci inesistenti)
- Categorie con link rossi
- Collegamenti a pagine di disambiguazione
- Eccesso di collegamenti (MOS:OVERLINK)

**Infobox**
- Numero di parametri e densità degli elenchi (rilevamento del gonfiamento)
- Parametri comunemente attesi mancanti
- Segnali infobox MOS:MILHIST

**Altro**
- Qualità della descrizione breve (mancante, troppo lunga, identica al titolo)
- Inventario dei template di avviso/manutenzione
- Igiene dei collegamenti ai progetti fratelli (MOS:SISTER)
- Rilevamento di voci orfane (nessun wikilink in entrata)
- Ricerca di potenziali backlink
- Schemi di intestazioni in stile cronologia/liveblog

Ogni controllo genera una segnalazione classificata per gravità (low/medium/high) con una penalità sul punteggio. Una voce pulita ottiene 100.

## Installazione

```
pip install .
```

mwparserfromhell è una dipendenza obbligatoria. Fornisce il parsing del wikitesto basato su AST per rilevare con precisione template, intestazioni e wikilink. Se non può essere compilato (nessun compilatore C disponibile), lo strumento ripiega automaticamente sul parsing basato su regex.

Per lo sviluppo:

```
pip install -e '.[dev]'
```

## Utilizzo

Analizza una voce live di Wikipedia:

```
wiki-mos-audit "Gettysburg Address"
```

Analizza da un URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Analizza un file wikitesto locale:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Analizza in batch una directory di file wikitesto:

```
wiki-mos-audit --dir ./articles/
```

Salta i controlli API (modalità offline):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Formati di output

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Controlli opzionali

Sono disattivati per impostazione predefinita perché lenti o perché richiedono l'accesso alla rete:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Correzione automatica

Le correzioni meccaniche sicure (spazi bianchi, formattazione) possono essere applicate automaticamente:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Anteprima senza scrivere su file:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Modalità diff

Confronta il wikitesto locale con la versione live:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Configurazione

Crea un file `.wiki-mos-audit.toml` per regolare le soglie o disabilitare controlli specifici:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Passalo esplicitamente:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Localizzazione

La guida della CLI, i messaggi diagnostici e l'interfaccia dei report testuali/HTML supportano 45 lingue (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) senza dipendenze aggiuntive. La risoluzione controlla `--lang` (distinto da `--language`, che seleziona l'edizione di Wikipedia), poi `LC_ALL`, `LC_MESSAGES` e `LANG`, ripiegando su `en`. Le chiavi dell'output JSON e i template del wikitesto restano invariati.

```
wiki-mos-audit "Article" --lang de --wikitext-file article.txt
LANG=fr_FR.UTF-8 wiki-mos-audit --help
```

## API Python

```python
from wiki_mos_audit import audit_mos

report = audit_mos("Article Title", wikitext)
print(f"Score: {report.score}/100")
for issue in report.issues:
    print(f"[{issue.severity}] {issue.check_id}: {issue.message}")
```

## Sviluppo

Esegui i test:

```
python -m pytest tests/ -x -q
```

Lint:

```
ruff check src/ tests/
```

## Requisiti

- Python 3.12+
- mwparserfromhell

## Licenza

MIT
