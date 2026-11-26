# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · **ไทย** · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

เครื่องมือตรวจสอบเบื้องต้นตาม[คู่มือการเขียน (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) สำหรับบทความ Wikipedia

## ที่มาของโปรเจกต์

ผมเป็นคนแก้ไขบทความบน Wikipedia แม้ไม่ได้ทำตลอดเวลา แต่ก็บ่อยพอที่จะเริ่มสังเกตเห็นรูปแบบเดิมๆ: ทุกครั้งที่เปิดบทความขึ้นมาเพื่อจัดระเบียบ ผมมักจะไล่เช็กรายการเดิมๆ ในใจเสมอ รูปแบบวันที่สอดคล้องกันไหม? มีคำเลี่ยงความชัดเจน (weasel words) หรือเปล่า? มีใครทิ้ง URL เปล่าไว้ในรายการอ้างอิงไหม? ส่วน See also เยิ่นเย้อเกินไปหรือเปล่า? ส่วนท้ายบทความเรียงลำดับถูกต้องไหม?

หลังจากต้องกวาดสายตาหาปัญหาเดิมๆ ซ้ำๆ เป็นสิบอย่างติดต่อกันสามสี่ครั้ง ผมก็เลยเขียนสคริปต์ขึ้นมา สคริปต์นั้นค่อยๆ เติบโต จนตอนนี้สามารถตรวจสอบได้มากกว่า 30 รายการที่ผมเคยทำด้วยมือ และช่วยจับจุดที่ผมอาจเผลอมองข้ามไปในคืนวันอังคารที่เหนื่อยล้า

เครื่องมือนี้ไม่ได้มีไว้แทนที่วิจารณญาณของบรรณาธิการ แต่เป็นเครื่องมือคัดกรองเบื้องต้นที่คอยบอกคุณว่าควรไปตรวจดูตรงไหน ไม่ใช่บอกว่าต้องเขียนอะไร

## สิ่งที่ตรวจสอบได้

**รูปแบบการเขียนและน้ำเสียง**
- คำเลี่ยงความชัดเจน (MOS:WEASEL) และคำเยินยอเกินจริง (MOS:PEACOCK)
- สำนวนบอกเวลาแบบสัมพัทธ์ ("recently", "currently") ที่จะล้าสมัยเมื่อเวลาผ่านไป
- สัญญาณเนื้อหาที่สร้างโดย AI: การอ้างอิงแหล่งที่มาในเนื้อหามากเกินไป (WP:AISIGNS), การเขียนลักษณะเรียงความ (WP:NOTESSAY)
- การแจ้งเตือนคำศัพท์ตามแนวทาง MOS:INDIGENOUS
- การจัดรูปแบบชื่อเรียกตามแนวทาง MOS:AVIATION
- ข้อความระบุยอดผู้เสียชีวิตหรือบาดเจ็บที่ไม่มีแหล่งอ้างอิงตามแนวทาง MOS:MILITARY

**โครงสร้างบทความ**
- ความยาวของส่วนนำและจำนวนย่อหน้า (MOS:LEAD)
- การเรียงลำดับหัวข้อเทียบกับ MOS:LAYOUT
- หัวข้อที่สั้นเกินไปหรือยังพัฒนาไม่สมบูรณ์
- หัวข้อที่ไม่มีแหล่งอ้างอิง (100+ คำ และไม่มี `<ref>`)
- ความเยิ่นเย้อของส่วน See also
- URL ภายนอกแบบเปล่าในเนื้อหาบทความ
- ความหนาแน่นของแม่แบบคำพูด (quote template)

**การอ้างอิงและแหล่งที่มา**
- URL เปล่าภายในแท็ก `<ref>` (ไม่ได้ใช้แม่แบบอ้างอิง cite)
- การตรวจสอบเลขตรวจสอบ (check digit) ของ ISBN
- URL ที่ผิดรูปแบบในแม่แบบการอ้างอิง
- ลิงก์ภายนอกที่เสียแล้ว (เปิดใช้งานเพิ่มเติมได้, ทำงานช้า)

**หมวดหมู่และลิงก์**
- บทความที่ยังไม่มีหมวดหมู่
- คุณภาพของหมวดหมู่ (มีหมวดหมู่น้อยเกินไป หรือกว้างเกินไป)
- การตรวจจับลิงก์แดง (ลิงก์วิกิไปยังบทความที่ยังไม่มีอยู่จริง)
- หมวดหมู่ที่เป็นลิงก์แดง
- ลิงก์ที่ชี้ไปยังหน้าแก้ความกำกวม (disambiguation)
- การใส่ลิงก์มากเกินจำเป็น (MOS:OVERLINK)

**กล่องข้อมูล (Infobox)**
- จำนวนพารามิเตอร์และความหนาแน่นของรายการ (ตรวจจับความเทอะทะ)
- พารามิเตอร์ที่มักคาดหวังแต่ขาดหายไป
- สัญญาณกล่องข้อมูลตามแนวทาง MOS:MILHIST

**อื่นๆ**
- คุณภาพของคำอธิบายสั้น (short description) เช่น ขาดหาย ยาวเกินไป หรือซ้ำกับชื่อเรื่อง
- รายการแม่แบบบำรุงรักษา (maintenance template)
- ความเรียบร้อยของลิงก์โครงการพี่น้อง (MOS:SISTER)
- การตรวจจับบทความกำพร้า (ไม่มีลิงก์วิกิจากหน้าอื่นโยงเข้ามา)
- การค้นหาลิงก์ย้อนกลับที่มีศักยภาพ
- รูปแบบหัวข้อแบบไทม์ไลน์หรือบล็อกสด (liveblog)

การตรวจสอบแต่ละอย่างจะรายงานปัญหาพร้อมระดับความรุนแรง (low/medium/high) และหักคะแนน บทความที่เรียบร้อยสมบูรณ์จะได้คะแนน 100

## การติดตั้ง

```
pip install .
```

`mwparserfromhell` เป็นแพ็กเกจที่จำเป็นต้องใช้ โดยทำหน้าที่แปลง wikitext เป็น AST เพื่อตรวจจับแม่แบบ หัวข้อ และลิงก์วิกิได้อย่างแม่นยำ หากไม่สามารถคอมไพล์ได้ (ไม่มีตัวคอมไพล์ภาษา C) เครื่องมือจะสลับไปใช้การแยกวิเคราะห์ด้วย regex โดยอัตโนมัติ

สำหรับการพัฒนา:

```
pip install -e '.[dev]'
```

## การใช้งาน

ตรวจสอบบทความ Wikipedia จริงบนเว็บ:

```
wiki-mos-audit "Gettysburg Address"
```

ตรวจสอบจาก URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

ตรวจสอบไฟล์ wikitext ในเครื่อง:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

ตรวจสอบไฟล์ wikitext เป็นชุดทั้งไดเรกทอรี:

```
wiki-mos-audit --dir ./articles/
```

ข้ามการตรวจสอบผ่าน API (โหมดออฟไลน์):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### รูปแบบผลลัพธ์

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### การตรวจสอบเพิ่มเติม (ตัวเลือก)

รายการเหล่านี้ถูกปิดไว้เป็นค่าเริ่มต้นเนื่องจากทำงานช้าหรือต้องเชื่อมต่อเครือข่าย:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### การแก้ไขอัตโนมัติ

การแก้ไขเชิงกลไกที่ปลอดภัย (ช่องว่าง, การจัดรูปแบบ) สามารถทำได้โดยอัตโนมัติ:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

ดูตัวอย่างการแก้ไขโดยไม่เขียนลงไฟล์:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### โหมดเปรียบเทียบ (Diff)

เปรียบเทียบไฟล์ wikitext ในเครื่องกับเวอร์ชันจริงบนเว็บ:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### การตั้งค่า

สร้างไฟล์ `.wiki-mos-audit.toml` เพื่อปรับค่าขีดจำกัดหรือปิดใช้งานการตรวจสอบบางรายการ:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

หรือระบุพาธของไฟล์ตั้งค่าโดยตรง:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### การรองรับหลายภาษา (Localization)

ข้อความช่วยเหลือของ CLI, ข้อความวินิจฉัย และส่วนประกอบหน้าต่างรายงานแบบข้อความ/HTML รองรับ 45 ภาษา (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) โดยไม่ต้องติดตั้งแพ็กเกจเพิ่มเติม การตรวจสอบภาษาจะเช็ก `--lang` (แยกต่างหากจาก `--language` ที่ใช้เลือกภาษาของฉบับ Wikipedia) ตามด้วย `LC_ALL`, `LC_MESSAGES` และ `LANG` และใช้ `en` เป็นค่าเริ่มต้น ส่วนคีย์ผลลัพธ์ JSON และแม่แบบ wikitext จะยังคงเดิมไม่เปลี่ยนแปลง

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

## การพัฒนา

รันการทดสอบ:

```
python -m pytest tests/ -x -q
```

ตรวจรูปแบบโค้ด (Lint):

```
ruff check src/ tests/
```

## ความต้องการของระบบ

- Python 3.12+
- mwparserfromhell

## สัญญาอนุญาต

MIT
