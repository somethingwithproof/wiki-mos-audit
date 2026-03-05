"""Shared pytest fixtures for wiki-mos-audit tests."""
from __future__ import annotations

import pytest

MINIMAL_WIKITEXT = """\
'''Test Article''' is a test article.

== History ==
Some history here with enough words to pass the short-section threshold easily.
This section has plenty of content to avoid triggering short-section checks.
We are adding more words here to make sure we clear the thirty-word minimum.

[[Category:Test articles]]
[[Category:Example category]]
"""

WIKITEXT_WITH_ISSUES = """\
'''Iconic Test''' is a legendary, world-class example of groundbreaking work.

Recently, it is said that many people believe this is widely regarded as prestigious.

== History ==
The battle resulted in many casualties. Losses were significant.

== See also ==
* [[Some article]]

[[Category:Tests]]
"""


@pytest.fixture
def minimal_wikitext() -> str:
    return MINIMAL_WIKITEXT


@pytest.fixture
def wikitext_with_issues() -> str:
    return WIKITEXT_WITH_ISSUES


@pytest.fixture
def sample_wikitext() -> str:
    """Minimal article wikitext for testing."""
    return """{{Short description|Test article}}
{{Infobox person
| name = Test Person
| birth_date = January 1, 2000
}}
'''Test Person''' is a fictional person used for testing.

== Early life ==
Test Person was born in [[Springfield]]. They attended [[Springfield High School|the local high school]].
<ref>{{cite web |url=https://example.com/bio |title=Test Bio |access-date=March 1, 2026}}</ref>

== Career ==
They worked at a factory.<ref>{{cite book |title=Test Book |isbn=978-0-306-40615-7}}</ref>

== See also ==
* [[Related article]]

== References ==
{{reflist}}

[[Category:Test articles]]
[[Category:Fictional people]]
"""


@pytest.fixture
def ai_heavy_wikitext() -> str:
    """Wikitext with AI writing signals."""
    return """'''Test Subject''' is a renowned figure who played a pivotal role in history.

A 2020 article in The New York Times described the subject's groundbreaking work.
A 2021 profile in The Atlantic noted their cutting-edge approach.
A 2019 report in Nature highlighted their contributions.

It is worth noting that the subject left a lasting legacy. This demonstrates that their work continues to be remembered.

== Early life ==
Test Subject was born recently. Currently they are widely considered one of the most important figures.

== References ==
<ref>https://example.com/bare-url</ref>
<ref>{{cite web |url=https://example.com/proper |title=Proper Citation}}</ref>

[[Category:Test]]
"""


@pytest.fixture
def bad_citations_wikitext() -> str:
    """Wikitext with CS1 errors."""
    return """'''Test''' is a test article.

== Section ==
Some text.<ref>{{cite book |title=Book |isbn=123-456-789-0}}</ref>
More text.<ref>{{cite web |url=not-a-url |title=Bad URL}}</ref>
Even more.<ref>{{cite web |url=https://example.com |title=Good URL |isbn=978-0-306-40615-7}}</ref>
Bare ref.<ref>https://example.com/bare</ref>

== References ==
{{reflist}}

[[Category:Test]]
"""
