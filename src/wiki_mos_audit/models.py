"""Data models, constants, and compiled regexes for wiki-mos-audit."""
from __future__ import annotations

import os
import re
from dataclasses import dataclass

VERSION = '0.3'

DEFAULT_USER_AGENT = 'wiki-mos-audit/0.3'
USER_AGENT = os.getenv('WIKI_MOS_AUDIT_USER_AGENT', DEFAULT_USER_AGENT).strip() or DEFAULT_USER_AGENT

MONTHS = (
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December',
)

# weasel words: the Wikipedia equivalent of "my cousin's friend said"
WEASEL_TERMS = (
    'some analysts',
    'critics say',
    'is believed to',
    'is widely regarded',
    'it is said',
    'many people',
    'observers say',
)

RELATIVE_TIME_TERMS = (
    'recently',
    'currently',
    'today',
    'yesterday',
    'last week',
    'last month',
    'at present',
    'so far',
)

# MOS:PEACOCK -- the Wikipedia equivalent of a press release written by a publicist
PEACOCK_TERMS = (
    'legendary',
    'iconic',
    'world-class',
    'renowned',
    'prestigious',
    'cutting-edge',
    'groundbreaking',
    'state-of-the-art',
    'one of the most',
    'widely considered',
)

MAINTENANCE_TEMPLATES = {
    'citation needed',
    'cn',
    'dubious',
    'weasel',
    'peacock',
    'cleanup',
    'clarify',
    'failed verification',
    'pov',
    'neutrality',
    'update',
}

SEVERITY_WEIGHTS = {
    'high': 15,
    'medium': 8,
    'low': 4,
}

INDIGENOUS_FLAG_TERMS = (
    'eskimo',
    'red indian',
    'primitive tribe',
    'savages',
)

SISTER_PROJECT_LINK_PATTERN = re.compile(
    r'https?://(?:[a-z]+\.)?(?:wiktionary|wikibooks|wikinews|wikiquote|wikisource'
    r'|wikiversity|wikivoyage|wikidata|commons\.wikimedia|species\.wikimedia)\.org',
    flags=re.IGNORECASE,
)

SISTER_PROJECT_TEMPLATES = {
    'commons',
    'commons category',
    'commonscat',
    'sisterlinks',
    'sister project links',
    'wiktionary',
    'wikiquote',
    'wikisource',
    'wikibooks',
    'wikivoyage',
    'wikinews',
    'wikidata',
}

COMMON_INFOBOX_REQUIREMENTS = {
    'infobox military conflict': (
        ('date',),
        ('place',),
        ('belligerents1', 'belligerent1', 'combatant1'),
        ('belligerents2', 'belligerent2', 'combatant2'),
    ),
    'infobox person': (
        ('name',),
    ),
    'infobox officeholder': (
        ('name',),
        ('office',),
    ),
    'infobox settlement': (
        ('name',),
        ('country',),
    ),
    'infobox country': (
        ('common_name', 'conventional_long_name'),
    ),
    'infobox organization': (
        ('name',),
    ),
    'infobox company': (
        ('name',),
    ),
    'infobox event': (
        ('date',),
    ),
    'infobox aircraft occurrence': (
        ('date',),
        ('summary',),
        ('site',),
    ),
    'infobox airport': (
        ('name',),
        ('location',),
    ),
}

ISSUE_TO_MAINTENANCE_TAG = {
    'lead-length': 'Lead too long',
    'weasel-terms': 'Weasel',
    'relative-time': 'Update',
    'date-style-mix': 'Cleanup',
    'quote-density': 'Cleanup rewrite',
    'timeline-structure': 'Cleanup rewrite',
    'infobox-bloat': 'Cleanup',
    'infobox-validation': 'Cleanup',
    'mos-indigenous-terms': 'Cleanup',
    'mos-aviation-style': 'Cleanup',
    'mos-military-style': 'Cleanup',
    'mos-milhist-style': 'Cleanup',
    'mos-sister-projects': 'Cleanup',
    'peacock-terms': 'Peacock',
    'bare-urls-in-refs': 'Cleanup bare URLs',
    'uncategorized': 'Uncategorized',
    'unreferenced-sections': 'More citations needed',
    'red-links': 'Cleanup red links',
    'red-categories': 'Cleanup red links',
    'ai-overattribution': 'Cleanup',
    'ai-essay-tone': 'Cleanup',
    'cs1-isbn-validation': 'Cleanup bare URLs',
    'cs1-url-validation': 'Cleanup bare URLs',
    'disambiguation-links': 'Disambiguation cleanup',
    'section-ordering': 'Cleanup',
    'dead-external-links': 'Cleanup bare URLs',
    'orphan-article': 'Orphan',
    'potential-backlinks': 'Orphan',
}

# language codes only; anything else is an injection vector
_LANG_CODE_RE = re.compile(r'^[a-z]{2,3}(-[a-z]{2,8})?$')


@dataclass
class Issue:
    check_id: str
    severity: str
    section: str
    message: str
    evidence: str
    suggestion: str


@dataclass
class AuditReport:
    title: str
    score: int
    issues: list[Issue]
