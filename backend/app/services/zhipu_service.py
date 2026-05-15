import json
from typing import Any

import httpx

from app.config import settings
from app.models.schemas import CandidateConcept, RiskAssessment
from app.services.safety_service import enforce_concept_boundary


SYSTEM_SAFETY_BOUNDARY = (
    "You are a scientific discovery assistant for concept-level bio/chemical exploration. "
    "Do not provide synthesis steps, experimental protocols, extraction methods, dosages, "
    "concentrations, temperatures, purification methods, or harmful operational instructions."
)


def generate_candidate_concept(
    user_input: str, cards: list[str], risk: RiskAssessment
) -> CandidateConcept:
    if not settings.zhipu_api_key:
        return _mock_candidate_concept(risk)

    try:
        content = _call_zhipu(
            [
                {"role": "system", "content": SYSTEM_SAFETY_BOUNDARY},
                {
                    "role": "user",
                    "content": (
                        "Return JSON only with keys name, description, and "
                        "possible_function_direction. Keep it concept-level. "
                        f"Input: {user_input}. Cards: {', '.join(cards)}. "
                        f"Risk: {risk.level}. Allowed output: {risk.allowed_output}."
                    ),
                },
            ]
        )
        parsed = json.loads(content)
        return CandidateConcept(
            name=str(parsed.get("name") or "Scorpion-Inspired Peptide Scaffold Concept"),
            description=enforce_concept_boundary(
                str(parsed.get("description") or _mock_candidate_concept(risk).description)
            ),
            status="simulation_only",
            possible_function_direction=[
                enforce_concept_boundary(str(item))
                for item in parsed.get("possible_function_direction", [])
                if str(item).strip()
            ]
            or _mock_candidate_concept(risk).possible_function_direction,
        )
    except Exception:
        return _mock_candidate_concept(risk)


def generate_follow_up_answer(message: str, risk_level: str) -> str:
    if not settings.zhipu_api_key:
        return _mock_follow_up_answer(risk_level)
    try:
        answer = _call_zhipu(
            [
                {"role": "system", "content": SYSTEM_SAFETY_BOUNDARY},
                {
                    "role": "user",
                    "content": (
                        "Answer in two concise concept-level sentences. "
                        f"Risk level: {risk_level}. User follow-up: {message}"
                    ),
                },
            ]
        )
        return enforce_concept_boundary(answer)
    except Exception:
        return _mock_follow_up_answer(risk_level)


def _call_zhipu(messages: list[dict[str, str]]) -> str:
    response = httpx.post(
        "https://open.bigmodel.cn/api/paas/v4/chat/completions",
        headers={
            "Authorization": f"Bearer {settings.zhipu_api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": settings.zhipu_model,
            "messages": messages,
            "temperature": 0.2,
        },
        timeout=settings.external_api_timeout_seconds,
    )
    response.raise_for_status()
    payload: dict[str, Any] = response.json()
    return str(payload["choices"][0]["message"]["content"])


def _mock_candidate_concept(risk: RiskAssessment) -> CandidateConcept:
    description = (
        "A hypothetical scorpion-inspired peptide scaffold concept with broad "
        "mammalian motif references. It is framed for concept-level structure-function "
        "education, public evidence review, and safer alternative exploration."
    )
    if risk.allowed_output == "blocked":
        description = (
            "This request is limited to safety education and non-operational alternatives."
        )

    return CandidateConcept(
        name="Scorpion-Inspired Peptide Scaffold Concept",
        description=enforce_concept_boundary(description),
        status="simulation_only",
        possible_function_direction=[
            "Stable peptide scaffold comparison",
            "Non-operational structure-function education",
            "Public database evidence review",
            "Safer non-toxin peptide family exploration",
        ],
    )


def _mock_follow_up_answer(risk_level: str) -> str:
    if risk_level in {"high", "blocked"}:
        return (
            "A safer direction is to avoid toxin-like functional claims and focus on "
            "non-toxic peptide scaffold families, public database summaries, and broad "
            "structure-function education."
        )
    return (
        "This can be explored as a concept-level comparison of biological references, "
        "public evidence cards, and lower-risk follow-up questions."
    )
