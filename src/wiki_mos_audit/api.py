"""MediaWiki API client for wiki-mos-audit. Read-only; no login, no edits."""
from __future__ import annotations

import http.cookiejar
import json
import time
import urllib.error
import urllib.parse
import urllib.request

from wiki_mos_audit.models import _LANG_CODE_RE, USER_AGENT


def create_api_opener() -> urllib.request.OpenerDirector:
    cookie_jar = http.cookiejar.CookieJar()
    return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))


def mediawiki_api_request(
    opener: urllib.request.OpenerDirector,
    api_url: str,
    params: dict[str, str],
    post: bool = False,
    *,
    max_retries: int = 3,
    backoff_seconds: float = 1.0,
    user_agent: str = USER_AGENT,
) -> dict:
    """Send a MediaWiki API request and return parsed JSON."""
    if max_retries < 1:
        raise ValueError('max_retries must be >= 1')

    for attempt in range(max_retries):
        if post:
            data = urllib.parse.urlencode(params).encode('utf-8')
            request = urllib.request.Request(api_url, data=data, headers={'User-Agent': user_agent})
        else:
            query = urllib.parse.urlencode(params)
            request = urllib.request.Request(f'{api_url}?{query}', headers={'User-Agent': user_agent})

        try:
            with opener.open(request, timeout=30) as response:  # noqa: S310
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as error:
            retryable = error.code in {429, 500, 502, 503, 504}
            if not retryable or attempt == max_retries - 1:
                raise
        except urllib.error.URLError:
            if attempt == max_retries - 1:
                raise

        time.sleep(backoff_seconds * (2**attempt))

    raise RuntimeError('unreachable mediawiki_api_request retry path')


class WikipediaApiClient:
    """Read-only MediaWiki API client. Fetches wikitext; nothing else."""

    def __init__(
        self,
        language: str = 'en',
        user_agent: str | None = None,
        request_pause: float = 0.0,
    ) -> None:
        if not _LANG_CODE_RE.match(language):
            raise ValueError(f'Invalid language code: {language!r}')
        if request_pause < 0:
            raise ValueError('request_pause must be >= 0')
        self.api_url = f'https://{language}.wikipedia.org/w/api.php'
        self.opener = create_api_opener()
        self.user_agent = (user_agent or USER_AGENT).strip()
        self.request_pause = request_pause

        if not self.user_agent:
            raise ValueError('user_agent must not be empty')

    def _request(self, params: dict[str, str], post: bool = False) -> dict:
        return mediawiki_api_request(
            opener=self.opener,
            api_url=self.api_url,
            params=params,
            post=post,
            user_agent=self.user_agent,
        )

    def fetch_wikitext(self, title: str) -> str:
        data = self._request(
            params={
                'action': 'query',
                'format': 'json',
                'formatversion': '2',
                'prop': 'revisions',
                'rvprop': 'content',
                'rvslots': 'main',
                'redirects': '1',
                'titles': title,
            },
        )

        pages = data.get('query', {}).get('pages', [])
        if not pages or 'missing' in pages[0]:
            raise ValueError(f'Article not found: {title}')

        revision = pages[0].get('revisions', [{}])[0]
        content = revision.get('slots', {}).get('main', {}).get('content')
        if not content:
            raise ValueError(f'No wikitext returned for: {title}')

        return content

    def check_page_existence(self, titles: list[str]) -> dict[str, bool]:
        """Batch-check whether pages exist. Returns {title: exists}."""
        result: dict[str, bool] = {}
        # MediaWiki accepts up to 50 titles per request.
        for i in range(0, len(titles), 50):
            chunk = titles[i:i + 50]
            data = self._request(
                params={
                    'action': 'query',
                    'format': 'json',
                    'formatversion': '2',
                    'titles': '|'.join(chunk),
                    'redirects': '1',
                },
            )
            # formatversion=2 gives pages as a list, not a dict keyed by pageid.
            # Redirects are resolved; the normalized/redirected title is in page['title'].
            # Build a set of titles that came back without 'missing'.
            existing: set[str] = set()
            for page in data.get('query', {}).get('pages', []):
                if not page.get('missing', False):
                    existing.add(page['title'])

            # Map requested titles to resolved titles via normalizations/redirects.
            normalized: dict[str, str] = {}
            for entry in data.get('query', {}).get('normalized', []):
                normalized[entry['from']] = entry['to']
            redirects: dict[str, str] = {}
            for entry in data.get('query', {}).get('redirects', []):
                redirects[entry['from']] = entry['to']

            for title in chunk:
                resolved = title
                resolved = normalized.get(resolved, resolved)
                resolved = redirects.get(resolved, resolved)
                result[title] = resolved in existing

            if self.request_pause > 0 and i + 50 < len(titles):
                time.sleep(self.request_pause)

        return result


    def check_disambiguation(self, titles: list[str]) -> list[str]:
        """Return titles that are disambiguation pages."""
        disambig: list[str] = []
        for i in range(0, len(titles), 50):
            chunk = titles[i:i + 50]
            data = self._request(
                params={
                    'action': 'query',
                    'format': 'json',
                    'formatversion': '2',
                    'titles': '|'.join(chunk),
                    'prop': 'pageprops',
                    'ppprop': 'disambiguation',
                    'redirects': '1',
                },
            )
            for page in data.get('query', {}).get('pages', []):
                if 'pageprops' in page and 'disambiguation' in page['pageprops']:
                    disambig.append(page['title'])

            if self.request_pause > 0 and i + 50 < len(titles):
                time.sleep(self.request_pause)

        return disambig


    def find_potential_backlinks(self, title: str, limit: int = 50) -> list[str]:
        """Find articles that mention the title but don't wikilink to it."""
        # step 1: search for articles mentioning the title
        data = self._request(params={
            'action': 'query',
            'format': 'json',
            'formatversion': '2',
            'list': 'search',
            'srsearch': f'"{title}"',
            'srnamespace': '0',
            'srlimit': str(min(limit, 50)),
            'srinfo': '',
            'srprop': '',
        })
        mentioning = [
            hit['title'] for hit in data.get('query', {}).get('search', [])
            if hit['title'] != title
        ]
        if not mentioning:
            return []

        # step 2: check which of those pages actually link to the target
        linking: set[str] = set()
        for i in range(0, len(mentioning), 50):
            chunk = mentioning[i:i + 50]
            link_data = self._request(params={
                'action': 'query',
                'format': 'json',
                'formatversion': '2',
                'titles': '|'.join(chunk),
                'prop': 'links',
                'pltitles': title,
                'pllimit': '500',
            })
            for page in link_data.get('query', {}).get('pages', []):
                if page.get('links'):
                    linking.add(page['title'])

            if self.request_pause > 0 and i + 50 < len(mentioning):
                time.sleep(self.request_pause)

        return [t for t in mentioning if t not in linking]


def fetch_wikitext(title: str, language: str = 'en') -> str:
    """Convenience wrapper: fetch wikitext for a single title."""
    return WikipediaApiClient(language=language).fetch_wikitext(title=title)
