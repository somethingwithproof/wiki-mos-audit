"""CLI entry point for wiki-mos-audit."""
from __future__ import annotations

import argparse
import difflib
import json
import sys
import urllib.error
import urllib.parse
from pathlib import Path

from wiki_mos_audit.api import WikipediaApiClient
from wiki_mos_audit.audit import audit_mos, template_names_from_wikitext
from wiki_mos_audit.config import AuditConfig, load_config
from wiki_mos_audit.formatter import (
    format_batch_summary,
    format_html_report,
    format_json_report,
    format_text_report,
)
from wiki_mos_audit.maintenance import (
    apply_maintenance_tags,
    parse_maintenance_tag_args,
    suggest_maintenance_tags,
)
from wiki_mos_audit.models import VERSION, AuditReport


def title_from_target(target: str) -> str:
    """Normalize a URL or bare title to a MediaWiki article title."""
    if target.startswith('http://') or target.startswith('https://'):
        parsed = urllib.parse.urlparse(target)
        path = parsed.path
        if '/wiki/' in path:
            title = path.split('/wiki/', 1)[1]
        else:
            query = urllib.parse.parse_qs(parsed.query)
            title = query.get('title', [''])[0]
        if not title:
            raise ValueError(f'Could not derive title from URL: {target}')
        return urllib.parse.unquote(title).replace('_', ' ')

    return target.replace('_', ' ')


def title_from_filename(path: Path) -> str:
    """Derive article title from filename conventions."""
    name = path.stem
    for suffix in ('-corrected', '-original', '-live', '_corrected', '_original', '_live'):
        if name.endswith(suffix):
            name = name[:len(name) - len(suffix)]
            break
    return name.replace('_', ' ')


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='First-pass MOS auditor for Wikipedia pages.')
    parser.add_argument('target', nargs='?', help='Wikipedia URL or article title.')
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')
    parser.add_argument('--language', default=None, help='Wikipedia language code (default: en).')
    parser.add_argument('--wikitext-file', help='Read wikitext from local file instead of API.')
    parser.add_argument('--dir', help='Scan all *-corrected.txt and *.wiki files in a directory.')
    parser.add_argument(
        '--format', choices=('text', 'json', 'html'), default=None,
        help='Output format (default: text).',
    )
    parser.add_argument('--json', action='store_true', help='Output JSON (shorthand for --format json).')
    parser.add_argument('--diff', action='store_true', help='Show diff between live and local wikitext.')
    parser.add_argument('--fix', action='store_true', help='Auto-fix safe mechanical issues.')
    parser.add_argument(
        '--add-maintenance-tags', action='store_true',
        help='Insert suggested maintenance templates from detected issues.',
    )
    parser.add_argument(
        '--maintenance-tag', action='append',
        help='Additional maintenance tag(s); comma-separated or repeatable.',
    )
    parser.add_argument('--output-wikitext-file', help='Write updated wikitext to this file.')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing.')
    parser.add_argument(
        '--skip-api-checks', '--offline', dest='offline', action='store_true',
        help='Skip red-link and category existence checks.',
    )
    parser.add_argument('--check-urls', action='store_true', help='HEAD-check cited URLs for dead links (slow).')
    parser.add_argument('--check-orphan', action='store_true', help='Check if article has incoming wikilinks.')
    parser.add_argument(
        '--check-backlinks', action='store_true',
        help='Find articles that mention but do not link here.',
    )
    parser.add_argument('--config', help='Path to .wiki-mos-audit.toml config file.')

    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('--verbose', '-v', action='store_true', help='Print which checks are running to stderr.')
    verbosity.add_argument('--quiet', '-q', action='store_true', help='Suppress non-error output; exit code only.')

    return parser.parse_args(argv)


def _audit_single(
    title: str,
    wikitext: str,
    args: argparse.Namespace,
    api_client: WikipediaApiClient | None,
    config: AuditConfig | None = None,
) -> tuple[AuditReport, str]:
    """Run audit on a single article. Returns (report, possibly-fixed wikitext)."""
    effective_client = None if args.offline else api_client

    report = audit_mos(
        title, wikitext,
        verbose=args.verbose,
        client=effective_client,
        check_urls=args.check_urls,
        check_orphan=args.check_orphan,
        check_backlinks=args.check_backlinks,
        config=config,
    )

    if args.fix:
        from wiki_mos_audit.fixer import fix_all
        result = fix_all(wikitext)
        wikitext = result.wikitext
        if result.fixes_applied and args.verbose:
            for fix_msg in result.fixes_applied:
                print(f'fix: {fix_msg}', file=sys.stderr)

    return report, wikitext


