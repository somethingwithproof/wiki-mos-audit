"""Unit tests for wiki_mos_audit.fixer."""
from __future__ import annotations

from wiki_mos_audit.fixer import (
    FixResult,
    fix_all,
    fix_bare_ref_urls,
    fix_heading_caps,
    fix_http_to_https,
    fix_whitespace,
)

# ---------------------------------------------------------------------------
# fix_bare_ref_urls
# ---------------------------------------------------------------------------

class TestFixBareRefUrls:
    def test_wraps_bare_http_url(self) -> None:
        text = '<ref>http://example.com/page</ref>'
        result, count = fix_bare_ref_urls(text)
        assert count == 1
        assert '{{cite web |url=http://example.com/page |title= |access-date=}}' in result
        assert result.startswith('<ref>')
        assert result.endswith('</ref>')

    def test_wraps_bare_https_url(self) -> None:
        text = '<ref>https://example.com/page</ref>'
        result, count = fix_bare_ref_urls(text)
        assert count == 1
        assert '{{cite web |url=https://example.com/page |title= |access-date=}}' in result

    def test_cite_template_unchanged(self) -> None:
        text = '<ref>{{cite web |url=https://example.com |title=Example}}</ref>'
        result, count = fix_bare_ref_urls(text)
        assert count == 0
        assert result == text

    def test_multiple_bare_refs(self) -> None:
        text = (
            '<ref>http://one.com</ref> text '
            '<ref>https://two.com/path</ref>'
        )
        result, count = fix_bare_ref_urls(text)
        assert count == 2
        assert '|url=http://one.com' in result
        assert '|url=https://two.com/path' in result

    def test_no_refs_at_all(self) -> None:
        text = 'Plain paragraph with no references.'
        result, count = fix_bare_ref_urls(text)
        assert count == 0
        assert result == text

    def test_named_ref_tag(self) -> None:
        text = '<ref name="foo">http://example.com</ref>'
        result, count = fix_bare_ref_urls(text)
        assert count == 1
        assert result.startswith('<ref name="foo">')
        assert '{{cite web |url=http://example.com' in result

    def test_case_insensitive_ref_tag(self) -> None:
        text = '<REF>http://example.com</REF>'
        result, count = fix_bare_ref_urls(text)
        assert count == 1
        assert '{{cite web' in result


# ---------------------------------------------------------------------------
# fix_whitespace
# ---------------------------------------------------------------------------

class TestFixWhitespace:
    def test_trailing_spaces_removed(self) -> None:
        text = 'hello   \nworld  '
        result, count = fix_whitespace(text)
        assert result == 'hello\nworld'
        assert count == 2

    def test_multiple_blank_lines_collapsed(self) -> None:
        text = 'a\n\n\n\nb'
        result, count = fix_whitespace(text)
        assert result == 'a\n\nb'
        assert count == 1

    def test_both_trailing_and_blank_lines(self) -> None:
        text = 'a  \n\n\n\nb  '
        result, count = fix_whitespace(text)
        assert result == 'a\n\nb'
        # trailing on 'a  ' and 'b  ' = 2, plus blank-line collapse = 1 => 3
        assert count == 3

    def test_already_clean(self) -> None:
        text = 'clean\ntext\n\nhere'
        result, count = fix_whitespace(text)
        assert count == 0
        assert result == text

    def test_single_trailing_space(self) -> None:
        text = 'line '
        result, count = fix_whitespace(text)
        assert result == 'line'
        assert count == 1

    def test_tabs_count_as_trailing(self) -> None:
        text = 'line\t'
        result, count = fix_whitespace(text)
        assert result == 'line'
        assert count == 1


# ---------------------------------------------------------------------------
# fix_heading_caps
# ---------------------------------------------------------------------------

class TestFixHeadingCaps:
    def test_title_case_converted(self) -> None:
        text = '== Early Life And Career =='
        result, count = fix_heading_caps(text)
        assert count == 1
        assert 'Early life and career' in result

    def test_sentence_case_unchanged(self) -> None:
        text = '== Early life and career =='
        result, count = fix_heading_caps(text)
        assert count == 0
        assert result == text

    def test_single_word_heading_skipped(self) -> None:
        text = '== History =='
        result, count = fix_heading_caps(text)
        assert count == 0
        assert result == text

    def test_heading_with_wikilinks_skipped(self) -> None:
        text = '== See [[Also]] Here =='
        result, count = fix_heading_caps(text)
        assert count == 0
        assert result == text

    def test_heading_with_templates_skipped(self) -> None:
        text = '== {{Some Template}} Section =='
        result, count = fix_heading_caps(text)
        assert count == 0
        assert result == text

    def test_level_three_heading(self) -> None:
        text = '=== Personal Life And Family ==='
        result, count = fix_heading_caps(text)
        assert count == 1
        assert 'Personal life and family' in result

    def test_multiple_headings(self) -> None:
        text = '== Early Life ==\ntext\n== Later Career =='
        result, count = fix_heading_caps(text)
        assert count == 2

    def test_abbreviations_preserved(self) -> None:
        # Words that are all-caps (abbreviations) should stay
        text = '== Work At NASA And IBM =='
        result, count = fix_heading_caps(text)
        assert count == 1
        assert 'NASA' in result
        assert 'IBM' in result

    def test_short_words_preserved(self) -> None:
        # Words <= 2 chars are kept as-is
        text = '== Life In The US =='
        result, count = fix_heading_caps(text)
        assert 'US' in result

    def test_not_title_case_below_threshold(self) -> None:
        # If fewer than 70% of words are capitalized, skip
        text = '== Some mostly lowercase heading here =='
        result, count = fix_heading_caps(text)
        assert count == 0
        assert result == text


