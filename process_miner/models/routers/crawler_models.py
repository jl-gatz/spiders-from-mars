from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


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
