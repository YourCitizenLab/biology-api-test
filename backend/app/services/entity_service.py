from app.models.schemas import Entity


ENTITY_LIBRARY = {
    "bull": Entity(
        raw="Bull",
        normalized="Bos taurus mammalian protein reference",
        type="animal_source",
        risk="low",
        databases=["UniProt", "RCSB PDB"],
    ),
    "tiger": Entity(
        raw="Tiger",
        normalized="Panthera tigris mammalian protein reference",
        type="animal_source",
        risk="low",
        databases=["UniProt", "RCSB PDB"],
    ),
    "blue scorpion": Entity(
        raw="Blue Scorpion",
        normalized="scorpion venom peptide",
        type="venom_peptide",
        risk="high",
        databases=["UniProt", "RCSB PDB", "AlphaFold DB", "ChEMBL"],
    ),
    "scorpion": Entity(
        raw="Scorpion",
        normalized="scorpion venom peptide",
        type="venom_peptide",
        risk="high",
        databases=["UniProt", "RCSB PDB", "AlphaFold DB", "ChEMBL"],
    ),
    "peptide": Entity(
        raw="Peptide",
        normalized="bioactive peptide scaffold",
        type="biomolecule",
        risk="medium",
        databases=["UniProt", "ChEMBL", "RCSB PDB"],
    ),
}


def extract_entities(user_input: str, cards: list[str]) -> list[Entity]:
    haystack = " ".join([user_input, *cards]).lower()
    entities: list[Entity] = []
    seen: set[str] = set()

    for keyword, entity in ENTITY_LIBRARY.items():
        if keyword in haystack and entity.normalized not in seen:
            entities.append(entity)
            seen.add(entity.normalized)

    if not entities:
        entities.append(
            Entity(
                raw=user_input,
                normalized="general bio/chem discovery concept",
                type="concept",
                risk="medium",
                databases=["PubChem", "UniProt", "ChEMBL", "RCSB PDB"],
            )
        )

    return entities
