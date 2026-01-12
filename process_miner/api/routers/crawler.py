from fastapi import APIRouter

from process_miner.core.crawler.crawler import crawl_site
from process_miner.core.crawler.crawler_lista_servicos import (
    crawl_lista_servicos,
)
from process_miner.models.routers.crawler_models import (
    CrawlRequest,
    CrawlResponse,
    PagePreview,
)

router = APIRouter()


@router.post('/', response_model=CrawlResponse)
def crawl(payload: CrawlRequest):
    result = crawl_site(
        start_url=str(payload.start_url), max_pages=payload.max_pages
    )

    pages = [
        PagePreview(
            url=page.url,
            title=page.title,
            text_excerpt=page.text[:500],
            headings=page.headings,
        )
        for page in result.pages
    ]

    return CrawlResponse(pages=pages)


@router.get('/lista-servicos/')
def crawl_lista_servicos_endpoint(start_url: str):
    return crawl_lista_servicos(start_url)
