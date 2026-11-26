# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · **Français (Sénégal)** · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Un outil d'audit de premier passage conforme au [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) pour les articles Wikipedia.

## Pourquoi cet outil existe

Je contribue à Wikipedia. Pas tout le temps, mais assez pour avoir remarqué une habitude : chaque fois que j'ouvrais un article pour le nettoyer, je déroulais la même liste de vérifications en tête. Les dates sont-elles cohérentes ? Y a-t-il des formules évasives ? Quelqu'un a-t-il laissé des URL brutes dans les références ? La section « See also » est-elle surchargée ? Les sections de fin d'article sont-elles dans le bon ordre ?

Après la troisième ou quatrième fois à passer manuellement en revue la même douzaine de défauts d'affilée, j'ai écrit un script. Ce script s'est développé. Aujourd'hui, il vérifie plus de 30 points que je contrôlais à la main, et il repère des choses qui m'échapperaient un mardi soir de fatigue.

Cet outil ne remplace pas le jugement éditorial. C'est un outil de tri. Il vous indique où regarder, pas quoi rédiger.

## Ce qu'il vérifie

**Style et ton**
- Formules évasives (MOS:WEASEL), termes emphatiques ou promotionnels (MOS:PEACOCK)
- Expressions temporelles relatives ("recently", "currently") qui vieillissent mal
- Signaux de contenu généré par IA : sur-attribution dans le corps du texte (WP:AISIGNS), tournures d'essai (WP:NOTESSAY)
- Signalements terminologiques MOS:INDIGENOUS
- Formatage des désignations MOS:AVIATION
- Mentions de pertes humaines non sourcées selon MOS:MILITARY

**Structure**
- Longueur du résumé introductif et nombre de paragraphes (MOS:LEAD)
- Ordre des sections selon MOS:LAYOUT
- Sections courtes ou peu développées
- Sections sans références (100+ mots, sans `<ref>`)
- Surcharge de la section « See also »
- URL externes brutes dans le corps de l'article
- Densité des modèles de citation

**Références et citations**
- URL brutes à l'intérieur des balises `<ref>` (sans modèle de citation)
- Validation de la clé de contrôle ISBN
- URL malformées dans les modèles de citation
- Liens externes morts (en option, lent)

**Catégories et liens**
- Catégories manquantes
- Qualité des catégories (sous-catégorisé, trop général)
- Détection des liens rouges (liens internes vers des articles inexistants)
- Catégories en lien rouge
- Liens vers des pages d'homonymie
- Sur-liage (MOS:OVERLINK)

**Infobox**
- Nombre de paramètres et densité des listes (détection de surcharge)
- Paramètres couramment attendus manquants
- Signaux d'infobox MOS:MILHIST

**Autres**
- Qualité de la description courte (absente, trop longue, identique au titre)
- Inventaire des bandeaux de maintenance
- Propreté des liens vers les projets frères (MOS:SISTER)
- Détection d'articles orphelins (aucun lien interne entrant)
- Découverte de liens retour potentiels
- Schémas de titres de type chronologie ou suivi en direct

Chaque vérification produit un problème classé par gravité (faible/moyenne/élevée) avec une déduction de points. Un article propre obtient un score de 100.

## Installation

```
pip install .
```

mwparserfromhell est une dépendance requise. Elle fournit une analyse du wikitexte fondée sur l'AST pour une détection précise des modèles, des titres et des liens internes. Si sa compilation est impossible (aucun compilateur C disponible), l'outil bascule automatiquement sur une analyse par expressions régulières.

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

Auditer en lot un dossier de fichiers wikitexte :

```
wiki-mos-audit --dir ./articles/
```

Ignorer les vérifications API (mode hors ligne) :

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

Elles sont désactivées par défaut parce qu'elles sont lentes ou exigent un accès réseau :

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

Prévisualiser sans écrire :

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Mode diff

Comparer un wikitexte local à la version en ligne :

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Configuration

Créez un fichier `.wiki-mos-audit.toml` pour ajuster les seuils ou désactiver certaines vérifications :

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Le passer explicitement :

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Localisation

L'aide CLI, les diagnostics et l'habillage des rapports texte/HTML prennent en charge 45 locales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) sans aucune dépendance supplémentaire. La résolution vérifie `--lang` (distinct de `--language`, qui choisit l'édition Wikipedia), puis `LC_ALL`, `LC_MESSAGES` et `LANG`, avec repli sur `en`. Les clés de sortie JSON et les modèles wikitexte restent inchangés.

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

Analyse de code :

```
ruff check src/ tests/
```

## Prérequis

- Python 3.12+
- mwparserfromhell

## Licence

MIT
