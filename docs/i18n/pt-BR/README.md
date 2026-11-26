# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · **Português (BR)** · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Um auditor de primeira passagem do [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) para artigos da Wikipedia.

## Por que isso existe

Eu edito a Wikipedia. Não constantemente, mas o suficiente para começar a notar um padrão: toda vez que eu abria um artigo para fazer uma revisão geral, passava pela mesma lista mental. As datas estão consistentes? Há termos evasivos? Alguém deixou URLs soltas nas referências? A seção See also está inchada? As seções finais estão na ordem certa?

Depois da terceira ou quarta vez procurando manualmente os mesmos problemas em sequência, escrevi um script. Esse script cresceu. Agora ele verifica mais de 30 coisas que eu fazia à mão e pega detalhes que eu deixaria passar em uma noite cansativa de terça-feira.

Isso não substitui o julgamento editorial. É uma ferramenta de triagem. Ela mostra onde olhar, não o que escrever.

## O que ele verifica

**Estilo e tom**
- Termos evasivos (MOS:WEASEL), termos elogiosos exagerados (MOS:PEACOCK)
- Expressões temporais relativas ("recently", "currently") que envelhecem mal
- Sinais de conteúdo gerado por IA: excesso de atribuição no corpo do texto (WP:AISIGNS), tom de ensaio (WP:NOTESSAY)
- Alertas de terminologia de MOS:INDIGENOUS
- Formatação de designações de MOS:AVIATION
- Declarações de baixas sem fontes em MOS:MILITARY

**Estrutura**
- Comprimento e quantidade de parágrafos da introdução (MOS:LEAD)
- Ordenação de seções em relação a MOS:LAYOUT
- Seções curtas ou pouco desenvolvidas
- Seções sem referências (100+ palavras, sem `<ref>`)
- Inchaço na seção See also
- URLs externas soltas no corpo do artigo
- Densidade de predefinições de citação

**Referências e citações**
- URLs soltas dentro de tags `<ref>` (sem predefinição de citação)
- Validação do dígito verificador de ISBN
- URLs malformadas em predefinições de citação
- Links externos quebrados (opcional, lento)

**Categorias e links**
- Categorias ausentes
- Qualidade das categorias (subcategorizado, amplo demais)
- Detecção de links vermelhos (wikilinks para artigos inexistentes)
- Categorias com link vermelho
- Links para páginas de desambiguação
- Excesso de links (MOS:OVERLINK)

**Infobox**
- Contagem de parâmetros e densidade de listas (detecção de inchaço)
- Parâmetros comumente esperados ausentes
- Sinais de infobox de MOS:MILHIST

**Outros**
- Qualidade da descrição curta (ausente, longa demais, igual ao título)
- Inventário de predefinições de manutenção
- Higiene de links para projetos irmãos (MOS:SISTER)
- Detecção de páginas órfãs (sem wikilinks de entrada)
- Descoberta de potenciais backlinks
- Padrões de cabeçalhos de linha do tempo ou liveblog

Cada verificação gera um problema classificado por severidade (low/medium/high) com uma dedução de pontuação. Um artigo limpo recebe pontuação 100.

## Instalação

```
pip install .
```

mwparserfromhell é uma dependência obrigatória. Ele fornece parsing de wikitext baseado em AST para detecção precisa de predefinições, cabeçalhos e wikilinks. Se não puder ser compilado (sem compilador C disponível), a ferramenta recorre automaticamente ao parsing baseado em regex.

Para desenvolvimento:

```
pip install -e '.[dev]'
```

## Uso

Auditar um artigo ativo da Wikipedia:

```
wiki-mos-audit "Gettysburg Address"
```

Auditar a partir de uma URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Auditar um arquivo wikitext local:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Auditar em lote um diretório de arquivos wikitext:

```
wiki-mos-audit --dir ./articles/
```

Pular verificações de API (modo offline):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Formatos de saída

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Verificações opcionais

Estas vêm desativadas por padrão porque são lentas ou exigem acesso à rede:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Correção automática

Correções mecânicas seguras (espaçamento, formatação) podem ser aplicadas automaticamente:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Pré-visualizar sem gravar:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Modo diff

Comparar wikitext local com a versão ativa:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Configuração

Crie um arquivo `.wiki-mos-audit.toml` para ajustar limites ou desativar verificações específicas:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Passe-o explicitamente:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Localização

A ajuda da CLI, os diagnósticos e os elementos de interface dos relatórios em texto/HTML oferecem suporte a 45 idiomas (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) sem dependências extras. A resolução verifica `--lang` (diferente de `--language`, que seleciona a edição da Wikipedia), depois `LC_ALL`, `LC_MESSAGES` e `LANG`, recorrendo a `en` como padrão. As chaves de saída JSON e as predefinições de wikitext permanecem inalteradas.

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

## Desenvolvimento

Executar testes:

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

## Licença

MIT
