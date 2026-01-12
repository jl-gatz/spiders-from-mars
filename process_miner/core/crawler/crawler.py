from collections import deque

from bs4 import BeautifulSoup

from process_miner.models.core.core_models import CrawlResult, Page

from .fetcher import fetch_html
from .parser import parse_html


def crawl_site(start_url: str, max_pages: int = 20) -> CrawlResult:
    visited = set()
    queue = deque([start_url])
    pages = []

    while queue and len(pages) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue

        visited.add(url)

        try:
            html = fetch_html(url)
        except Exception:
            continue

        soup = BeautifulSoup(html, 'html.parser')
        title, headings, text = parse_html(html)

        page = Page(
            url=url, title=title, text=text, headings=headings, links=[]
        )
        pages.append(page)

        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('http'):
                queue.append(href)

    return CrawlResult(start_url=start_url, pages=pages)
