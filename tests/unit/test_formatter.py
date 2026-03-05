"""Unit tests for wiki_mos_audit.formatter."""
from __future__ import annotations

import json

from wiki_mos_audit.formatter import (
    _html_escape,
    format_batch_summary,
    format_html_report,
    format_json_report,
    format_text_report,
)
from wiki_mos_audit.models import AuditReport, Issue


def _make_issue(
    check_id: str = 'check-0',
    severity: str = 'medium',
    section: str = 'global',
    message: str = 'msg 0',
    evidence: str = 'ev 0',
    suggestion: str = 'fix 0',
) -> Issue:
    return Issue(
        check_id=check_id,
        severity=severity,
        section=section,
        message=message,
        evidence=evidence,
        suggestion=suggestion,
    )


def _make_report(n_issues: int = 0, title: str = 'Test Article', score: int = 85) -> AuditReport:
    issues = [
        Issue(
            check_id=f'check-{i}',
            severity='medium',
            section='global',
            message=f'msg {i}',
            evidence=f'ev {i}',
            suggestion=f'fix {i}',
        )
        for i in range(n_issues)
    ]
    return AuditReport(title=title, score=score, issues=issues)


# ---------------------------------------------------------------------------
# format_text_report
# ---------------------------------------------------------------------------

class TestFormatTextReport:
    def test_with_issues(self) -> None:
        report = _make_report(n_issues=2)
        text = format_text_report(report)
        assert 'Test Article' in text
        assert '85/100' in text
        assert '[medium]' in text
        assert 'check-0' in text
        assert 'check-1' in text
        assert 'msg 0' in text
        assert 'Evidence: ev 0' in text
        assert 'Fix: fix 0' in text

    def test_no_issues(self) -> None:
        report = _make_report(n_issues=0)
        text = format_text_report(report)
        assert 'No first-pass MOS issues detected.' in text
        assert 'Test Article' in text
        assert '85/100' in text

    def test_formatting_pattern(self) -> None:
        report = _make_report(n_issues=1)
        text = format_text_report(report)
        lines = text.split('\n')
        assert lines[0] == 'MOS first-pass audit: Test Article'
        assert lines[1] == 'Score: 85/100'
        assert lines[2] == ''
        assert lines[3].startswith('- [medium] check-0')

    def test_severity_in_brackets(self) -> None:
        issue = _make_issue(severity='high')
        report = AuditReport(title='T', score=50, issues=[issue])
        text = format_text_report(report)
        assert '[high]' in text

    def test_section_in_parens(self) -> None:
        issue = _make_issue(section='Lead')
        report = AuditReport(title='T', score=50, issues=[issue])
        text = format_text_report(report)
        assert '(Lead)' in text


# ---------------------------------------------------------------------------
# format_json_report
# ---------------------------------------------------------------------------

class TestFormatJsonReport:
    def test_valid_json(self) -> None:
        report = _make_report(n_issues=1)
        output = format_json_report(report)
        data = json.loads(output)
        assert isinstance(data, dict)

    def test_all_keys_present(self) -> None:
        report = _make_report(n_issues=1)
        output = format_json_report(report)
        data = json.loads(output)
        expected_keys = {
            'title', 'score', 'issue_count', 'issues',
            'suggested_maintenance_tags', 'added_maintenance_tags',
            'dry_run', 'output_file',
        }
        assert set(data.keys()) == expected_keys

    def test_with_suggested_tags(self) -> None:
        report = _make_report(n_issues=0)
        output = format_json_report(report, suggested_tags=['Cleanup', 'Stub'])
        data = json.loads(output)
        assert data['suggested_maintenance_tags'] == ['Cleanup', 'Stub']

    def test_empty_issues(self) -> None:
        report = _make_report(n_issues=0)
        output = format_json_report(report)
        data = json.loads(output)
        assert data['issue_count'] == 0
        assert data['issues'] == []

    def test_suggested_tags_default_empty(self) -> None:
        report = _make_report()
        output = format_json_report(report)
        data = json.loads(output)
        assert data['suggested_maintenance_tags'] == []
        assert data['added_maintenance_tags'] == []

    def test_dry_run_flag(self) -> None:
        report = _make_report()
        output = format_json_report(report, dry_run=True)
        data = json.loads(output)
        assert data['dry_run'] is True

    def test_output_file_param(self, tmp_path) -> None:
        report = _make_report()
        out = str(tmp_path / 'out.json')
        output = format_json_report(report, output_file=out)
        data = json.loads(output)
        assert data['output_file'] == out

    def test_issue_fields_in_json(self) -> None:
        report = _make_report(n_issues=1)
        output = format_json_report(report)
        data = json.loads(output)
        issue = data['issues'][0]
        assert issue['check_id'] == 'check-0'
        assert issue['severity'] == 'medium'
        assert issue['section'] == 'global'
        assert issue['message'] == 'msg 0'
        assert issue['evidence'] == 'ev 0'
        assert issue['suggestion'] == 'fix 0'

    def test_added_tags(self) -> None:
        report = _make_report()
        output = format_json_report(report, added_tags=['Stub'])
        data = json.loads(output)
        assert data['added_maintenance_tags'] == ['Stub']


