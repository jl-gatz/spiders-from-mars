from typing import List, Optional

from pydantic import AfterValidator, BaseModel
from pydantic_string_url import HttpUrl
from typing_extensions import Annotated

HttpURLString = Annotated[HttpUrl, AfterValidator(str)]


class Page(BaseModel):
    url: HttpURLString
    title: Optional[str]
    text: str
    headings: List[str] = []
    links: List[HttpUrl] = []


class CrawlResult(BaseModel):
    start_url: HttpURLString
    pages: List[Page]


class Process(BaseModel):
    name: str
    actors: List[str]
    steps: List[str]
