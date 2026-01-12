from collections import deque
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from process_miner.core.crawler.fetcher import fetch_html
from process_miner.models.core.core_models import CrawlResult, Page

# Nota: Removi parse_html para evitar processamento duplo,
# assumindo que podemos extrair tudo via BeautifulSoup aqui.
# Se parse_html for complexo, ele deve aceitar o objeto 'soup' como argumento.


def crawl_site(start_url: str, max_pages: int = 20) -> CrawlResult:  # noqa: PLR0914
    # Normaliza a URL inicial e extrai o domínio base para evitar "fuga"
    start_url = start_url.rstrip('/')
    base_domain = urlparse(start_url).netloc

    visited = set([start_url])  # Marca inicial como visitada imediatamente
    queue = deque([start_url])
    pages = []

    print(f'Iniciando crawl em: {start_url} (Domínio: {base_domain})')

    while queue and len(pages) < max_pages:
        current_url = queue.popleft()

        try:
            html = fetch_html(current_url)
        except Exception as e:
            # É boa prática logar o erro em vez de apenas 'continue'
            print(f'Erro ao baixar {current_url}: {e}')
            continue

        soup = BeautifulSoup(html, 'html.parser')

        # Extração de dados
        # (Substituindo a lógica do parse_html para eficiência)
        title_tag = soup.find('title')
        title = title_tag.get_text(strip=True) if title_tag else 'Sem Título'

        # Exemplo simples de extração de texto e cabeçalhos
        headings = [
            h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])
        ]
        text = soup.get_text(separator=' ', strip=True)

        # Extração e normalização de links
        page_links = []
        for a in soup.find_all('a', href=True):
            raw_href = a['href']

            # 1. Resolve URLs relativas (/contato -> https://site.com/contato)
            full_url = urljoin(current_url, raw_href)

            # Remove fragmentos (#secao) para evitar duplicação de conteúdo
            full_url = full_url.split('#')[0].rstrip('/')

            # 2. Verifica se o link é válido e pertence ao mesmo domínio
            parsed_url = urlparse(full_url)
            if parsed_url.netloc == base_domain:
                if full_url not in visited:
                    visited.add(
                        full_url
                    )  # Marca como visitado ANTES de entrar na fila
                    queue.append(full_url)

                # Adiciona à lista de links desta página específica
                page_links.append(full_url)

        # Criação do objeto Page com dados completos
        page = Page(
            url=current_url,
            title=title,
            text=text,
            headings=headings,
            links=page_links,  # Agora populado corretamente
        )
        pages.append(page)

    return CrawlResult(start_url=start_url, pages=pages)
