# wiki-mos-audit

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_wiki-mos-audit&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_wiki-mos-audit)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/wiki-mos-audit/main/pyproject.toml)](../../../pyproject.toml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/wiki-mos-audit/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/wiki-mos-audit)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · **বাংলা** · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Wikipedia নিবন্ধের জন্য একটি প্রাথমিক পর্যায়ের [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) নিরীক্ষক (auditor)।

## এটি কেন তৈরি করা হয়েছে

আমি Wikipedia সম্পাদনা করি। নিয়মিত নয়, তবে যথেষ্ট পরিমাণে যে আমি একটি ধারা লক্ষ্য করতে শুরু করি: প্রতিবার যখনই আমি কোনো নিবন্ধ পরিচ্ছন্ন করতে খুলতাম, আমি একই মানসিক চেকলিস্ট অনুসরণ করতাম। তারিখগুলো কি সামঞ্জস্যপূর্ণ? কোনো অস্পষ্ট বা ফাঁপা শব্দ (weasel words) আছে কি? কেউ কি রেফারেন্সে সরাসরি URL রেখে দিয়েছে? "আরও দেখুন" (See also) অনুচ্ছেদটি কি অতিরিক্ত বড় হয়ে গেছে? নিচের দিকের অনুচ্ছেদগুলো কি সঠিক ক্রমে সাজানো আছে?

পরপর তিন বা চারবার হাতে-কলমে একই এক ডজন সমস্যা খুঁজে দেখার পর, আমি একটি স্ক্রিপ্ট লিখলাম। সেই স্ক্রিপ্টটি বড় হলো। এখন এটি ৩০টিরও বেশি বিষয় পরীক্ষা করে যা আমি আগে হাতে করতাম, এবং ক্লান্ত মঙ্গলবার সন্ধ্যায় আমি যা এড়িয়ে যেতাম তা এটি ধরে ফেলে।

এটি সম্পাদকীয় বিচারবুদ্ধির বিকল্প নয়। এটি একটি বাছাইকরণ (triage) টুল। এটি আপনাকে বলে কোথায় দেখতে হবে, কী লিখতে হবে তা নয়।

## এটি কী কী পরীক্ষা করে

**শৈলী এবং সুর**
- অস্পষ্ট বা ফাঁপা শব্দ (MOS:WEASEL), অতিরঞ্জিত শব্দ (MOS:PEACOCK)
- আপেক্ষিক সময়সূচক অভিব্যক্তি ("সম্প্রতি", "বর্তমানে") যা সময়ের সাথে পুরনো হয়ে যায়
- AI-সৃষ্ট বিষয়বস্তুর সংকেত: মূল লেখায় অতিরিক্ত অ্যাট্রিবিউশন (WP:AISIGNS), প্রবন্ধসুলভ বাক্যভঙ্গি (WP:NOTESSAY)
- MOS:INDIGENOUS পরিভাষা সংক্রান্ত সতর্কতা
- MOS:AVIATION পদবি/চিহ্নিতকরণ ফরম্যাটিং
- MOS:MILITARY তথ্যসূত্রহীন হতাহতের বিবৃতি

**গঠন**
- সূচনা অংশের দৈর্ঘ্য এবং অনুচ্ছেদ সংখ্যা (MOS:LEAD)
- MOS:LAYOUT অনুযায়ী অনুচ্ছেদের ক্রম
- সংক্ষিপ্ত বা অসম্পূর্ণ অনুচ্ছেদ
- তথ্যসূত্রহীন অনুচ্ছেদ (১০০+ শব্দ, কোনো `<ref>` নেই)
- "আরও দেখুন" (See also) অনুচ্ছেদের স্ফীতি
- নিবন্ধের মূল অংশে সরাসরি বহিরাগত URL
- উদ্ধৃতি টেমপ্লেটের ঘনত্ব

**তথ্যসূত্র এবং উদ্ধৃতি**
- `<ref>` ট্যাগের ভেতরে সরাসরি URL (কোনো উদ্ধৃতি টেমপ্লেট ছাড়া)
- ISBN চেক ডিজিট যাচাইকরণ
- উদ্ধৃতি টেমপ্লেটে ত্রুটিপূর্ণ URL
- অকার্যকর বহিরাগত লিংক (ঐচ্ছিক, ধীরগতির)

**বিষয়শ্রেণী এবং লিংক**
- অনুপস্থিত বিষয়শ্রেণী
- বিষয়শ্রেণীর মান (অপর্যাপ্ত বিষয়শ্রেণী, অতিরিক্ত বিস্তৃত)
- লাল-লিংক শনাক্তকরণ (অস্তিত্বহীন নিবন্ধে উইকিলিংক)
- লাল-লিংক বিষয়শ্রেণী
- দ্ব্যর্থতা নিরসন পৃষ্ঠার লিংক
- অতিরিক্ত লিংকিং (MOS:OVERLINK)

**তথ্যছক (Infobox)**
- প্যারামিটার সংখ্যা এবং তালিকার ঘনত্ব (স্ফীতি শনাক্তকরণ)
- সাধারণত প্রত্যাশিত প্যারামিটারের অনুপস্থিতি
- MOS:MILHIST তথ্যছকের সংকেত

