from typing import Optional

from app.models.schemas import Entity, EvidenceItem
from app.connectors.chembl import search_chembl
from app.connectors.pubchem import search_pubchem
from app.connectors.rcsb_pdb import search_rcsb_pdb
from app.connectors.uniprot import search_uniprot


MOCK_DATABASE_RESULTS = {
    "uniprot": {
        "database": "UniProt",
        "records_found": 10,
        "top_records": [
            {
                "name": "toxin-related peptide family record",
                "organism": "scorpion species",
                "summary": "Public annotation describing venom peptide family membership.",
            }
        ],
        "confidence": "medium",
    },
    "pdb": {
        "database": "RCSB PDB",
        "records_found": 4,
        "top_records": [
            {
                "name": "peptide scaffold structure reference",
                "organism": "animal source",
                "summary": "Public structure metadata useful for concept-level comparison.",
            }
        ],
        "confidence": "medium",
    },
    "rcsb pdb": {
        "database": "RCSB PDB",
        "records_found": 4,
        "top_records": [
            {
                "name": "peptide scaffold structure reference",
                "organism": "animal source",
                "summary": "Public structure metadata useful for concept-level comparison.",
            }
        ],
        "confidence": "medium",
    },
    "chembl": {
        "database": "ChEMBL",
        "records_found": 6,
        "top_records": [
            {
                "name": "bioactivity summary record",
                "organism": "not specified",
                "summary": "Public bioactivity-style metadata for educational comparison.",
            }
        ],
        "confidence": "low",
    },
    "pubchem": {
        "database": "PubChem",
        "records_found": 2,
        "top_records": [
            {
                "name": "peptide-related concept record",
                "organism": "not applicable",
                "summary": "Public compound identity-style metadata where applicable.",
            }
        ],
        "confidence": "low",
    },
    "alphafold db": {
        "database": "AlphaFold DB",
        "records_found": 3,
        "top_records": [
            {
                "name": "predicted protein structure reference",
                "organism": "animal source",
                "summary": "Public predicted-structure metadata for non-operational review.",
            }
        ],
        "confidence": "low",
    },
}


def aggregate_evidence(entities: list[Entity]) -> list[EvidenceItem]:
    items: list[EvidenceItem] = []
    seen_sources: set[str] = set()

    for entity in entities:
        for database in entity.databases:
            result = _search_database(database, entity.normalized)
            if not result or result["database"] in seen_sources:
                continue
            items.append(
                EvidenceItem(
                    source=result["database"],
                    records_found=result["records_found"],
                    summary=(
                        f"{result['database']} mock evidence related to "
                        f"{entity.normalized}. Summaries are public database-style "
                        "and concept-level only."
                    ),
                    confidence=result["confidence"],
                    query=entity.normalized,
                    top_records=result["top_records"],
                )
            )
            seen_sources.add(result["database"])

    return items


def search_mock_evidence(query: str, databases: list[str]) -> list[dict]:
    results: list[dict] = []
    for database in databases:
        result = _search_database(database, query)
        if result:
            copied = dict(result)
            copied["top_records"] = [
                {
                    **record,
                    "summary": (
                        f"{record['summary']} Query matched '{query}' at a "
                        "conceptual, non-operational level."
                    ),
                }
                for record in result["top_records"]
            ]
            results.append(copied)
    return results


def _search_database(database: str, query: str) -> Optional[dict]:
    key = database.lower()
    if key == "uniprot":
        return search_uniprot(query)
    if key in {"pdb", "rcsb pdb"}:
        return search_rcsb_pdb(query)
    if key == "chembl":
        return search_chembl(query)
    if key == "pubchem":
        return search_pubchem(query)
    return MOCK_DATABASE_RESULTS.get(key)
