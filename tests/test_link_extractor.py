from bs4 import BeautifulSoup

from process_miner.core.crawler.link_extractor import extract_internal_links


def test_extract_internal_links():
    html = """
    <html>
    <body>
        <a href="/page1">Page 1</a>
        <a href="https://example.com/page2">Page 2</a>
        <a href="https://other.com/page3">External</a>
        <a href="#anchor">Anchor</a>
    </body>
    </html>
    """
    soup = BeautifulSoup(html, 'html.parser')
    links = extract_internal_links('https://example.com', soup)
    expected = [
        'https://example.com/page1',
        'https://example.com/page2',
        'https://example.com#anchor',
    ]
    assert set(links) == set(expected)
