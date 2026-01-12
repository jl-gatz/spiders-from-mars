from unittest.mock import patch

from process_miner.core.crawler.crawler import crawl_site


def test_crawl_site():
    # Mock fetch_html to return sample HTML
    html1 = """
    <html>
    <head><title>Page 1</title></head>
    <body>
        <h1>Heading 1</h1>
        <p>Text 1</p>
        <a href="https://example.com/page2">Link</a>
    </body>
    </html>
    """
    html2 = """
    <html>
    <head><title>Page 2</title></head>
    <body>
        <h2>Heading 2</h2>
        <p>Text 2</p>
    </body>
    </html>
    """

    def mock_fetch(url):
        if url == 'https://example.com':
            return html1
        elif url == 'https://example.com/page2':
            return html2
        else:
            raise Exception('Unexpected URL')

    with patch(
        'process_miner.core.crawler.crawler.fetch_html', side_effect=mock_fetch
    ):
        result = crawl_site('https://example.com', max_pages=2)
        assert result.start_url == 'https://example.com'
        assert len(result.pages) == 2  # noqa: PLR2004
        assert result.pages[0].url == 'https://example.com'
        assert result.pages[0].title == 'Page 1'
        assert 'Heading 1' in result.pages[0].headings
        assert 'Text 1' in result.pages[0].text
        assert result.pages[1].url == 'https://example.com/page2'
        assert result.pages[1].title == 'Page 2'
