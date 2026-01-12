from pydantic import BaseModel, HttpUrl


class ProcessRequest(BaseModel):
    url: HttpUrl


class ProcessResponse(BaseModel):
    name: str
    bpmn_mermaid: str
