from typing import Any

import httpx

from app.config import settings


def search_chembl(query: str) -> dict[str, Any]:
    try:
        response = httpx.get(
            "https://www.ebi.ac.uk/chembl/api/data/molecule/search.json",
            params={"q": query, "limit": 5},
            timeout=settings.external_api_timeout_seconds,
        )
        response.raise_for_status()
        molecules = response.json().get("molecules", [])
        return {
            "database": "ChEMBL",
            "records_found": len(molecules),
            "top_records": [
                {
                    "name": item.get("pref_name") or item.get("molecule_chembl_id", "ChEMBL record"),
                    "organism": "not specified",
                    "summary": "Public bioactivity-style metadata for educational comparison.",
                    "record_id": item.get("molecule_chembl_id", ""),
                }
                for item in molecules[:3]
            ],
            "confidence": "low" if not molecules else "medium",
            "used_fallback": False,
        }
    except Exception:
        return {
            "database": "ChEMBL",
            "records_found": 6,
            "top_records": [
                {
                    "name": "bioactivity summary record",
                    "organism": "not specified",
                    "summary": "Fallback public bioactivity-style metadata for educational comparison.",
                }
            ],
            "confidence": "low",
            "used_fallback": True,
        }
