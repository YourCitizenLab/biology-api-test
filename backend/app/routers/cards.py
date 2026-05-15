from fastapi import APIRouter

from app.models.schemas import (
    CardSuggestionRequest,
    CardSuggestionResponse,
    SuggestedCard,
)
from app.services.safety_service import classify_text_risk

router = APIRouter(tags=["cards"])


@router.post("/cards/suggest", response_model=CardSuggestionResponse)
def suggest_cards(request: CardSuggestionRequest) -> CardSuggestionResponse:
    risk = classify_text_risk(request.input)
    suggestions = [
        SuggestedCard(name="Antimicrobial Peptide", category="Biomolecule", risk="medium"),
        SuggestedCard(name="Plant Peptide", category="Biomolecule", risk="low"),
        SuggestedCard(name="Structure-Function Education", category="Function", risk="low"),
    ]

    if risk == "high":
        suggestions.insert(
            0,
            SuggestedCard(
                name="Non-Toxic Peptide Scaffold",
                category="Safer Alternative",
                risk="low",
            ),
        )

    return CardSuggestionResponse(suggested_cards=suggestions)
