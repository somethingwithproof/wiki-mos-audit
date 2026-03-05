"""Unit tests for wiki_mos_audit.maintenance."""
from __future__ import annotations

import re

import pytest

from wiki_mos_audit.maintenance import (
    apply_maintenance_tags,
    find_lead_template_insertion_index,
    parse_maintenance_tag_args,
    suggest_maintenance_tags,
)
from wiki_mos_audit.models import Issue

# ---------------------------------------------------------------------------
# parse_maintenance_tag_args
# ---------------------------------------------------------------------------

class TestParseMaintenanceTagArgs:
    def test_none_returns_empty(self) -> None:
        assert parse_maintenance_tag_args(None) == []

    def test_empty_list_returns_empty(self) -> None:
        assert parse_maintenance_tag_args([]) == []

    def test_single_value(self) -> None:
        assert parse_maintenance_tag_args(['Cleanup']) == ['Cleanup']

    def test_comma_separated_single_string(self) -> None:
        result = parse_maintenance_tag_args(['Cleanup,Update'])
        assert result == ['Cleanup', 'Update']

    def test_comma_separated_with_spaces(self) -> None:
        result = parse_maintenance_tag_args(['Cleanup, Update, Peacock'])
        assert result == ['Cleanup', 'Update', 'Peacock']

    def test_multiple_list_entries(self) -> None:
        result = parse_maintenance_tag_args(['Cleanup', 'Peacock'])
        assert result == ['Cleanup', 'Peacock']

    def test_multiple_entries_comma_mixed(self) -> None:
        result = parse_maintenance_tag_args(['Cleanup,Update', 'Peacock'])
        assert result == ['Cleanup', 'Update', 'Peacock']

    def test_strips_braces(self) -> None:
        # Values passed with brace remnants are cleaned up.
        result = parse_maintenance_tag_args(['{{Cleanup}}'])
        assert result == ['Cleanup']

    def test_strips_partial_braces(self) -> None:
        result = parse_maintenance_tag_args(['{Cleanup}'])
        assert result == ['Cleanup']

    def test_empty_string_in_list_yields_empty(self) -> None:
        assert parse_maintenance_tag_args(['']) == []

    def test_whitespace_only_entry_ignored(self) -> None:
        result = parse_maintenance_tag_args(['  '])
        assert result == []

    def test_repeated_values_preserved_as_received(self) -> None:
        # The function does not deduplicate; that is the caller's concern.
        result = parse_maintenance_tag_args(['Cleanup', 'Cleanup'])
        assert result == ['Cleanup', 'Cleanup']

    @pytest.mark.parametrize('raw_tag', [
        'Cleanup}}\n[[Category:Evil]]',
        'Cleanup|reason=x',
        'Cleanup<script>',
        'Cleanup[]',
    ])
    def test_rejects_invalid_maintenance_tags(self, raw_tag: str) -> None:
        with pytest.raises(ValueError, match='Invalid maintenance tag'):
            parse_maintenance_tag_args([raw_tag])

    @pytest.mark.parametrize('values,expected', [
        (None, []),
        ([], []),
        (['Weasel'], ['Weasel']),
        (['Weasel,Update'], ['Weasel', 'Update']),
        (['{{Peacock}}'], ['Peacock']),
        (['  Cleanup  '], ['Cleanup']),
    ])
    def test_parametrized_cases(self, values: list[str] | None, expected: list[str]) -> None:
        assert parse_maintenance_tag_args(values) == expected


# ---------------------------------------------------------------------------
# suggest_maintenance_tags
# ---------------------------------------------------------------------------

