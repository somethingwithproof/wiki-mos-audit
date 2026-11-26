# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · **Bahasa Indonesia**

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Auditor [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) tahap awal untuk artikel Wikipedia.

## Mengapa alat ini ada

Saya menyunting Wikipedia. Tidak terus-menerus, tetapi cukup sering hingga saya mulai melihat sebuah pola: setiap kali membuka artikel untuk dirapikan, saya menjalankan daftar periksa mental yang sama. Apakah penulisan tanggalnya konsisten? Adakah kata bersayap? Apakah ada yang meninggalkan URL mentah di bagian referensi? Apakah bagian Lihat pula terlalu panjang? Apakah bagian penutup berada pada urutan yang tepat?

Setelah tiga atau keempat kalinya memindai belasan masalah yang sama secara manual berturut-turut, saya menulis sebuah skrip. Skrip itu berkembang. Kini skrip tersebut memeriksa lebih dari 30 hal yang sebelumnya saya lakukan secara manual, dan menangkap hal-hal yang mungkin terlewat pada Selasa malam yang melelahkan.

Alat ini bukan pengganti pertimbangan editorial. Ini adalah alat triase. Alat ini memberi tahu Anda di mana harus melihat, bukan apa yang harus ditulis.

## Yang diperiksa

**Gaya bahasa dan nada**
- Kata bersayap (MOS:WEASEL), istilah hiperbolis (MOS:PEACOCK)
- Ungkapan waktu relatif ("baru-baru ini", "saat ini") yang cepat kedaluwarsa
- Sinyal konten buatan AI: atribusi berlebihan dalam teks isi (WP:AISIGNS), frasa bergaya esai (WP:NOTESSAY)
- Penandaan terminologi MOS:INDIGENOUS
- Pemformatan penamaan MOS:AVIATION
- Pernyataan korban jiwa tanpa rujukan MOS:MILITARY

**Struktur**
- Panjang paragraf pembuka dan jumlah paragraf (MOS:LEAD)
- Urutan bagian terhadap MOS:LAYOUT
- Bagian yang terlalu pendek atau kurang berkembang
- Bagian tanpa rujukan (100+ kata, tanpa `<ref>`)
- Pembengkakan bagian Lihat pula
- URL eksternal mentah di isi artikel
- Kepadatan templat kutipan

**Referensi dan kutipan**
- URL mentah di dalam tag `<ref>` (tanpa templat kutipan)
- Validasi digit periksa ISBN
- URL cacat dalam templat kutipan
- Tautan eksternal mati (opsional, lambat)

**Kategori dan tautan**
- Kategori yang hilang
- Kualitas kategori (kurang terkategori, terlalu luas)
- Deteksi tautan merah (pranala wiki ke artikel yang belum ada)
- Kategori tautan merah
- Tautan ke halaman disambiguasi
- Penautan berlebihan (MOS:OVERLINK)

**Kotak info**
- Jumlah parameter dan kepadatan daftar (deteksi pembengkakan)
- Parameter yang umumnya diharapkan tetapi hilang
- Sinyal kotak info MOS:MILHIST

**Lainnya**
- Kualitas deskripsi singkat (hilang, terlalu panjang, sama dengan judul)
- Inventaris templat pemeliharaan
- Kebersihan tautan proyek saudari (MOS:SISTER)
- Deteksi artikel yatim (tanpa pranala wiki masuk)
- Penemuan potensi tautan balik
- Pola judul linimasa/blog langsung

Setiap pemeriksaan menghasilkan temuan bertingkat keparahan (rendah/sedang/tinggi) dengan pengurangan skor. Artikel yang bersih mendapat skor 100.

## Instalasi

```
pip install .
```

mwparserfromhell adalah dependensi wajib. Pustaka ini menyediakan penguraian wikitext berbasis AST untuk deteksi templat, judul bagian, dan pranala wiki secara akurat. Jika tidak dapat dikompilasi (tidak tersedia kompiler C), alat ini otomatis beralih ke penguraian berbasis regex.

Untuk pengembangan:

```
pip install -e '.[dev]'
```

## Penggunaan

Audit artikel Wikipedia langsung:

```
wiki-mos-audit "Gettysburg Address"
```

Audit dari URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Audit berkas wikitext lokal:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Audit massal direktori berkas wikitext:

```
wiki-mos-audit --dir ./articles/
```

Lewati pemeriksaan API (mode luring):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Format keluaran

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Pemeriksaan opsional

Pemeriksaan ini nonaktif secara bawaan karena lambat atau memerlukan akses jaringan:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Perbaikan otomatis

Perbaikan mekanis yang aman (spasi, pemformatan) dapat diterapkan secara otomatis:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Pratinjau tanpa menulis:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Mode diff

Bandingkan wikitext lokal dengan versi langsung:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Konfigurasi

Buat berkas `.wiki-mos-audit.toml` untuk menyesuaikan ambang batas atau menonaktifkan pemeriksaan tertentu:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Teruskan secara eksplisit:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Pelokalan

Bantuan CLI, diagnostik, dan bingkai laporan teks/HTML mendukung 45 lokal (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) tanpa dependensi tambahan. Resolusi memeriksa `--lang` (berbeda dari `--language`, yang memilih edisi Wikipedia), lalu `LC_ALL`, `LC_MESSAGES`, dan `LANG`, dengan fallback ke `en`. Kunci keluaran JSON dan templat wikitext tetap tidak berubah.

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

## Pengembangan

Jalankan pengujian:

```
python -m pytest tests/ -x -q
```

Lint:

```
ruff check src/ tests/
```

## Persyaratan

- Python 3.12+
- mwparserfromhell

## Lisensi

MIT