# ---------------------------------------------------------------------------
# fix_http_to_https
# ---------------------------------------------------------------------------

class TestFixHttpToHttps:
    def test_url_param_upgraded(self) -> None:
        text = '{{cite web |url=http://example.com |title=Test}}'
        result, count = fix_http_to_https(text)
        assert count == 1
        assert '|url=https://example.com' in result

    def test_archive_url_upgraded(self) -> None:
        text = '{{cite web |archive-url=http://web.archive.org/page |title=T}}'
        result, count = fix_http_to_https(text)
        assert count == 1
        assert '|archive-url=https://web.archive.org/page' in result

    def test_chapter_url_upgraded(self) -> None:
        text = '{{cite book |chapter-url=http://example.com/ch1 |title=Book}}'
        result, count = fix_http_to_https(text)
        assert count == 1
        assert '|chapter-url=https://example.com/ch1' in result

    def test_https_unchanged(self) -> None:
        text = '{{cite web |url=https://example.com |title=Test}}'
        result, count = fix_http_to_https(text)
        assert count == 0
        assert result == text

    def test_body_text_http_unchanged(self) -> None:
        text = 'Visit http://example.com for details.'
        result, count = fix_http_to_https(text)
        assert count == 0
        assert result == text

    def test_multiple_citations(self) -> None:
        text = (
            '{{cite web |url=http://a.com}}\n'
            '{{cite web |url=http://b.com}}'
        )
        result, count = fix_http_to_https(text)
        assert count == 2
        assert 'http://' not in result

    def test_case_insensitive_param(self) -> None:
        text = '{{cite web |URL=http://example.com |title=T}}'
        result, count = fix_http_to_https(text)
        assert count == 1
        assert 'https://example.com' in result

    def test_spaces_around_equals(self) -> None:
        text = '{{cite web | url = http://example.com |title=T}}'
        result, count = fix_http_to_https(text)
        assert count == 1
        assert 'https://example.com' in result


# ---------------------------------------------------------------------------
# fix_all
# ---------------------------------------------------------------------------

class TestFixAll:
    def test_chains_all_fixes(self) -> None:
        text = (
            '<ref>http://example.com</ref>\n'
            '== Early Life And Career ==\n'
            'Some text  \n\n\n\n'
            '{{cite web |url=http://other.com |title=T}}'
        )
        result = fix_all(text)
        assert isinstance(result, FixResult)
        assert len(result.fixes_applied) == 4
        # bare ref wrapped
        assert any('bare ref' in f.lower() for f in result.fixes_applied)
        # whitespace fixed
        assert any('whitespace' in f.lower() for f in result.fixes_applied)
        # heading caps fixed
        assert any('heading' in f.lower() for f in result.fixes_applied)
        # http upgraded
        assert any('http' in f.lower() for f in result.fixes_applied)

    def test_clean_text_no_fixes(self) -> None:
        text = '== History ==\n\nClean paragraph here.\n\nAnother paragraph.'
        result = fix_all(text)
        assert isinstance(result, FixResult)
        assert result.fixes_applied == []
        assert result.wikitext == text

    def test_returns_fix_result(self) -> None:
        result = fix_all('hello')
        assert isinstance(result, FixResult)
        assert isinstance(result.wikitext, str)
        assert isinstance(result.fixes_applied, list)

    def test_partial_fixes(self) -> None:
        # Only whitespace issue, nothing else
        text = 'clean text  '
        result = fix_all(text)
        assert len(result.fixes_applied) == 1
        assert 'whitespace' in result.fixes_applied[0].lower()
        assert result.wikitext == 'clean text'

    def test_fix_counts_in_messages(self) -> None:
        text = (
            '<ref>http://a.com</ref>\n'
            '<ref>http://b.com</ref>'
        )
        result = fix_all(text)
        assert any('2 bare ref' in f.lower() for f in result.fixes_applied)
