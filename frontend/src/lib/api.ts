export type RiskLevel = "low" | "medium" | "high" | "blocked";

export type Entity = {
  raw: string;
  normalized: string;
  type: string;
  risk: RiskLevel;
  databases: string[];
};

export type EvidenceItem = {
  source: string;
  records_found: number;
  summary: string;
  confidence: "low" | "medium" | "high";
  query?: string | null;
  top_records: Array<Record<string, string>>;
};

export type SimulationResult = {
  candidate_concept: {
    name: string;
    description: string;
    status: "simulation_only";
    possible_function_direction: string[];
  };
  entities: Entity[];
  evidence: EvidenceItem[];
  risk: {
    level: RiskLevel;
    reason: string;
    allowed_output: "normal" | "caution" | "concept_only" | "blocked";
    safer_alternatives: string[];
  };
  follow_up_questions: string[];
  confidence_score: number;
};

export type FollowUpResponse = {
  answer: string;
  risk_level: RiskLevel;
  suggested_actions: string[];
};

const apiBaseUrl = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

async function postJson<T>(path: string, body: unknown): Promise<T> {
  const response = await fetch(`${apiBaseUrl}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!response.ok) {
    throw new Error(`Request failed with ${response.status}`);
  }
  return response.json() as Promise<T>;
}

export function simulateDiscovery(input: string, cards: string[]) {
  return postJson<SimulationResult>("/api/simulate", {
    input,
    cards,
    mode: "interactive_demo",
    output_level: "concept_only",
  });
}

export function askFollowUp(message: string, result: SimulationResult | null) {
  return postJson<FollowUpResponse>("/api/chat/follow-up", {
    simulation_id: "local-demo",
    message,
    context: {
      candidate_name: result?.candidate_concept.name,
      risk_level: result?.risk.level,
    },
  });
}
