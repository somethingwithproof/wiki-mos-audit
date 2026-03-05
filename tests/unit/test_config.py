"""Unit tests for wiki_mos_audit.config."""
from __future__ import annotations

import pytest

from wiki_mos_audit.config import (
    AuditConfig,
    _parse_config,
    load_config,
    severity_meets_minimum,
)

# ---------------------------------------------------------------------------
# AuditConfig
# ---------------------------------------------------------------------------

class TestAuditConfig:
    def test_default_values(self) -> None:
        cfg = AuditConfig()
        assert cfg.disabled_checks == set()
        assert cfg.min_severity == 'low'
        assert cfg.custom_banned_phrases == []
        assert cfg.language == 'en'
        assert cfg.check_urls is False
        assert cfg.check_orphan is False
        assert cfg.check_backlinks is False
        assert cfg.max_lead_words == 260
        assert cfg.max_lead_paragraphs == 4
        assert cfg.overlink_threshold == 3
        assert cfg.short_section_words == 30
        assert cfg.see_also_max == 10
        assert cfg.quote_density_threshold == 4

    def test_is_check_enabled_empty_disabled(self) -> None:
        cfg = AuditConfig()
        assert cfg.is_check_enabled('weasel-terms') is True
        assert cfg.is_check_enabled('any-check') is True

    def test_is_check_enabled_with_disabled(self) -> None:
        cfg = AuditConfig(disabled_checks={'weasel-terms', 'peacock-terms'})
        assert cfg.is_check_enabled('weasel-terms') is False
        assert cfg.is_check_enabled('peacock-terms') is False
        assert cfg.is_check_enabled('bare-urls') is True

    def test_custom_init(self) -> None:
        cfg = AuditConfig(
            min_severity='high',
            language='de',
            check_urls=True,
            check_backlinks=True,
            max_lead_words=300,
        )
        assert cfg.min_severity == 'high'
        assert cfg.language == 'de'
        assert cfg.check_urls is True
        assert cfg.check_backlinks is True
        assert cfg.max_lead_words == 300


# ---------------------------------------------------------------------------
# severity_meets_minimum
# ---------------------------------------------------------------------------

class TestSeverityMeetsMinimum:
    @pytest.mark.parametrize(
        ('severity', 'minimum', 'expected'),
        [
            ('low', 'low', True),
            ('medium', 'low', True),
            ('high', 'low', True),
            ('low', 'medium', False),
            ('medium', 'medium', True),
            ('high', 'medium', True),
            ('low', 'high', False),
            ('medium', 'high', False),
            ('high', 'high', True),
        ],
    )
    def test_all_combinations(self, severity: str, minimum: str, expected: bool) -> None:
        assert severity_meets_minimum(severity, minimum) is expected

    def test_unknown_severity_treated_as_low(self) -> None:
        # Unknown severity gets default 0, same as 'low'
        assert severity_meets_minimum('unknown', 'low') is True
        assert severity_meets_minimum('unknown', 'medium') is False

    def test_unknown_minimum_treated_as_low(self) -> None:
        assert severity_meets_minimum('high', 'unknown') is True
        assert severity_meets_minimum('low', 'unknown') is True


# ---------------------------------------------------------------------------
# load_config
# ---------------------------------------------------------------------------

class TestLoadConfig:
    def test_no_config_file_returns_defaults(self, tmp_path: object) -> None:
        from pathlib import Path
        # Point to a nonexistent file
        cfg = load_config(config_path=Path('/nonexistent/.wiki-mos-audit.toml'))
        assert isinstance(cfg, AuditConfig)
        assert cfg.min_severity == 'low'
        assert cfg.disabled_checks == set()

    def test_explicit_path(self, tmp_path: object) -> None:
        from pathlib import Path
        p = Path(str(tmp_path)) / '.wiki-mos-audit.toml'
        p.write_text(
            '[audit]\n'
            'min_severity = "medium"\n'
            'disabled_checks = ["weasel-terms"]\n'
        )
        cfg = load_config(config_path=p)
        assert cfg.min_severity == 'medium'
        assert 'weasel-terms' in cfg.disabled_checks

    def test_none_path_no_file(self, monkeypatch: pytest.MonkeyPatch, tmp_path: object) -> None:
        from pathlib import Path
        # Monkeypatch cwd and home to tmp_path so no config is found
        monkeypatch.setattr(Path, 'cwd', classmethod(lambda cls: Path(str(tmp_path))))
        monkeypatch.setattr(Path, 'home', classmethod(lambda cls: Path(str(tmp_path))))
        cfg = load_config(config_path=None)
        assert isinstance(cfg, AuditConfig)
        assert cfg.min_severity == 'low'


# ---------------------------------------------------------------------------
# _parse_config
# ---------------------------------------------------------------------------

class TestParseConfig:
    def test_valid_toml(self, tmp_path: object) -> None:
        from pathlib import Path
        p = Path(str(tmp_path)) / 'config.toml'
        p.write_text(
            '[audit]\n'
            'min_severity = "high"\n'
            'disabled_checks = ["check-a", "check-b"]\n'
            'custom_banned_phrases = ["foo", "bar"]\n'
            'language = "fr"\n'
            'check_urls = true\n'
            'check_orphan = true\n'
            'check_backlinks = true\n'
            '\n'
            '[thresholds]\n'
            'max_lead_words = 300\n'
            'max_lead_paragraphs = 5\n'
            'overlink_threshold = 4\n'
            'short_section_words = 50\n'
            'see_also_max = 15\n'
            'quote_density_threshold = 6\n'
        )
        cfg = _parse_config(p)
        assert cfg.min_severity == 'high'
        assert cfg.disabled_checks == {'check-a', 'check-b'}
        assert cfg.custom_banned_phrases == ['foo', 'bar']
        assert cfg.language == 'fr'
        assert cfg.check_urls is True
        assert cfg.check_orphan is True
        assert cfg.check_backlinks is True
        assert cfg.max_lead_words == 300
        assert cfg.max_lead_paragraphs == 5
        assert cfg.overlink_threshold == 4
        assert cfg.short_section_words == 50
        assert cfg.see_also_max == 15
        assert cfg.quote_density_threshold == 6

    def test_invalid_min_severity_raises(self, tmp_path: object) -> None:
        from pathlib import Path
        p = Path(str(tmp_path)) / 'bad.toml'
        p.write_text('[audit]\nmin_severity = "critical"\n')
        with pytest.raises(ValueError, match='Invalid min_severity'):
            _parse_config(p)

    def test_partial_config(self, tmp_path: object) -> None:
        from pathlib import Path
        p = Path(str(tmp_path)) / 'partial.toml'
        p.write_text('[audit]\nlanguage = "de"\n')
        cfg = _parse_config(p)
        assert cfg.language == 'de'
        # Defaults for everything else
        assert cfg.min_severity == 'low'
        assert cfg.disabled_checks == set()
        assert cfg.max_lead_words == 260

    def test_thresholds_only(self, tmp_path: object) -> None:
        from pathlib import Path
        p = Path(str(tmp_path)) / 'thresh.toml'
        p.write_text('[thresholds]\nmax_lead_words = 500\nsee_also_max = 20\n')
        cfg = _parse_config(p)
        assert cfg.max_lead_words == 500
        assert cfg.see_also_max == 20
        # Audit section defaults
        assert cfg.min_severity == 'low'

    def test_empty_toml(self, tmp_path: object) -> None:
        from pathlib import Path
        p = Path(str(tmp_path)) / 'empty.toml'
        p.write_text('')
        cfg = _parse_config(p)
        assert cfg.min_severity == 'low'
        assert cfg.disabled_checks == set()