# ---------------------------------------------------------------------------
# format_html_report
# ---------------------------------------------------------------------------

class TestFormatHtmlReport:
    def test_contains_title(self) -> None:
        report = _make_report(n_issues=0)
        html = format_html_report(report)
        assert '<title>MOS Audit: Test Article</title>' in html
        assert '<h1>MOS Audit: Test Article</h1>' in html

    def test_contains_score_bar(self) -> None:
        report = _make_report(n_issues=0, score=85)
        html = format_html_report(report)
        assert 'score-bar' in html
        assert 'score-fill' in html
        assert '85/100' in html

    def test_contains_issue_table(self) -> None:
        report = _make_report(n_issues=1)
        html = format_html_report(report)
        assert '<table>' in html
        assert '<thead>' in html
        assert 'Severity' in html
        assert 'check-0' in html

    def test_no_issues_message(self) -> None:
        report = _make_report(n_issues=0)
        html = format_html_report(report)
        assert 'No issues detected.' in html

    def test_severity_color_high(self) -> None:
        issue = _make_issue(severity='high')
        report = AuditReport(title='T', score=50, issues=[issue])
        html = format_html_report(report)
        assert '#dc3545' in html
        assert 'HIGH' in html

    def test_severity_color_medium(self) -> None:
        issue = _make_issue(severity='medium')
        report = AuditReport(title='T', score=60, issues=[issue])
        html = format_html_report(report)
        assert '#fd7e14' in html
        assert 'MEDIUM' in html

    def test_severity_color_low(self) -> None:
        issue = _make_issue(severity='low')
        report = AuditReport(title='T', score=90, issues=[issue])
        html = format_html_report(report)
        assert '#ffc107' in html
        assert 'LOW' in html

    def test_unknown_severity_fallback_color(self) -> None:
        issue = _make_issue(severity='info')
        report = AuditReport(title='T', score=90, issues=[issue])
        html = format_html_report(report)
        assert '#6c757d' in html

    def test_html_escaping_in_title(self) -> None:
        report = _make_report(title='<script>alert("xss")</script>')
        html = format_html_report(report)
        assert '<script>' not in html
        assert '&lt;script&gt;' in html

    def test_html_escaping_in_issue_fields(self) -> None:
        issue = Issue(
            check_id='ck',
            severity='low',
            section='s',
            message='<b>bold</b>',
            evidence='a & b',
            suggestion='use "quotes"',
        )
        report = AuditReport(title='T', score=90, issues=[issue])
        html = format_html_report(report)
        assert '&lt;b&gt;bold&lt;/b&gt;' in html
        assert 'a &amp; b' in html
        assert '&quot;quotes&quot;' in html

    def test_score_bar_green_high(self) -> None:
        report = _make_report(score=80)
        html = format_html_report(report)
        assert '#28a745' in html

    def test_score_bar_orange_mid(self) -> None:
        report = _make_report(score=65)
        html = format_html_report(report)
        assert '#fd7e14' in html

    def test_score_bar_red_low(self) -> None:
        report = _make_report(score=30)
        html = format_html_report(report)
        assert '#dc3545' in html

    def test_valid_html_structure(self) -> None:
        report = _make_report(n_issues=1)
        html = format_html_report(report)
        assert html.startswith('<!DOCTYPE html>')
        assert '</html>' in html
        assert '<body>' in html
        assert '</body>' in html

    def test_issue_count_displayed(self) -> None:
        report = _make_report(n_issues=3)
        html = format_html_report(report)
        assert '3 issue(s) found.' in html


