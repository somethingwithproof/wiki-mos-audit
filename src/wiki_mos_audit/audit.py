"""Core MOS audit logic for wiki-mos-audit."""
from __future__ import annotations

import ipaddress
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Iterable

from wiki_mos_audit.api import WikipediaApiClient
from wiki_mos_audit.config import AuditConfig, severity_meets_minimum
from wiki_mos_audit.models import (
    COMMON_INFOBOX_REQUIREMENTS,
    INDIGENOUS_FLAG_TERMS,
    MAINTENANCE_TEMPLATES,
    MONTHS,
    PEACOCK_TERMS,
    RELATIVE_TIME_TERMS,
    SEVERITY_WEIGHTS,
    SISTER_PROJECT_LINK_PATTERN,
    SISTER_PROJECT_TEMPLATES,
    USER_AGENT,
    WEASEL_TERMS,
    AuditReport,
    Issue,
)

try:
    import mwparserfromhell  # type: ignore
except ImportError:  # pragma: no cover
    mwparserfromhell = None

# pythoncoder and asilvering both caught these -- never again
AI_OVERATTRIBUTION_RE = re.compile(
    r'\b[Aa]n?\s+\d{4}\s+'
    r'(?:article|profile|piece|report|study|review|survey|feature|interview|book|paper|investigation)\s+'
    r'(?:in|by|from|for|published\s+(?:in|by))\s+'
    r'(?:the\s+)?[A-Z]',
)

ESSAY_TONE_PHRASES = (
    'it is worth noting',
    'it should be noted',
    'it is important to note',
    'one can argue',
    'it should be mentioned',
    'it is interesting to note',
    'it bears mentioning',
    'it is significant that',
    'this demonstrates that',
    'this illustrates',
    'this highlights',
    'this underscores',
    'played a significant role',
    'played a crucial role',
    'played a pivotal role',
    'made significant contributions',
    'left a lasting legacy',
    'left an indelible mark',
    'remains a testament',
    'continues to be remembered',
)

ISBN_PARAM_RE = re.compile(r'\|\s*isbn\s*=\s*([^|}\n]+)', re.IGNORECASE)
URL_PARAM_RE = re.compile(r'\|\s*(?:url|archive-url|chapter-url)\s*=\s*([^|}\n]+)', re.IGNORECASE)
SHORT_DESC_RE = re.compile(r'\{\{[Ss]hort description\|([^}]+)\}\}')


def _isbn10_valid(digits: str) -> bool:
    if len(digits) != 10:
        return False
    # guard against unexpected characters
    if not (digits[:9].isdigit() and (digits[9].isdigit() or digits[9] == 'X')):
        return False
    total = sum((10 - i) * (10 if c == 'X' else int(c)) for i, c in enumerate(digits))
    return total % 11 == 0


def _isbn13_valid(digits: str) -> bool:
    if len(digits) != 13 or not digits.isdigit():
        return False
    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits))
    return total % 10 == 0


