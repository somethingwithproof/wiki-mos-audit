# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · **한국어** · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Wikipedia 문서를 위한 1차 [편집 지침(Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) 감사 도구입니다.

## 제작 배경

저는 Wikipedia를 편집합니다. 아주 자주 하는 것은 아니지만, 어느 순간 일정한 패턴을 발견하게 되었습니다. 문서를 정리하려고 열 때마다 매번 머릿속으로 같은 체크리스트를 돌리고 있었습니다. 날짜 형식이 일관적인가? 모호한 표현(weasel words)은 없는가? 누군가 각주에 일반 URL만 남겨두지는 않았는가? '같이 보기(See also)' 문단이 지나치게 길지는 않은가? 하단 항목 문단들의 순서가 올바른가?

같은 열두 가지 문제를 연달아 세네 번 수동으로 훑어본 뒤, 스크립트를 하나 작성했습니다. 그 스크립트가 점점 커졌습니다. 이제는 손으로 확인하던 30가지 이상의 항목을 검사하며, 피곤한 화요일 저녁에 놓치기 쉬운 부분까지 잡아냅니다.

이 도구는 편집자의 판단을 대체하지 않습니다. 분류(triage) 도구입니다. 무엇을 써야 할지가 아니라 어디를 살펴봐야 할지 알려줍니다.

## 검사 항목

**문체 및 어조**
- 모호한 표현(MOS:WEASEL), 과장된 표현(MOS:PEACOCK)
- 시간이 지나면 부적절해지는 상대적 시간 표현("recently", "currently")
- AI 생성 콘텐츠 신호: 본문 내 과도한 출처 귀속(WP:AISIGNS), 에세이풍 표현(WP:NOTESSAY)
- MOS:INDIGENOUS 용어 플래그
- MOS:AVIATION 제식 명칭 서식
- MOS:MILITARY 출처 없는 사상자 서술

**구조**
- 도입부 길이 및 문단 수(MOS:LEAD)
- MOS:LAYOUT 기준 문단 순서
- 짧거나 충분히 작성되지 않은 문단
- 출처 없는 문단(100단어 이상, `<ref>` 없음)
- '같이 보기(See also)' 문단 비대화
- 문서 본문 내 일반 외부 URL
- 인용문 틀 밀도

**출처 및 인용**
- `<ref>` 태그 내부의 일반 URL(인용 틀 미사용)
- ISBN 체크 디지트 검증
- 인용 틀 내 잘못된 형식의 URL
- 죽은 외부 링크(선택적 활성화, 느림)

**분류 및 링크**
- 누락된 분류
- 분류 품질(분류 부족, 지나치게 광범위함)
- 빨간 링크 감지(존재하지 않는 문서로의 위키링크)
- 빨간 링크 분류
- 동음이의어 문서 링크
- 과도한 링크(MOS:OVERLINK)

**정보상자(Infobox)**
- 매개변수 수 및 목록 밀도(비대화 감지)
- 일반적으로 기대되는 매개변수 누락
- MOS:MILHIST 정보상자 신호

**기타**
- 짧은 설명(Short description) 품질(누락, 너무 김, 제목과 일치)
- 정비 틀 목록
- 자매 프로젝트 링크 위생(MOS:SISTER)
- 외톨이 문서 감지(들어오는 위키링크 없음)
- 잠재적 역링크 탐색
- 타임라인/라이브블로그 형식의 제목 패턴

각 검사는 점수 차감과 함께 심각도 등급(low/medium/high)이 지정된 이슈를 생성합니다. 깨끗한 문서는 100점을 받습니다.

## 설치

```
pip install .
```

mwparserfromhell은 필수 종속성입니다. 정확한 틀, 제목 및 위키링크 감지를 위해 AST 기반 위키텍스트 파싱을 제공합니다. 컴파일할 수 없는 경우(사용 가능한 C 컴파일러가 없는 경우) 도구는 자동으로 정규표현식 기반 파싱으로 폴백합니다.

개발용 설치:

```
pip install -e '.[dev]'
```

## 사용법

라이브 Wikipedia 문서 감사:

```
wiki-mos-audit "Gettysburg Address"
```

URL로 감사:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

로컬 위키텍스트 파일 감사:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

위키텍스트 파일 디렉터리 일괄 감사:

```
wiki-mos-audit --dir ./articles/
```

API 검사 건너뛰기(오프라인 모드):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### 출력 형식

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### 선택적 검사

다음 항목은 속도가 느리거나 네트워크 접근이 필요하므로 기본적으로 꺼져 있습니다:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### 자동 수정

안전한 기계적 수정(공백, 서식)은 자동으로 적용할 수 있습니다:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

파일에 쓰지 않고 미리 보기:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Diff 모드

로컬 위키텍스트를 라이브 버전과 비교:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### 구성

임계값을 조정하거나 특정 검사를 비활성화하려면 `.wiki-mos-audit.toml` 파일을 생성하세요:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

명시적으로 전달하기:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### 지역화

CLI 도움말, 진단 및 텍스트/HTML 보고서 크롬(chrome)은 추가 종속성 없이 45개 로캘(`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`)을 지원합니다. 로캘 확인은 `--lang`(Wikipedia 에디션을 선택하는 `--language`와 구분됨), `LC_ALL`, `LC_MESSAGES`, `LANG` 순서로 확인하며 기본값은 `en`입니다. JSON 출력 키와 위키텍스트 틀은 변경되지 않습니다.

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

## 개발

테스트 실행:

```
python -m pytest tests/ -x -q
```

린트:

```
ruff check src/ tests/
```

## 요구 사항

- Python 3.12+
- mwparserfromhell

## 라이선스

MIT
