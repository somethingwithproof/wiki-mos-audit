# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · **Tiếng Việt** · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Công cụ kiểm tra bước đầu theo [Cẩm nang biên soạn (Manual of Style)](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) dành cho các bài viết Wikipedia.

## Lý do ra đời

Tôi có tham gia sửa đổi Wikipedia. Không phải liên tục, nhưng đủ nhiều để nhận ra một quy luật: mỗi lần mở một bài viết ra để dọn dẹp, tôi lại rà soát trong đầu cùng một danh sách kiểm tra. Định dạng ngày tháng có nhất quán không? Có từ ngữ né tránh (weasel words) nào không? Có ai để URL trần trong phần chú thích không? Mục Xem thêm (See also) có bị phình to quá mức không? Các mục cuối bài có đúng thứ tự chưa?

Sau ba bốn lần liên tiếp tự rà soát thủ công cả tá vấn đề giống hệt nhau, tôi đã viết một đoạn script. Đoạn script đó dần phát triển lên. Giờ đây nó kiểm tra hơn 30 mục mà trước đây tôi phải làm bằng tay, và phát hiện được những lỗi mà tôi rất dễ bỏ sót vào một buổi tối thứ Ba mệt mỏi.

Đây không phải là công cụ thay thế cho phán đoán biên tập. Nó là một công cụ phân loại bước đầu. Nó chỉ cho bạn biết cần nhìn vào đâu, chứ không bảo bạn phải viết gì.

## Những gì công cụ kiểm tra

**Văn phong và giọng điệu**
- Từ ngữ né tránh (MOS:WEASEL), từ ngữ tô hồng (MOS:PEACOCK)
- Các cách diễn đạt thời gian tương đối ("gần đây", "hiện tại") dễ bị lỗi thời
- Dấu hiệu nội dung do AI tạo: quy kết quá mức trong nội dung chính (WP:AISIGNS), cách hành văn giống bài tiểu luận (WP:NOTESSAY)
- Cờ cảnh báo thuật ngữ liên quan đến người bản địa theo MOS:INDIGENOUS
- Định dạng ký hiệu định danh hàng không theo MOS:AVIATION
- Các tuyên bố về thương vong chưa có nguồn dẫn theo MOS:MILITARY

**Cấu trúc**
- Độ dài và số lượng đoạn văn phần mở đầu (MOS:LEAD)
- Thứ tự các mục đối chiếu với MOS:LAYOUT
- Các mục quá ngắn hoặc chưa phát triển đầy đủ
- Các mục không có nguồn tham khảo (trên 100 từ, không có `<ref>`)
- Mục See also bị phình to quá mức
- URL liên kết ngoài dạng trần trong phần thân bài
- Mật độ bản mẫu trích dẫn (quote template)

**Tham khảo và chú thích**
- URL trần bên trong thẻ `<ref>` (không dùng bản mẫu cite)
- Kiểm tra chữ số kiểm soát của mã ISBN
- URL sai định dạng trong các bản mẫu chú thích
- Liên kết ngoài hỏng (tùy chọn bật thêm, chạy chậm)

**Thể loại và liên kết**
- Thiếu thể loại
- Chất lượng thể loại (quá ít thể loại, quá chung chung)
- Phát hiện liên kết đỏ (wikilink trỏ tới bài viết chưa tồn tại)
- Thể loại liên kết đỏ
- Liên kết tới trang định hướng (disambiguation)
- Gắn quá nhiều liên kết (MOS:OVERLINK)

**Hộp thông tin (Infobox)**
- Số lượng tham số và mật độ danh sách (phát hiện phình to)
- Thiếu các tham số thường được kỳ vọng
- Tín hiệu hộp thông tin theo MOS:MILHIST

**Khác**
- Chất lượng mô tả ngắn (short description: bị thiếu, quá dài, trùng với tiêu đề)
- Thống kê các bản mẫu bảo trì
- Vệ sinh liên kết dự án chị em (MOS:SISTER)
- Phát hiện bài mồ côi (không có wikilink trỏ tới)
- Khám phá các liên kết ngược tiềm năng
- Các mẫu tiêu đề dạng dòng thời gian/tường thuật trực tiếp

Mỗi phép kiểm tra tạo ra một vấn đề kèm mức độ nghiêm trọng (low/medium/high) và mức trừ điểm. Một bài viết sạch sẽ đạt 100 điểm.

## Cài đặt

```
pip install .
```

mwparserfromhell là một phụ thuộc bắt buộc. Nó cung cấp khả năng phân tích cú pháp wikitext dựa trên AST để phát hiện chính xác bản mẫu, tiêu đề và wikilink. Nếu không thể biên dịch được (không có sẵn trình biên dịch C), công cụ sẽ tự động chuyển sang phân tích cú pháp dựa trên regex.

Dành cho phát triển:

```
pip install -e '.[dev]'
```

## Cách sử dụng

Kiểm tra một bài viết Wikipedia trực tuyến:

```
wiki-mos-audit "Gettysburg Address"
```

Kiểm tra từ một URL:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

Kiểm tra một tệp wikitext cục bộ:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

Kiểm tra hàng loạt một thư mục chứa các tệp wikitext:

```
wiki-mos-audit --dir ./articles/
```

Bỏ qua kiểm tra qua API (chế độ ngoại tuyến):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### Định dạng đầu ra

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### Các kiểm tra tùy chọn

Các kiểm tra này mặc định được tắt vì chúng chạy chậm hoặc cần truy cập mạng:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### Tự động sửa lỗi

Các sửa lỗi cơ học an toàn (khoảng trắng, định dạng) có thể được áp dụng tự động:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

Xem trước mà không ghi vào tệp:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### Chế độ so sánh (Diff)

So sánh wikitext cục bộ với phiên bản trực tuyến:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### Cấu hình

Tạo tệp `.wiki-mos-audit.toml` để điều chỉnh ngưỡng hoặc tắt các kiểm tra cụ thể:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

Truyền tệp cấu hình một cách tường minh:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### Bản địa hóa

Trợ giúp CLI, các chẩn đoán và giao diện báo cáo dạng văn bản/HTML hỗ trợ 45 ngôn ngữ/vùng (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) mà không cần thêm phụ thuộc. Thứ tự phân giải kiểm tra `--lang` (khác với `--language`, cờ dùng để chọn phiên bản ngôn ngữ Wikipedia), sau đó đến `LC_ALL`, `LC_MESSAGES` và `LANG`, rồi dự phòng về `en`. Các khóa JSON đầu ra và các bản mẫu wikitext vẫn giữ nguyên.

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

## Phát triển

Chạy kiểm thử:

```
python -m pytest tests/ -x -q
```

Kiểm tra mã nguồn (Lint):

```
ruff check src/ tests/
```

## Yêu cầu

- Python 3.12+
- mwparserfromhell

## Giấy phép

MIT