def strip_markup(text: str) -> str:
    """Approximately plain text -- good enough for style checks, not for display."""
    if mwparserfromhell is not None:
        return mwparserfromhell.parse(text).strip_code(normalize=True, collapse=True)

    text = re.sub(r'<ref[^>]*>.*?</ref>', ' ', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    # loop to handle nested templates
    for _ in range(10):  # max 10 nesting levels, enough for any sane wikitext
        new_text = re.sub(r'\{\{[^{}]*\}\}', ' ', text)
        if new_text == text:
            break
        text = new_text
    text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', text)
    return re.sub(r'\s+', ' ', text).strip()


def extract_lead_wikitext(wikitext: str) -> str:
    # find nowiki spans to avoid matching headings inside them
    nowiki_spans = [(m.start(), m.end()) for m in re.finditer(r'<nowiki>.*?</nowiki>', wikitext, flags=re.DOTALL)]
    for match in re.finditer(r'\n==[^=].*?==\s*\n', wikitext):
        if not any(start <= match.start() < end for start, end in nowiki_spans):
            return wikitext[:match.start()]
    return wikitext


def find_date_formats(text: str) -> tuple[int, int]:
    # date formats: the DMY vs MDY holy war, now with regex
    month_group = '|'.join(MONTHS)
    dmy = len(re.findall(rf'\b\d{{1,2}}\s(?:{month_group})\s\d{{4}}\b', text))
    mdy = len(re.findall(rf'\b(?:{month_group})\s\d{{1,2}},\s\d{{4}}\b', text))
    return dmy, mdy


def find_phrases(text: str, phrases: Iterable[str]) -> list[str]:
    lower = text.lower()
    return sorted({phrase for phrase in phrases if phrase in lower})


def normalize_template_name(name: str) -> str:
    return re.sub(r'\s+', ' ', name.replace('_', ' ').strip().lower())


def _extract_wikilink_targets(wikitext: str, code: object | None = None) -> list[str]:
    """Extract and normalize wikilink targets, skipping namespaced/section-only links."""
    if code is not None:
        raw_targets: list[str] = []
        for wl in code.filter_wikilinks(recursive=True):
            t = str(wl.title).strip()
            if '#' in t:
                t = t.split('#', 1)[0].strip()
            if ':' in t or not t:
                continue
            normalized = t[0].upper() + t[1:] if t else t
            raw_targets.append(normalized)
        return list(dict.fromkeys(raw_targets))

    raw = re.findall(r'\[\[([^\]|#][^\]|]*?)(?:\|[^\]]+)?\]\]', wikitext)
    targets: list[str] = []
    for target in raw:
        t = target.strip()
        if '#' in t:
            t = t.split('#', 1)[0].strip()
        if ':' in t or not t:
            continue
        normalized = t[0].upper() + t[1:] if t else t
        targets.append(normalized)
    return list(dict.fromkeys(targets))


def _extract_category_names(wikitext: str, code: object | None = None) -> list[str]:
    """Extract category names from wikitext, stripping the Category: prefix."""
    if code is not None:
        names: list[str] = []
        for wl in code.filter_wikilinks(recursive=True):
            title = str(wl.title).strip()
            if title.lower().startswith('category:'):
                names.append(title[len('category:'):].strip())
        return names

    return [n.strip() for n in re.findall(r'\[\[Category:([^\]|]+)', wikitext, flags=re.IGNORECASE)]


_BOTTOM_MATTER_ORDER = (
    'works', 'publications', 'filmography', 'discography', 'bibliography',
    'see also', 'notes', 'footnotes', 'references', 'sources',
    'further reading', 'external links',
)


def _normalize_heading_text(heading: str) -> str:
    heading_plain = strip_markup(heading).strip()
    heading_plain = re.sub(r'^=+\s*', '', heading_plain)
    heading_plain = re.sub(r'\s*=+$', '', heading_plain)
    return heading_plain.strip()


def _is_public_http_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {'http', 'https'} or not parsed.hostname:
        return False

    hostname = parsed.hostname.strip('.').lower()
    if not hostname or hostname == 'localhost' or hostname.endswith(('.local', '.internal')):
        return False

    try:
        ip = ipaddress.ip_address(hostname)
    except ValueError:
        return True

    return not (
        ip.is_private
        or ip.is_loopback
        or ip.is_link_local
        or ip.is_multicast
        or ip.is_reserved
        or ip.is_unspecified
    )


def _check_url_liveness(urls: list[str], timeout: float = 5.0) -> list[str]:
    """HEAD-check URLs, return list of dead ones."""
    dead: list[str] = []
    for url in urls[:20]:  # cap at 20 to avoid abuse
        if not _is_public_http_url(url):
            dead.append(url)
            continue

        try:
            req = urllib.request.Request(url, method='HEAD',
                headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:  # nosec B310
                if resp.status >= 400:
                    dead.append(url)
        except urllib.error.HTTPError as e:
            if e.code == 405:
                # server rejects HEAD; retry with GET
                try:
                    req = urllib.request.Request(url, method='GET',
                        headers={'User-Agent': USER_AGENT})
                    with urllib.request.urlopen(req, timeout=timeout) as resp:  # nosec B310
                        if resp.status >= 400:
                            dead.append(url)
                except (TimeoutError, ValueError, urllib.error.HTTPError, urllib.error.URLError):
                    dead.append(url)
            else:
                dead.append(url)
        except (TimeoutError, ValueError, urllib.error.URLError):
            dead.append(url)
    return dead


def template_names_from_wikitext(wikitext: str, code: object | None = None) -> set[str]:
    if code is not None:
        return {
            normalize_template_name(str(template.name))
            for template in code.filter_templates(recursive=True)
        }

    return {
        normalize_template_name(match)
        for match in re.findall(r'\{\{\s*([^|}\n]+)', wikitext)
    }


def audit_mos(
    title: str,
    wikitext: str,
    verbose: bool = False,
    client: WikipediaApiClient | None = None,
    check_urls: bool = False,
    check_orphan: bool = False,
    check_backlinks: bool = False,
    config: AuditConfig | None = None,
) -> AuditReport:
    """Run first-pass MOS checks and return a scored report."""
    if config is None:
        config = AuditConfig()
    issues: list[Issue] = []
    code = mwparserfromhell.parse(wikitext) if mwparserfromhell is not None else None

    if code is not None:
        sections = code.get_sections(include_lead=True, include_headings=False)
        lead_raw = str(sections[0]) if sections else wikitext
    else:
        lead_raw = extract_lead_wikitext(wikitext)

    lead_text = strip_markup(lead_raw)
    full_text = strip_markup(wikitext)

    if mwparserfromhell is None:
        issues.append(Issue(
            check_id='ast-parser',
            severity='medium',
            section='global',
            message='AST parser unavailable.',
            evidence='mwparserfromhell is not installed.',
            suggestion='Install mwparserfromhell for stronger template/heading checks.',
        ))

    # if you're reading this, yes, 260 words is the threshold. fight me.
    if verbose:
        print('check: lead-length', file=sys.stderr)
    lead_words = len(re.findall(r"\b[\w'-]+\b", lead_text))
    lead_paragraphs = len([p for p in re.split(r'\n\s*\n', lead_raw) if p.strip()])
    if lead_words > config.max_lead_words or lead_paragraphs > config.max_lead_paragraphs:
        issues.append(Issue(
            check_id='lead-length',
            severity='medium',
            section='lead',
            message='Lead may be too detailed for MOS:LEAD.',
            evidence=f'Lead words={lead_words}, paragraphs={lead_paragraphs}.',
            suggestion='Trim to concise overview and move operational detail to body sections.',
        ))

    if verbose:
        print('check: weasel-terms', file=sys.stderr)
    weasel_matches = find_phrases(full_text, WEASEL_TERMS)
    if weasel_matches:
        issues.append(Issue(
            check_id='weasel-terms',
            severity='medium',
            section='global',
            message='Potential MOS:WEASEL wording found.',
            evidence=', '.join(weasel_matches),
            suggestion='Replace with direct attribution or precise statements.',
        ))

    if verbose:
        print('check: relative-time', file=sys.stderr)
    relative_time = find_phrases(full_text, RELATIVE_TIME_TERMS)
    if relative_time:
        issues.append(Issue(
            check_id='relative-time',
            severity='low',
            section='global',
            message='Relative-time wording may age poorly.',
            evidence=', '.join(relative_time),
            suggestion='Prefer explicit dates over relative phrasing.',
        ))

    if verbose:
        print('check: mos-indigenous-terms', file=sys.stderr)
    indigenous_matches = find_phrases(full_text, INDIGENOUS_FLAG_TERMS)
    if indigenous_matches:
        issues.append(Issue(
            check_id='mos-indigenous-terms',
            severity='medium',
            section='global',
            message='Potential MOS:INDIGENOUS terminology issues found.',
            evidence=', '.join(indigenous_matches),
            suggestion='Use precise, attributed, and community-preferred terminology.',
        ))

    if verbose:
        print('check: date-style-mix', file=sys.stderr)
    dmy_count, mdy_count = find_date_formats(full_text)
    if dmy_count > 0 and mdy_count > 0:
        issues.append(Issue(
            check_id='date-style-mix',
            severity='medium',
            section='global',
            message='Mixed date styles detected.',
            evidence=f'DMY={dmy_count}, MDY={mdy_count}.',
            suggestion='Standardize to one date format per MOS:DATEUNIFY.',
        ))

    if verbose:
        print('check: mos-aviation-style', file=sys.stderr)
    aviation_context = any(
        term in full_text.lower()
        for term in ('aircraft', 'aviation', 'airport', 'runway', 'squadron', 'airfield', 'bomber', 'fighter')
    )
    aviation_style_hits = sorted(set(
        re.findall(r'\b(?:F|B|C|A|P|E)-?\d{2,3}[A-Z]?\b', full_text)
        + re.findall(r'\b(?:Su|MiG|SU|MIG)-\d{1,3}\b', full_text)
    ))
    if aviation_context and aviation_style_hits:
        issues.append(Issue(
            check_id='mos-aviation-style',
            severity='low',
            section='global',
            message='Potential MOS:AVIATION aircraft designation formatting issues.',
            evidence=', '.join(aviation_style_hits[:12]),
            suggestion='Use standard designation style (for example, F-15, MiG-29, Su-35).',
        ))

    if verbose:
        print('check: quote-density', file=sys.stderr)
    if code is not None:
        quote_templates = sum(
            1 for t in code.filter_templates(recursive=True)
            if str(t.name).strip().lower() in {'quote', 'blockquote', 'quotation'}
        )
    else:
        quote_templates = len(re.findall(r'\{\{\s*(?:quote|blockquote|quotation)\b', wikitext, flags=re.IGNORECASE))
    if quote_templates >= config.quote_density_threshold:
        issues.append(Issue(
            check_id='quote-density',
            severity='low',
            section='global',
            message='High quote-template density.',
            evidence=f'quote templates={quote_templates}',
            suggestion='Summarize in prose and keep only essential direct quotations.',
        ))

    if verbose:
        print('check: timeline-structure', file=sys.stderr)
    if code is not None:
        daily_heading_count = sum(
            1 for h in code.filter_headings()
            if re.search(r'^\d{1,2}\s(?:' + '|'.join(MONTHS) + r')$', strip_markup(str(h.title)).strip())
        )
    else:
        daily_heading_count = len(re.findall(
            r'\n===?\s*\d{1,2}\s(?:' + '|'.join(MONTHS) + r')\s*===?\n', wikitext,
        ))
    if daily_heading_count >= 4:
        issues.append(Issue(
            check_id='timeline-structure',
            severity='low',
            section='structure',
            message='Many day-by-day headings can read like a liveblog.',
            evidence=f'daily headings={daily_heading_count}',
            suggestion='Consider consolidating into thematic narrative sections.',
        ))

    if verbose:
        print('check: mos-military-style', file=sys.stderr)
    military_context = any(
        term in full_text.lower()
        for term in ('war', 'battle', 'conflict', 'military', 'airstrike', 'missile')
    )
    uncited_casualty_lines: list[str] = []
    if military_context:
        for line in wikitext.splitlines():
            stripped = re.sub(r'\s+', ' ', line.strip())
            if not stripped or stripped.startswith('==') or stripped.startswith('{{'):
                continue
            if (
                re.search(r'\b(casualties|killed|injured|fatalities|losses)\b', stripped, flags=re.IGNORECASE)
                and '<ref' not in stripped
            ):
                uncited_casualty_lines.append(stripped[:120])

    if uncited_casualty_lines:
        issues.append(Issue(
            check_id='mos-military-style',
            severity='medium',
            section='global',
            message='Potential MOS:MILITARY sourcing gaps for casualty/loss statements.',
            evidence=' | '.join(uncited_casualty_lines[:3]),
            suggestion='Ensure casualty and losses statements are precisely attributed and cited.',
        ))

    if verbose:
        print('check: maintenance-tags', file=sys.stderr)
    if code is not None:
        maintenance_hits = sorted({
            normalize_template_name(str(t.name))
            for t in code.filter_templates(recursive=True)
            if normalize_template_name(str(t.name)) in MAINTENANCE_TEMPLATES
        })
    else:
        maintenance_hits = sorted({
            normalize_template_name(m)
            for m in re.findall(r'\{\{\s*([^|}\n]+)', wikitext)
            if normalize_template_name(m) in MAINTENANCE_TEMPLATES
        })
    if maintenance_hits:
        issues.append(Issue(
            check_id='maintenance-tags',
            severity='medium',
            section='global',
            message='Maintenance templates present in article text.',
            evidence=', '.join(maintenance_hits),
            suggestion='Resolve sourcing/style issues where possible.',
        ))

    if verbose:
        print('check: mos-sister-projects', file=sys.stderr)
    existing_template_names = template_names_from_wikitext(wikitext, code)
    sister_link_hits = sorted(set(SISTER_PROJECT_LINK_PATTERN.findall(wikitext)))
    if sister_link_hits and not (existing_template_names & SISTER_PROJECT_TEMPLATES):
        issues.append(Issue(
            check_id='mos-sister-projects',
            severity='low',
            section='global',
            message='Direct sister-project links found without sister-link templates.',
            evidence=', '.join(sister_link_hits),
            suggestion='Prefer MOS:SISTER-compliant sister project templates over raw external links.',
        ))

    if verbose:
        print('check: infobox-bloat, infobox-validation, mos-milhist-style', file=sys.stderr)
    infobox_name = ''
    infobox_param_names: set[str] = set()
    if code is not None:
        infobox = None
        for template in code.filter_templates(recursive=False):
            name = normalize_template_name(str(template.name))
            if name.startswith('infobox'):
                infobox = template
                break
        if infobox is not None:
            infobox_name = normalize_template_name(str(infobox.name))
            infobox_param_names = {normalize_template_name(str(p.name)) for p in infobox.params}
            infobox_text = str(infobox)
            param_lines = list(infobox.params)
            list_like = re.findall(r'(?:\{\{ubl|\{\{plainlist|<br\s*/?>|\n\*)', infobox_text, flags=re.IGNORECASE)
        else:
            param_lines = []
            list_like = []
    else:
        infobox_match = re.search(r'\{\{\s*Infobox[^}]*?(?:\n\|.*?)+\n\}\}', wikitext, re.IGNORECASE | re.DOTALL)
        if infobox_match:
            name_match = re.search(r'\{\{\s*([^|}\n]+)', infobox_match.group(0))
            if name_match:
                infobox_name = normalize_template_name(name_match.group(1))
            param_lines = re.findall(r'^\|', infobox_match.group(0), flags=re.MULTILINE)
            infobox_param_names = {
                normalize_template_name(m)
                for m in re.findall(r'^\|\s*([^=\n]+)=', infobox_match.group(0), flags=re.MULTILINE)
            }
            list_like = re.findall(
                r'(?:\{\{ubl|\{\{plainlist|<br\s*/?>|\n\*)',
                infobox_match.group(0),
                flags=re.IGNORECASE,
            )
        else:
            param_lines = []
            list_like = []

    if param_lines:
        if len(param_lines) > 35 or len(list_like) > 10:
            issues.append(Issue(
                check_id='infobox-bloat',
                severity='medium',
                section='infobox',
                message='Infobox may be overloaded with detail.',
                evidence=f'params={len(param_lines)}, list_markers={len(list_like)}',
                suggestion='Keep infobox summary-level and move detail to body.',
            ))

    if infobox_name:
        requirements = COMMON_INFOBOX_REQUIREMENTS.get(infobox_name)
        if requirements:
            missing_groups = [
                '/'.join(group)
                for group in requirements
                if not any(opt in infobox_param_names for opt in group)
            ]
            if missing_groups:
                issues.append(Issue(
                    check_id='infobox-validation',
                    severity='medium',
                    section='infobox',
                    message='Infobox is missing commonly expected parameters.',
                    evidence=', '.join(missing_groups),
                    suggestion='Fill missing fields or verify infobox choice against article scope.',
                ))
        else:
            issues.append(Issue(
                check_id='infobox-validation',
                severity='low',
                section='infobox',
                message='Infobox template is outside the common verification list.',
                evidence=infobox_name,
                suggestion='Manually verify infobox parameter completeness and template suitability.',
            ))

    if infobox_name == 'infobox military conflict':
        if not any(name.startswith('casualties') for name in infobox_param_names):
            issues.append(Issue(
                check_id='mos-milhist-style',
                severity='low',
                section='infobox',
                message='MOS:MILHIST signal: military conflict infobox has no casualties fields.',
                evidence='No casualties* parameter found.',
                suggestion='Include casualties fields if reliably sourced data exists.',
            ))

    # the rest of the owl: checks that catch the stuff editors actually care about

    if verbose:
        print('check: peacock-terms', file=sys.stderr)
    peacock_matches = find_phrases(full_text, PEACOCK_TERMS)
    if peacock_matches:
        issues.append(Issue(
            check_id='peacock-terms',
            severity='medium',
            section='global',
            message='Potential MOS:PEACOCK promotional language found.',
            evidence=', '.join(peacock_matches),
            suggestion='Replace with neutral, factual phrasing and attribution.',
        ))

    if verbose:
        print('check: bare-urls-in-refs', file=sys.stderr)
    bare_ref_urls: list[str] = []
    if code is not None:
        for tag in code.filter_tags(matches='ref'):
            content = str(tag.contents).strip()
            if re.match(r'^https?://[^\s<]+$', content):
                bare_ref_urls.append(str(tag))
    else:
        bare_ref_urls = re.findall(r'<ref[^>]*>https?://[^\s<]+</ref>', wikitext, flags=re.IGNORECASE)
    if bare_ref_urls:
        issues.append(Issue(
            check_id='bare-urls-in-refs',
            severity='medium',
            section='references',
            message='Bare URLs inside <ref> tags; no citation template.',
            evidence='; '.join(str(u) for u in bare_ref_urls[:5]),
            suggestion='Wrap bare URLs in {{cite web}} or equivalent citation template.',
        ))

    if verbose:
        print('check: uncategorized', file=sys.stderr)
    cat_names_all = _extract_category_names(wikitext, code)
    if len(cat_names_all) == 0:
        issues.append(Issue(
            check_id='uncategorized',
            severity='low',
            section='global',
            message='Article has no categories.',
            evidence='0 [[Category:...]] tags found.',
            suggestion='Add appropriate categories to aid navigation and classification.',
        ))

    if verbose:
        print('check: unreferenced-sections', file=sys.stderr)
    unreferenced_section_headings: list[str] = []
    if code is not None:
        for section in code.get_sections(levels=[2], include_headings=True):
            headings = section.filter_headings()
            if not headings:
                continue
            heading_plain = strip_markup(str(headings[0].title)).strip()
            body_raw = str(section)
            body_plain = strip_markup(body_raw)
            word_count = len(re.findall(r"\b[\w'-]+\b", body_plain))
            if word_count >= 100 and '<ref' not in body_raw:
                unreferenced_section_headings.append(heading_plain)
    else:
        section_splits = re.split(r'\n(==[^=][^=]*==)\s*\n', wikitext)
        if len(section_splits) > 2:
            for i in range(1, len(section_splits) - 1, 2):
                heading_raw = section_splits[i]
                body_raw = section_splits[i + 1] if i + 1 < len(section_splits) else ''
                heading_plain = _normalize_heading_text(heading_raw)
                body_plain = strip_markup(body_raw)
                word_count = len(re.findall(r"\b[\w'-]+\b", body_plain))
                if word_count >= 100 and '<ref' not in body_raw:
                    unreferenced_section_headings.append(heading_plain)
    if unreferenced_section_headings:
        issues.append(Issue(
            check_id='unreferenced-sections',
            severity='medium',
            section='structure',
            message='Body sections with 100+ words and no inline citations.',
            evidence=', '.join(unreferenced_section_headings[:5]),
            suggestion='Add inline citations for all major claims per MOS:CITE.',
        ))

    if verbose:
        print('check: overlinking', file=sys.stderr)
    link_counts: dict[str, int] = {}
    if code is not None:
        for wl in code.filter_wikilinks(recursive=True):
            target = str(wl.title).strip()
            if ':' in target or not target:
                continue
            key = target[0].upper() + target[1:]
            link_counts[key] = link_counts.get(key, 0) + 1
    else:
        raw_links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', wikitext)
        for target in raw_links:
            key = target.strip()
            if key:
                key = key[0].upper() + key[1:]
            link_counts[key] = link_counts.get(key, 0) + 1
    overlinked = sorted(
        [(target, count) for target, count in link_counts.items() if count >= config.overlink_threshold],
        key=lambda x: -x[1],
    )
    if overlinked:
        issues.append(Issue(
            check_id='overlinking',
            severity='low',
            section='global',
            message=f'Wikilinks repeated {config.overlink_threshold}+ times; per MOS:OVERLINK, link only on first use.',
            evidence=', '.join(f'{t} ({c}x)' for t, c in overlinked[:5]),
            suggestion='Delink all but the first occurrence of each repeated wikilink.',
        ))

    if verbose:
        print('check: short-sections', file=sys.stderr)
    _SKIP_SHORT = {'see also', 'references', 'external links', 'further reading', 'notes', 'bibliography'}
    short_section_names: list[str] = []
    if code is not None:
        all_headings = list(code.filter_headings())
        for idx, heading in enumerate(all_headings):
            level = heading.level
            if level not in (2, 3):
                continue
            heading_plain = strip_markup(str(heading.title)).strip()
            if heading_plain.lower() in _SKIP_SHORT:
                continue
            # preamble skip: if next heading is deeper, this is just an intro
            if idx + 1 < len(all_headings) and all_headings[idx + 1].level > level:
                continue
            # get body between this heading and the next
            section_start = str(code).find(str(heading)) + len(str(heading))
            if idx + 1 < len(all_headings):
                section_end = str(code).find(str(all_headings[idx + 1]), section_start)
            else:
                section_end = len(str(code))
            body_raw = str(code)[section_start:section_end]
            body_plain = strip_markup(body_raw)
            word_count = len(re.findall(r"\b[\w'-]+\b", body_plain))
            if 0 < word_count < config.short_section_words:
                short_section_names.append(heading_plain)
    else:
        section_splits_23 = re.split(r'\n(={2,3}[^=][^=]*={2,3})\s*\n', wikitext)
        if len(section_splits_23) > 2:
            for i in range(1, len(section_splits_23) - 1, 2):
                heading_raw = section_splits_23[i]
                body_raw = section_splits_23[i + 1] if i + 1 < len(section_splits_23) else ''
                heading_plain = _normalize_heading_text(heading_raw).lower()
                if heading_plain in _SKIP_SHORT:
                    continue
                current_level = len(heading_raw) - len(heading_raw.lstrip('='))
                if i + 2 < len(section_splits_23):
                    next_level = len(section_splits_23[i + 2]) - len(section_splits_23[i + 2].lstrip('='))
                    if next_level > current_level:
                        continue
                body_plain = strip_markup(body_raw)
                word_count = len(re.findall(r"\b[\w'-]+\b", body_plain))
                if 0 < word_count < config.short_section_words:
                    short_section_names.append(_normalize_heading_text(heading_raw))
    if short_section_names:
        issues.append(Issue(
            check_id='short-sections',
            severity='low',
            section='structure',
            message=f'Sections with fewer than {config.short_section_words} words of prose.',
            evidence=', '.join(short_section_names),
            suggestion='Expand underdeveloped sections or merge them with a related section.',
        ))

    if verbose:
        print('check: see-also-bloat', file=sys.stderr)
    see_also_body = None
    if code is not None:
        for section in code.get_sections(levels=[2], include_headings=True):
            headings = section.filter_headings()
            if headings and strip_markup(str(headings[0].title)).strip().lower() == 'see also':
                see_also_body = str(section)
                break
    else:
        see_also_match = re.search(
            r'\n==\s*See also\s*==\s*\n(.*?)(?=\n==|\Z)', wikitext, flags=re.IGNORECASE | re.DOTALL,
        )
        if see_also_match:
            see_also_body = see_also_match.group(1)
    if see_also_body is not None:
        see_also_items = re.findall(r'^\*', see_also_body, flags=re.MULTILINE)
        if len(see_also_items) > config.see_also_max:
            issues.append(Issue(
                check_id='see-also-bloat',
                severity='low',
                section='structure',
                message=f'See also section has {len(see_also_items)} items; should be curated.',
                evidence=f'{len(see_also_items)} bullet items.',
                suggestion='Trim to the most directly related articles; remove anything already linked in body.',
            ))

    if verbose:
        print('check: external-links-in-body', file=sys.stderr)
    wikitext_no_refs = re.sub(r'<ref[^>]*>.*?</ref>', '', wikitext, flags=re.IGNORECASE | re.DOTALL)
    if code is not None:
        ext_body = wikitext_no_refs
        for section in code.get_sections(levels=[2], include_headings=True):
            headings = section.filter_headings()
            if headings and strip_markup(str(headings[0].title)).strip().lower() in ('external links', 'external link'):
                ext_section_text = str(section)
                idx = wikitext_no_refs.find(ext_section_text)
                if idx >= 0:
                    ext_body = wikitext_no_refs[:idx]
                break
    else:
        ext_links_section_match = re.search(
            r'\n==\s*External links?\s*==\s*\n', wikitext_no_refs, flags=re.IGNORECASE,
        )
        ext_body = (
            wikitext_no_refs[:ext_links_section_match.start()]
            if ext_links_section_match
            else wikitext_no_refs
        )
    bare_body_urls = re.findall(r'https?://\S+', ext_body)
    if bare_body_urls:
        issues.append(Issue(
            check_id='external-links-in-body',
            severity='low',
            section='global',
            message='Bare external URLs in article prose (outside refs and External links).',
            evidence='; '.join(bare_body_urls[:3]),
            suggestion='Move to External links section, convert to {{cite}} template, or wikilink.',
        ))

    # red links: the broken windows of Wikipedia
    if client is not None:
        if verbose:
            print('check: red-links', file=sys.stderr)
        unique_targets = _extract_wikilink_targets(wikitext, code)
        if unique_targets:
            existence = client.check_page_existence(unique_targets)
            red_links = [t for t in unique_targets if not existence.get(t, True)]
            if red_links:
                issues.append(Issue(
                    check_id='red-links',
                    severity='medium',
                    section='global',
                    message='Wikilinks point to non-existent articles.',
                    evidence=', '.join(red_links[:8]),
                    suggestion='Create the target article, fix the spelling, or remove/unlink.',
                ))

    if client is not None:
        if verbose:
            print('check: red-categories', file=sys.stderr)
        cat_names = _extract_category_names(wikitext, code)
        cat_titles = [f'Category:{name}' for name in cat_names]
        if cat_titles:
            cat_existence = client.check_page_existence(cat_titles)
            red_cats = [t for t in cat_titles if not cat_existence.get(t, True)]
            if red_cats:
                issues.append(Issue(
                    check_id='red-categories',
                    severity='medium',
                    section='categories',
                    message='Article uses categories that do not exist.',
                    evidence=', '.join(red_cats),
                    suggestion='Create the category, fix the spelling, or use an existing parent category.',
                ))

    if verbose:
        print('check: category-quality', file=sys.stderr)
    all_cat_names = _extract_category_names(wikitext, code)
    cat_quality_issues: list[str] = []
    if len(all_cat_names) < 2:
        category_suffix = 'y' if len(all_cat_names) == 1 else 'ies'
        cat_quality_issues.append(
            f'only {len(all_cat_names)} categor{category_suffix} found (undercategorized)'
        )
    broad_cats = [n for n in all_cat_names if len(n.split()) == 1]
    if broad_cats:
        cat_quality_issues.append(f'broad single-word categories: {", ".join(broad_cats)}')
    if cat_quality_issues:
        issues.append(Issue(
            check_id='category-quality',
            severity='low',
            section='categories',
            message='Category coverage may be insufficient or too broad.',
            evidence='; '.join(cat_quality_issues),
            suggestion='Add more specific categories per WP:CAT.',
        ))

    if verbose:
        print('check: ai-overattribution', file=sys.stderr)
    overattr_matches = AI_OVERATTRIBUTION_RE.findall(full_text)
    if len(overattr_matches) >= 2:
        evidence_items = [m.strip()[:80] for m in overattr_matches[:3]]
        issues.append(Issue(
            check_id='ai-overattribution',
            severity='high',
            section='global',
            message='Over-attribution pattern detected (WP:AISIGNS).',
            evidence='; '.join(evidence_items),
            suggestion='State facts and cite with footnotes. Don\'t narrate sources in body text (WP:AISIGNS).',
        ))

    if verbose:
        print('check: ai-essay-tone', file=sys.stderr)
    essay_matches = find_phrases(full_text, ESSAY_TONE_PHRASES)
    if essay_matches:
        issues.append(Issue(
            check_id='ai-essay-tone',
            severity='medium',
            section='global',
            message='Essay-like phrasing detected (WP:AISIGNS).',
            evidence=', '.join(essay_matches),
            suggestion=(
                'Rewrite in neutral encyclopedic tone. These phrases are flagged under '
                'WP:AISIGNS and WP:NOTESSAY.'
            ),
        ))

    if verbose:
        print('check: cs1-isbn-validation', file=sys.stderr)
    isbn_matches: list[str] = []
    if code is not None:
        for template in code.filter_templates(recursive=True):
            if template.has('isbn', ignore_empty=True):
                isbn_matches.append(str(template.get('isbn').value).strip())
    else:
        isbn_matches = ISBN_PARAM_RE.findall(wikitext)
    invalid_isbns: list[str] = []
    for raw_isbn in isbn_matches:
        cleaned = raw_isbn.strip().upper().replace('-', '').replace(' ', '')
        if not cleaned:
            continue
        if len(cleaned) == 10:
            if not (cleaned[:9].isdigit() and (cleaned[9].isdigit() or cleaned[9] == 'X')):
                invalid_isbns.append(raw_isbn.strip())
            elif not _isbn10_valid(cleaned):
                invalid_isbns.append(raw_isbn.strip())
        elif len(cleaned) == 13:
            if not _isbn13_valid(cleaned):
                invalid_isbns.append(raw_isbn.strip())
        else:
            invalid_isbns.append(raw_isbn.strip())
    if invalid_isbns:
        issues.append(Issue(
            check_id='cs1-isbn-validation',
            severity='medium',
            section='references',
            message='Invalid ISBN format or check digit in citation templates.',
            evidence=', '.join(invalid_isbns[:5]),
            suggestion='Fix ISBN formatting. Qwerfjkl bot will flag these automatically.',
        ))

    if verbose:
        print('check: cs1-url-validation', file=sys.stderr)
    url_matches: list[str] = []
    if code is not None:
        for template in code.filter_templates(recursive=True):
            for param_name in ('url', 'archive-url', 'chapter-url'):
                if template.has(param_name, ignore_empty=True):
                    url_matches.append(str(template.get(param_name).value).strip())
    else:
        url_matches = URL_PARAM_RE.findall(wikitext)
    broken_urls: list[str] = []
    for raw_url in url_matches:
        url = raw_url.strip()
        if not url:
            continue
        if not url.startswith(('http://', 'https://')):
            broken_urls.append(url[:80])
        elif ' ' in url:
            broken_urls.append(url[:80])
        elif '.' not in url.split('//')[1].split('/')[0]:
            broken_urls.append(url[:80])
    if broken_urls:
        issues.append(Issue(
            check_id='cs1-url-validation',
            severity='medium',
            section='references',
            message='Malformed URLs in citation templates.',
            evidence='; '.join(broken_urls[:5]),
            suggestion='Fix malformed URLs in citations. Qwerfjkl bot will flag these.',
        ))

    if client is not None:
        if verbose:
            print('check: disambiguation-links', file=sys.stderr)
        unique_dab_targets = _extract_wikilink_targets(wikitext, code)
        if unique_dab_targets:
            disambig_hits = client.check_disambiguation(unique_dab_targets)
            if disambig_hits:
                issues.append(Issue(
                    check_id='disambiguation-links',
                    severity='medium',
                    section='global',
                    message='Wikilinks point to disambiguation pages.',
                    evidence=', '.join(disambig_hits[:8]),
                    suggestion='Link to the specific article, not the disambiguation page. DPL bot will flag these.',
                ))

    if verbose:
        print('check: short-description-quality', file=sys.stderr)
    sd_text = None
    if code is not None:
        for template in code.filter_templates(recursive=False):
            if normalize_template_name(str(template.name)) == 'short description':
                if template.params:
                    sd_text = str(template.params[0].value).strip()
                break
    else:
        sd_match = SHORT_DESC_RE.search(wikitext)
        if sd_match:
            sd_text = sd_match.group(1).strip()
    if sd_text is not None:
        sd_lower = sd_text.lower()
        title_lower = title.replace('_', ' ').lower()
        if sd_lower == title_lower:
            issues.append(Issue(
                check_id='short-description-quality',
                severity='low',
                section='global',
                message='Short description is just the article title.',
                evidence=sd_text,
                suggestion='Write a brief description of the subject, not just its name (WP:SDNONE).',
            ))
        elif sd_lower != 'none' and len(sd_text) > 40:
            issues.append(Issue(
                check_id='short-description-quality',
                severity='low',
                section='global',
                message='Short description is too long.',
                evidence=f'{sd_text} ({len(sd_text)} chars)',
                suggestion='Keep short descriptions under 40 characters for mobile display.',
            ))
    else:
        issues.append(Issue(
            check_id='short-description-quality',
            severity='low',
            section='global',
            message='No short description found.',
            evidence='{{Short description}} template missing.',
            suggestion='Add {{Short description|...}} at the top of the article.',
        ))

    # MOS:LAYOUT section ordering -- the bottom-matter police
    if verbose:
        print('check: section-ordering', file=sys.stderr)
    level2_headings: list[str] = []
    if code is not None:
        for heading in code.filter_headings():
            if heading.level == 2:
                level2_headings.append(strip_markup(str(heading.title)).strip().lower())
    else:
        level2_headings = [
            _normalize_heading_text(h).lower()
            for h in re.findall(r'\n==\s*([^=].*?)\s*==\s*\n', wikitext)
        ]
    bottom_positions = [
        (i, heading)
        for i, heading in enumerate(level2_headings)
        if heading in _BOTTOM_MATTER_ORDER
    ]
    if len(bottom_positions) >= 2:
        canonical_indices = [_BOTTOM_MATTER_ORDER.index(h) for _, h in bottom_positions]
        misordered = []
        for j in range(len(canonical_indices) - 1):
            if canonical_indices[j] > canonical_indices[j + 1]:
                misordered.append(f'{bottom_positions[j][1]} before {bottom_positions[j + 1][1]}')
        if misordered:
            issues.append(Issue(
                check_id='section-ordering',
                severity='low',
                section='structure',
                message='Bottom-matter sections out of MOS:LAYOUT order.',
                evidence='; '.join(misordered),
                suggestion='Reorder per MOS:LAYOUT: See also > Notes > References > Further reading > External links.',
            ))

    # dead external links -- slow, opt-in only
    if check_urls:
        if verbose:
            print('check: dead-external-links', file=sys.stderr)
        all_urls = re.findall(r'https?://[^\s<>\[\]|{}]+', wikitext)
        # dedupe preserving order
        seen_urls: set[str] = set()
        unique_urls: list[str] = []
        for u in all_urls:
            if u not in seen_urls:
                seen_urls.add(u)
                unique_urls.append(u)
        dead_urls = _check_url_liveness(unique_urls)
        if dead_urls:
            issues.append(Issue(
                check_id='dead-external-links',
                severity='medium',
                section='references',
                message='External URLs returned errors or timed out.',
                evidence='; '.join(dead_urls[:5]),
                suggestion='Replace dead links with archive URLs or remove.',
            ))

    # orphan check -- does anything link here?
    if client is not None and check_orphan:
        if verbose:
            print('check: orphan-article', file=sys.stderr)
        try:
            data = client._request(params={
                'action': 'query',
                'format': 'json',
                'formatversion': '2',
                'titles': title,
                'prop': 'linkshere',
                'lhlimit': '1',
                'lhnamespace': '0',
            })
            pages = data.get('query', {}).get('pages', [])
            has_incoming = any(page.get('linkshere') for page in pages)
            if not has_incoming:
                issues.append(Issue(
                    check_id='orphan-article',
                    severity='low',
                    section='global',
                    message='No other articles link to this page.',
                    evidence='0 incoming mainspace wikilinks.',
                    suggestion='Add wikilinks from related articles or list pages.',
                ))
        except (TimeoutError, TypeError, ValueError, KeyError, urllib.error.HTTPError, urllib.error.URLError) as exc:
            if verbose:
                print(f'note: orphan check unavailable: {exc}', file=sys.stderr)
            issues.append(Issue(
                check_id='orphan-check-unavailable',
                severity='low',
                section='global',
                message='Orphan-link check could not complete due to API/network error.',
                evidence=str(exc)[:120] or 'API request failed.',
                suggestion='Retry later or rerun with stable API/network connectivity.',
            ))

    # potential backlinks: who talks about us but doesn't link?
    if client is not None and check_backlinks:
        if verbose:
            print('check: potential-backlinks', file=sys.stderr)
        try:
            candidates = client.find_potential_backlinks(title, limit=50)
            if candidates:
                issues.append(Issue(
                    check_id='potential-backlinks',
                    severity='low',
                    section='global',
                    message='Articles mention this subject but do not wikilink to it.',
                    evidence=', '.join(candidates[:10]),
                    suggestion='Add [[wikilinks]] from these articles to improve discoverability.',
                ))
        except (TimeoutError, TypeError, ValueError, KeyError, urllib.error.HTTPError, urllib.error.URLError) as exc:
            if verbose:
                print(f'note: backlinks check unavailable: {exc}', file=sys.stderr)
            issues.append(Issue(
                check_id='backlinks-check-unavailable',
                severity='low',
                section='global',
                message='Potential-backlinks check could not complete due to API/network error.',
                evidence=str(exc)[:120] or 'API request failed.',
                suggestion='Retry later or rerun with stable API/network connectivity.',
            ))

    # filter by disabled checks and minimum severity from config
    issues = [
        i for i in issues
        if config.is_check_enabled(i.check_id)
        and severity_meets_minimum(i.severity, config.min_severity)
    ]

    score = 100 - sum(SEVERITY_WEIGHTS.get(issue.severity, 0) for issue in issues)
    return AuditReport(title=title, score=max(0, score), issues=issues)
