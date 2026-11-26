# SPDX-FileCopyrightText: 2026 Thomas Vincent <thomasvincent@gmail.com>
# SPDX-License-Identifier: MIT

"""Tests for 20-locale i18n support in wiki-mos-audit."""
from __future__ import annotations

import re

import pytest

from wiki_mos_audit.cli import parse_args
from wiki_mos_audit.formatter import format_html_report, format_text_report
from wiki_mos_audit.i18n import (
    DEFAULT_LOCALE,
    SUPPORTED_LOCALES,
    detect_locale,
    get_locale,
    load_catalog,
    normalize_locale,
    set_locale,
    t,
)
from wiki_mos_audit.models import AuditReport

PLACEHOLDER_RE = re.compile(r'\{[a-zA-Z0-9_]+\}')


@pytest.fixture(autouse=True)
def _reset_locale(monkeypatch: pytest.MonkeyPatch):
    for var in ('LC_ALL', 'LC_MESSAGES', 'LANG'):
        monkeypatch.delenv(var, raising=False)
    set_locale(None)
    yield
    set_locale(None)


def test_all_20_locales_load_with_key_and_placeholder_parity() -> None:
    assert len(SUPPORTED_LOCALES) == 20
    en = load_catalog(DEFAULT_LOCALE)
    assert len(en) > 0
    for locale in SUPPORTED_LOCALES:
        catalog = load_catalog(locale)
        assert set(catalog.keys()) == set(en.keys()), locale
        for key, en_val in en.items():
            assert catalog[key].strip(), (locale, key)
            assert sorted(PLACEHOLDER_RE.findall(catalog[key])) == sorted(
                PLACEHOLDER_RE.findall(en_val)
            ), (locale, key)


@pytest.mark.parametrize(
    ('raw', 'expected'),
    [
        (None, 'en'),
        ('', 'en'),
        ('C', 'en'),
        ('POSIX', 'en'),
        ('de_DE.UTF-8', 'de'),
        ('zh_TW', 'zh-TW'),
        ('zh_HK.UTF-8', 'zh-TW'),
        ('zh-TW-x-test', 'zh-TW'),
        ('zh-HK-x-test', 'zh-TW'),
        ('zh-Hant-TW', 'zh-TW'),
        ('zh-Hans-TW', 'zh-CN'),
        ('zh_CN.UTF-8', 'zh-CN'),
        ('zh', 'zh-CN'),
        ('pt_BR.UTF-8', 'pt-BR'),
        ('pt_PT', 'pt-BR'),
        ('x-test', 'en'),
        ('xx_YY', 'en'),
    ],
)
def test_normalize_locale(raw: str | None, expected: str) -> None:
    assert normalize_locale(raw) == expected


def test_env_precedence_and_override(monkeypatch: pytest.MonkeyPatch) -> None:
    assert detect_locale() == 'en'
    monkeypatch.setenv('LANG', 'fr_FR.UTF-8')
    assert detect_locale() == 'fr'
    monkeypatch.setenv('LC_MESSAGES', 'uk_UA.UTF-8')
    assert detect_locale() == 'uk'
    monkeypatch.setenv('LC_ALL', 'de_DE.UTF-8')
    assert detect_locale() == 'de'
    assert detect_locale('ar') == 'ar'

    assert set_locale('ja') == 'ja'
    assert get_locale() == 'ja'
    assert set_locale(None) == 'de'
    assert get_locale() == 'de'


def test_default_english_and_localized_reports(capsys: pytest.CaptureFixture[str]) -> None:
    report = AuditReport(title='Test Article', score=100, issues=[])
    assert t('missing.key') == 'missing.key'
    assert 'No first-pass MOS issues detected.' in format_text_report(report)
    assert '<html lang="en">' in format_html_report(report)

    args = parse_args(['Test', '--lang', 'de', '--language', 'fr'])
    assert args.ui_lang == 'de'
    assert args.language == 'fr'
    assert get_locale() == 'de'
    assert t('report.no_issues', locale='de') in format_text_report(report)
    assert '<html lang="de">' in format_html_report(report)

    with pytest.raises(SystemExit) as exc:
        parse_args(['--lang', 'en', '--lang', 'de', '--help'])
    assert exc.value.code == 0
    assert ' '.join(t('cli.description', locale='de').split()) in ' '.join(
        capsys.readouterr().out.split()
    )
