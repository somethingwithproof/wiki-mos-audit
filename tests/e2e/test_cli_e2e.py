"""E2E tests: invoke the CLI as a subprocess."""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]
_MODULE = [sys.executable, '-m', 'wiki_mos_audit']


def _run(*args: str, cwd: str = str(PROJECT_ROOT)) -> subprocess.CompletedProcess:
    return subprocess.run(
        [*_MODULE, *args],
        capture_output=True, text=True, cwd=cwd,
    )


# ---------------------------------------------------------------------------
# Basic CLI invocations
# ---------------------------------------------------------------------------

def test_version() -> None:
    result = _run('--version')
    assert '0.3' in result.stdout


def test_help() -> None:
    result = _run('--help')
    assert result.returncode == 0
    assert '--json' in result.stdout
    assert '--verbose' in result.stdout


def test_help_includes_language_flag() -> None:
    result = _run('--help')
    assert '--language' in result.stdout


def test_help_includes_dry_run_flag() -> None:
    result = _run('--help')
    assert '--dry-run' in result.stdout


# ---------------------------------------------------------------------------
# File-based invocations (no network)
# ---------------------------------------------------------------------------

def test_offline_with_file(tmp_path: Path) -> None:
    wikitext_file = tmp_path / 'test.txt'
    wikitext_file.write_text(
        "'''Test''' is a test.\n\n== Section ==\nContent.\n\n"
        '[[Category:Test]]\n[[Category:Examples]]\n'
    )
    result = _run('Test', '--wikitext-file', str(wikitext_file), '--json')
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert 'score' in data
    assert 'issues' in data


def test_quiet_returns_no_stdout(tmp_path: Path) -> None:
    wikitext_file = tmp_path / 'test.txt'
    wikitext_file.write_text(
        "'''Test''' is a test.\n\n[[Category:Test]]\n[[Category:Examples]]\n"
    )
    result = _run('Test', '--wikitext-file', str(wikitext_file), '--quiet')
    assert result.returncode == 0
    assert result.stdout.strip() == ''


def test_verbose_prints_checks_to_stderr(tmp_path: Path) -> None:
    wikitext_file = tmp_path / 'test.txt'
    wikitext_file.write_text(
        "'''Test''' is a test.\n\n[[Category:Test]]\n[[Category:Examples]]\n"
    )
    result = _run('Test', '--wikitext-file', str(wikitext_file), '--verbose')
    assert result.returncode == 0
    # --verbose prints "check: <name>" lines to stderr
    assert 'check:' in result.stderr


def test_dry_run_with_add_maintenance_tags(tmp_path: Path) -> None:
    wikitext_file = tmp_path / 'test.txt'
    # Weasel terms trigger a maintenance tag suggestion
    wikitext_file.write_text(
        "'''Test''' is widely regarded as the best.\n"
        'It is said that many people agree.\n\n'
        '[[Category:Test]]\n[[Category:Examples]]\n'
    )
    result = _run(
        'Test', '--wikitext-file', str(wikitext_file),
        '--add-maintenance-tags', '--dry-run',
    )
    assert result.returncode == 0
    assert 'Maintenance tags' in result.stdout


# ---------------------------------------------------------------------------
# Error cases
# ---------------------------------------------------------------------------

def test_invalid_language() -> None:
    result = _run('Test', '--language', 'evil.com/x#')
    assert result.returncode == 1
    assert 'Invalid language code' in result.stderr


def test_missing_target_returns_error() -> None:
    result = _run()
    assert result.returncode == 2
    assert 'target is required' in result.stderr


def test_missing_wikitext_file_returns_1() -> None:
    result = _run('Test', '--wikitext-file', '/nonexistent/path/article.txt')
    assert result.returncode == 1


def test_json_output_is_valid_json(tmp_path: Path) -> None:
    wikitext_file = tmp_path / 'article.txt'
    fixture = PROJECT_ROOT / 'fixtures' / 'sample_article.txt'
    wikitext_file.write_text(fixture.read_text(encoding='utf-8'))
    result = _run('Cascade Range', '--wikitext-file', str(wikitext_file), '--json')
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data['title'] == 'Cascade Range'
    assert isinstance(data['score'], int)
    assert isinstance(data['issues'], list)
