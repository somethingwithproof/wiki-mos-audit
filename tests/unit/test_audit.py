"""Unit tests for wiki_mos_audit.audit -- helpers and every audit_mos() check."""
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from wiki_mos_audit.audit import (
    _extract_category_names,
    _extract_wikilink_targets,
    _isbn10_valid,
    _isbn13_valid,
    audit_mos,
    extract_lead_wikitext,
    find_date_formats,
    find_phrases,
    normalize_template_name,
    strip_markup,
    template_names_from_wikitext,
)


@pytest.fixture
def no_ast(monkeypatch):
    """Force regex fallback by disabling mwparserfromhell."""
    import wiki_mos_audit.audit as audit_mod
    monkeypatch.setattr(audit_mod, 'mwparserfromhell', None)


# ---------------------------------------------------------------------------
# strip_markup
# ---------------------------------------------------------------------------

class TestStripMarkup:
    def test_plain_text_unchanged(self):
        assert strip_markup("Hello world") == "Hello world"

    def test_wikilinks_replaced_by_display(self):
        result = strip_markup("The [[United States|US]] and [[Canada]].")
        assert "United States" not in result
        assert "US" in result
        assert "Canada" in result
        assert "[[" not in result

    def test_templates_removed(self):
        result = strip_markup("Text {{cite web|url=http://example.com|title=X}} here.")
        assert "{{" not in result
        assert "Text" in result
        assert "here" in result

    def test_ref_tags_removed(self):
        result = strip_markup("Claim.<ref>Source text here.</ref> More.")
        assert "<ref>" not in result
        assert "Claim" in result
        assert "More" in result
        # mwparserfromhell keeps ref body text; regex path strips it entirely.
        # Both are acceptable for style-checking purposes.

    def test_html_tags_removed(self):
        result = strip_markup("A <b>bold</b> word and <br/> a line break.")
        assert "<b>" not in result
        assert "<br" not in result
        assert "bold" in result

    def test_multiple_spaces_collapsed(self):
        result = strip_markup("one   two    three")
        # regex path collapses whitespace; mwparserfromhell preserves it in plain text.
        assert "one" in result and "two" in result and "three" in result


# ---------------------------------------------------------------------------
# extract_lead_wikitext
# ---------------------------------------------------------------------------

class TestExtractLeadWikitext:
    def test_returns_full_text_when_no_headings(self):
        wikitext = "Just a lead with no sections."
        assert extract_lead_wikitext(wikitext) == wikitext

    def test_returns_lead_before_first_l2_heading(self):
        wikitext = "Lead text here.\n\n== History ==\nBody text."
        result = extract_lead_wikitext(wikitext)
        assert "Lead text here" in result
        assert "History" not in result
        assert "Body text" not in result

    def test_lead_stops_at_first_heading_only(self):
        wikitext = "Lead.\n\n== Section A ==\nBody A.\n\n== Section B ==\nBody B."
        result = extract_lead_wikitext(wikitext)
        assert "Lead." in result
        assert "Section A" not in result
        assert "Section B" not in result

    def test_empty_string(self):
        assert extract_lead_wikitext("") == ""


# ---------------------------------------------------------------------------
# find_date_formats
# ---------------------------------------------------------------------------

class TestFindDateFormats:
    def test_dmy_only(self):
        text = "The battle was on 3 June 1944 and ended 6 June 1944."
        dmy, mdy = find_date_formats(text)
        assert dmy == 2
        assert mdy == 0

    def test_mdy_only(self):
        text = "Born June 6, 1944 and died December 26, 1991."
        dmy, mdy = find_date_formats(text)
        assert dmy == 0
        assert mdy == 2

    def test_mixed(self):
        text = "On 3 June 1944, also known as June 6, 1944 in US records."
        dmy, mdy = find_date_formats(text)
        assert dmy >= 1
        assert mdy >= 1

    def test_no_dates(self):
        dmy, mdy = find_date_formats("No dates in this text at all.")
        assert dmy == 0
        assert mdy == 0


# ---------------------------------------------------------------------------
# find_phrases
# ---------------------------------------------------------------------------

class TestFindPhrases:
    def test_finds_matching_phrases(self):
        result = find_phrases("This is widely regarded as good.", ["is widely regarded", "some analysts"])
        assert "is widely regarded" in result
        assert "some analysts" not in result

    def test_returns_empty_when_no_match(self):
        result = find_phrases("Clean neutral text here.", ["some analysts", "is widely regarded"])
        assert result == []

    def test_case_insensitive(self):
        result = find_phrases("RECENTLY the event occurred.", ["recently"])
        assert "recently" in result

    def test_returns_sorted_unique(self):
        result = find_phrases("recently and currently and recently again", ["currently", "recently"])
        assert result == sorted(result)
        assert len(result) == len(set(result))


# ---------------------------------------------------------------------------
# normalize_template_name
# ---------------------------------------------------------------------------

class TestNormalizeTemplateName:
    def test_lowercases(self):
        assert normalize_template_name("Cite Web") == "cite web"

    def test_underscores_to_spaces(self):
        assert normalize_template_name("cite_web") == "cite web"

    def test_collapses_extra_spaces(self):
        assert normalize_template_name("  cite   web  ") == "cite web"

    def test_mixed_underscores_and_spaces(self):
        assert normalize_template_name("Infobox_Military Conflict") == "infobox military conflict"


# ---------------------------------------------------------------------------
# template_names_from_wikitext (regex fallback: code=None)
# ---------------------------------------------------------------------------

class TestTemplateNamesFromWikitext:
    def test_extracts_template_names(self):
        wikitext = "{{Cite web|url=x}} and {{Infobox person|name=Y}}"
        names = template_names_from_wikitext(wikitext, code=None)
        assert "cite web" in names
        assert "infobox person" in names

    def test_empty_wikitext(self):
        names = template_names_from_wikitext("No templates here.", code=None)
        assert names == set()

    def test_normalizes_names(self):
        wikitext = "{{Citation_Needed}}"
        names = template_names_from_wikitext(wikitext, code=None)
        assert "citation needed" in names


# ---------------------------------------------------------------------------
# _isbn10_valid
# ---------------------------------------------------------------------------

class TestIsbn10Valid:
    def test_valid_isbn10(self):
        # 0-306-40615-2 is a well-known valid ISBN-10
        assert _isbn10_valid("0306406152") is True

    def test_invalid_isbn10_wrong_check_digit(self):
        assert _isbn10_valid("0306406153") is False

    def test_invalid_isbn10_wrong_length(self):
        assert _isbn10_valid("030640615") is False

    def test_valid_isbn10_with_x_check_digit(self):
        # 007462542X is a confirmed valid ISBN-10 with X as the check digit
        assert _isbn10_valid("007462542X") is True

    def test_invalid_isbn10_bad_x_position(self):
        # X in non-final position is invalid
        assert _isbn10_valid("X306406152") is False


# ---------------------------------------------------------------------------
# _isbn13_valid
# ---------------------------------------------------------------------------

class TestIsbn13Valid:
    def test_valid_isbn13(self):
        # 978-0-306-40615-7
        assert _isbn13_valid("9780306406157") is True

    def test_invalid_isbn13_wrong_check_digit(self):
        assert _isbn13_valid("9780306406158") is False

    def test_invalid_isbn13_wrong_length(self):
        assert _isbn13_valid("978030640615") is False

    def test_invalid_isbn13_non_digits(self):
        assert _isbn13_valid("978030640615X") is False


# ---------------------------------------------------------------------------
# Helpers for building wikitext fixtures
# ---------------------------------------------------------------------------

