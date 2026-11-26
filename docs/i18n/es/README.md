# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · **Español** · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Un auditor de primera pasada del [Manual de Estilo](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) para artículos de Wikipedia.

## Por qué existe esto

Edito Wikipedia. No constantemente, pero sí lo suficiente como para empezar a notar un patrón: cada vez que abría un artículo para limpiarlo, repasaba la misma lista mental. ¿Son consistentes las fechas? ¿Hay palabras comadreja? ¿Alguien dejó URLs desnudas en las referencias? ¿Está inflada la sección Véase también? ¿Están en el orden correcto las secciones finales?

Después de la tercera o cuarta vez revisando manualmente la misma docena de problemas seguidos, escribí un script. Ese script creció. Ahora comprueba más de 30 cosas que antes hacía a mano y detecta detalles que se me escaparían un martes por la noche con cansancio.

Esto no sustituye el criterio editorial. Es una herramienta de triaje. Te dice dónde mirar, no qué escribir.

## Qué comprueba

**Estilo y tono**
- Palabras comadreja (MOS:WEASEL), términos grandilocuentes (MOS:PEACOCK)
- Expresiones de tiempo relativas ("recientemente", "actualmente") que envejecen mal
- Señales de contenido generado por IA: exceso de atribución en el texto del cuerpo (WP:AISIGNS), redacción con tono de ensayo (WP:NOTESSAY)
- Avisos de terminología de MOS:INDIGENOUS
- Formato de designaciones de MOS:AVIATION
- Declaraciones de bajas sin citar según MOS:MILITARY

**Estructura**
- Longitud de la introducción y número de párrafos (MOS:LEAD)
- Orden de las secciones según MOS:LAYOUT
- Secciones cortas o poco desarrolladas
- Secciones sin referencias (más de 100 palabras, sin `<ref>`)
- Exceso de enlaces en la sección Véase también
- URLs externas desnudas en el cuerpo del artículo
- Densidad de plantillas de citas textuales

**Referencias y citas**
- URLs desnudas dentro de etiquetas `<ref>` (sin plantilla de cita)
- Validación del dígito de control de ISBN
- URLs mal formadas en plantillas de citas
- Enlaces externos rotos (opcional, lento)

**Categorías y enlaces**
- Categorías faltantes
- Calidad de las categorías (subcategorizado, demasiado general)
- Detección de enlaces en rojo (wikienlaces a artículos inexistentes)
- Categorías en rojo
- Enlaces a páginas de desambiguación
- Exceso de enlaces internos (MOS:OVERLINK)

**Ficha (Infobox)**
- Cantidad de parámetros y densidad de listas (detección de sobrecarga)
- Parámetros esperados habitualmente faltantes
- Señales de ficha MOS:MILHIST

**Otros**
- Calidad de la descripción corta (faltante, demasiado larga, coincide con el título)
- Inventario de plantillas de mantenimiento
- Higiene de enlaces a proyectos hermanos (MOS:SISTER)
- Detección de artículos huérfanos (sin wikienlaces entrantes)
- Descubrimiento de posibles enlaces entrantes
- Patrones de encabezados de cronología/blog en vivo

Cada comprobación genera un problema con nivel de gravedad (baja/media/alta) y una deducción de puntuación. Un artículo limpio obtiene 100 puntos.

## Instalación

```
pip install .
```

mwparserfromhell es una dependencia obligatoria. Proporciona análisis sintáctico de wikitexto basado en AST para una detección precisa de plantillas, encabezados y wikienlaces. Si no puede compilarse (no hay un compilador de C disponible), la herramienta recurre automáticamente al análisis basado en expresiones regulares.

Para desarrollo:

```
pip install -e '.[dev]'
```

## Uso

Auditar un artículo de Wikipedia en vivo:

```
wiki-mos-audit "Gettysburg Address"
```

Auditar desde una URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Auditar un archivo de wikitexto local:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Auditar por lotes un directorio de archivos de wikitexto:

```
wiki-mos-audit --dir ./articles/
```

Omitir comprobaciones de API (modo sin conexión):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Formatos de salida

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Comprobaciones opcionales

Están desactivadas de forma predeterminada porque son lentas o requieren acceso a la red:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Corrección automática

Se pueden aplicar automáticamente correcciones mecánicas seguras (espacios en blanco, formato):

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Vista previa sin escribir cambios:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Modo diff

Comparar el wikitexto local con la versión en vivo:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Configuración

Crea un archivo `.wiki-mos-audit.toml` para ajustar umbrales o desactivar comprobaciones específicas:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Pásalo explícitamente:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Localización

La ayuda de la CLI, los diagnósticos y la interfaz de los informes en texto/HTML admiten 45 configuraciones regionales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) sin dependencias adicionales. La resolución comprueba `--lang` (distinto de `--language`, que selecciona la edición de Wikipedia), luego `LC_ALL`, `LC_MESSAGES` y `LANG`, recurriendo a `en`. Las claves de salida JSON y las plantillas de wikitexto permanecen sin cambios.

```
wiki-mos-audit "Article" --lang de --wikitext-file article.txt
LANG=fr_FR.UTF-8 wiki-mos-audit --help
```

## API de Python

```python
from wiki_mos_audit import audit_mos

report = audit_mos("Article Title", wikitext)
print(f"Score: {report.score}/100")
for issue in report.issues:
    print(f"[{issue.severity}] {issue.check_id}: {issue.message}")
```

## Desarrollo

Ejecutar pruebas:

```
python -m pytest tests/ -x -q
```

Lint:

```
ruff check src/ tests/
```

## Requisitos

- Python 3.12+
- mwparserfromhell

## Licencia

MIT