# ---------------------------------------------------------------------------
# format_batch_summary
# ---------------------------------------------------------------------------

class TestFormatBatchSummary:
    def test_text_format(self) -> None:
        reports = [_make_report(n_issues=1, title='A', score=80), _make_report(n_issues=2, title='B', score=60)]
        text = format_batch_summary(reports, format='text')
        assert 'MOS Audit Batch Summary' in text
        assert 'A' in text
        assert 'B' in text
        assert '80' in text
        assert '60' in text

    def test_text_average_score(self) -> None:
        reports = [_make_report(score=80), _make_report(score=60)]
        text = format_batch_summary(reports, format='text')
        assert 'Average' in text
        # (80+60)/2 = 70
        assert '70' in text

    def test_text_long_title_truncated(self) -> None:
        long_title = 'A' * 50
        reports = [_make_report(title=long_title)]
        text = format_batch_summary(reports, format='text')
        assert '..' in text

    def test_json_format(self) -> None:
        reports = [_make_report(n_issues=1, title='A', score=90)]
        output = format_batch_summary(reports, format='json')
        data = json.loads(output)
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]['title'] == 'A'
        assert data[0]['score'] == 90
        assert data[0]['issue_count'] == 1

    def test_json_multiple_reports(self) -> None:
        reports = [_make_report(title='X'), _make_report(title='Y')]
        output = format_batch_summary(reports, format='json')
        data = json.loads(output)
        assert len(data) == 2

    def test_html_format(self) -> None:
        reports = [_make_report(n_issues=1, title='A', score=90)]
        html = format_batch_summary(reports, format='html')
        assert '<!DOCTYPE html>' in html
        assert 'MOS Audit Batch Summary' in html
        assert '<table>' in html
        assert 'A' in html

    def test_html_escaping_in_batch(self) -> None:
        reports = [_make_report(title='<b>Test</b>')]
        html = format_batch_summary(reports, format='html')
        assert '&lt;b&gt;Test&lt;/b&gt;' in html

    def test_empty_reports_text(self) -> None:
        text = format_batch_summary([], format='text')
        assert 'Average' in text

    def test_default_is_text(self) -> None:
        reports = [_make_report()]
        text = format_batch_summary(reports)
        assert 'MOS Audit Batch Summary' in text


# ---------------------------------------------------------------------------
# _html_escape
# ---------------------------------------------------------------------------

class TestHtmlEscape:
    def test_ampersand(self) -> None:
        assert _html_escape('a & b') == 'a &amp; b'

    def test_less_than(self) -> None:
        assert _html_escape('a < b') == 'a &lt; b'

    def test_greater_than(self) -> None:
        assert _html_escape('a > b') == 'a &gt; b'

    def test_double_quote(self) -> None:
        assert _html_escape('a "b" c') == 'a &quot;b&quot; c'

    def test_all_special_chars(self) -> None:
        assert _html_escape('&<>"') == '&amp;&lt;&gt;&quot;'

    def test_no_special_chars(self) -> None:
        assert _html_escape('plain text') == 'plain text'

    def test_empty_string(self) -> None:
        assert _html_escape('') == ''

    def test_ampersand_first(self) -> None:
        # Ampersand must be replaced first to avoid double-escaping
        assert _html_escape('&lt;') == '&amp;lt;'
