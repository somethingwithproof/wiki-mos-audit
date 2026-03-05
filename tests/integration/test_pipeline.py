"""Integration tests for the full audit pipeline (network mocked)."""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

import pytest

from wiki_mos_audit.audit import audit_mos, template_names_from_wikitext
from wiki_mos_audit.cli import main
from wiki_mos_audit.maintenance import apply_maintenance_tags, suggest_maintenance_tags

# ---------------------------------------------------------------------------
# Fixture wikitext strings (supplement conftest.py fixtures)
# ---------------------------------------------------------------------------

AI_HEAVY_WIKITEXT = textwrap.dedent("""\
    '''AI Article''' covers a topic.

    A 2019 article in the New York Times described the subject and noted its importance.
    An 2021 profile in The Guardian highlighted the ongoing relevance of this work.
    It is worth noting that this illustrates the broader trend.

    == History ==

    This demonstrates that early efforts played a significant role in shaping outcomes.
    It is important to note that the subject left an indelible mark on the field.

    [[Category:Test articles]]
    [[Category:Examples]]
""")

BAD_CITATIONS_WIKITEXT = textwrap.dedent("""\
    '''Citation Article''' is an article.

    == References ==

    {{cite book |title=Some Book |isbn=1234567890123}}
    {{cite web |url=not a url |title=Bad link}}

    [[Category:Test articles]]
    [[Category:Examples]]
""")

MAINTENANCE_TAG_WIKITEXT = textwrap.dedent("""\
    '''Weasel Article''' is widely regarded as the best.
    It is said that many people agree.

    == History ==

    Some history with enough words to avoid short section.
    This section continues with more content to pass the threshold.
    Adding more words here to clear the thirty word minimum easily.

    [[Category:Test articles]]
    [[Category:Examples]]
""")

SAMPLE_ARTICLE = (
    Path(__file__).parent.parent.parent / 'fixtures' / 'sample_article.txt'
)


# ---------------------------------------------------------------------------
# audit_mos pipeline
# ---------------------------------------------------------------------------

class TestAuditMosPipeline:
    def test_sample_fixture_produces_report(self) -> None:
        wikitext = SAMPLE_ARTICLE.read_text(encoding='utf-8')
        report = audit_mos('Cascade Range', wikitext)
        assert report.title == 'Cascade Range'
        assert isinstance(report.score, int)
        assert 0 <= report.score <= 100
        assert isinstance(report.issues, list)

    def test_report_structure_fields(self) -> None:
        wikitext = SAMPLE_ARTICLE.read_text(encoding='utf-8')
        report = audit_mos('Cascade Range', wikitext)
        for issue in report.issues:
            assert issue.check_id
            assert issue.severity in ('low', 'medium', 'high')
            assert issue.section
            assert issue.message
            assert issue.evidence is not None
            assert issue.suggestion

    def test_ai_heavy_fires_overattribution(self) -> None:
        report = audit_mos('AI Article', AI_HEAVY_WIKITEXT)
        check_ids = {i.check_id for i in report.issues}
        assert 'ai-overattribution' in check_ids, (
            f'Expected ai-overattribution; got {sorted(check_ids)}'
        )

    def test_ai_heavy_fires_essay_tone(self) -> None:
        report = audit_mos('AI Article', AI_HEAVY_WIKITEXT)
        check_ids = {i.check_id for i in report.issues}
        assert 'ai-essay-tone' in check_ids, (
            f'Expected ai-essay-tone; got {sorted(check_ids)}'
        )

    def test_bad_citations_fires_isbn_validation(self) -> None:
        report = audit_mos('Citation Article', BAD_CITATIONS_WIKITEXT)
        check_ids = {i.check_id for i in report.issues}
        assert 'cs1-isbn-validation' in check_ids, (
            f'Expected cs1-isbn-validation; got {sorted(check_ids)}'
        )

    def test_bad_citations_fires_url_validation(self) -> None:
        report = audit_mos('Citation Article', BAD_CITATIONS_WIKITEXT)
        check_ids = {i.check_id for i in report.issues}
        assert 'cs1-url-validation' in check_ids, (
            f'Expected cs1-url-validation; got {sorted(check_ids)}'
        )

    def test_score_decreases_with_issues(self) -> None:
        clean_wikitext = textwrap.dedent("""\
            {{Short description|A mountain range}}
            '''Clean Article''' is a clean article about a topic.

            == Geography ==

            The area contains notable geographic features. This section has enough words
            to avoid short-section flagging. Adding more content here to be sure.
            The geography of the region is well documented in academic sources.<ref>Source.</ref>

            [[Category:Mountain ranges]]
            [[Category:Geographic articles]]
        """)
        report_clean = audit_mos('Clean Article', clean_wikitext)
        report_issues = audit_mos('AI Article', AI_HEAVY_WIKITEXT)
        assert report_clean.score >= report_issues.score

    def test_no_client_skips_red_link_check(self) -> None:
        wikitext = "'''Test''' is a test.\n\n[[Nonexistent Article XYZ]]\n\n[[Category:Tests]]\n"
        report = audit_mos('Test', wikitext, client=None)
        check_ids = {i.check_id for i in report.issues}
        assert 'red-links' not in check_ids


