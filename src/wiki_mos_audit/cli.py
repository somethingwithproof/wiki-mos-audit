# SPDX-FileCopyrightText: 2026 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT

"""CLI entry point for wiki-mos-audit."""
from __future__ import annotations

import argparse
import difflib
import json
import os
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
from wiki_mos_audit.i18n import set_locale, t
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
            raise ValueError(t('error.derive_title', target=target))
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


def _extract_lang(argv: list[str] | None) -> str | None:
    """Read --lang before argparse runs so --help uses the requested locale."""
    raw = sys.argv[1:] if argv is None else argv
    for idx, arg in enumerate(raw):
        if arg == '--lang' and idx + 1 < len(raw):
            return raw[idx + 1]
        if arg.startswith('--lang='):
            return arg.split('=', 1)[1]
    return None


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    set_locale(_extract_lang(argv))
    parser = argparse.ArgumentParser(description=t('cli.description'))
    parser.add_argument('target', nargs='?', help=t('cli.target_help'))
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')
    parser.add_argument('--language', default=None, help=t('cli.language_help'))
    parser.add_argument('--lang', dest='ui_lang', default=None, help=t('cli.lang_help'))
    parser.add_argument('--wikitext-file', help=t('cli.wikitext_file_help'))
    parser.add_argument('--dir', help=t('cli.dir_help'))
    parser.add_argument(
        '--format', choices=('text', 'json', 'html'), default=None,
        help=t('cli.format_help'),
    )
    parser.add_argument('--json', action='store_true', help=t('cli.json_help'))
    parser.add_argument('--diff', action='store_true', help=t('cli.diff_help'))
    parser.add_argument('--fix', action='store_true', help=t('cli.fix_help'))
    parser.add_argument(
        '--add-maintenance-tags', action='store_true',
        help=t('cli.add_maintenance_tags_help'),
    )
    parser.add_argument(
        '--maintenance-tag', action='append',
        help=t('cli.maintenance_tag_help'),
    )
    parser.add_argument('--output-wikitext-file', help=t('cli.output_wikitext_file_help'))
    parser.add_argument('--dry-run', action='store_true', help=t('cli.dry_run_help'))
    parser.add_argument(
        '--skip-api-checks', '--offline', dest='offline', action='store_true',
        help=t('cli.offline_help'),
    )
    parser.add_argument('--check-urls', action='store_true', help=t('cli.check_urls_help'))
    parser.add_argument('--check-orphan', action='store_true', help=t('cli.check_orphan_help'))
    parser.add_argument(
        '--check-backlinks', action='store_true',
        help=t('cli.check_backlinks_help'),
    )
    parser.add_argument('--config', help=t('cli.config_help'))

    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('--verbose', '-v', action='store_true', help=t('cli.verbose_help'))
    verbosity.add_argument('--quiet', '-q', action='store_true', help=t('cli.quiet_help'))

    parsed = parser.parse_args(argv)
    set_locale(parsed.ui_lang)
    return parsed


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


