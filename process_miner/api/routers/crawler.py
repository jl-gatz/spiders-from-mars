from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field, HttpUrl

from process_miner.core.crawler.crawler import crawl_site

router = APIRouter()


class CrawlRequest(BaseModel):
    start_url: HttpUrl
    max_pages: int = Field(default=10, ge=1, le=50)


class PagePreview(BaseModel):
    url: HttpUrl
    title: Optional[str]
    text_excerpt: str
    headings: List[str]


class CrawlResponse(BaseModel):
    pages: List[PagePreview]


@router.post("/", response_model=CrawlResponse)
def crawl(payload: CrawlRequest):
    result = crawl_site(
        start_url=str(payload.start_url),
        max_pages=payload.max_pages
    )

    pages = [
        PagePreview(
            url=page.url,
            title=page.title,
            text_excerpt=page.text[:500],
            headings=page.headings
        )
        for page in result.pages
    ]

    return CrawlResponse(pages=pages)
