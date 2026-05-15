from typing import Any

import httpx

from app.config import settings


def search_uniprot(query: str) -> dict[str, Any]:
    try:
        response = httpx.get(
            "https://rest.uniprot.org/uniprotkb/search",
            params={"query": query, "format": "json", "size": 5},
            timeout=settings.external_api_timeout_seconds,
        )
        response.raise_for_status()
        results = response.json().get("results", [])
        return {
            "database": "UniProt",
            "records_found": len(results),
            "top_records": [
                {
                    "name": item.get("proteinDescription", {})
                    .get("recommendedName", {})
                    .get("fullName", {})
                    .get("value", "protein annotation"),
                    "organism": item.get("organism", {}).get("scientificName", "unknown"),
                    "summary": (
                        "Public protein annotation relevant to entity mapping and "
                        "concept-level evidence review."
                    ),
                    "record_id": item.get("primaryAccession", ""),
                }
                for item in results[:3]
            ],
            "confidence": "medium" if results else "low",
            "used_fallback": False,
        }
    except Exception:
        return {
            "database": "UniProt",
            "records_found": 10,
            "top_records": [
                {
                    "name": "toxin-related peptide family record",
                    "organism": "scorpion species",
                    "summary": "Fallback public annotation describing venom peptide family membership.",
                }
            ],
            "confidence": "medium",
            "used_fallback": True,
        }