class TestSuggestMaintenanceTags:
    def _make_issue(self, check_id: str) -> Issue:
        return Issue(
            check_id=check_id,
            severity='medium',
            section='Lead',
            message='msg',
            evidence='ev',
            suggestion='sug',
        )

    def test_no_issues_returns_empty(self) -> None:
        assert suggest_maintenance_tags([]) == []

    def test_known_check_id_maps_to_tag(self) -> None:
        result = suggest_maintenance_tags([self._make_issue('weasel-terms')])
        assert 'Weasel' in result

    def test_unknown_check_id_skipped(self) -> None:
        result = suggest_maintenance_tags([self._make_issue('unknown-check')])
        assert result == []

    def test_deduplicates_tags(self) -> None:
        issues = [
            self._make_issue('weasel-terms'),
            self._make_issue('weasel-terms'),
        ]
        result = suggest_maintenance_tags(issues)
        assert result.count('Weasel') == 1

    def test_multiple_distinct_checks(self) -> None:
        issues = [
            self._make_issue('weasel-terms'),
            self._make_issue('peacock-terms'),
            self._make_issue('relative-time'),
        ]
        result = suggest_maintenance_tags(issues)
        assert 'Weasel' in result
        assert 'Peacock' in result
        assert 'Update' in result

    def test_mix_of_known_and_unknown(self) -> None:
        issues = [
            self._make_issue('peacock-terms'),
            self._make_issue('does-not-exist'),
        ]
        result = suggest_maintenance_tags(issues)
        assert 'Peacock' in result
        assert len(result) == 1

    def test_preserves_insertion_order(self) -> None:
        # Tags should appear in the order their check_ids are first encountered.
        issues = [
            self._make_issue('weasel-terms'),
            self._make_issue('peacock-terms'),
        ]
        result = suggest_maintenance_tags(issues)
        assert result.index('Weasel') < result.index('Peacock')


# ---------------------------------------------------------------------------
# find_lead_template_insertion_index
# ---------------------------------------------------------------------------

class TestFindLeadTemplateInsertionIndex:
    def test_empty_string(self) -> None:
        assert find_lead_template_insertion_index('') == 0

    def test_plain_text_starts_at_zero(self) -> None:
        text = "'''Article''' is about something."
        assert find_lead_template_insertion_index(text) == 0

    def test_leading_whitespace_skipped(self) -> None:
        text = "\n\n'''Article''' is about something."
        idx = find_lead_template_insertion_index(text)
        assert text[idx] == "'"

    def test_leading_comment_skipped(self) -> None:
        text = '<!-- comment -->Some text here.'
        idx = find_lead_template_insertion_index(text)
        assert text[idx:].startswith('Some text')

    def test_leading_comment_then_template_skipped(self) -> None:
        text = '<!-- comment -->{{Short description|Test}}\nProse here.'
        idx = find_lead_template_insertion_index(text)
        assert text[idx:].startswith('Prose here.')

    def test_single_leading_template_skipped(self) -> None:
        text = '{{Short description|A test article}}\nProse starts here.'
        idx = find_lead_template_insertion_index(text)
        assert text[idx:].startswith('Prose starts here.')

    def test_multiple_leading_templates_skipped(self) -> None:
        text = '{{Short description|Foo}}\n{{Use mdy dates}}\nProse here.'
        idx = find_lead_template_insertion_index(text)
        assert text[idx:].startswith('Prose here.')

    def test_nested_template_skipped(self) -> None:
        text = '{{Infobox person\n| birth_date = {{birth date|1980|1|1}}\n}}\nProse.'
        idx = find_lead_template_insertion_index(text)
        assert text[idx:].startswith('Prose.')

    def test_unclosed_comment_returns_length(self) -> None:
        text = '<!-- unclosed comment without end'
        assert find_lead_template_insertion_index(text) == len(text)

    def test_unclosed_template_returns_template_start(self) -> None:
        text = '{{unclosed\nArticle text here'
        idx = find_lead_template_insertion_index(text)
        assert idx == 0

    def test_index_within_bounds(self) -> None:
        text = '{{Foo}}\nBar'
        idx = find_lead_template_insertion_index(text)
        assert 0 <= idx <= len(text)

    @pytest.mark.parametrize('wikitext,expected_start', [
        ("'''Bold'''", "'''Bold'''"),
        ('{{Tmpl}}\nProse', 'Prose'),
        ('<!-- c -->{{Tmpl}}\nProse', 'Prose'),
        ('\n{{Tmpl}}\nProse', 'Prose'),
    ])
    def test_parametrized_insertion_points(self, wikitext: str, expected_start: str) -> None:
        idx = find_lead_template_insertion_index(wikitext)
        assert wikitext[idx:].startswith(expected_start)


# ---------------------------------------------------------------------------
# apply_maintenance_tags
# ---------------------------------------------------------------------------

