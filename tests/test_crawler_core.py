from unittest.mock import patch

from process_miner.core.crawler.crawler import crawl_site
from process_miner.models.core.core_models import CrawlResult


def test_crawl_site_single_page():
    html = """
    <html>
    <head><title>Test Title</title></head>
    <body>
    <h1>Heading 1</h1>
    <p>This is some text.</p>
    </body>
    </html>
    """
    with patch(
        'process_miner.core.crawler.crawler.fetch_html', return_value=html
    ):
        result = crawl_site('https://example.com')
        assert isinstance(result, CrawlResult)
        assert result.start_url == 'https://example.com'
        assert len(result.pages) == 1
        page = result.pages[0]
        assert page.url == 'https://example.com'
        assert page.title == 'Test Title'
        assert page.headings == ['Heading 1']
        assert 'This is some text' in page.text
        assert page.links == []


def test_crawl_site_with_links():
    def mock_fetch(url):
        if url == 'https://example.com':
            return """
            <html><head><title>Home</title></head><body><a href="/page1">
            Page 1</a></body></html>
            """
        elif url == 'https://example.com/page1':
            return """
            <html><head><title>Page 1</title></head><body>
            <h2>Sub Heading</h2></body></html>
            """
        else:
            raise ValueError('Unexpected URL')

    with patch(
        'process_miner.core.crawler.crawler.fetch_html', side_effect=mock_fetch
    ):
        result = crawl_site('https://example.com', max_pages=2)
        assert len(result.pages) == 2  # noqa: PLR2004
        urls = [p.url for p in result.pages]
        assert 'https://example.com' in urls
        assert 'https://example.com/page1' in urls


def test_crawl_site_fetch_error():
    with patch(
        'process_miner.core.crawler.crawler.fetch_html',
        side_effect=Exception('Fetch error'),
    ):
        result = crawl_site('https://example.com')
        assert len(result.pages) == 0
        assert result.start_url == 'https://example.com'
