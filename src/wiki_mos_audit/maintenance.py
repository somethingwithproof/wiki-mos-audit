"""Maintenance tag suggestion and insertion for wiki-mos-audit."""
from __future__ import annotations

import re
from datetime import UTC, datetime

from wiki_mos_audit.audit import normalize_template_name
from wiki_mos_audit.models import ISSUE_TO_MAINTENANCE_TAG, Issue

_MAINTENANCE_TAG_RE = re.compile(r'^[A-Za-z][A-Za-z0-9 _-]{0,79}$')


def parse_maintenance_tag_args(values: list[str] | None) -> list[str]:
    if not values:
        return []

    tags: list[str] = []
    for value in values:
        for tag in value.split(','):
            cleaned = tag.strip().strip('{}')
            if cleaned:
                if not _MAINTENANCE_TAG_RE.fullmatch(cleaned):
                    raise ValueError(f'Invalid maintenance tag: {cleaned!r}')
                tags.append(cleaned)

    return tags


def suggest_maintenance_tags(issues: list[Issue]) -> list[str]:
    suggestions: list[str] = []
    for issue in issues:
        tag = ISSUE_TO_MAINTENANCE_TAG.get(issue.check_id)
        if tag and tag not in suggestions:
            suggestions.append(tag)
    return suggestions


def find_lead_template_insertion_index(wikitext: str) -> int:
    """Walk past top-of-page templates and comments to find where prose starts."""
    index = 0
    length = len(wikitext)

    while index < length:
        while index < length and wikitext[index].isspace():
            index += 1

        if wikitext.startswith('<!--', index):
            end = wikitext.find('-->', index + 4)
            if end == -1:
                return length
            index = end + 3
            continue

        if wikitext.startswith('{{', index):
            depth = 0
            template_start = index
            closed = False
            while index < length - 1:
                if wikitext.startswith('{{', index):
                    depth += 1
                    index += 2
                    continue
                if wikitext.startswith('}}', index):
                    depth -= 1
                    index += 2
                    if depth <= 0:
                        closed = True
                        break
                    continue
                index += 1
            if not closed:
                return template_start
            continue

        break

    return index


def apply_maintenance_tags(
    wikitext: str,
    tags: list[str],
    existing_template_names: set[str],
    dry_run: bool = False,
) -> tuple[str, list[str]]:
    """Insert maintenance templates at the top of article text."""
    added_tags: list[str] = []
    for tag in tags:
        normalized = normalize_template_name(tag)
        if normalized not in existing_template_names and tag not in added_tags:
            added_tags.append(tag)

    if not added_tags or dry_run:
        return wikitext, added_tags

    date_stamp = datetime.now(UTC).strftime('%B %Y')
    tag_block = ''.join(f'{{{{{tag}|date={date_stamp}}}}}\n' for tag in added_tags)
    insert_at = find_lead_template_insertion_index(wikitext)
    prefix = wikitext[:insert_at]
    suffix = wikitext[insert_at:]
    if prefix and not prefix.endswith('\n'):
        prefix += '\n'

    return prefix + tag_block + suffix, added_tags
