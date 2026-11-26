# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · **Türkçe** · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Wikipedia maddeleri için ilk aşama bir [Biçem El Kitabı (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) denetleyicisi.

## Neden var

Wikipedia üzerinde düzenleme yapıyorum. Sürekli değil, ancak bir örüntü fark etmeye yetecek kadar sık: temizlik için her maddeyi açtığımda zihnimden aynı kontrol listesini geçiriyordum. Tarihler tutarlı mı? Kaçamak ifadeler (weasel words) var mı? Birileri kaynaklarda çıplak URL bırakmış mı? "Ayrıca bakınız" bölümü şişmiş mi? Alt kısım bölümleri doğru sırada mı?

Art arda aynı düzine sorunu elle taramaktan üçüncü ya da dördüncü kez yorulunca bir betik yazdım. O betik zamanla büyüdü. Şimdi elle kontrol ettiğim 30'dan fazla şeyi denetliyor ve yorgun bir salı akşamında gözümden kaçacak ayrıntıları yakalıyor.

Bu araç editoryal yargının yerini almaz. Bir ön eleme (triyaj) aracıdır. Ne yazacağınızı değil, nereye bakmanız gerektiğini söyler.

## Neleri denetler

**Üslup ve ton**
- Kaçamak ifadeler (MOS:WEASEL), abartılı övgü terimleri (MOS:PEACOCK)
- Zamanla güncelliğini yitiren göreli zaman ifadeleri ("yakın zamanda", "şu anda")
- Yapay zeka üretimi içerik sinyalleri: gövde metninde aşırı atıf (WP:AISIGNS), deneme benzeri ifadeler (WP:NOTESSAY)
- MOS:INDIGENOUS terminoloji uyarıları
- MOS:AVIATION adlandırma biçimlendirmesi
- MOS:MILITARY kaynaksız kayıp ifadeleri

**Yapı**
- Giriş bölümü uzunluğu ve paragraf sayısı (MOS:LEAD)
- MOS:LAYOUT kuralına göre bölüm sıralaması
- Kısa veya yeterince geliştirilmemiş bölümler
- Kaynaksız bölümler (100+ sözcük, `<ref>` yok)
- "Ayrıca bakınız" bölümü şişkinliği
- Madde gövdesinde çıplak harici URL'ler
- Alıntı şablonu yoğunluğu

**Kaynaklar ve atıflar**
- `<ref>` etiketleri içindeki çıplak URL'ler (kaynak şablonu olmadan)
- ISBN doğrulama basamağı denetimi
- Kaynak şablonlarında bozuk URL'ler
- Kırık harici bağlantılar (isteğe bağlı, yavaştır)

**Kategoriler ve bağlantılar**
- Eksik kategoriler
- Kategori kalitesi (yetersiz kategorize edilmiş, aşırı genel)
- Kırmızı bağlantı algılama (var olmayan maddelere vikibağlantılar)
- Kırmızı bağlantılı kategoriler
- Anlam ayrımı sayfası bağlantıları
- Aşırı bağlantı verme (MOS:OVERLINK)

**Bilgi kutusu (Infobox)**
- Parametre sayısı ve liste yoğunluğu (şişkinlik algılama)
- Yaygın olarak beklenen eksik parametreler
- MOS:MILHIST bilgi kutusu sinyalleri

**Diğer**
- Kısa açıklama kalitesi (eksik, çok uzun, başlıkla eşleşiyor)
- Bakım şablonu envanteri
- Kardeş proje bağlantısı hijyeni (MOS:SISTER)
- Öksüz sayfa algılama (gelen vikibağlantı yok)
- Olası geri bağlantı keşfi
- Zaman çizelgesi/canlı blog başlık örüntüleri

Her denetim, puan kesintisiyle birlikte önem derecesi atanmış (düşük/orta/yüksek) bir sorun üretir. Temiz bir madde 100 puan alır.

## Kurulum

```
pip install .
```

mwparserfromhell zorunlu bir bağımlılıktır. Doğru şablon, başlık ve vikibağlantı algılaması için AST tabanlı wikitext ayrıştırması sağlar. Derlenemezse (C derleyicisi yoksa), araç otomatik olarak düzenli ifade (regex) tabanlı ayrıştırmaya geri döner.

Geliştirme için:

```
pip install -e '.[dev]'
```

## Kullanım

Canlı bir Wikipedia maddesini denetleyin:

```
wiki-mos-audit "Gettysburg Address"
```

Bir URL'den denetleyin:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Yerel bir wikitext dosyasını denetleyin:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Bir wikitext dosyaları dizinini toplu olarak denetleyin:

```
wiki-mos-audit --dir ./articles/
```

API denetimlerini atlayın (çevrimdışı kip):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Çıktı biçimleri

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### İsteğe bağlı denetimler

Bunlar yavaş oldukları veya ağ erişimi gerektirdikleri için varsayılan olarak kapalıdır:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Otomatik düzeltme

Güvenli mekanik düzeltmeler (boşluklar, biçimlendirme) otomatik olarak uygulanabilir:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Yazmadan önizleyin:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Fark (Diff) kipi

Yerel wikitext'i canlı sürümle karşılaştırın:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Yapılandırma

Eşikleri ayarlamak veya belirli denetimleri devre dışı bırakmak için bir `.wiki-mos-audit.toml` dosyası oluşturun:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Açıkça belirtin:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Yerelleştirme

CLI yardımı, tanılamalar ve metin/HTML rapor çerçevesi sıfır ek bağımlılıkla 45 yerel ayarı (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) destekler. Çözümleme önce `--lang` seçeneğini (Wikipedia sürümünü seçen `--language` seçeneğinden ayrıdır), ardından `LC_ALL`, `LC_MESSAGES` ve `LANG` değişkenlerini denetler; hiçbiri yoksa `en` değerine geri döner. JSON çıktı anahtarları ve wikitext şablonları değişmeden kalır.

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

## Geliştirme

Testleri çalıştırın:

```
python -m pytest tests/ -x -q
```

Lint:

```
ruff check src/ tests/
```

## Gereksinimler

- Python 3.12+
- mwparserfromhell

## Lisans

MIT
