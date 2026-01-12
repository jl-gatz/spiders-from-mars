from bs4 import BeautifulSoup


def parse_html(html: str) -> tuple[str, list[str], str]:
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
        tag.decompose()

    title = soup.title.string.strip() if soup.title else None
    headings = [
        h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])
    ]
    text = soup.get_text(separator='\n', strip=True)

    return title, headings, text
