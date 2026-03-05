"""Unit tests for wiki_mos_audit.models."""
from __future__ import annotations

import pytest

from wiki_mos_audit.models import (
    _LANG_CODE_RE,
    COMMON_INFOBOX_REQUIREMENTS,
    ISSUE_TO_MAINTENANCE_TAG,
    MAINTENANCE_TEMPLATES,
    MONTHS,
    PEACOCK_TERMS,
    RELATIVE_TIME_TERMS,
    SEVERITY_WEIGHTS,
    SISTER_PROJECT_LINK_PATTERN,
    VERSION,
    WEASEL_TERMS,
    AuditReport,
    Issue,
)

# ---------------------------------------------------------------------------
# Issue dataclass
# ---------------------------------------------------------------------------

class TestIssue:
    def test_field_access(self) -> None:
        issue = Issue(
            check_id='weasel-terms',
            severity='medium',
            section='Lead',
            message='Weasel word detected',
            evidence='is believed to',
            suggestion='Attribute the claim or remove it.',
        )
        assert issue.check_id == 'weasel-terms'
        assert issue.severity == 'medium'
        assert issue.section == 'Lead'
        assert issue.message == 'Weasel word detected'
        assert issue.evidence == 'is believed to'
        assert issue.suggestion == 'Attribute the claim or remove it.'

    def test_equality(self) -> None:
        a = Issue('x', 'low', 'Body', 'msg', 'ev', 'sug')
        b = Issue('x', 'low', 'Body', 'msg', 'ev', 'sug')
        assert a == b

    def test_inequality_on_any_field(self) -> None:
        base = Issue('x', 'low', 'Body', 'msg', 'ev', 'sug')
        assert base != Issue('y', 'low', 'Body', 'msg', 'ev', 'sug')
        assert base != Issue('x', 'high', 'Body', 'msg', 'ev', 'sug')


# ---------------------------------------------------------------------------
# AuditReport dataclass
# ---------------------------------------------------------------------------

class TestAuditReport:
    def test_field_access(self) -> None:
        issues = [Issue('x', 'low', 'Body', 'msg', 'ev', 'sug')]
        report = AuditReport(title='Test Article', score=72, issues=issues)
        assert report.title == 'Test Article'
        assert report.score == 72
        assert report.issues is issues

    def test_empty_issues(self) -> None:
        report = AuditReport(title='Clean Article', score=100, issues=[])
        assert report.issues == []

    def test_negative_score_allowed(self) -> None:
        # Score is an int field; no clamping defined in the model.
        report = AuditReport(title='Bad Article', score=-5, issues=[])
        assert report.score == -5


# ---------------------------------------------------------------------------
# Constant tuples: non-empty and element types
# ---------------------------------------------------------------------------

@pytest.mark.parametrize('constant,name', [
    (MONTHS, 'MONTHS'),
    (WEASEL_TERMS, 'WEASEL_TERMS'),
    (RELATIVE_TIME_TERMS, 'RELATIVE_TIME_TERMS'),
    (PEACOCK_TERMS, 'PEACOCK_TERMS'),
])
def test_constant_tuple_nonempty(constant: tuple, name: str) -> None:
    assert len(constant) > 0, f'{name} must not be empty'


def test_months_has_twelve_entries() -> None:
    assert len(MONTHS) == 12


def test_months_all_strings() -> None:
    assert all(isinstance(m, str) for m in MONTHS)


@pytest.mark.parametrize('term', WEASEL_TERMS)
def test_weasel_terms_are_lowercase_strings(term: str) -> None:
    assert isinstance(term, str)
    assert term == term.lower()


@pytest.mark.parametrize('term', PEACOCK_TERMS)
def test_peacock_terms_are_lowercase_strings(term: str) -> None:
    assert isinstance(term, str)
    assert term == term.lower()


# ---------------------------------------------------------------------------
# SEVERITY_WEIGHTS
# ---------------------------------------------------------------------------

def test_severity_weights_has_expected_keys() -> None:
    assert set(SEVERITY_WEIGHTS.keys()) == {'high', 'medium', 'low'}


def test_severity_weights_values_are_positive_ints() -> None:
    for key, val in SEVERITY_WEIGHTS.items():
        assert isinstance(val, int), f'{key} weight must be int'
        assert val > 0, f'{key} weight must be positive'


def test_severity_weights_ordering() -> None:
    # high > medium > low by definition
    assert SEVERITY_WEIGHTS['high'] > SEVERITY_WEIGHTS['medium'] > SEVERITY_WEIGHTS['low']


# ---------------------------------------------------------------------------
# MAINTENANCE_TEMPLATES
# ---------------------------------------------------------------------------

def test_maintenance_templates_is_set() -> None:
    assert isinstance(MAINTENANCE_TEMPLATES, set)


def test_maintenance_templates_nonempty() -> None:
    assert len(MAINTENANCE_TEMPLATES) > 0


