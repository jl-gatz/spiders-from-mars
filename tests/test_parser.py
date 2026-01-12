from process_miner.core.crawler.parser import parse_html


def test_parse_html():
    html = """
    <html>
    <head><title>Test Page</title></head>
    <body>
        <h1>Main Heading</h1>
        <p>This is some text.</p>
        <h2>Sub Heading</h2>
        <p>More text.</p>
        <script>alert('ignore');</script>
        <nav>Navigation</nav>
    </body>
    </html>
    """
    title, headings, text = parse_html(html)
    assert title == "Test Page"
    assert headings == ["Main Heading", "Sub Heading"]
    assert "This is some text." in text
    assert "More text." in text
    assert "alert" not in text  # script removed
    assert "Navigation" not in text  # nav removed