def _run_batch(args: argparse.Namespace, config: AuditConfig | None = None) -> int:
    """Scan a directory of wikitext files."""
    scan_dir = Path(args.dir)
    if not scan_dir.is_dir():
        print(f'Error: {args.dir} is not a directory.', file=sys.stderr)
        return 1

    files = sorted(
        list(scan_dir.glob('*-corrected.txt'))
        + list(scan_dir.glob('*.wiki'))
        + list(scan_dir.glob('*_corrected.txt'))
    )
    if not files:
        print(f'No *-corrected.txt or *.wiki files found in {args.dir}', file=sys.stderr)
        return 1

    reports: list[AuditReport] = []
    api_client: WikipediaApiClient | None = None
    if not args.offline:
        try:
            api_client = WikipediaApiClient(language=args.language)
        except (ValueError, OSError) as exc:
            if args.verbose:
                print(f'note: API checks disabled in batch mode: {exc}', file=sys.stderr)

    processed_files = 0
    for filepath in files:
        try:
            wikitext = filepath.read_text(encoding='utf-8')
        except UnicodeDecodeError as exc:
            print(f'Warning: skipping {filepath.name} (not UTF-8): {exc}', file=sys.stderr)
            continue
        except OSError as exc:
            print(f'Warning: skipping {filepath.name}: {exc}', file=sys.stderr)
            continue

        processed_files += 1
        title = title_from_filename(filepath)
        report, fixed_wikitext = _audit_single(title, wikitext, args, api_client, config=config)
        reports.append(report)

        if args.fix and fixed_wikitext != wikitext:
            try:
                filepath.write_text(fixed_wikitext, encoding='utf-8')
            except OSError as exc:
                print(f'Warning: could not write fixes to {filepath.name}: {exc}', file=sys.stderr)
            else:
                if args.verbose:
                    print(f'fixed: {filepath.name}', file=sys.stderr)

    if processed_files == 0:
        print(f'Error: no readable UTF-8 wikitext files found in {args.dir}', file=sys.stderr)
        return 1

    if args.quiet:
        return 0

    output_format = args.format or ('json' if args.json else 'text')
    print(format_batch_summary(reports, format=output_format))
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    # load config and apply defaults
    config_path = Path(args.config) if args.config else None
    config = load_config(config_path)
    if args.language is None:
        args.language = config.language
    if config.check_urls and not args.check_urls:
        args.check_urls = True
    if config.check_orphan and not args.check_orphan:
        args.check_orphan = True
    if config.check_backlinks and not args.check_backlinks:
        args.check_backlinks = True

    # batch mode
    if args.dir:
        return _run_batch(args, config=config)

    if args.target is None:
        print('Error: target is required (or use --dir for batch mode).', file=sys.stderr)
        return 2

    try:
        title = title_from_target(args.target)
    except ValueError as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1

    api_client: WikipediaApiClient | None = None
    try:
        if args.wikitext_file:
            wikitext = Path(args.wikitext_file).read_text(encoding='utf-8')
            if args.verbose:
                print('note: --wikitext-file supplied; reading from local file', file=sys.stderr)
        else:
            api_client = WikipediaApiClient(language=args.language)
            wikitext = api_client.fetch_wikitext(title=title)
    except (ValueError, urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1

    # create API client for red-link/disambiguation checks even with --wikitext-file
    if args.wikitext_file and not args.offline and api_client is None:
        try:
            api_client = WikipediaApiClient(language=args.language)
        except (ValueError, OSError):
            if args.verbose:
                print('note: could not create API client; skipping API-based checks', file=sys.stderr)

    # diff mode: compare local file against live
    if args.diff and args.wikitext_file:
        try:
            live_client = api_client or WikipediaApiClient(language=args.language)
            live_wikitext = live_client.fetch_wikitext(title=title)
            diff = difflib.unified_diff(
                live_wikitext.splitlines(keepends=True),
                wikitext.splitlines(keepends=True),
                fromfile=f'{title} (live)',
                tofile=f'{title} (local)',
            )
            diff_text = ''.join(diff)
            if diff_text:
                print(diff_text)
            else:
                print('No differences between live and local wikitext.')
        except Exception as exc:
            print(f'Warning: diff unavailable: {exc}', file=sys.stderr)

    if args.fix and not args.output_wikitext_file:
        print('Warning: --fix without --output-wikitext-file; fixes will not be saved.', file=sys.stderr)

    report, wikitext = _audit_single(title, wikitext, args, api_client, config=config)

    auto_tags = suggest_maintenance_tags(report.issues) if args.add_maintenance_tags else []
    try:
        manual_tags = parse_maintenance_tag_args(args.maintenance_tag)
    except ValueError as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1

    tag_requests = auto_tags + manual_tags
    _, added_tags = apply_maintenance_tags(
        wikitext=wikitext,
        tags=tag_requests,
        existing_template_names=template_names_from_wikitext(wikitext),
        dry_run=True,
    )

    if tag_requests and not args.dry_run and not args.output_wikitext_file:
        print('Error: --output-wikitext-file is required when adding tags without --dry-run.', file=sys.stderr)
        return 2

    if tag_requests and not args.dry_run and args.output_wikitext_file:
        updated_wikitext, applied_tags = apply_maintenance_tags(
            wikitext=wikitext,
            tags=tag_requests,
            existing_template_names=template_names_from_wikitext(wikitext),
            dry_run=False,
        )
        Path(args.output_wikitext_file).write_text(updated_wikitext, encoding='utf-8')
        added_tags = applied_tags

    # write fixed wikitext if --fix + --output-wikitext-file
    if args.fix and args.output_wikitext_file and not tag_requests:
        Path(args.output_wikitext_file).write_text(wikitext, encoding='utf-8')

    if args.quiet:
        return 0

    output_format = args.format or ('json' if args.json else 'text')
    if output_format == 'json':
        output_path = args.output_wikitext_file if (args.output_wikitext_file and not args.dry_run) else None
        print(format_json_report(
            report,
            suggested_tags=auto_tags,
            added_tags=added_tags,
            dry_run=args.dry_run,
            output_file=output_path,
        ))
    elif output_format == 'html':
        print(format_html_report(report))
    else:
        text_report = format_text_report(report)
        if tag_requests:
            mode_text = 'would add' if args.dry_run else 'added'
            tag_text = ', '.join(added_tags) if added_tags else 'none'
            text_report = f'{text_report}\n\nMaintenance tags {mode_text}: {tag_text}'
            if args.output_wikitext_file and not args.dry_run:
                text_report = f'{text_report}\nWikitext written to: {args.output_wikitext_file}'

        print(text_report)

    return 0