def test_maintenance_templates_all_lowercase_strings() -> None:
    for t in MAINTENANCE_TEMPLATES:
        assert isinstance(t, str)
        assert t == t.lower()


# ---------------------------------------------------------------------------
# ISSUE_TO_MAINTENANCE_TAG
# ---------------------------------------------------------------------------

def test_issue_to_maintenance_tag_maps_to_strings() -> None:
    for check_id, tag in ISSUE_TO_MAINTENANCE_TAG.items():
        assert isinstance(check_id, str), f'key {check_id!r} must be str'
        assert isinstance(tag, str), f'value for {check_id!r} must be str'
        assert tag, f'tag for {check_id!r} must not be empty'


def test_issue_to_maintenance_tag_nonempty() -> None:
    assert len(ISSUE_TO_MAINTENANCE_TAG) > 0


# ---------------------------------------------------------------------------
# COMMON_INFOBOX_REQUIREMENTS
# ---------------------------------------------------------------------------

def test_common_infobox_requirements_nonempty() -> None:
    assert len(COMMON_INFOBOX_REQUIREMENTS) > 0


def test_common_infobox_requirements_keys_are_lowercase() -> None:
    for key in COMMON_INFOBOX_REQUIREMENTS:
        assert key == key.lower(), f'key {key!r} should be lowercase'


def test_common_infobox_requirements_values_are_tuple_of_tuples_of_strings() -> None:
    for infobox_name, field_groups in COMMON_INFOBOX_REQUIREMENTS.items():
        assert isinstance(field_groups, tuple), (
            f'{infobox_name}: outer container must be tuple'
        )
        for group in field_groups:
            assert isinstance(group, tuple), (
                f'{infobox_name}: each field group must be a tuple'
            )
            assert len(group) > 0, (
                f'{infobox_name}: field groups must not be empty'
            )
            for field in group:
                assert isinstance(field, str), (
                    f'{infobox_name}: field name {field!r} must be str'
                )


@pytest.mark.parametrize('infobox_name', [
    'infobox person',
    'infobox settlement',
    'infobox military conflict',
])
def test_known_infoboxes_present(infobox_name: str) -> None:
    assert infobox_name in COMMON_INFOBOX_REQUIREMENTS


# ---------------------------------------------------------------------------
# VERSION
# ---------------------------------------------------------------------------

def test_version_is_string() -> None:
    assert isinstance(VERSION, str)


def test_version_nonempty() -> None:
    assert VERSION.strip()


# ---------------------------------------------------------------------------
# _LANG_CODE_RE
# ---------------------------------------------------------------------------

@pytest.mark.parametrize('code', [
    'en',
    'fr',
    'chr',
    'zh',
    'pt',
    'en-us',
    'zh-hans',
    'chr-latn',
])
def test_lang_code_re_accepts_valid_codes(code: str) -> None:
    assert _LANG_CODE_RE.match(code), f'{code!r} should be accepted'


@pytest.mark.parametrize('code', [
    '',
    'e',                  # too short
    'EN',                 # uppercase not allowed
    'en_us',              # underscore separator not allowed
    'en-',                # trailing dash
    '-en',                # leading dash
    'en-US',              # uppercase subtag
    'en us',              # space
    'English',            # full word
    'a1',                 # digit
    '123',                # digits only
    'en; DROP TABLE',     # injection attempt
])
def test_lang_code_re_rejects_invalid_codes(code: str) -> None:
    assert not _LANG_CODE_RE.match(code), f'{code!r} should be rejected'


# ---------------------------------------------------------------------------
# SISTER_PROJECT_LINK_PATTERN
# ---------------------------------------------------------------------------

@pytest.mark.parametrize('url', [
    'https://en.wiktionary.org/wiki/test',
    'https://commons.wikimedia.org/wiki/File:Test.jpg',
    'https://fr.wikisource.org/wiki/Page',
    'https://www.wikiquote.org/wiki/Test',
    'https://species.wikimedia.org/wiki/Testus',
    'http://wikidata.org/wiki/Q42',
    'https://en.wikivoyage.org/wiki/Paris',
    'https://en.wikibooks.org/wiki/Test',
    'https://en.wikinews.org/wiki/Test',
    'https://en.wikiversity.org/wiki/Test',
])
def test_sister_project_link_pattern_matches(url: str) -> None:
    assert SISTER_PROJECT_LINK_PATTERN.search(url), f'{url!r} should match'


@pytest.mark.parametrize('url', [
    'https://en.wikipedia.org/wiki/Test',
    'https://example.com/wiki/Test',
    'https://mediawiki.org/wiki/Test',
    'https://wikia.com/wiki/Test',
])
def test_sister_project_link_pattern_no_match(url: str) -> None:
    assert not SISTER_PROJECT_LINK_PATTERN.search(url), f'{url!r} should not match'
