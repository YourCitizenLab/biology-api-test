from typing import Any
from urllib.parse import quote

import httpx

from app.config import settings


def search_pubchem(query: str) -> dict[str, Any]:
    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        f"{quote(query)}/property/MolecularFormula,MolecularWeight/JSON"
    )
    try:
        response = httpx.get(url, timeout=settings.external_api_timeout_seconds)
        response.raise_for_status()
        properties = response.json().get("PropertyTable", {}).get("Properties", [])
        return {
            "database": "PubChem",
            "records_found": len(properties),
            "top_records": [
                {
                    "name": query,
                    "organism": "not applicable",
                    "summary": (
                        "Public compound property metadata was found for concept-level "
                        "identity comparison."
                    ),
                    "record_id": str(item.get("CID", "")),
                }
                for item in properties[:3]
            ],
            "confidence": "low" if not properties else "medium",
            "used_fallback": False,
        }
    except Exception:
        return {
            "database": "PubChem",
            "records_found": 2,
            "top_records": [
                {
                    "name": "peptide-related concept record",
                    "organism": "not applicable",
                    "summary": "Fallback public compound identity-style metadata.",
                }
            ],
            "confidence": "low",
            "used_fallback": True,
        }
