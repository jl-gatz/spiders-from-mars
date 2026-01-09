from typing import List

from pydantic import BaseModel


class Process(BaseModel):
    name: str
    actors: List[str]
    steps: List[str]
