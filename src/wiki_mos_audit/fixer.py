"""Auto-fix module for wiki-mos-audit. Handles safe, mechanical corrections only."""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class FixResult:
    """Result of an auto-fix pass."""
    wikitext: str
    fixes_applied: list[str]


def fix_all(wikitext: str) -> FixResult:
    """Apply all safe auto-fixes and return the result."""
    fixes: list[str] = []

    wikitext, n = fix_bare_ref_urls(wikitext)
    if n:
        fixes.append(f'Wrapped {n} bare ref URL(s) in {{{{cite web}}}}')

    wikitext, n = fix_whitespace(wikitext)
    if n:
        fixes.append(f'Fixed {n} whitespace issue(s)')

    wikitext, n = fix_heading_caps(wikitext)
    if n:
        fixes.append(f'Fixed {n} heading capitalization issue(s)')

    wikitext, n = fix_http_to_https(wikitext)
    if n:
        fixes.append(f'Upgraded {n} http:// URL(s) to https://')

    return FixResult(wikitext=wikitext, fixes_applied=fixes)


def fix_bare_ref_urls(wikitext: str) -> tuple[str, int]:
    """Wrap bare URLs in <ref> tags with {{cite web}} stubs."""
    pattern = re.compile(r'(<ref[^>]*>)(https?://[^\s<]+)(</ref>)', flags=re.IGNORECASE)
    count = 0

    def replacer(m: re.Match) -> str:
        nonlocal count
        count += 1
        url = m.group(2)
        return f'{m.group(1)}{{{{cite web |url={url} |title= |access-date=}}}}{m.group(3)}'

    result = pattern.sub(replacer, wikitext)
    return result, count


def fix_whitespace(wikitext: str) -> tuple[str, int]:
    """Fix common whitespace issues."""
    count = 0

    # trailing whitespace on lines
    lines = wikitext.split('\n')
    new_lines = []
    for line in lines:
        stripped = line.rstrip()
        if stripped != line:
            count += 1
        new_lines.append(stripped)
    result = '\n'.join(new_lines)

    # multiple blank lines -> double
    new_result = re.sub(r'\n{3,}', '\n\n', result)
    if new_result != result:
        count += 1
        result = new_result

    return result, count


def fix_heading_caps(wikitext: str) -> tuple[str, int]:
    """Fix Title Case headings to sentence case (per MOS:HEAD)."""
    _TITLE_CASE_RE = re.compile(r'^(={2,})\s*(.+?)\s*(={2,})\s*$', re.MULTILINE)
    count = 0

    def to_sentence_case(m: re.Match) -> str:
        nonlocal count
        open_eq = m.group(1)
        heading = m.group(2)
        close_eq = m.group(3)

        words = heading.split()
        if len(words) < 2:
            return m.group(0)

        # Check if it looks like Title Case (most words capitalized)
        cap_count = sum(1 for w in words if w[0].isupper() and w not in ('I', 'II', 'III', 'IV', 'V'))
        if cap_count < len(words) * 0.7:
            return m.group(0)  # not Title Case

        # Skip if it contains proper nouns (wikilinks, template references)
        if '[[' in heading or '{{' in heading:
            return m.group(0)

        # Convert: keep first word capitalized, lowercase the rest unless they look like proper nouns
        new_words = [words[0]]
        for word in words[1:]:
            # Keep capitalized if it looks like a proper noun (single caps, abbreviation, etc.)
            if len(word) <= 2 or word.isupper() or not word[0].isupper():
                new_words.append(word)
            else:
                new_words.append(word[0].lower() + word[1:])

        new_heading = ' '.join(new_words)
        if new_heading != heading:
            count += 1
            return f'{open_eq} {new_heading} {close_eq}'
        return m.group(0)

    result = _TITLE_CASE_RE.sub(to_sentence_case, wikitext)
    return result, count


def fix_http_to_https(wikitext: str) -> tuple[str, int]:
    """Upgrade http:// URLs to https:// in citation templates."""
    # Only fix URLs inside citation templates, not in body text
    pattern = re.compile(
        r'(\|\s*(?:url|archive-url|chapter-url)\s*=\s*)http://',
        flags=re.IGNORECASE,
    )
    result, count = pattern.subn(r'\1https://', wikitext)
    return result, count
