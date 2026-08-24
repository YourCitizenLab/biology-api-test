from fastapi import APIRouter

from app.models.schemas import (
    CardSuggestionRequest,
    CardSuggestionResponse,
    SuggestedCard,
)
from app.services.entity_service import extract_entities
from app.services.safety_service import classify_text_risk

router = APIRouter(tags=["cards"])


CARD_METADATA = {
    "Bull": ("Animal Source", "low"),
    "Tiger": ("Animal Source", "low"),
    "Blue Scorpion": ("Animal Source", "high"),
    "Scorpion": ("Animal Source", "high"),
    "Peptide": ("Biomolecule", "medium"),
    "Antimicrobial Peptide": ("Biomolecule", "medium"),
    "Plant Peptide": ("Biomolecule", "low"),
    "PubChem": ("Database", "low"),
    "UniProt": ("Database", "low"),
    "ChEMBL": ("Database", "low"),
    "RCSB PDB": ("Database", "low"),
    "Non-Toxic Peptide Scaffold": ("Safer Alternative", "low"),
    "Structure-Function Education": ("Function", "low"),
    "Venom Risk Review": ("Risk Context", "high"),
}


def _make_card(name: str) -> SuggestedCard:
    category, risk = CARD_METADATA[name]
    return SuggestedCard(name=name, category=category, risk=risk)


@router.post("/cards/suggest", response_model=CardSuggestionResponse)
def suggest_cards(request: CardSuggestionRequest) -> CardSuggestionResponse:
    risk = classify_text_risk(request.input)
    entities = extract_entities(request.input, [])
    suggestions: list[SuggestedCard] = []
    seen: set[str] = set()

    def add(name: str) -> None:
        if name in CARD_METADATA and name not in seen:
            suggestions.append(_make_card(name))
            seen.add(name)

    for entity in entities:
        add(entity.raw)
        for database in entity.databases:
            if database in CARD_METADATA:
                add(database)

    add("Peptide")
    add("Antimicrobial Peptide")
    add("Plant Peptide")
    add("Structure-Function Education")

    if risk == "high":
        suggestions.insert(0, _make_card("Non-Toxic Peptide Scaffold"))
        if "Non-Toxic Peptide Scaffold" not in seen:
            seen.add("Non-Toxic Peptide Scaffold")
        add("Venom Risk Review")

    return CardSuggestionResponse(suggested_cards=suggestions)