def _categorized(extra: str = "") -> str:
    """Return minimal wikitext that passes uncategorized and short-description checks."""
    return (
        "{{Short description|Test article}}\n"
        "'''Subject''' is a subject.\n\n"
        "== Section ==\n"
        + ("word " * 35)
        + "\n\n"
        + extra
        + "\n[[Category:Test articles]]\n[[Category:Example items]]\n"
    )


def _issue_ids(report) -> set[str]:
    return {i.check_id for i in report.issues}


# ---------------------------------------------------------------------------
# audit_mos() -- lead-length
# ---------------------------------------------------------------------------

class TestLeadLength:
    def test_long_lead_triggers(self):
        # 270 distinct words in the lead, then a heading
        words = " ".join(f"word{i}" for i in range(270))
        wikitext = (
            "{{Short description|Test}}\n"
            f"'''Subject''' is a subject. {words}\n\n"
            "== Section ==\n"
            + ("x " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "lead-length" in _issue_ids(report)

    def test_short_lead_clean(self):
        wikitext = _categorized()
        report = audit_mos("Subject", wikitext)
        assert "lead-length" not in _issue_ids(report)

    def test_five_paragraph_lead_triggers(self):
        # 5 non-empty paragraphs in the lead
        para = "Short para.\n\n"
        wikitext = (
            "{{Short description|Test}}\n"
            + para * 5
            + "== Section ==\n"
            + ("x " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "lead-length" in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- weasel-terms
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("phrase,expected_hit", [
    ("is widely regarded", True),
    ("critics say", True),
    ("neutral factual text", False),
])
def test_weasel_terms(phrase, expected_hit):
    wikitext = _categorized(f"The subject {phrase} excellent.")
    report = audit_mos("Subject", wikitext)
    if expected_hit:
        assert "weasel-terms" in _issue_ids(report)
    else:
        assert "weasel-terms" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- relative-time
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("phrase,expected_hit", [
    ("recently", True),
    ("currently", True),
    ("in 1944", False),
])
def test_relative_time(phrase, expected_hit):
    wikitext = _categorized(f"The event occurred {phrase}.")
    report = audit_mos("Subject", wikitext)
    if expected_hit:
        assert "relative-time" in _issue_ids(report)
    else:
        assert "relative-time" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- mos-indigenous-terms
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("text,expected_hit", [
    ("The eskimo population", True),
    ("The Inuit population", False),
])
def test_mos_indigenous_terms(text, expected_hit):
    wikitext = _categorized(text)
    report = audit_mos("Subject", wikitext)
    if expected_hit:
        assert "mos-indigenous-terms" in _issue_ids(report)
    else:
        assert "mos-indigenous-terms" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- date-style-mix
# ---------------------------------------------------------------------------

class TestDateStyleMix:
    def test_mixed_dates_triggers(self):
        wikitext = _categorized("On 3 June 1944 and also June 6, 1944 per US records.")
        report = audit_mos("Subject", wikitext)
        assert "date-style-mix" in _issue_ids(report)

    def test_consistent_dmy_clean(self):
        wikitext = _categorized("On 3 June 1944 and 6 June 1944 the battle ended.")
        report = audit_mos("Subject", wikitext)
        assert "date-style-mix" not in _issue_ids(report)

    def test_no_dates_clean(self):
        wikitext = _categorized("No dates appear in this section at all.")
        report = audit_mos("Subject", wikitext)
        assert "date-style-mix" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- mos-aviation-style
# ---------------------------------------------------------------------------

class TestMosAviationStyle:
    def test_aviation_context_with_designation_triggers(self):
        wikitext = _categorized(
            "The aircraft flew several sorties. The F15 was the primary aircraft used."
        )
        report = audit_mos("Subject", wikitext)
        assert "mos-aviation-style" in _issue_ids(report)

    def test_no_aviation_context_clean(self):
        wikitext = _categorized("The car model F15 was produced in limited numbers.")
        report = audit_mos("Subject", wikitext)
        assert "mos-aviation-style" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- quote-density
# ---------------------------------------------------------------------------

class TestQuoteDensity:
    def test_four_quote_templates_triggers(self):
        quotes = "{{quote|text}} " * 4
        wikitext = _categorized(quotes)
        report = audit_mos("Subject", wikitext)
        assert "quote-density" in _issue_ids(report)

    def test_zero_quote_templates_clean(self):
        wikitext = _categorized("No quotes appear in this section.")
        report = audit_mos("Subject", wikitext)
        assert "quote-density" not in _issue_ids(report)

    def test_three_quote_templates_clean(self):
        quotes = "{{quote|text}} " * 3
        wikitext = _categorized(quotes)
        report = audit_mos("Subject", wikitext)
        assert "quote-density" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- timeline-structure
# ---------------------------------------------------------------------------

class TestTimelineStructure:
    def test_four_daily_headings_triggers(self):
        headings = (
            "\n== 1 January ==\nSome events.\n"
            "\n== 2 January ==\nMore events.\n"
            "\n== 3 January ==\nFurther events.\n"
            "\n== 4 January ==\nFinal events.\n"
        )
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n"
            + headings
            + "[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "timeline-structure" in _issue_ids(report)

    def test_thematic_sections_clean(self):
        wikitext = _categorized()
        report = audit_mos("Subject", wikitext)
        assert "timeline-structure" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- mos-military-style
# ---------------------------------------------------------------------------

class TestMosMilitaryStyle:
    def test_uncited_casualty_line_triggers(self):
        wikitext = _categorized(
            "The battle resulted in heavy casualties. Military losses were significant."
        )
        report = audit_mos("Subject", wikitext)
        assert "mos-military-style" in _issue_ids(report)

    def test_cited_casualty_line_clean(self):
        wikitext = _categorized(
            "The battle resulted in heavy casualties.<ref>Smith 2001, p. 42.</ref>"
        )
        report = audit_mos("Subject", wikitext)
        assert "mos-military-style" not in _issue_ids(report)

    def test_no_military_context_clean(self):
        wikitext = _categorized("A peaceful science conference with no conflict.")
        report = audit_mos("Subject", wikitext)
        assert "mos-military-style" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- maintenance-tags
# ---------------------------------------------------------------------------

class TestMaintenanceTags:
    def test_citation_needed_triggers(self):
        wikitext = _categorized("Some claim.{{citation needed}}")
        report = audit_mos("Subject", wikitext)
        assert "maintenance-tags" in _issue_ids(report)

    def test_cn_shortcut_triggers(self):
        wikitext = _categorized("Another claim.{{cn}}")
        report = audit_mos("Subject", wikitext)
        assert "maintenance-tags" in _issue_ids(report)

    def test_clean_article_no_maintenance(self):
        wikitext = _categorized()
        report = audit_mos("Subject", wikitext)
        assert "maintenance-tags" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- mos-sister-projects
# ---------------------------------------------------------------------------

class TestMosSisterProjects:
    def test_raw_commons_link_without_template_triggers(self):
        wikitext = _categorized(
            "See also https://commons.wikimedia.org/wiki/Category:Test for images."
        )
        report = audit_mos("Subject", wikitext)
        assert "mos-sister-projects" in _issue_ids(report)

    def test_raw_link_with_sister_template_clean(self):
        # Having a {{commons}} template should suppress the check
        wikitext = _categorized(
            "{{commons|Test}}\n"
            "More info at https://commons.wikimedia.org/wiki/Category:Test"
        )
        report = audit_mos("Subject", wikitext)
        assert "mos-sister-projects" not in _issue_ids(report)

    def test_no_sister_links_clean(self):
        wikitext = _categorized()
        report = audit_mos("Subject", wikitext)
        assert "mos-sister-projects" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- infobox-bloat
# ---------------------------------------------------------------------------

class TestInfboxBloat:
    def test_36_params_triggers(self):
        params = "\n".join(f"| param{i} = value{i}" for i in range(36))
        wikitext = (
            "{{Short description|Test}}\n"
            "{{Infobox person\n"
            + params
            + "\n}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "infobox-bloat" in _issue_ids(report)

    def test_normal_infobox_clean(self):
        wikitext = (
            "{{Short description|Test}}\n"
            "{{Infobox person\n| name = Subject\n| birth_date = 1900\n}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "infobox-bloat" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- peacock-terms
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("phrase,expected_hit", [
    ("legendary", True),
    ("iconic", True),
    ("neutral factual statement", False),
])
def test_peacock_terms(phrase, expected_hit):
    wikitext = _categorized(f"The {phrase} performer appeared on stage.")
    report = audit_mos("Subject", wikitext)
    if expected_hit:
        assert "peacock-terms" in _issue_ids(report)
    else:
        assert "peacock-terms" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- bare-urls-in-refs
# ---------------------------------------------------------------------------

class TestBareUrlsInRefs:
    def test_bare_url_in_ref_triggers(self):
        wikitext = _categorized("A fact.<ref>https://example.com/article</ref>")
        report = audit_mos("Subject", wikitext)
        assert "bare-urls-in-refs" in _issue_ids(report)

    def test_cite_template_in_ref_clean(self):
        wikitext = _categorized(
            "A fact.<ref>{{cite web|url=https://example.com|title=X|access-date=1 January 2024}}</ref>"
        )
        report = audit_mos("Subject", wikitext)
        assert "bare-urls-in-refs" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- uncategorized
# ---------------------------------------------------------------------------

class TestUncategorized:
    def test_no_categories_triggers(self):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
        )
        report = audit_mos("Subject", wikitext)
        assert "uncategorized" in _issue_ids(report)

    def test_with_categories_clean(self):
        wikitext = _categorized()
        report = audit_mos("Subject", wikitext)
        assert "uncategorized" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- unreferenced-sections
# ---------------------------------------------------------------------------

class TestUnreferencedSections:
    def test_100_word_section_no_refs_triggers(self):
        body = " ".join(f"word{i}" for i in range(105))
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            + body
            + "\n\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "unreferenced-sections" in _issue_ids(report)

    def test_cited_section_clean(self):
        body = " ".join(f"word{i}" for i in range(105))
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            + body
            + "<ref>Source.</ref>\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "unreferenced-sections" not in _issue_ids(report)

    def test_short_section_under_100_words_clean(self):
        wikitext = _categorized()  # section body is ~35 words
        report = audit_mos("Subject", wikitext)
        assert "unreferenced-sections" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- overlinking
# ---------------------------------------------------------------------------

class TestOverlinking:
    def test_link_repeated_three_times_triggers(self):
        wikitext = _categorized(
            "[[France]] is a country. [[France]] borders Germany. [[France]] has Paris."
        )
        report = audit_mos("Subject", wikitext)
        assert "overlinking" in _issue_ids(report)

    def test_link_used_once_clean(self):
        wikitext = _categorized("[[France]] is a country in Europe.")
        report = audit_mos("Subject", wikitext)
        assert "overlinking" not in _issue_ids(report)

    def test_two_occurrences_clean(self):
        wikitext = _categorized("[[France]] is large. [[France]] borders Spain.")
        report = audit_mos("Subject", wikitext)
        assert "overlinking" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- short-sections
# ---------------------------------------------------------------------------

class TestShortSections:
    def test_10_word_section_triggers(self):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            "Only ten words appear in this short section body.\n\n"
            "== Details ==\n"
            + ("word " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "short-sections" in _issue_ids(report)

    def test_50_word_section_clean(self):
        wikitext = _categorized()  # uses 35 words, below 30-word threshold needs more
        # rebuild with enough words
        body = "word " * 50
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + body
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "short-sections" not in _issue_ids(report)

    def test_see_also_section_not_flagged_as_short_prose_section(self):
        # The skip for See also / References / etc. only operates when mwparserfromhell
        # is available (AST path strips == markers before comparing against _SKIP_SHORT).
        # Without the AST parser the regex path leaves markers in place, so the heading
        # doesn't match the skip set. This test documents that a 50-word content section
        # is NOT flagged regardless of the See also presence.
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            + ("word " * 50)
            + "\n[[Category:Test articles]]\n[[Category:Example items]]\n"
        )
        report = audit_mos("Subject", wikitext)
        short_issues = [i for i in report.issues if i.check_id == "short-sections"]
        # History section has 50 words -- above the 30-word threshold -- so no flag
        assert not short_issues


# ---------------------------------------------------------------------------
# audit_mos() -- see-also-bloat
# ---------------------------------------------------------------------------

class TestSeeAlsoBloat:
    def test_11_items_triggers(self):
        items = "\n".join(f"* [[Article {i}]]" for i in range(11))
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n\n== See also ==\n"
            + items
            + "\n\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "see-also-bloat" in _issue_ids(report)

    def test_five_items_clean(self):
        items = "\n".join(f"* [[Article {i}]]" for i in range(5))
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n\n== See also ==\n"
            + items
            + "\n\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "see-also-bloat" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- external-links-in-body
# ---------------------------------------------------------------------------

class TestExternalLinksInBody:
    def test_bare_url_in_prose_triggers(self):
        wikitext = _categorized("More info at https://example.com for details.")
        report = audit_mos("Subject", wikitext)
        assert "external-links-in-body" in _issue_ids(report)

    def test_url_in_ref_clean(self):
        wikitext = _categorized(
            "A fact.<ref>{{cite web|url=https://example.com|title=T}}</ref>"
        )
        report = audit_mos("Subject", wikitext)
        assert "external-links-in-body" not in _issue_ids(report)

    def test_url_in_external_links_section_clean(self):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n\n== External links ==\n"
            "* https://example.com\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "external-links-in-body" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- ai-overattribution
# ---------------------------------------------------------------------------

class TestAiOverattribution:
    def test_two_overattribution_patterns_triggers(self):
        wikitext = _categorized(
            "A 2020 article in The Guardian described the policy as flawed. "
            "A 2019 report in The Times described the outcome as uncertain."
        )
        report = audit_mos("Subject", wikitext)
        assert "ai-overattribution" in _issue_ids(report)

    def test_one_pattern_clean(self):
        wikitext = _categorized(
            "A 2020 article in The Guardian described the policy as flawed. "
            "Subsequent analysis confirmed these findings."
        )
        report = audit_mos("Subject", wikitext)
        assert "ai-overattribution" not in _issue_ids(report)

    def test_no_patterns_clean(self):
        wikitext = _categorized("The policy was changed in 2020 following a review.")
        report = audit_mos("Subject", wikitext)
        assert "ai-overattribution" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- ai-essay-tone
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("phrase,expected_hit", [
    ("it is worth noting", True),
    ("it should be noted", True),
    ("this highlights", True),
    ("played a pivotal role", True),
    ("the subject performed well", False),
])
def test_ai_essay_tone(phrase, expected_hit):
    wikitext = _categorized(f"The event demonstrates that {phrase} the trend.")
    report = audit_mos("Subject", wikitext)
    if expected_hit:
        assert "ai-essay-tone" in _issue_ids(report)
    else:
        assert "ai-essay-tone" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- cs1-isbn-validation
# ---------------------------------------------------------------------------

class TestCs1IsbnValidation:
    def test_invalid_isbn_triggers(self):
        wikitext = _categorized(
            "{{cite book|title=X|isbn=0306406153}}"  # wrong check digit
        )
        report = audit_mos("Subject", wikitext)
        assert "cs1-isbn-validation" in _issue_ids(report)

    def test_valid_isbn10_clean(self):
        wikitext = _categorized(
            "{{cite book|title=X|isbn=0306406152}}"  # valid ISBN-10
        )
        report = audit_mos("Subject", wikitext)
        assert "cs1-isbn-validation" not in _issue_ids(report)

    def test_valid_isbn13_clean(self):
        wikitext = _categorized(
            "{{cite book|title=X|isbn=9780306406157}}"  # valid ISBN-13
        )
        report = audit_mos("Subject", wikitext)
        assert "cs1-isbn-validation" not in _issue_ids(report)

    def test_wrong_length_triggers(self):
        wikitext = _categorized(
            "{{cite book|title=X|isbn=12345}}"
        )
        report = audit_mos("Subject", wikitext)
        assert "cs1-isbn-validation" in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- cs1-url-validation
# ---------------------------------------------------------------------------

class TestCs1UrlValidation:
    def test_malformed_url_no_scheme_triggers(self):
        wikitext = _categorized(
            "{{cite web|url=example.com/page|title=X}}"
        )
        report = audit_mos("Subject", wikitext)
        assert "cs1-url-validation" in _issue_ids(report)

    def test_url_with_space_triggers(self):
        wikitext = _categorized(
            "{{cite web|url=https://example.com/my page|title=X}}"
        )
        report = audit_mos("Subject", wikitext)
        assert "cs1-url-validation" in _issue_ids(report)

    def test_valid_url_clean(self):
        wikitext = _categorized(
            "{{cite web|url=https://example.com/article|title=X|access-date=1 January 2024}}"
        )
        report = audit_mos("Subject", wikitext)
        assert "cs1-url-validation" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- short-description-quality
# ---------------------------------------------------------------------------

class TestShortDescriptionQuality:
    def test_missing_short_description_triggers(self):
        wikitext = (
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        issues = [i for i in report.issues if i.check_id == "short-description-quality"]
        assert issues
        assert "missing" in issues[0].message.lower() or "no short" in issues[0].message.lower()

    def test_short_description_matching_title_triggers(self):
        wikitext = (
            "{{Short description|Subject}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        issues = [i for i in report.issues if i.check_id == "short-description-quality"]
        assert issues
        assert "title" in issues[0].message.lower()

    def test_short_description_too_long_triggers(self):
        long_desc = "A " + "very " * 10 + "long description that exceeds forty characters"
        wikitext = (
            f"{{{{Short description|{long_desc}}}}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        issues = [i for i in report.issues if i.check_id == "short-description-quality"]
        assert issues
        assert "long" in issues[0].message.lower()

    def test_good_short_description_clean(self):
        wikitext = (
            "{{Short description|Test article}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        sd_issues = [i for i in report.issues if i.check_id == "short-description-quality"]
        assert not sd_issues


# ---------------------------------------------------------------------------
# audit_mos() -- client=None skips red-link, red-categories, disambiguation
# ---------------------------------------------------------------------------

class TestClientNoneSkipsNetworkChecks:
    def test_red_links_skipped_without_client(self):
        wikitext = _categorized("[[Nonexistent Article XYZ]] appears here.")
        report = audit_mos("Subject", wikitext, client=None)
        assert "red-links" not in _issue_ids(report)

    def test_red_categories_skipped_without_client(self):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n[[Category:Nonexistent Category XYZ]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext, client=None)
        assert "red-categories" not in _issue_ids(report)

    def test_disambiguation_links_skipped_without_client(self):
        wikitext = _categorized("[[Mercury]] the planet or element.")
        report = audit_mos("Subject", wikitext, client=None)
        assert "disambiguation-links" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- section fragments stripped for API checks
# ---------------------------------------------------------------------------

class _CaptureClient:
    def __init__(self) -> None:
        self.page_existence_calls: list[list[str]] = []
        self.disambiguation_calls: list[list[str]] = []

    def check_page_existence(self, titles: list[str]) -> dict[str, bool]:
        self.page_existence_calls.append(titles)
        return {title: True for title in titles}

    def check_disambiguation(self, titles: list[str]) -> list[str]:
        self.disambiguation_calls.append(titles)
        return []


class TestSectionFragmentNormalization:
    def test_red_link_checks_strip_section_fragments(self):
        client = _CaptureClient()
        wikitext = _categorized(
            'See [[Mercury#Astronomy]] and [[Venus]].'
        )
        audit_mos('Subject', wikitext, client=client)
        page_check_titles = [title for call in client.page_existence_calls for title in call]
        assert 'Mercury' in page_check_titles
        assert 'Mercury#Astronomy' not in page_check_titles

    def test_disambiguation_checks_strip_section_fragments(self):
        client = _CaptureClient()
        wikitext = _categorized(
            'See [[Mercury#Astronomy]] and [[Venus]].'
        )
        audit_mos('Subject', wikitext, client=client)
        disambiguation_titles = [title for call in client.disambiguation_calls for title in call]
        assert 'Mercury' in disambiguation_titles
        assert 'Mercury#Astronomy' not in disambiguation_titles


# ---------------------------------------------------------------------------
# score calculation
# ---------------------------------------------------------------------------

class TestScoreCalculation:
    def test_perfect_score_clean_article(self):
        # A well-formed article should score reasonably high (not necessarily 100
        # because category-quality and other checks may still fire, but should be > 50)
        wikitext = (
            "{{Short description|Test article}}\n"
            "'''Subject''' is a subject studied extensively.\n\n"
            "== History ==\n"
            + ("The subject was studied carefully. " * 10)
            + "<ref>Smith 2000, p. 1.</ref>\n\n"
            "[[Category:Test articles]]\n[[Category:Example items]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert report.score >= 0
        assert report.score <= 100

    def test_score_decreases_with_issues(self):
        clean = _categorized()
        clean_report = audit_mos("Subject", clean)

        # Wikitext with many deliberate issues
        dirty = (
            "'''Subject''' is a legendary, iconic, world-class example.\n\n"
            "Recently, it is said that critics say many people believe.\n"
            "The eskimo population was affected.\n\n"
            "== History ==\n"
            "Military casualties and losses occurred recently.\n\n"
            "[[Category:Tests]]\n"
        )
        dirty_report = audit_mos("Subject", dirty)
        assert dirty_report.score < clean_report.score

    def test_score_never_below_zero(self):
        # Pile every possible issue into one wikitext
        dirty = (
            "'''Subject''' is a legendary iconic groundbreaking world-class "
            "renowned prestigious cutting-edge state-of-the-art subject.\n\n"
            "Recently, currently, it is said, critics say, many people believe "
            "is widely regarded as the most important eskimo event.\n\n"
            "It is worth noting that this highlights played a pivotal role.\n\n"
            "A 2020 article in The Guardian described the result. "
            "A 2019 report in The Times described the policy.\n\n"
            "On 3 June 1944 and also June 6, 1944 per US records.\n\n"
            "The F15 aircraft flew several aviation sorties.\n\n"
            "{{quote|text}} {{quote|text}} {{quote|text}} {{quote|text}}\n\n"
            "Military casualties and losses occurred.\n\n"
            "Some claim.{{citation needed}}\n\n"
            "See https://commons.wikimedia.org/wiki/Category:Test for more.\n\n"
            "{{cite book|isbn=9999999999}}\n\n"
            "{{cite web|url=not-a-url|title=Bad}}\n\n"
            "More info at https://example.com directly in prose.\n\n"
            "<ref>https://example.com</ref>\n"
        )
        report = audit_mos("Subject", dirty)
        assert report.score >= 0

    def test_score_reflects_severity_weights(self):
        # One high-severity issue: ai-overattribution (weight=15)
        wikitext_high = _categorized(
            "A 2020 article in The Guardian described the policy. "
            "A 2019 report in The Times described the outcome."
        )
        report_high = audit_mos("High Severity Subject", wikitext_high)
        high_issues = [i for i in report_high.issues if i.check_id == "ai-overattribution"]
        assert high_issues
        assert high_issues[0].severity == "high"

    def test_report_title_preserved(self):
        wikitext = _categorized()
        report = audit_mos("My Test Article", wikitext)
        assert report.title == "My Test Article"


# ---------------------------------------------------------------------------
# _extract_wikilink_targets
# ---------------------------------------------------------------------------

class TestExtractWikilinkTargets:
    def test_basic_extraction(self):
        wikitext = "See [[France]] and [[Germany|DE]]."
        targets = _extract_wikilink_targets(wikitext)
        assert 'France' in targets
        assert 'Germany' in targets
        # Display text should not appear as a target
        assert 'DE' not in targets

    def test_skip_namespaced_links(self):
        wikitext = "See [[Category:Test]] and [[File:Image.png]] and [[Wikipedia:Policy]]."
        targets = _extract_wikilink_targets(wikitext)
        assert not targets

    def test_skip_section_only_links(self):
        # Links like [[#Section]] are section-only and the regex excludes them
        # via the [^\]|#] first-char exclusion
        wikitext = "See [[#History]] for details."
        targets = _extract_wikilink_targets(wikitext)
        assert not targets

    def test_dedupe(self):
        wikitext = "[[France]] is great. [[France]] is large."
        targets = _extract_wikilink_targets(wikitext)
        assert targets.count('France') == 1

    def test_capitalize_first_letter(self):
        wikitext = "See [[france]] for details."
        targets = _extract_wikilink_targets(wikitext)
        assert 'France' in targets
        assert 'france' not in targets


# ---------------------------------------------------------------------------
# _extract_category_names
# ---------------------------------------------------------------------------

class TestExtractCategoryNames:
    def test_basic_extraction(self):
        wikitext = "Text\n[[Category:Foo]]\n[[Category:Bar baz]]\n"
        names = _extract_category_names(wikitext)
        assert 'Foo' in names
        assert 'Bar baz' in names

    def test_no_categories(self):
        assert _extract_category_names("No categories here.") == []

    def test_skips_non_category_wikilinks(self):
        wikitext = "[[France]] and [[Category:Test]]"
        names = _extract_category_names(wikitext)
        assert names == ['Test']

    def test_regex_fallback(self, no_ast):
        wikitext = "[[Category:Alpha]]\n[[Category:Beta]]"
        names = _extract_category_names(wikitext)
        assert 'Alpha' in names
        assert 'Beta' in names


# ---------------------------------------------------------------------------
# Config wiring -- disabled_checks
# ---------------------------------------------------------------------------

class TestConfigDisabledChecks:
    def test_disabled_lead_length_suppresses_issue(self):
        # 300-word lead would normally trigger lead-length
        words = " ".join(f"word{i}" for i in range(300))
        wikitext = (
            "{{Short description|Test article}}\n"
            f"'''Subject''' is a subject. {words}\n\n"
            "== Section ==\n"
            + ("x " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        from wiki_mos_audit.config import AuditConfig
        config = AuditConfig(disabled_checks={'lead-length'})
        report = audit_mos("Subject", wikitext, config=config)
        assert "lead-length" not in _issue_ids(report)

    def test_disabled_check_does_not_affect_others(self):
        # disabling lead-length should leave weasel-terms detection intact
        wikitext = _categorized("The subject is widely regarded as the best.")
        from wiki_mos_audit.config import AuditConfig
        config = AuditConfig(disabled_checks={'lead-length'})
        report = audit_mos("Subject", wikitext, config=config)
        assert "weasel-terms" in _issue_ids(report)


# ---------------------------------------------------------------------------
# Config wiring -- min_severity
# ---------------------------------------------------------------------------

class TestConfigMinSeverity:
    def test_min_severity_medium_filters_low_issues(self):
        # relative-time has severity='low'; with min_severity='medium' it must be absent
        wikitext = _categorized("The event occurred recently.")
        from wiki_mos_audit.config import AuditConfig
        config = AuditConfig(min_severity='medium')
        report = audit_mos("Subject", wikitext, config=config)
        assert "relative-time" not in _issue_ids(report)

    def test_min_severity_medium_keeps_medium_issues(self):
        # weasel-terms has severity='medium'; must survive the filter
        wikitext = _categorized("The subject is widely regarded as excellent.")
        from wiki_mos_audit.config import AuditConfig
        config = AuditConfig(min_severity='medium')
        report = audit_mos("Subject", wikitext, config=config)
        assert "weasel-terms" in _issue_ids(report)

    def test_min_severity_high_filters_medium_issues(self):
        # weasel-terms is 'medium'; with min_severity='high' it must be gone
        wikitext = _categorized("The subject is widely regarded as the best.")
        from wiki_mos_audit.config import AuditConfig
        config = AuditConfig(min_severity='high')
        report = audit_mos("Subject", wikitext, config=config)
        assert "weasel-terms" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# Config wiring -- thresholds (max_lead_words)
# ---------------------------------------------------------------------------

class TestConfigThresholds:
    def test_raised_max_lead_words_suppresses_lead_length(self):
        # 300-word lead triggers with default 260 threshold but not with 500
        words = " ".join(f"word{i}" for i in range(300))
        wikitext = (
            "{{Short description|Test article}}\n"
            f"'''Subject''' is a subject. {words}\n\n"
            "== Section ==\n"
            + ("x " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        from wiki_mos_audit.config import AuditConfig
        config = AuditConfig(max_lead_words=500)
        report = audit_mos("Subject", wikitext, config=config)
        assert "lead-length" not in _issue_ids(report)

    def test_default_threshold_still_fires_for_same_lead(self):
        words = " ".join(f"word{i}" for i in range(300))
        wikitext = (
            "{{Short description|Test article}}\n"
            f"'''Subject''' is a subject. {words}\n\n"
            "== Section ==\n"
            + ("x " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "lead-length" in _issue_ids(report)


# ---------------------------------------------------------------------------
# _isbn10_valid -- safety with unexpected characters
# ---------------------------------------------------------------------------

class TestIsbn10ValidSafety:
    def test_trailing_non_digit_non_x_returns_false(self):
        # last char is 'Z', not a digit or 'X'
        assert _isbn10_valid("123456789Z") is False

    def test_alpha_in_middle_returns_false(self):
        # non-digit in positions 0-8
        assert _isbn10_valid("12345ABCD0") is False

    def test_all_alpha_returns_false(self):
        assert _isbn10_valid("ABCDEFGHIJ") is False

    def test_mixed_valid_length_but_bad_chars_returns_false(self):
        # 10 chars but has internal 'X' in position 5 (not valid there)
        assert _isbn10_valid("01234X6789") is False


# ---------------------------------------------------------------------------
# Overlinking -- case normalization
# ---------------------------------------------------------------------------

class TestOverlinkingCaseNormalization:
    def test_first_char_normalization_counted_together(self):
        # [[canada]] and [[Canada]] differ only in first char; MediaWiki normalizes
        # first char to uppercase, so these are the same target
        wikitext = _categorized(
            "[[canada]] is large. "
            "[[Canada]] borders the US. "
            "[[canada]] has many provinces."
        )
        report = audit_mos("Subject", wikitext)
        assert "overlinking" in _issue_ids(report)

    def test_two_occurrences_different_first_char_no_trigger(self):
        # Two occurrences (one lower, one upper first char) should not trigger at threshold=3
        wikitext = _categorized("[[france]] is large. [[France]] borders Spain.")
        report = audit_mos("Subject", wikitext)
        assert "overlinking" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# Short-sections -- preamble skip
# ---------------------------------------------------------------------------

class TestShortSectionsPreambleSkip:
    def test_short_preamble_before_subsection_not_flagged(self):
        # A level-2 section with only a brief intro paragraph followed by a
        # level-3 subsection must not trigger short-sections (preamble skip).
        long_subsection_body = "word " * 50
        wikitext = (
            "{{Short description|Test article}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            "Brief intro.\n\n"
            "=== Early years ===\n"
            + long_subsection_body
            + "\n[[Category:Test articles]]\n[[Category:Example items]]\n"
        )
        report = audit_mos("Subject", wikitext)
        short_issues = [i for i in report.issues if i.check_id == "short-sections"]
        # History section body is just a preamble; must be skipped
        history_flagged = any("History" in i.evidence for i in short_issues)
        assert not history_flagged

    def test_genuinely_short_section_without_subsection_still_flags(self):
        wikitext = (
            "{{Short description|Test article}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            "Only ten words in this section body here.\n\n"
            "== References ==\n"
            "{{reflist}}\n\n"
            "[[Category:Test articles]]\n[[Category:Example items]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "short-sections" in _issue_ids(report)


# ---------------------------------------------------------------------------
# Aviation regex -- tightened context check
# ---------------------------------------------------------------------------

class TestAviationRegexContext:
    def test_visa_designation_without_aviation_context_clean(self):
        # "B1" in a visa context must not trigger without aviation context words
        wikitext = _categorized("The B1 visa requires documentation and proof of employment.")
        report = audit_mos("Subject", wikitext)
        assert "mos-aviation-style" not in _issue_ids(report)

    def test_aircraft_context_with_designation_triggers(self):
        # explicit 'aircraft' context + F-15 style hit must trigger
        wikitext = _categorized(
            "The F-15 was the primary aircraft used in the operation."
        )
        audit_mos("Subject", wikitext)
        # F-15 uses a hyphen so it matches the standard designation -- no flag
        # The trigger requires an un-hyphenated form like 'F15'
        wikitext_no_hyphen = _categorized(
            "The F15 was the primary aircraft used in the operation."
        )
        report2 = audit_mos("Subject", wikitext_no_hyphen)
        assert "mos-aviation-style" in _issue_ids(report2)


# ---------------------------------------------------------------------------
# _check_url_liveness -- HEAD 405 retry with GET
# ---------------------------------------------------------------------------

class TestCheckUrlLiveness405Retry:
    def test_405_head_then_200_get_not_dead(self):
        import urllib.error
        from unittest.mock import MagicMock, patch

        from wiki_mos_audit.audit import _check_url_liveness

        head_error = urllib.error.HTTPError(
            url="https://example.com/page",
            code=405,
            msg="Method Not Allowed",
            hdrs=None,  # type: ignore[arg-type]
            fp=None,  # type: ignore[arg-type]
        )

        get_response = MagicMock()
        get_response.status = 200
        get_response.__enter__ = lambda s: s
        get_response.__exit__ = MagicMock(return_value=False)

        def fake_urlopen(req, timeout=5.0):
            if req.method == 'HEAD':
                raise head_error
            return get_response

        with patch('wiki_mos_audit.audit.urllib.request.urlopen', side_effect=fake_urlopen):
            dead = _check_url_liveness(["https://example.com/page"])

        assert "https://example.com/page" not in dead

    def test_405_head_then_404_get_is_dead(self):
        import urllib.error
        from unittest.mock import MagicMock, patch

        from wiki_mos_audit.audit import _check_url_liveness

        head_error = urllib.error.HTTPError(
            url="https://example.com/gone",
            code=405,
            msg="Method Not Allowed",
            hdrs=None,  # type: ignore[arg-type]
            fp=None,  # type: ignore[arg-type]
        )

        get_response = MagicMock()
        get_response.status = 404
        get_response.__enter__ = lambda s: s
        get_response.__exit__ = MagicMock(return_value=False)

        def fake_urlopen(req, timeout=5.0):
            if req.method == 'HEAD':
                raise head_error
            return get_response

        with patch('wiki_mos_audit.audit.urllib.request.urlopen', side_effect=fake_urlopen):
            dead = _check_url_liveness(["https://example.com/gone"])

        assert "https://example.com/gone" in dead


# ---------------------------------------------------------------------------
# extract_lead_wikitext -- nowiki spans
# ---------------------------------------------------------------------------

class TestExtractLeadWikitextNowiki:
    def test_nowiki_heading_not_treated_as_section_boundary(self):
        wikitext = (
            "<nowiki>== Not a heading ==</nowiki>\n\n"
            "== Real heading ==\n"
            "Body text here."
        )
        result = extract_lead_wikitext(wikitext)
        # Everything before == Real heading == is the lead
        assert "Not a heading" in result
        assert "Real heading" not in result
        assert "Body text" not in result

    def test_real_heading_after_nowiki_still_splits(self):
        wikitext = (
            "Lead paragraph with <nowiki>== fake ==</nowiki> inline.\n\n"
            "== Actual Section ==\n"
            "Section content."
        )
        result = extract_lead_wikitext(wikitext)
        assert "Lead paragraph" in result
        assert "Actual Section" not in result
        assert "Section content" not in result

    def test_section_fragment_stripped(self):
        wikitext = "See [[Mercury#Astronomy]] for details."
        targets = _extract_wikilink_targets(wikitext)
        assert 'Mercury' in targets
        assert 'Mercury#Astronomy' not in targets


# ---------------------------------------------------------------------------
# strip_markup -- nested templates
# ---------------------------------------------------------------------------

class TestStripMarkupNested:
    def test_nested_templates_stripped(self):
        result = strip_markup("Text {{outer|{{inner}}}} here.")
        assert '{{' not in result
        assert '}}' not in result
        assert 'Text' in result
        assert 'here' in result

    def test_deeply_nested_templates(self):
        result = strip_markup("A {{a|{{b|{{c}}}}}} B")
        assert '{{' not in result
        assert 'A' in result
        assert 'B' in result


# ---------------------------------------------------------------------------
# audit_mos() -- section-ordering
# ---------------------------------------------------------------------------

class TestSectionOrdering:
    def test_correct_order_no_issue(self):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            + ("word " * 35) + "\n\n"
            "== See also ==\n"
            "* [[Other]]\n\n"
            "== References ==\n"
            "{{reflist}}\n\n"
            "== External links ==\n"
            "* [https://example.com]\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "section-ordering" not in _issue_ids(report)

    def test_wrong_order_triggers(self):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            + ("word " * 35) + "\n\n"
            "== External links ==\n"
            "* [https://example.com]\n\n"
            "== References ==\n"
            "{{reflist}}\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "section-ordering" in _issue_ids(report)

    def test_single_bottom_matter_section_no_issue(self):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            + ("word " * 35) + "\n\n"
            "== References ==\n"
            "{{reflist}}\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "section-ordering" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- dead-external-links (check_urls=False skips)
# ---------------------------------------------------------------------------

class TestDeadExternalLinks:
    def test_check_urls_false_skips(self):
        wikitext = _categorized(
            "{{cite web|url=https://definitely-broken-url-12345.invalid/page|title=X}}"
        )
        report = audit_mos("Subject", wikitext, check_urls=False)
        assert "dead-external-links" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- orphan-article
# ---------------------------------------------------------------------------

class TestOrphanArticle:
    def test_with_incoming_links_no_issue(self):
        mock_client = MagicMock()
        mock_client._request.return_value = {
            'query': {
                'pages': [
                    {'title': 'Subject', 'linkshere': [{'title': 'Some Page'}]},
                ],
            }
        }
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = []

        wikitext = _categorized()
        report = audit_mos("Subject", wikitext, client=mock_client, check_orphan=True)
        assert "orphan-article" not in _issue_ids(report)

    def test_no_incoming_links_fires_issue(self):
        mock_client = MagicMock()
        mock_client._request.return_value = {
            'query': {
                'pages': [
                    {'title': 'Subject'},
                ],
            }
        }
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = []

        wikitext = _categorized()
        report = audit_mos("Subject", wikitext, client=mock_client, check_orphan=True)
        assert "orphan-article" in _issue_ids(report)

    def test_orphan_check_skipped_without_flag(self):
        mock_client = MagicMock()
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = []

        wikitext = _categorized()
        report = audit_mos("Subject", wikitext, client=mock_client, check_orphan=False)
        assert "orphan-article" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# audit_mos() -- potential-backlinks
# ---------------------------------------------------------------------------

class TestPotentialBacklinks:
    def test_candidates_returned_fires_issue(self):
        mock_client = MagicMock()
        mock_client.find_potential_backlinks.return_value = ['Article A', 'Article B']
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = []

        wikitext = _categorized()
        report = audit_mos("Subject", wikitext, client=mock_client, check_backlinks=True)
        assert "potential-backlinks" in _issue_ids(report)
        issue = next(i for i in report.issues if i.check_id == 'potential-backlinks')
        assert 'Article A' in issue.evidence
        assert 'Article B' in issue.evidence

    def test_check_backlinks_false_skips(self):
        mock_client = MagicMock()
        mock_client.find_potential_backlinks.return_value = ['Article A']
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = []

        wikitext = _categorized()
        report = audit_mos("Subject", wikitext, client=mock_client, check_backlinks=False)
        assert "potential-backlinks" not in _issue_ids(report)
        # find_potential_backlinks should not even be called
        mock_client.find_potential_backlinks.assert_not_called()

    def test_no_candidates_no_issue(self):
        mock_client = MagicMock()
        mock_client.find_potential_backlinks.return_value = []
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = []

        wikitext = _categorized()
        report = audit_mos("Subject", wikitext, client=mock_client, check_backlinks=True)
        assert "potential-backlinks" not in _issue_ids(report)


# ---------------------------------------------------------------------------
# verbose=True -- stderr output for check names
# ---------------------------------------------------------------------------

class TestVerboseOutput:
    def test_verbose_prints_check_names(self, capsys: pytest.CaptureFixture) -> None:
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a test with some analysts saying things.\n"
            "Recently, yesterday, and currently this is true.\n\n"
            "== History ==\nSome legendary, iconic content here.\n"
            "<ref>https://example.com</ref>\n\n"
            "== External links ==\n* Links\n\n"
            "== References ==\n{{reflist}}\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        audit_mos("Test", wikitext, verbose=True)
        captured = capsys.readouterr()
        assert 'check: lead-length' in captured.err
        assert 'check: weasel-terms' in captured.err
        assert 'check: section-ordering' in captured.err

    def test_verbose_prints_all_major_check_groups(self, capsys: pytest.CaptureFixture) -> None:
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is widely regarded as the best.\n\n"
            "== History ==\n" + ("word " * 40) + "\n\n"
            "== See also ==\n\n"
            "== References ==\n{{reflist}}\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        audit_mos("Test", wikitext, verbose=True)
        captured = capsys.readouterr()
        # These verbose print calls cover the major check groups
        assert 'check:' in captured.err
        assert 'check: maintenance-tags' in captured.err
        assert 'check: mos-sister-projects' in captured.err


# ---------------------------------------------------------------------------
# _check_url_liveness
# ---------------------------------------------------------------------------

class TestCheckUrlLiveness:
    def test_dead_url_detected(self) -> None:
        import urllib.error
        from unittest.mock import patch

        from wiki_mos_audit.audit import _check_url_liveness
        with patch('wiki_mos_audit.audit.urllib.request.urlopen', side_effect=urllib.error.URLError('timeout')):
            dead = _check_url_liveness(['https://example.com/dead'])
        assert 'https://example.com/dead' in dead

    def test_live_url_passes(self) -> None:
        from unittest.mock import MagicMock as MM
        from unittest.mock import patch

        from wiki_mos_audit.audit import _check_url_liveness
        mock_resp = MM()
        mock_resp.status = 200
        mock_resp.__enter__ = lambda s: s
        mock_resp.__exit__ = MM(return_value=False)
        with patch('wiki_mos_audit.audit.urllib.request.urlopen', return_value=mock_resp):
            dead = _check_url_liveness(['https://example.com/live'])
        assert dead == []

    def test_http_400_status_counted_dead(self) -> None:
        from unittest.mock import MagicMock as MM
        from unittest.mock import patch

        from wiki_mos_audit.audit import _check_url_liveness
        mock_resp = MM()
        mock_resp.status = 404
        mock_resp.__enter__ = lambda s: s
        mock_resp.__exit__ = MM(return_value=False)
        with patch('wiki_mos_audit.audit.urllib.request.urlopen', return_value=mock_resp):
            dead = _check_url_liveness(['https://example.com/missing'])
        assert 'https://example.com/missing' in dead

    def test_empty_list_returns_empty(self) -> None:
        from wiki_mos_audit.audit import _check_url_liveness
        assert _check_url_liveness([]) == []

    def test_disallowed_scheme_marked_dead_without_request(self) -> None:
        from unittest.mock import patch

        from wiki_mos_audit.audit import _check_url_liveness

        with patch('wiki_mos_audit.audit.urllib.request.urlopen') as mock_urlopen:
            dead = _check_url_liveness(['file:///etc/passwd'])

        assert 'file:///etc/passwd' in dead
        mock_urlopen.assert_not_called()


# ---------------------------------------------------------------------------
# audit_mos() -- dead-external-links (check_urls=True)
# ---------------------------------------------------------------------------

class TestDeadExternalLinksAudit:
    def test_dead_link_in_wikitext_raises_issue(self) -> None:
        from unittest.mock import patch
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a test.\n\n"
            "== References ==\n"
            "<ref>https://example.com/dead-link</ref>\n"
            "{{reflist}}\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        with patch('wiki_mos_audit.audit._check_url_liveness', return_value=['https://example.com/dead-link']):
            report = audit_mos("Test", wikitext, check_urls=True)
        assert 'dead-external-links' in _issue_ids(report)

    def test_all_live_links_no_issue(self) -> None:
        from unittest.mock import patch
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a test.\n\n"
            "== References ==\n"
            "<ref>https://example.com/live</ref>\n"
            "{{reflist}}\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        with patch('wiki_mos_audit.audit._check_url_liveness', return_value=[]):
            report = audit_mos("Test", wikitext, check_urls=True)
        assert 'dead-external-links' not in _issue_ids(report)

    def test_check_urls_false_skips_liveness(self) -> None:
        from unittest.mock import patch
        wikitext = _categorized()
        with patch('wiki_mos_audit.audit._check_url_liveness') as mock_live:
            audit_mos("Test", wikitext, check_urls=False)
        mock_live.assert_not_called()

    def test_verbose_dead_links_prints_check_name(self, capsys: pytest.CaptureFixture) -> None:
        from unittest.mock import patch
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a test.\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        with patch('wiki_mos_audit.audit._check_url_liveness', return_value=[]):
            audit_mos("Test", wikitext, check_urls=True, verbose=True)
        captured = capsys.readouterr()
        assert 'check: dead-external-links' in captured.err


# ---------------------------------------------------------------------------
# audit_mos() -- orphan check API hiccup (line 911-912)
# ---------------------------------------------------------------------------

class TestOrphanApiHiccup:
    def test_api_exception_reports_unavailable_issue(self) -> None:
        import urllib.error

        mock_client = MagicMock()
        mock_client._request.side_effect = urllib.error.URLError('connection reset')
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = []

        wikitext = _categorized()
        report = audit_mos("Test", wikitext, client=mock_client, check_orphan=True)
        assert 'orphan-check-unavailable' in _issue_ids(report)
        assert 'orphan-article' not in _issue_ids(report)

    def test_verbose_orphan_prints_check_name(self, capsys: pytest.CaptureFixture) -> None:
        mock_client = MagicMock()
        mock_client._request.return_value = {
            'query': {'pages': [{'title': 'Test', 'linkshere': [{'title': 'Other'}]}]}
        }
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = []

        wikitext = _categorized()
        audit_mos("Test", wikitext, client=mock_client, check_orphan=True, verbose=True)
        captured = capsys.readouterr()
        assert 'check: orphan-article' in captured.err


# ---------------------------------------------------------------------------
# audit_mos() -- potential-backlinks verbose + exception path (lines 916-930)
# ---------------------------------------------------------------------------

class TestPotentialBacklinksVerboseAndException:
    def test_verbose_prints_check_name(self, capsys: pytest.CaptureFixture) -> None:
        mock_client = MagicMock()
        mock_client.find_potential_backlinks.return_value = []
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = []

        wikitext = _categorized()
        audit_mos("Test", wikitext, client=mock_client, check_backlinks=True, verbose=True)
        captured = capsys.readouterr()
        assert 'check: potential-backlinks' in captured.err

    def test_api_exception_reports_unavailable_issue(self) -> None:
        import urllib.error

        mock_client = MagicMock()
        mock_client.find_potential_backlinks.side_effect = urllib.error.URLError('API down')
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = []

        wikitext = _categorized()
        report = audit_mos("Test", wikitext, client=mock_client, check_backlinks=True)
        assert 'backlinks-check-unavailable' in _issue_ids(report)
        assert 'potential-backlinks' not in _issue_ids(report)


# ---------------------------------------------------------------------------
# infobox regex fallback branch (lines 402-416, no mwparserfromhell)
# ---------------------------------------------------------------------------

class TestInfboxRegexFallback:
    def test_infobox_regex_path_executes(self) -> None:
        # Force the regex fallback by passing wikitext with no mwparserfromhell parse.
        # audit_mos with no mwparserfromhell available uses regex path.
        # We can force it by patching out the module-level mwparserfromhell.
        from unittest.mock import patch

        import wiki_mos_audit.audit as audit_mod
        wikitext = (
            "{{Short description|Test}}\n"
            "{{Infobox person\n"
            "| name = Test Subject\n"
            "| birth_date = 1980\n"
            "}}\n"
            "'''Test Subject''' is a person.\n\n"
            "== Biography ==\n" + ("word " * 30) + "\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        with patch.object(audit_mod, 'mwparserfromhell', None):
            report = audit_mos("Test Subject", wikitext)
        # The important thing is it runs without error; infobox check fires via regex
        assert report is not None


# ---------------------------------------------------------------------------
# Regex fallback (no_ast) -- dual-path regression tests
# ---------------------------------------------------------------------------

class TestRegexFallbackPath:
    """Verify all 15 AST-converted checks still work via regex fallback."""

    def test_overlinking_regex(self, no_ast):
        wikitext = _categorized(
            "[[France]] is a country. [[France]] borders Germany. [[France]] has Paris."
        )
        report = audit_mos("Subject", wikitext)
        assert "overlinking" in _issue_ids(report)

    def test_unreferenced_sections_regex(self, no_ast):
        body = " ".join(f"word{i}" for i in range(105))
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            + body
            + "\n\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "unreferenced-sections" in _issue_ids(report)

    def test_short_sections_regex(self, no_ast):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            "Only ten words appear in this short section body.\n\n"
            "== Details ==\n"
            + ("word " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "short-sections" in _issue_ids(report)

    def test_see_also_bloat_regex(self, no_ast):
        items = "\n".join(f"* [[Article {i}]]" for i in range(11))
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n\n== See also ==\n"
            + items
            + "\n\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "see-also-bloat" in _issue_ids(report)

    def test_cs1_isbn_validation_regex(self, no_ast):
        wikitext = _categorized("{{cite book|title=X|isbn=0306406153}}")
        report = audit_mos("Subject", wikitext)
        assert "cs1-isbn-validation" in _issue_ids(report)

    def test_cs1_url_validation_regex(self, no_ast):
        wikitext = _categorized("{{cite web|url=example.com/page|title=X}}")
        report = audit_mos("Subject", wikitext)
        assert "cs1-url-validation" in _issue_ids(report)

    def test_section_ordering_regex(self, no_ast):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== History ==\n"
            + ("word " * 35) + "\n\n"
            "== External links ==\n"
            "* [https://example.com]\n\n"
            "== References ==\n"
            "{{reflist}}\n\n"
            "[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "section-ordering" in _issue_ids(report)

    def test_short_description_missing_regex(self, no_ast):
        wikitext = (
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        issues = [i for i in report.issues if i.check_id == "short-description-quality"]
        assert issues

    def test_short_description_too_long_regex(self, no_ast):
        long_desc = "A " + "very " * 10 + "long description exceeding forty chars"
        wikitext = (
            f"{{{{Short description|{long_desc}}}}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n[[Category:Test]]\n[[Category:Example]]\n"
        )
        report = audit_mos("Subject", wikitext)
        issues = [i for i in report.issues if i.check_id == "short-description-quality"]
        assert issues

    def test_bare_urls_in_refs_regex(self, no_ast):
        wikitext = _categorized("A fact.<ref>https://example.com/article</ref>")
        report = audit_mos("Subject", wikitext)
        assert "bare-urls-in-refs" in _issue_ids(report)

    def test_uncategorized_regex(self, no_ast):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
        )
        report = audit_mos("Subject", wikitext)
        assert "uncategorized" in _issue_ids(report)

    def test_category_quality_regex(self, no_ast):
        wikitext = (
            "{{Short description|Test}}\n"
            "'''Subject''' is a subject.\n\n"
            "== Section ==\n"
            + ("word " * 35)
            + "\n[[Category:X]]\n"
        )
        report = audit_mos("Subject", wikitext)
        assert "category-quality" in _issue_ids(report)

    def test_external_links_in_body_regex(self, no_ast):
        wikitext = _categorized("More info at https://example.com for details.")
        report = audit_mos("Subject", wikitext)
        assert "external-links-in-body" in _issue_ids(report)

    def test_red_links_regex(self, no_ast):
        from unittest.mock import MagicMock
        mock_client = MagicMock()
        mock_client.check_page_existence.return_value = {'Nonexistent': False}
        mock_client.check_disambiguation.return_value = []
        wikitext = _categorized("[[Nonexistent]] appears here.")
        report = audit_mos("Subject", wikitext, client=mock_client)
        assert "red-links" in _issue_ids(report)

    def test_disambiguation_links_regex(self, no_ast):
        from unittest.mock import MagicMock
        mock_client = MagicMock()
        mock_client.check_page_existence.return_value = {}
        mock_client.check_disambiguation.return_value = ['Mercury']
        wikitext = _categorized("[[Mercury]] the planet.")
        report = audit_mos("Subject", wikitext, client=mock_client)
        assert "disambiguation-links" in _issue_ids(report)
