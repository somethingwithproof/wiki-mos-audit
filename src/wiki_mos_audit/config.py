"""Configuration loading for wiki-mos-audit."""
from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class AuditConfig:
    """Runtime configuration for audit checks."""
    disabled_checks: set[str] = field(default_factory=set)
    min_severity: str = 'low'  # low, medium, high
    custom_banned_phrases: list[str] = field(default_factory=list)
    language: str = 'en'
    check_urls: bool = False
    check_orphan: bool = False
    check_backlinks: bool = False
    max_lead_words: int = 260
    max_lead_paragraphs: int = 4
    overlink_threshold: int = 3
    short_section_words: int = 30
    see_also_max: int = 10
    quote_density_threshold: int = 4

    def is_check_enabled(self, check_id: str) -> bool:
        return check_id not in self.disabled_checks


_SEVERITY_ORDER = {'low': 0, 'medium': 1, 'high': 2}


def severity_meets_minimum(severity: str, minimum: str) -> bool:
    """Check if a severity level meets the minimum threshold."""
    return _SEVERITY_ORDER.get(severity, 0) >= _SEVERITY_ORDER.get(minimum, 0)


def load_config(config_path: Path | None = None) -> AuditConfig:
    """Load config from .wiki-mos-audit.toml, searching cwd then home."""
    if config_path and config_path.exists():
        return _parse_config(config_path)

    # search cwd, then home
    for search_dir in (Path.cwd(), Path.home()):
        candidate = search_dir / '.wiki-mos-audit.toml'
        if candidate.exists():
            return _parse_config(candidate)

    return AuditConfig()


def _parse_config(path: Path) -> AuditConfig:
    """Parse a TOML config file into AuditConfig."""
    with open(path, 'rb') as f:
        data = tomllib.load(f)

    audit = data.get('audit', {})
    config = AuditConfig()

    if 'disabled_checks' in audit:
        config.disabled_checks = set(audit['disabled_checks'])
    if 'min_severity' in audit:
        if audit['min_severity'] not in _SEVERITY_ORDER:
            raise ValueError(f"Invalid min_severity: {audit['min_severity']!r}")
        config.min_severity = audit['min_severity']
    if 'custom_banned_phrases' in audit:
        config.custom_banned_phrases = list(audit['custom_banned_phrases'])
    if 'language' in audit:
        config.language = audit['language']
    if 'check_urls' in audit:
        config.check_urls = bool(audit['check_urls'])
    if 'check_orphan' in audit:
        config.check_orphan = bool(audit['check_orphan'])
    if 'check_backlinks' in audit:
        config.check_backlinks = bool(audit['check_backlinks'])

    thresholds = data.get('thresholds', {})
    for attr in ('max_lead_words', 'max_lead_paragraphs', 'overlink_threshold',
                 'short_section_words', 'see_also_max', 'quote_density_threshold'):
        if attr in thresholds:
            setattr(config, attr, int(thresholds[attr]))

    return config