**অন্যান্য**
- সংক্ষিপ্ত বিবরণের মান (অনুপস্থিত, অতিরিক্ত দীর্ঘ, শিরোনামের সাথে মিলে যাওয়া)
- রক্ষণাবেক্ষণ টেমপ্লেটের তালিকা
- সহপ্রকল্পের লিংক পরিচ্ছন্নতা (MOS:SISTER)
- অনাথ নিবন্ধ শনাক্তকরণ (কোনো আগত উইকিলিংক নেই)
- সম্ভাব্য ব্যাকলিংক অনুসন্ধান
- সময়রেখা/লাইভব্লগ শিরোনামের ধরন

প্রতিটি পরীক্ষা গুরুত্বের স্তরসহ (low/medium/high) একটি সমস্যা চিহ্নিত করে এবং স্কোর কর্তন করে। একটি পরিচ্ছন্ন নিবন্ধের স্কোর হয় ১০০।

## ইনস্টলেশন

```
pip install .
```

mwparserfromhell একটি প্রয়োজনীয় ডিপেন্ডেন্সি। এটি নির্ভুল টেমপ্লেট, শিরোনাম এবং উইকিলিংক শনাক্তকরণের জন্য AST-ভিত্তিক উইকিটেক্সট পার্সিং সরবরাহ করে। যদি এটি কম্পাইল করা না যায় (কোনো C কম্পাইলার উপলব্ধ না থাকলে), টুলটি স্বয়ংক্রিয়ভাবে regex-ভিত্তিক পার্সিংয়ে ফিরে যায়।

উন্নয়নের জন্য:

```
pip install -e '.[dev]'
```

## ব্যবহার

একটি লাইভ Wikipedia নিবন্ধ নিরীক্ষা করুন:

```
wiki-mos-audit "Gettysburg Address"
```

একটি URL থেকে নিরীক্ষা করুন:

```
wiki-mos-audit "https://en.wikipedia.org/wiki/Gettysburg_Address"
```

একটি স্থানীয় উইকিটেক্সট ফাইল নিরীক্ষা করুন:

```
wiki-mos-audit --wikitext-file article_corrected.txt
```

উইকিটেক্সট ফাইলের একটি ডিরেক্টরি ব্যাচ নিরীক্ষা করুন:

```
wiki-mos-audit --dir ./articles/
```

API পরীক্ষাগুলো এড়িয়ে যান (অফলাইন মোড):

```
wiki-mos-audit --wikitext-file article.txt --offline
```

### আউটপুট ফরম্যাটসমূহ

```
wiki-mos-audit "Article" --format text   # default
wiki-mos-audit "Article" --format json
wiki-mos-audit "Article" --json          # shorthand
wiki-mos-audit "Article" --format html
```

### ঐচ্ছিক পরীক্ষাসমূহ

এগুলো ডিফল্টভাবে বন্ধ থাকে কারণ এগুলো ধীরগতির বা এগুলোর জন্য নেটওয়ার্ক অ্যাক্সেস প্রয়োজন:

```
wiki-mos-audit "Article" --check-urls       # HEAD-check all cited URLs
wiki-mos-audit "Article" --check-orphan     # check for incoming wikilinks
wiki-mos-audit "Article" --check-backlinks  # find articles that mention but don't link here
```

### স্বয়ংক্রিয় সংশোধন (Auto-fix)

নিরাপদ যান্ত্রিক সংশোধনগুলো (হোয়াইটস্পেস, ফরম্যাটিং) স্বয়ংক্রিয়ভাবে প্রয়োগ করা যায়:

```
wiki-mos-audit --wikitext-file article.txt --fix --output-wikitext-file article_fixed.txt
```

না লিখেই প্রাকদর্শন করুন:

```
wiki-mos-audit --wikitext-file article.txt --fix --dry-run
```

### ডিফ (Diff) মোড

লাইভ সংস্করণের সাথে স্থানীয় উইকিটেক্সটের তুলনা করুন:

```
wiki-mos-audit --wikitext-file article_corrected.txt --diff
```

### কনফিগারেশন

থ্রেশহোল্ড সমন্বয় করতে বা নির্দিষ্ট পরীক্ষাগুলো নিষ্ক্রিয় করতে একটি `.wiki-mos-audit.toml` ফাইল তৈরি করুন:

```toml
min_severity = "low"
disabled_checks = ["mos-aviation-style"]
max_lead_words = 300
short_section_words = 40
overlink_threshold = 4
```

এটি সুস্পষ্টভাবে পাস করুন:

```
wiki-mos-audit "Article" --config .wiki-mos-audit.toml
```

### লোকালাইজেশন

CLI সাহায্য, ডায়াগনস্টিকস এবং টেক্সট/HTML রিপোর্ট ক্রোম কোনো অতিরিক্ত ডিপেন্ডেন্সি ছাড়াই ৪৫টি লোকেল (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) সমর্থন করে। লোকেল নির্ধারণে প্রথমে `--lang` (`--language` থেকে আলাদা, যা Wikipedia সংস্করণ নির্বাচন করে), তারপর `LC_ALL`, `LC_MESSAGES` এবং `LANG` পরীক্ষা করা হয়, এবং না পাওয়া গেলে `en`-এ ফিরে যায়। JSON আউটপুট কী এবং উইকিটেক্সট টেমপ্লেট অপরিবর্তিত থাকে।

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

## উন্নয়ন

টেস্ট চালান:

```
python -m pytest tests/ -x -q
```

লিন্ট করুন:

```
ruff check src/ tests/
```

## প্রয়োজনীয়তা

- Python 3.12+
- mwparserfromhell

## লাইসেন্স

MIT
