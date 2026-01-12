from fastapi import APIRouter

from process_miner.core.extractor import extract_process
from process_miner.models.routers.process_models import (
    ProcessRequest,
    ProcessResponse,
)

# from process_miner.core.diagram import generate_bpmn_mermaid

router = APIRouter()


@router.post('/extract', response_model=ProcessResponse)
def extract_process_from_url(payload: ProcessRequest):
    process = extract_process(str(payload.url))
    diagram = 'generate_bpmn_mermaid(process)'

    return ProcessResponse(name=process.name, bpmn_mermaid=diagram)
