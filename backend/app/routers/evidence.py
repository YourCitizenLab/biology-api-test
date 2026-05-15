from fastapi import APIRouter

from app.models.schemas import (
    EvidenceSearchRequest,
    EvidenceSearchResponse,
    EvidenceSearchResult,
)
from app.services.evidence_aggregator import search_mock_evidence

router = APIRouter(tags=["evidence"])


@router.post("/evidence/search", response_model=EvidenceSearchResponse)
def search_evidence(request: EvidenceSearchRequest) -> EvidenceSearchResponse:
    databases = request.databases or ["uniprot", "pdb", "chembl", "pubchem"]
    results = [
        EvidenceSearchResult(**result)
        for result in search_mock_evidence(request.query, databases)
    ]
    return EvidenceSearchResponse(results=results)