_DATE_PATTERN = re.compile(
    r'(January|February|March|April|May|June|July|August|September|October|November|December) \d{4}'
)


class TestApplyMaintenanceTags:
    def test_adds_new_tag(self) -> None:
        wikitext = "'''Article''' is prose."
        result, added = apply_maintenance_tags(wikitext, ['Cleanup'], set())
        assert 'Cleanup' in added
        assert '{{Cleanup|date=' in result

    def test_skips_existing_tag(self) -> None:
        wikitext = "'''Article''' is prose."
        result, added = apply_maintenance_tags(wikitext, ['cleanup'], {'cleanup'})
        assert added == []
        assert result == wikitext

    def test_dry_run_does_not_modify_wikitext(self) -> None:
        wikitext = "'''Article''' is prose."
        result, added = apply_maintenance_tags(wikitext, ['Cleanup'], set(), dry_run=True)
        assert result == wikitext
        assert 'Cleanup' in added

    def test_dry_run_still_reports_would_add(self) -> None:
        wikitext = "'''Article''' is prose."
        _, added = apply_maintenance_tags(wikitext, ['Peacock', 'Weasel'], set(), dry_run=True)
        assert 'Peacock' in added
        assert 'Weasel' in added

    def test_date_stamp_format(self) -> None:
        wikitext = "'''Article''' is prose."
        result, _ = apply_maintenance_tags(wikitext, ['Cleanup'], set())
        match = _DATE_PATTERN.search(result)
        assert match is not None, 'date stamp should be Month YYYY format'

    def test_tag_inserted_before_prose(self) -> None:
        wikitext = "'''Article''' is prose."
        result, _ = apply_maintenance_tags(wikitext, ['Cleanup'], set())
        cleanup_pos = result.index('{{Cleanup')
        prose_pos = result.index("'''Article'''")
        assert cleanup_pos < prose_pos

    def test_tag_inserted_after_leading_templates(self) -> None:
        wikitext = '{{Short description|Test}}\n{{Use mdy dates}}\nProse.'
        result, _ = apply_maintenance_tags(wikitext, ['Cleanup'], set())
        short_desc_pos = result.index('{{Short description')
        cleanup_pos = result.index('{{Cleanup')
        prose_pos = result.index('Prose.')
        assert short_desc_pos < cleanup_pos < prose_pos

    def test_multiple_tags_added(self) -> None:
        wikitext = "'''Article''' is prose."
        result, added = apply_maintenance_tags(wikitext, ['Cleanup', 'Peacock'], set())
        assert 'Cleanup' in added
        assert 'Peacock' in added
        assert '{{Cleanup|date=' in result
        assert '{{Peacock|date=' in result

    def test_no_tags_returns_original(self) -> None:
        wikitext = "'''Article''' is prose."
        result, added = apply_maintenance_tags(wikitext, [], set())
        assert result == wikitext
        assert added == []

    def test_all_tags_already_exist_returns_original(self) -> None:
        wikitext = "'''Article''' is prose."
        result, added = apply_maintenance_tags(
            wikitext, ['cleanup', 'weasel'], {'cleanup', 'weasel'}
        )
        assert result == wikitext
        assert added == []

    def test_partial_existing_tags_only_adds_new(self) -> None:
        wikitext = "'''Article''' is prose."
        result, added = apply_maintenance_tags(
            wikitext, ['Cleanup', 'Peacock'], {'cleanup'}
        )
        assert added == ['Peacock']
        assert '{{Peacock|date=' in result
        assert result.count('{{Cleanup') == 0

    def test_prefix_gets_newline_before_tag_block(self) -> None:
        # When there is a prefix that doesn't end with \n, one must be added.
        wikitext = '{{Short description|Foo}}\nProse.'
        result, _ = apply_maintenance_tags(wikitext, ['Weasel'], set())
        # The short description template should end with \n before the tag block.
        short_desc_end = result.index('\n', result.index('{{Short description'))
        weasel_start = result.index('{{Weasel')
        assert short_desc_end < weasel_start

    def test_unclosed_template_does_not_split_prose(self) -> None:
        wikitext = '{{unclosed\nArticle text here'
        result, added = apply_maintenance_tags(wikitext, ['Cleanup'], set(), dry_run=False)
        assert added == ['Cleanup']
        assert 'Article text here' in result