def _write_within(path: Path, root: Path, text: str) -> bool:
    """Write text to path under root, or return False without writing.

    A symlink placed in the scanned directory otherwise lets --fix write
    outside the tree the operator pointed at. Validating the path and writing
    it are two steps, so the leaf is opened relative to the scan root with
    O_NOFOLLOW: swapping it for a symlink after the check still fails. The
    scan is one level deep, so the leaf is the only component that can move.
    """
    safe_root = root.resolve()
    try:
        relative = path.resolve().relative_to(safe_root)
    except ValueError:
        return False
    if len(relative.parts) != 1:
        return False

    # O_DIRECTORY | O_NOFOLLOW: the root is already resolved, so it must still
    # be a real directory here; a symlink swapped in after the check is refused.
    dir_fd = os.open(safe_root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        fd = os.open(
            relative.parts[0],
            os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW,
            0o644,
            dir_fd=dir_fd,
        )
    finally:
        os.close(dir_fd)
    with os.fdopen(fd, 'w', encoding='utf-8') as handle:
        handle.write(text)
    return True


def _run_batch(args: argparse.Namespace, config: AuditConfig | None = None) -> int:
    """Scan a directory of wikitext files."""
    scan_dir = Path(args.dir)
    if not scan_dir.is_dir():
        print(t('error.not_a_directory', path=args.dir), file=sys.stderr)
        return 1

    files = sorted(
        list(scan_dir.glob('*-corrected.txt'))
        + list(scan_dir.glob('*.wiki'))
        + list(scan_dir.glob('*_corrected.txt'))
    )
    if not files:
        print(t('error.no_files_found', path=args.dir), file=sys.stderr)
        return 1

    reports: list[AuditReport] = []
    api_client: WikipediaApiClient | None = None
    if not args.offline:
        try:
            api_client = WikipediaApiClient(language=args.language)
        except (ValueError, OSError) as exc:
            if args.verbose:
                print(t('note.api_disabled_batch', error=exc), file=sys.stderr)

    processed_files = 0
    for filepath in files:
        try:
            wikitext = filepath.read_text(encoding='utf-8')
        except UnicodeDecodeError as exc:
            print(t('warn.skipping_not_utf8', name=filepath.name, error=exc), file=sys.stderr)
            continue
        except OSError as exc:
            print(t('warn.skipping_file', name=filepath.name, error=exc), file=sys.stderr)
            continue

        processed_files += 1
        title = title_from_filename(filepath)
        report, fixed_wikitext = _audit_single(title, wikitext, args, api_client, config=config)
        reports.append(report)

        if args.fix and fixed_wikitext != wikitext:
            try:
                written = _write_within(filepath, scan_dir, fixed_wikitext)
            except OSError as exc:
                print(t('warn.could_not_write_fixes', name=filepath.name, error=exc), file=sys.stderr)
            else:
                if not written:
                    print(
                        t('warn.refusing_write_outside', name=filepath.name, dir=args.dir),
                        file=sys.stderr,
                    )
                    continue
                if args.verbose:
                    print(f'fixed: {filepath.name}', file=sys.stderr)

    if processed_files == 0:
        print(t('error.no_readable_utf8', path=args.dir), file=sys.stderr)
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
        print(t('error.target_required'), file=sys.stderr)
        return 2

    try:
        title = title_from_target(args.target)
    except ValueError as exc:
        print(t('error.generic', error=exc), file=sys.stderr)
        return 1

    api_client: WikipediaApiClient | None = None
    try:
        if args.wikitext_file:
            wikitext = Path(args.wikitext_file).read_text(encoding='utf-8')
            if args.verbose:
                print(t('note.reading_local_file'), file=sys.stderr)
        else:
            api_client = WikipediaApiClient(language=args.language)
            wikitext = api_client.fetch_wikitext(title=title)
    except (ValueError, urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
        print(t('error.generic', error=exc), file=sys.stderr)
        return 1

    # create API client for red-link/disambiguation checks even with --wikitext-file
    if args.wikitext_file and not args.offline and api_client is None:
        try:
            api_client = WikipediaApiClient(language=args.language)
        except (ValueError, OSError):
            if args.verbose:
                print(t('note.skipping_api_checks'), file=sys.stderr)

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
                print(t('status.no_diff'))
        except Exception as exc:
            print(t('warn.diff_unavailable', error=exc), file=sys.stderr)

    if args.fix and not args.output_wikitext_file:
        print(t('warn.fix_without_output'), file=sys.stderr)

    report, wikitext = _audit_single(title, wikitext, args, api_client, config=config)

    auto_tags = suggest_maintenance_tags(report.issues) if args.add_maintenance_tags else []
    try:
        manual_tags = parse_maintenance_tag_args(args.maintenance_tag)
    except ValueError as exc:
        print(t('error.generic', error=exc), file=sys.stderr)
        return 1

    tag_requests = auto_tags + manual_tags
    _, added_tags = apply_maintenance_tags(
        wikitext=wikitext,
        tags=tag_requests,
        existing_template_names=template_names_from_wikitext(wikitext),
        dry_run=True,
    )

    if tag_requests and not args.dry_run and not args.output_wikitext_file:
        print(t('error.output_required_for_tags'), file=sys.stderr)
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
            tag_text = ', '.join(added_tags) if added_tags else t('status.none')
            tag_key = 'status.maintenance_tags_would_add' if args.dry_run else 'status.maintenance_tags_added'
            text_report = f'{text_report}\n\n{t(tag_key, tags=tag_text)}'
            if args.output_wikitext_file and not args.dry_run:
                text_report = f'{text_report}\n{t("status.wikitext_written", path=args.output_wikitext_file)}'

        print(text_report)

    return 0
