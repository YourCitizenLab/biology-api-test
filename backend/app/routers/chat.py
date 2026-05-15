from fastapi import APIRouter

from app.models.schemas import FollowUpRequest, FollowUpResponse
from app.services.deepseek_service import generate_follow_up_answer
from app.services.safety_service import classify_text_risk

router = APIRouter(tags=["chat"])

RISK_PRIORITY = {
    "low": 0,
    "medium": 1,
    "high": 2,
    "blocked": 3,
}


@router.post("/chat/follow-up", response_model=FollowUpResponse)
def follow_up(request: FollowUpRequest) -> FollowUpResponse:
    text_risk = classify_text_risk(request.message)
    context_risk = request.context.risk_level or "low"
    risk_level = max((text_risk, context_risk), key=RISK_PRIORITY.__getitem__)

    return FollowUpResponse(
        answer=generate_follow_up_answer(request.message, risk_level),
        risk_level=risk_level,
        suggested_actions=[
            "Search non-toxic antimicrobial peptide families",
            "Replace venom or toxin cards with safer biomolecule cards",
            "Review public database summaries at a concept level",
        ],
    )
