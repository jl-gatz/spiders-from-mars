from urllib.parse import urljoin, urlparse


def extract_internal_links(base_url: str, soup) -> list[str]:
    base_domain = urlparse(base_url).netloc
    links = set()

    for a in soup.find_all("a", href=True):
        href = urljoin(base_url, a["href"])
        if urlparse(href).netloc == base_domain:
            links.add(href)

    return list(links)
