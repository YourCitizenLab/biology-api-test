from typing import Any, Literal, Optional

from pydantic import BaseModel, Field


RiskLevel = Literal["low", "medium", "high", "blocked"]
OutputLevel = Literal["normal", "caution", "concept_only", "blocked"]


class SimulationRequest(BaseModel):
    input: str = Field(..., min_length=1)
    cards: list[str] = Field(default_factory=list)
    mode: str = "interactive_demo"
    output_level: OutputLevel = "concept_only"


class Entity(BaseModel):
    raw: str
    normalized: str
    type: str
    risk: RiskLevel
    databases: list[str]


class EvidenceItem(BaseModel):
    source: str
    records_found: int
    summary: str
    confidence: Literal["low", "medium", "high"]
    query: Optional[str] = None
    top_records: list[dict[str, Any]] = Field(default_factory=list)


class CandidateConcept(BaseModel):
    name: str
    description: str
    status: Literal["simulation_only"]
    possible_function_direction: list[str]


class RiskAssessment(BaseModel):
    level: RiskLevel
    reason: str
    allowed_output: OutputLevel
    safer_alternatives: list[str] = Field(default_factory=list)


class SimulationResponse(BaseModel):
    candidate_concept: CandidateConcept
    entities: list[Entity]
    evidence: list[EvidenceItem]
    risk: RiskAssessment
    follow_up_questions: list[str]
    confidence_score: float = Field(..., ge=0, le=1)


class EvidenceSearchRequest(BaseModel):
    query: str = Field(..., min_length=1)
    databases: list[str] = Field(default_factory=list)


class EvidenceSearchResult(BaseModel):
    database: str
    records_found: int
    top_records: list[dict[str, Any]]
    confidence: Literal["low", "medium", "high"] = "medium"


class EvidenceSearchResponse(BaseModel):
    results: list[EvidenceSearchResult]


class FollowUpContext(BaseModel):
    candidate_name: Optional[str] = None
    risk_level: Optional[RiskLevel] = None


class FollowUpRequest(BaseModel):
    simulation_id: Optional[str] = None
    message: str = Field(..., min_length=1)
    context: FollowUpContext = Field(default_factory=FollowUpContext)


class FollowUpResponse(BaseModel):
    answer: str
    risk_level: RiskLevel
    suggested_actions: list[str]


class CardSuggestionRequest(BaseModel):
    input: str = Field(..., min_length=1)


class SuggestedCard(BaseModel):
    name: str
    category: str
    risk: RiskLevel


class CardSuggestionResponse(BaseModel):
    suggested_cards: list[SuggestedCard]
