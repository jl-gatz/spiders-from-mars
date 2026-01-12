from typing import Any
from urllib.request import urlopen

from bs4 import BeautifulSoup


def crawl_lista_servicos(start_url: str) -> list[Any]:
    html = urlopen(start_url)
    bs = BeautifulSoup(html, 'html.parser')
    linhas = bs.find_all('div', {'class': 'single-product'})
    resultados = []

    for i in linhas:
        resultados.append(i.text.strip())

    return resultados
