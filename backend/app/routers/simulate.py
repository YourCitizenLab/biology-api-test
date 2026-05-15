from fastapi import APIRouter

from app.models.schemas import SimulationRequest, SimulationResponse
from app.services.entity_service import extract_entities
from app.services.evidence_aggregator import aggregate_evidence
from app.services.safety_service import assess_risk
from app.services.zhipu_service import generate_candidate_concept

router = APIRouter(tags=["simulate"])


@router.post("/simulate", response_model=SimulationResponse)
def simulate_discovery(request: SimulationRequest) -> SimulationResponse:
    entities = extract_entities(request.input, request.cards)
    risk = assess_risk(request.input, request.cards, entities)
    evidence = aggregate_evidence(entities)
    concept = generate_candidate_concept(request.input, request.cards, risk)

    return SimulationResponse(
        candidate_concept=concept,
        entities=entities,
        evidence=evidence,
        risk=risk,
        follow_up_questions=[
            "Why is blue scorpion related to venom peptides?",
            "Which public databases support this interpretation?",
            "Can this concept be made safer?",
            "Explain this concept for non-scientists.",
        ],
        confidence_score=0.62 if risk.level == "high" else 0.7,
    )
