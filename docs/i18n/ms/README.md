# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · **Bahasa Melayu** · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Pengaudit [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) laluan pertama untuk rencana Wikipedia.

## Mengapa ia wujud

Saya menyunting Wikipedia. Tidaklah sentiasa, tetapi cukup kerap sehingga saya mula menyedari satu corak: setiap kali saya membuka rencana untuk memperkemaskannya, saya melalui senarai semak mental yang sama. Adakah tarikhnya konsisten? Adakah terdapat kata samar? Adakah seseorang meninggalkan URL terdedah dalam rujukan? Adakah bahagian Lihat juga terlalu sarat? Adakah bahagian bawah rencana berada dalam susunan yang betul?

Selepas kali ketiga atau keempat mengimbas secara manual untuk sedozen masalah yang sama berturut-turut, saya menulis satu skrip. Skrip itu berkembang. Kini ia menyemak lebih daripada 30 perkara yang dahulunya saya lakukan secara manual, dan ia mengesan perkara yang mungkin saya terlepas pada malam Selasa yang penat.

Ini bukanlah pengganti kepada pertimbangan penyuntingan. Ia ialah alat triaj. Ia memberitahu anda di mana hendak melihat, bukan apa yang hendak ditulis.

## Apa yang disemak

**Gaya dan nada**
- Kata samar (MOS:WEASEL), istilah memuji berlebihan (MOS:PEACOCK)
- Ungkapan masa relatif ("baru-baru ini", "pada masa ini") yang cepat lapuk
- Isyarat kandungan janaan AI: atribusi berlebihan dalam teks badan (WP:AISIGNS), ungkapan seakan-akan esei (WP:NOTESSAY)
- Penanda istilah MOS:INDIGENOUS
- Pemformatan penetapan MOS:AVIATION
- Pernyataan korban tidak bersumber MOS:MILITARY

**Struktur**
- Panjang pendahuluan dan bilangan perenggan (MOS:LEAD)
- Susunan bahagian mengikut MOS:LAYOUT
- Bahagian yang pendek atau kurang berkembang
- Bahagian tanpa rujukan (100+ perkataan, tiada `<ref>`)
- Bahagian Lihat juga yang terlalu sarat
- URL luaran terdedah dalam badan rencana
- Ketumpatan templat petikan

**Rujukan dan petikan**
- URL terdedah di dalam tag `<ref>` (tiada templat petikan)
- Pengesahan digit semak ISBN
- URL cacat dalam templat petikan
- Pautan luaran mati (ikut serta, perlahan)

**Kategori dan pautan**
- Kategori yang hilang
- Kualiti kategori (kurang berkategori, terlalu luas)
- Pengesanan pautan merah (pautan wiki ke rencana yang tidak wujud)
- Kategori pautan merah
- Pautan laman nyahkekaburan
- Pemautan berlebihan (MOS:OVERLINK)

**Kotak info**
- Bilangan parameter dan ketumpatan senarai (pengesanan kesaratan)
- Parameter yang lazimnya dijangka tetapi hilang
- Isyarat kotak info MOS:MILHIST

**Lain-lain**
- Kualiti huraian ringkas (hilang, terlalu panjang, sepadan dengan tajuk)
- Inventori templat penyelenggaraan
- Kebersihan pautan projek saudara (MOS:SISTER)
- Pengesanan rencana yatim (tiada pautan wiki masuk)
- Penemuan pautan balik berpotensi
- Corak tajuk garis masa/blog langsung

Setiap semakan menghasilkan isu bertaraf keterukan (rendah/sederhana/tinggi) dengan potongan skor. Rencana yang bersih mendapat skor 100.

## Pemasangan

```
pip install .
```

mwparserfromhell ialah kebergantungan yang diperlukan. Ia menyediakan penghuraian teks wiki berasaskan AST untuk pengesanan templat, tajuk, dan pautan wiki yang tepat. Jika ia tidak dapat dikompilasi (tiada pengkompil C tersedia), alat ini akan berbalik kepada penghuraian berasaskan regex secara automatik.

Untuk pembangunan:

```
pip install -e '.[dev]'
```

## Penggunaan

Audit rencana Wikipedia secara langsung:

```
wiki-mos-audit "Gettysburg Address"
```

Audit daripada URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Audit fail teks wiki setempat:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Audit kelompok direktori fail teks wiki:

```
wiki-mos-audit --dir ./articles/
```

Langkau semakan API (mod luar talian):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Format output

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Semakan pilihan

Ini dimatikan secara lalai kerana ia perlahan atau memerlukan akses rangkaian:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Autopembaikan

Pembaikan mekanikal yang selamat (ruang putih, pemformatan) boleh digunakan secara automatik:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Pratonton tanpa menulis:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Mod diff

Bandingkan teks wiki setempat dengan versi langsung:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Konfigurasi

Cipta fail `.wiki-mos-audit.toml` untuk melaraskan ambang atau melumpuhkan semakan tertentu:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Hantarkannya secara eksplisit:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Penyetempatan

Bantuan CLI, diagnostik, dan bingkai laporan teks/HTML menyokong 45 lokal (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) tanpa kebergantungan tambahan. Penyelesaian menyemak `--lang` (berbeza daripada `--language`, yang memilih edisi Wikipedia), kemudian `LC_ALL`, `LC_MESSAGES`, dan `LANG`, berbalik kepada `en`. Kunci output JSON dan templat teks wiki kekal tidak berubah.

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

## Pembangunan

Jalankan ujian:

```
python -m pytest tests/ -x -q
```

Lint:

```
ruff check src/ tests/
```

## Keperluan

- Python 3.12+
- mwparserfromhell

## Lesen

MIT
