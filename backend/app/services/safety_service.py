from app.models.schemas import Entity, RiskAssessment, RiskLevel


HIGH_RISK_TERMS = {
    "toxin",
    "venom",
    "poison",
    "pathogen",
    "virus",
    "bacteria culture",
    "weaponize",
    "enhance toxicity",
    "blue scorpion",
    "scorpion",
}

OPERATIONAL_TERMS = {
    "synthesis protocol",
    "synthesize",
    "extract",
    "extraction",
    "purify",
    "purification",
    "dosage",
    "concentration",
    "temperature",
    "reaction time",
    "wet-lab",
    "protocol",
}

SAFER_ALTERNATIVES = [
    "Explore non-toxic peptide scaffold families",
    "Focus on public database summaries",
    "Use general structure-function education",
    "Replace venom-related entities with lower-risk biomolecule cards",
]


def classify_text_risk(text: str) -> RiskLevel:
    normalized = text.lower()
    if any(term in normalized for term in OPERATIONAL_TERMS):
        return "blocked"
    if any(term in normalized for term in HIGH_RISK_TERMS):
        return "high"
    if any(term in normalized for term in {"bioactive", "drug", "peptide"}):
        return "medium"
    return "low"


def assess_risk(user_input: str, cards: list[str], entities: list[Entity]) -> RiskAssessment:
    combined_text = " ".join([user_input, *cards])
    text_risk = classify_text_risk(combined_text)
    entity_high_risk = any(entity.risk == "high" for entity in entities)

    if text_risk == "blocked":
        return RiskAssessment(
            level="blocked",
            reason="Operational bio/chem instruction request detected.",
            allowed_output="blocked",
            safer_alternatives=SAFER_ALTERNATIVES,
        )

    if entity_high_risk or text_risk == "high":
        return RiskAssessment(
            level="high",
            reason="Venom/toxin-related entity detected.",
            allowed_output="concept_only",
            safer_alternatives=SAFER_ALTERNATIVES,
        )

    if text_risk == "medium" or any(entity.risk == "medium" for entity in entities):
        return RiskAssessment(
            level="medium",
            reason="Bioactive molecule or peptide-related concept detected.",
            allowed_output="caution",
            safer_alternatives=SAFER_ALTERNATIVES[:2],
        )

    return RiskAssessment(
        level="low",
        reason="No high-risk biological or chemical terms detected.",
        allowed_output="normal",
    )


def enforce_concept_boundary(text: str) -> str:
    lower_text = text.lower()
    if any(term in lower_text for term in OPERATIONAL_TERMS):
        return (
            "This concept is restricted to high-level scientific education and "
            "public database-style summaries. Operational biological or chemical "
            "instructions are not provided."
        )
    return text