# ---------------------------------------------------------------------------
# main() JSON output
# ---------------------------------------------------------------------------

class TestMainJsonOutput:
    def test_json_output_structure(self, tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
        f = tmp_path / 'art.txt'
        f.write_text(SAMPLE_ARTICLE.read_text(encoding='utf-8'))
        result = main(['Cascade Range', '--wikitext-file', str(f), '--json'])
        assert result == 0
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert 'title' in data
        assert 'score' in data
        assert 'issues' in data
        assert isinstance(data['issues'], list)
        assert data['title'] == 'Cascade Range'

    def test_json_issue_fields(self, tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
        f = tmp_path / 'art.txt'
        f.write_text(AI_HEAVY_WIKITEXT)
        main(['AI Article', '--wikitext-file', str(f), '--json'])
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        if data['issues']:
            issue = data['issues'][0]
            for field in ('check_id', 'severity', 'section', 'message', 'evidence', 'suggestion'):
                assert field in issue, f'Missing field: {field}'


# ---------------------------------------------------------------------------
# Maintenance tag integration
# ---------------------------------------------------------------------------

class TestMaintenanceTagIntegration:
    def test_dry_run_suggests_tags(self, tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
        f = tmp_path / 'art.txt'
        f.write_text(MAINTENANCE_TAG_WIKITEXT)
        result = main([
            'Weasel Article', '--wikitext-file', str(f),
            '--add-maintenance-tags', '--dry-run',
        ])
        assert result == 0
        captured = capsys.readouterr()
        # dry-run output should mention maintenance tags
        assert 'would add' in captured.out or 'Maintenance tags' in captured.out

    def test_apply_tags_modifies_wikitext(self) -> None:
        wikitext = MAINTENANCE_TAG_WIKITEXT
        report = audit_mos('Weasel Article', wikitext)
        auto_tags = suggest_maintenance_tags(report.issues)
        assert auto_tags, 'Expected at least one suggested tag for weasel-heavy wikitext'

        existing = template_names_from_wikitext(wikitext)
        updated, added = apply_maintenance_tags(
            wikitext=wikitext,
            tags=auto_tags,
            existing_template_names=existing,
            dry_run=False,
        )
        assert added
        for tag in added:
            assert f'{{{{{tag}' in updated

    def test_dry_run_does_not_modify_wikitext(self) -> None:
        wikitext = MAINTENANCE_TAG_WIKITEXT
        report = audit_mos('Weasel Article', wikitext)
        auto_tags = suggest_maintenance_tags(report.issues)
        existing = template_names_from_wikitext(wikitext)
        updated, added = apply_maintenance_tags(
            wikitext=wikitext,
            tags=auto_tags,
            existing_template_names=existing,
            dry_run=True,
        )
        # dry_run: wikitext unchanged, but added list still populated
        assert updated == wikitext
        assert isinstance(added, list)

    def test_json_dry_run_output_structure(self, tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
        f = tmp_path / 'art.txt'
        f.write_text(MAINTENANCE_TAG_WIKITEXT)
        result = main([
            'Weasel Article', '--wikitext-file', str(f),
            '--add-maintenance-tags', '--dry-run', '--json',
        ])
        assert result == 0
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert 'suggested_maintenance_tags' in data
        assert 'dry_run' in data
        assert data['dry_run'] is True
