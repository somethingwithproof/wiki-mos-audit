# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · **Français (Maroc)** · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Un outil d'audit de premier passage conforme au [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) pour les articles Wikipedia.

## Pourquoi cet outil existe

Je contribue sur Wikipedia. Pas en permanence, mais suffisamment pour avoir remarqué un schéma récurrent : à chaque fois que j'ouvrais un article pour le nettoyer, je déroulais la même liste de vérification mentale. Les dates sont-elles cohérentes ? Y a-t-il des tournures évasives ? Quelqu'un a-t-il laissé des URL nues dans les références ? La section Voir aussi est-elle surchargée ? Les sections de fin d'article sont-elles dans le bon ordre ?

Après avoir parcouru manuellement la même douzaine de problèmes trois ou quatre fois de suite, j'ai écrit un script. Ce script s'est étoffé. Aujourd'hui, il vérifie plus de 30 points que je contrôlais à la main, et il repère des détails qui m'auraient échappé un mardi soir de fatigue.

Cet outil ne remplace pas le jugement éditorial. C'est un outil de tri. Il vous indique où regarder, pas ce qu'il faut écrire.

## Ce qu'il vérifie

**Style et ton**
- Tournures évasives (MOS:WEASEL), termes dithyrambiques (MOS:PEACOCK)
- Expressions temporelles relatives ("récemment", "actuellement") qui vieillissent mal
- Signaux de contenu généré par IA : sur-attribution dans le corps du texte (WP:AISIGNS), tournures de style essai (WP:NOTESSAY)
- Alertes terminologiques MOS:INDIGENOUS
- Mise en forme des désignations MOS:AVIATION
- Mentions de pertes non sourcées selon MOS:MILITARY

**Structure**
- Longueur du résumé introductif et nombre de paragraphes (MOS:LEAD)
- Ordre des sections par rapport à MOS:LAYOUT
- Sections courtes ou insuffisamment développées
- Sections sans références (100+ mots, sans `<ref>`)
- Surcharge de la section Voir aussi
- URL externes nues dans le corps de l'article
- Densité des modèles de citation

**Références et citations**
- URL nues à l'intérieur des balises `<ref>` (sans modèle de citation)
- Validation de la clé de contrôle ISBN
- URL mal formées dans les modèles de citation
- Liens externes morts (en option, lent)

**Catégories et liens**
- Catégories manquantes
- Qualité des catégories (sous-catégorisation, catégories trop générales)
- Détection des liens rouges (liens wiki vers des articles inexistants)
- Catégories en lien rouge
- Liens vers des pages d'homonymie
- Sur-liaison interne (MOS:OVERLINK)

**Infobox**
- Nombre de paramètres et densité de listes (détection de surcharge)
- Paramètres couramment attendus mais absents
- Signaux d'infobox MOS:MILHIST

**Autres**
- Qualité de la description courte (absente, trop longue, identique au titre)
- Inventaire des bandeaux de maintenance
- Conformité des liens vers les projets frères (MOS:SISTER)
- Détection des articles orphelins (aucun lien wiki entrant)
- Découverte de liens retour potentiels
- Motifs de titres de type chronologie ou direct (liveblog)

Chaque contrôle produit une anomalie assortie d'un niveau de gravité (faible/moyen/élevé) et d'une déduction de points. Un article propre obtient un score de 100.

## Installation

```
pip install .
```

mwparserfromhell est une dépendance requise. Elle assure une analyse du wikitexte fondée sur l'AST pour une détection précise des modèles, des titres et des liens wiki. Si sa compilation est impossible (absence de compilateur C), l'outil bascule automatiquement vers une analyse par expressions régulières.

Pour le développement :

```
pip install -e '.[dev]'
```

## Utilisation

Auditer un article Wikipedia en ligne :

```
wiki-mos-audit "Gettysburg Address"
```

Auditer depuis une URL :

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Auditer un fichier wikitexte local :

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Auditer par lot un répertoire de fichiers wikitexte :

```
wiki-mos-audit --dir ./articles/
```

Ignorer les vérifications via l'API (mode hors ligne) :

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Formats de sortie

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Vérifications optionnelles

Elles sont désactivées par défaut car elles sont lentes ou nécessitent un accès réseau :

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Correction automatique

Des corrections mécaniques sûres (espaces, mise en forme) peuvent être appliquées automatiquement :

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Prévisualiser sans enregistrer :

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Mode diff

Comparer un wikitexte local avec la version en ligne :

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Configuration

Créez un fichier `.wiki-mos-audit.toml` pour ajuster les seuils ou désactiver certains contrôles :

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Le transmettre explicitement :

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Localisation

L'aide en ligne de commande, les diagnostics et l'habillage des rapports texte/HTML prennent en charge 45 locales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) sans aucune dépendance supplémentaire. La résolution vérifie `--lang` (distinct de `--language`, qui sélectionne l'édition de Wikipedia), puis `LC_ALL`, `LC_MESSAGES` et `LANG`, avec repli sur `en`. Les clés de sortie JSON et les modèles wikitexte demeurent inchangés.

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

## Développement

Lancer les tests :

```
python -m pytest tests/ -x -q
```

Analyse statique :

```
ruff check src/ tests/
```

## Prérequis

- Python 3.12+
- mwparserfromhell

## Licence

MIT
