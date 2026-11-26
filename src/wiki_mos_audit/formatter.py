# SPDX-FileCopyrightText: 2026 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT

"""Output formatters for wiki-mos-audit reports."""
from __future__ import annotations

import json
from dataclasses import asdict

from wiki_mos_audit.i18n import get_locale, t
from wiki_mos_audit.models import AuditReport


def format_json_report(
    report: AuditReport,
    suggested_tags: list[str] | None = None,
    added_tags: list[str] | None = None,
    dry_run: bool = False,
    output_file: str | None = None,
) -> str:
    """Format report as JSON string."""
    return json.dumps({
        'title': report.title,
        'score': report.score,
        'issue_count': len(report.issues),
        'issues': [asdict(issue) for issue in report.issues],
        'suggested_maintenance_tags': suggested_tags or [],
        'added_maintenance_tags': added_tags or [],
        'dry_run': dry_run,
        'output_file': output_file,
    }, indent=2)


def format_text_report(report: AuditReport) -> str:
    """Format report as plain text."""
    lines = [
        t('report.text_header', title=report.title),
        t('report.score', score=report.score),
        '',
    ]
    if not report.issues:
        lines.append(t('report.no_issues'))
        return '\n'.join(lines)

    for issue in report.issues:
        lines.append(f'- [{issue.severity}] {issue.check_id} ({issue.section})')
        lines.append(f'  {issue.message}')
        lines.append(f'  {t("report.evidence", evidence=issue.evidence)}')
        lines.append(f'  {t("report.fix", suggestion=issue.suggestion)}')
        lines.append('')

    return '\n'.join(lines).rstrip()


def format_html_report(report: AuditReport) -> str:
    """Format report as a self-contained HTML document."""
    severity_colors = {
        'high': '#dc3545',
        'medium': '#fd7e14',
        'low': '#ffc107',
    }

    issue_rows = []
    for issue in report.issues:
        color = severity_colors.get(issue.severity, '#6c757d')
        msg = _html_escape(issue.message)
        evidence = _html_escape(issue.evidence)
        suggestion = _html_escape(issue.suggestion)
        issue_rows.append(
            f'<tr>'
            f'<td><span style="color:{color};font-weight:bold">{issue.severity.upper()}</span></td>'
            f'<td><code>{issue.check_id}</code></td>'
            f'<td>{issue.section}</td>'
            f'<td>{msg}</td>'
            f'<td><small>{evidence}</small></td>'
            f'<td><small>{suggestion}</small></td>'
            f'</tr>'
        )

    no_issues_html = _html_escape(t('report.html_no_issues'))
    table_html = '\n'.join(issue_rows) if issue_rows else f'<tr><td colspan="6">{no_issues_html}</td></tr>'

    if report.score >= 80:
        bar_color = '#28a745'
    elif report.score >= 50:
        bar_color = '#fd7e14'
    else:
        bar_color = '#dc3545'

    css = (
        'body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;'
        'max-width:960px;margin:2em auto;padding:0 1em;color:#202122}'
        'h1{font-size:1.5em}'
        '.score-bar{background:#eee;border-radius:4px;overflow:hidden;height:24px;margin:1em 0}'
        f'.score-fill{{background:{bar_color};height:100%;line-height:24px;color:white;'
        f'text-align:center;font-size:.85em;font-weight:bold;width:{report.score}%}}'
        'table{border-collapse:collapse;width:100%;margin-top:1em;font-size:.9em}'
        'th,td{border:1px solid #c8ccd1;padding:6px 8px;text-align:left;vertical-align:top}'
        'th{background:#eaecf0}'
        'code{background:#f8f9fa;padding:1px 4px;border-radius:2px;font-size:.9em}'
    )

    page_title = _html_escape(t('report.html_title', title=report.title))
    issues_found = _html_escape(t('report.html_issues_found', count=len(report.issues)))
    footer_text = _html_escape(t('report.html_footer'))
    headers = ''.join(
        f'<th>{_html_escape(t(key))}</th>'
        for key in (
            'report.col_severity',
            'report.col_check',
            'report.col_section',
            'report.col_message',
            'report.col_evidence',
            'report.col_suggestion',
        )
    )

    return f'''<!DOCTYPE html>
<html lang="{get_locale()}">
<head>
<meta charset="utf-8">
<title>{page_title}</title>
<style>{css}</style>
</head>
<body>
<h1>{page_title}</h1>
<div class="score-bar"><div class="score-fill">{report.score}/100</div></div>
<p>{issues_found}</p>
<table>
<thead><tr>{headers}</tr></thead>
<tbody>
{table_html}
</tbody>
</table>
<footer><p><small>{footer_text}</small></p></footer>
</body>
</html>'''


def format_batch_summary(reports: list[AuditReport], format: str = 'text') -> str:
    """Format a summary of multiple audit reports."""
    if format == 'json':
        return json.dumps([
            {'title': r.title, 'score': r.score, 'issue_count': len(r.issues)}
            for r in reports
        ], indent=2)

    if format == 'html':
        rows = '\n'.join(
            f'<tr><td>{_html_escape(r.title)}</td><td>{r.score}</td><td>{len(r.issues)}</td></tr>'
            for r in reports
        )
        batch_css = (
            'body{font-family:sans-serif;max-width:800px;margin:2em auto}'
            'table{border-collapse:collapse;width:100%}'
            'th,td{border:1px solid #ccc;padding:6px 8px;text-align:left}'
            'th{background:#eaecf0}'
        )
        batch_title = _html_escape(t('report.batch_title'))
        batch_heading = _html_escape(t('report.batch_heading'))
        col_article = _html_escape(t('report.batch_col_article'))
        col_score = _html_escape(t('report.batch_col_score'))
        col_issues = _html_escape(t('report.batch_col_issues'))
        return f'''<!DOCTYPE html>
<html lang="{get_locale()}"><head><meta charset="utf-8"><title>{batch_title}</title>
<style>{batch_css}</style>
</head><body><h1>{batch_heading}</h1>
<table><thead><tr><th>{col_article}</th><th>{col_score}</th><th>{col_issues}</th></tr></thead>
<tbody>{rows}</tbody></table></body></html>'''

    # text format
    lines = [t('report.batch_heading'), '=' * 60, '']
    lines.append(
        f'{t("report.batch_col_article"):<40} {t("report.batch_col_score"):>5} {t("report.batch_col_issues"):>6}'
    )
    lines.append('-' * 60)
    for r in reports:
        truncated = r.title[:38] + '..' if len(r.title) > 40 else r.title
        lines.append(f'{truncated:<40} {r.score:>5} {len(r.issues):>6}')
    lines.append('-' * 60)
    avg = sum(r.score for r in reports) / len(reports) if reports else 0
    lines.append(f'{t("report.batch_average"):<40} {avg:>5.0f} {"":>6}')
    return '\n'.join(lines)


def _html_escape(text: str) -> str:
    """Escape HTML special characters."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
