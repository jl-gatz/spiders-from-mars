from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class Page(BaseModel):
    url: HttpUrl
    title: Optional[str]
    text: str
    headings: List[str] = []
    links: List[HttpUrl] = []


class CrawlResult(BaseModel):
    start_url: HttpUrl
    pages: List[Page]
