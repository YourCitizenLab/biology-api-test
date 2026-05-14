# TRD: Interactive AI Bio/Chem Discovery Simulator Demo

## 1. Technical Overview

This TRD defines the technical implementation for the **Interactive AI Bio/Chem Discovery Simulator Demo**.

The system is a monorepo-based web application with:

- a Next.js frontend;
- a FastAPI backend;
- Zhipu AI as the LLM / Agent orchestration layer;
- public scientific database connectors;
- safety filtering;
- structured evidence aggregation;
- interactive follow-up chat.

Repository:

```text
https://github.com/YourCitizenLab/biology-api-test
```

---

## 2. Repository Structure

Recommended structure:

```text
biology-api-test/
├── README.md
├── .gitignore
├── .env.example
├── docker-compose.yml
├── docs/
│   ├── PRD.md
│   ├── TRD.md
│   └── Demo-Script.md
│
├── frontend/
│   ├── package.json
│   ├── next.config.js
│   ├── tailwind.config.js
│   ├── tsconfig.json
│   └── src/
│       ├── app/
│       │   ├── page.tsx
│       │   ├── lab/
│       │   │   └── page.tsx
│       │   └── result/
│       │       └── page.tsx
│       ├── components/
│       │   ├── DiscoveryInput.tsx
│       │   ├── CardLibrary.tsx
│       │   ├── SimulationCanvas.tsx
│       │   ├── AgentReasoningPanel.tsx
│       │   ├── ResultDashboard.tsx
│       │   ├── EvidenceDrawer.tsx
│       │   ├── RiskBanner.tsx
│       │   └── FollowUpChat.tsx
│       ├── lib/
│       │   └── api.ts
│       └── styles/
│           └── globals.css
│
├── backend/
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── app/
│       ├── main.py
│       ├── config.py
│       ├── routers/
│       │   ├── simulate.py
│       │   ├── evidence.py
│       │   ├── chat.py
│       │   └── cards.py
│       ├── services/
│       │   ├── agent_service.py
│       │   ├── zhipu_service.py
│       │   ├── entity_service.py
│       │   ├── safety_service.py
│       │   ├── evidence_aggregator.py
│       │   └── database_router.py
│       ├── connectors/
│       │   ├── pubchem.py
│       │   ├── chembl.py
│       │   ├── uniprot.py
│       │   ├── rcsb_pdb.py
│       │   ├── alphafold.py
│       │   ├── comptox.py
│       │   └── rhea.py
│       ├── models/
│       │   ├── schemas.py
│       │   └── database.py
│       └── utils/
│           ├── http_client.py
│           └── logger.py
│
└── data/
    ├── demo_cards.json
    ├── sample_prompts.json
    └── mock_evidence.json
```

---

## 3. System Architecture

```text
User
↓
Next.js Frontend
↓
FastAPI Backend
↓
Agent Orchestrator
↓
Zhipu AI Service
↓
Entity Extraction / Query Planning / Explanation Generation
↓
Database Router
↓
Scientific Database Connectors
↓
Evidence Aggregator
↓
Safety Filter
↓
Structured JSON Response
↓
Interactive Result Dashboard
```

---

## 4. Frontend Architecture

### 4.1 Technology Stack

```text
Next.js
React
TypeScript
Tailwind CSS
Framer Motion
React DnD
```

### 4.2 Main Pages

| Page | Path | Purpose |
|---|---|---|
| Home | `/` | natural language discovery input |
| Lab | `/lab` | drag-and-drop interactive card lab |
| Result | `/result` | candidate concept and evidence dashboard |

### 4.3 Main Components

| Component | Responsibility |
|---|---|
| `DiscoveryInput` | accepts natural language prompt |
| `CardLibrary` | displays draggable bio/chem cards |
| `SimulationCanvas` | receives selected cards |
| `AgentReasoningPanel` | shows user-visible reasoning summary |
| `ResultDashboard` | displays final structured result |
| `EvidenceDrawer` | displays external database evidence |
| `RiskBanner` | displays safety warnings |
| `FollowUpChat` | handles multi-turn questions |

### 4.4 Frontend API Client

File:

```text
frontend/src/lib/api.ts
```

Responsibilities:

```text
call /api/simulate
call /api/evidence/search
call /api/chat/follow-up
call /api/cards/suggest
handle loading states
handle API errors
```

---

## 5. Backend Architecture

### 5.1 Technology Stack

```text
FastAPI
Python 3.11+
Pydantic
HTTPX
Zhipu AI SDK
Redis
PostgreSQL
```

### 5.2 Backend Entry

```text
backend/app/main.py
```

Required FastAPI routers:

```text
/api/simulate
/api/evidence/search
/api/chat/follow-up
/api/cards/suggest
/api/health
```

---

## 6. API Design

### 6.1 Health API

```http
GET /api/health
```

Response:

```json
{
  "status": "ok",
  "service": "biology-api-test"
}
```

---

### 6.2 Simulate API

```http
POST /api/simulate
```

Request:

```json
{
  "input": "Making a new peptide out of bull, tiger, and blue scorpion.",
  "cards": ["Bull", "Tiger", "Blue Scorpion", "Peptide"],
  "mode": "interactive_demo",
  "output_level": "concept_only"
}
```

Response:

```json
{
  "candidate_concept": {
    "name": "Scorpion-Inspired Peptide Scaffold Concept",
    "description": "A hypothetical peptide concept inspired by scorpion venom peptide scaffolds and mammalian protein motif references.",
    "status": "simulation_only"
  },
  "entities": [
    {
      "raw": "blue scorpion",
      "normalized": "scorpion venom peptide",
      "type": "venom_peptide",
      "risk": "high",
      "databases": ["UniProt", "RCSB PDB", "AlphaFold DB", "ChEMBL"]
    }
  ],
  "evidence": [
    {
      "source": "UniProt",
      "records_found": 10,
      "summary": "Related toxin peptide entries found.",
      "confidence": "medium"
    }
  ],
  "risk": {
    "level": "high",
    "reason": "Venom/toxin-related entity detected.",
    "allowed_output": "concept_only"
  },
  "follow_up_questions": [
    "Why is blue scorpion related to venom peptides?",
    "Show related peptide structures.",
    "Can this concept be made safer?",
    "Explain this for non-scientists."
  ],
  "confidence_score": 0.62
}
```

---

### 6.3 Evidence Search API

```http
POST /api/evidence/search
```

Request:

```json
{
  "query": "scorpion toxin peptide",
  "databases": ["uniprot", "pdb", "chembl"]
}
```

Response:

```json
{
  "results": [
    {
      "database": "UniProt",
      "records_found": 10,
      "top_records": [
        {
          "name": "toxin-related peptide record",
          "organism": "scorpion species",
          "summary": "Venom peptide-related protein annotation."
        }
      ]
    }
  ]
}
```

---

### 6.4 Follow-up Chat API

```http
POST /api/chat/follow-up
```

Request:

```json
{
  "simulation_id": "sim_001",
  "message": "Can this concept be made safer?",
  "context": {
    "candidate_name": "Scorpion-Inspired Peptide Scaffold Concept",
    "risk_level": "high"
  }
}
```

Response:

```json
{
  "answer": "A safer exploration direction would avoid toxin-like functional claims and focus on non-toxic peptide scaffold stability or general structure-function education.",
  "risk_level": "medium",
  "suggested_actions": [
    "Search non-toxic antimicrobial peptide families",
    "Remove venom/toxin card",
    "Replace Blue Scorpion with Plant Peptide"
  ]
}
```

---

### 6.5 Card Suggestion API

```http
POST /api/cards/suggest
```

Request:

```json
{
  "input": "I want something inspired by venom but safer"
}
```

Response:

```json
{
  "suggested_cards": [
    {
      "name": "Antimicrobial Peptide",
      "category": "Biomolecule",
      "risk": "medium"
    },
    {
      "name": "Plant Peptide",
      "category": "Biomolecule",
      "risk": "low"
    }
  ]
}
```

---

## 7. Zhipu AI Integration

### 7.1 Purpose

Zhipu AI is used for:

```text
entity extraction
query planning
candidate concept generation
plain-language explanation
follow-up chat
safety-aware response formatting
```

It must not be the sole source of scientific facts. Scientific evidence should come from external database connectors whenever possible.

### 7.2 Environment Variables

```bash
ZHIPU_API_KEY=your_zhipu_api_key_here
ZHIPU_MODEL=glm-4-plus
```

### 7.3 Service File

```text
backend/app/services/zhipu_service.py
```

### 7.4 System Prompt Requirement

The system prompt must include:

```text
You are a scientific discovery assistant for concept-level bio/chemical exploration.
You must not provide synthesis steps, experimental protocols, extraction methods, dosages, concentrations, temperatures, purification methods, or harmful operational instructions.
When toxins, venom, pathogens, controlled chemicals, or hazardous bioactivity are involved, restrict the output to high-level concept explanation, public database evidence, and safety warnings.
Always distinguish database-backed evidence, scientific inference, and hypothetical concept generation.
```

---

## 8. Scientific Database Connectors

Connector path:

```text
backend/app/connectors/
```

### 8.1 PubChem Connector

File:

```text
backend/app/connectors/pubchem.py
```

Purpose:

```text
compound identity
CID
SMILES
molecular formula
molecular weight
synonyms
```

Example endpoint:

```text
https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/property/CanonicalSMILES,MolecularFormula,MolecularWeight/JSON
```

### 8.2 UniProt Connector

File:

```text
backend/app/connectors/uniprot.py
```

Purpose:

```text
protein sequence
peptide annotation
organism
toxin-related records
functional annotation
```

Example endpoint:

```text
https://rest.uniprot.org/uniprotkb/search?query=scorpion%20toxin%20peptide&format=json&size=10
```

### 8.3 ChEMBL Connector

File:

```text
backend/app/connectors/chembl.py
```

Purpose:

```text
bioactivity
targets
assays
small molecule records
```

Example endpoint:

```text
https://www.ebi.ac.uk/chembl/api/data/molecule/search?q=scorpion
```

### 8.4 RCSB PDB Connector

File:

```text
backend/app/connectors/rcsb_pdb.py
```

Purpose:

```text
3D experimental structures
PDB entry metadata
experimental method
resolution
```

Example endpoint:

```text
https://data.rcsb.org/rest/v1/core/entry/{pdb_id}
```

### 8.5 AlphaFold Connector

File:

```text
backend/app/connectors/alphafold.py
```

Purpose:

```text
predicted protein structures
confidence data
PDB/mmCIF file URLs
```

Example endpoint:

```text
https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}
```

### 8.6 EPA CompTox Connector

File:

```text
backend/app/connectors/comptox.py
```

Purpose:

```text
toxicity
hazard
exposure
environmental safety
```

Requires API key when enabled:

```bash
EPA_COMPTOX_API_KEY=your_epa_key_here
```

### 8.7 Rhea Connector

File:

```text
backend/app/connectors/rhea.py
```

Purpose:

```text
biochemical reactions
enzyme-related pathways
substrate-product relationships
```

---

## 9. Agent Workflow

```text
1. Receive user input and selected cards.
2. Run safety pre-check.
3. Use Zhipu AI to extract structured entities.
4. Normalize entity types.
5. Route entities to suitable database connectors.
6. Fetch public database evidence.
7. Aggregate and deduplicate evidence.
8. Run safety post-check.
9. Use Zhipu AI to generate concept-level response.
10. Validate output against safety policy.
11. Return structured JSON to frontend.
```

---

## 10. Safety Filter Design

Service file:

```text
backend/app/services/safety_service.py
```

### 10.1 Pre-check

Detect risky intent before external API calls.

High-risk keywords include:

```text
toxin
venom
poison
pathogen
virus
bacteria culture
synthesis protocol
extract
purify
weaponize
enhance toxicity
dosage
concentration
temperature
reaction time
```

### 10.2 Post-check

Validate generated output to ensure it does not contain operational instructions.

Blocked content includes:

```text
step-by-step wet lab procedures
exact reaction conditions
specific extraction or purification instructions
instructions to enhance toxicity or biological activity
controlled chemical preparation
pathogen manipulation
```

### 10.3 Output Modes

| Mode | Description |
|---|---|
| `normal` | normal educational concept output |
| `caution` | medium-risk output with disclaimers |
| `concept_only` | high-risk concept-only explanation |
| `blocked` | refusal and safer redirection |

---

## 11. Data Models

### 11.1 Simulation

```sql
CREATE TABLE simulations (
  id UUID PRIMARY KEY,
  user_input TEXT,
  cards JSONB,
  candidate_name TEXT,
  candidate_description TEXT,
  risk_level TEXT,
  confidence_score FLOAT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### 11.2 Entity

```sql
CREATE TABLE entities (
  id UUID PRIMARY KEY,
  simulation_id UUID REFERENCES simulations(id),
  raw_text TEXT,
  normalized_name TEXT,
  entity_type TEXT,
  risk_level TEXT,
  databases JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### 11.3 Evidence

```sql
CREATE TABLE evidence (
  id UUID PRIMARY KEY,
  simulation_id UUID REFERENCES simulations(id),
  entity_id UUID REFERENCES entities(id),
  source_database TEXT,
  source_record_id TEXT,
  query TEXT,
  summary TEXT,
  confidence TEXT,
  raw_response JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### 11.4 Chat Message

```sql
CREATE TABLE chat_messages (
  id UUID PRIMARY KEY,
  simulation_id UUID REFERENCES simulations(id),
  role TEXT,
  message TEXT,
  risk_level TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 12. Environment Variables

`.env.example` should include:

```bash
BACKEND_ENV=development
BACKEND_PORT=8000
ZHIPU_API_KEY=your_zhipu_api_key_here
ZHIPU_MODEL=glm-4-plus
EPA_COMPTOX_API_KEY=your_epa_comptox_api_key_here
DATABASE_URL=postgresql://biology:biology@localhost:5432/biology_demo
REDIS_URL=redis://localhost:6379/0
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

Never commit real secrets.

---

## 13. Local Development

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Windows PowerShell:

```bash
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

Backend URL:

```text
http://localhost:8000
```

---

## 14. Error Handling

### 14.1 External API Failure

If one database fails, the system should:

1. continue using other databases;
2. return partial evidence;
3. show a warning in the evidence card;
4. not fail the entire simulation unless all evidence sources fail.

### 14.2 Zhipu AI Failure

If Zhipu AI fails:

1. return a structured error;
2. show retry option;
3. optionally return mock demo result for the Jordan example.

### 14.3 Safety Failure

If output violates safety rules:

1. block unsafe sections;
2. regenerate safer response;
3. if still unsafe, return refusal and safe explanation.

---

## 15. Caching Strategy

Use Redis for:

```text
PubChem query cache
UniProt query cache
ChEMBL query cache
RCSB PDB query cache
AlphaFold query cache
Zhipu entity extraction cache
simulation result cache
```

Recommended TTL:

```text
external database results: 24 hours
Zhipu extraction result: 6 hours
simulation result: 24 hours
```

---

## 16. Deployment Plan

### MVP Deployment

Recommended:

```text
Frontend: Vercel
Backend: Render / Railway / Fly.io / AWS ECS
Database: Supabase Postgres or managed PostgreSQL
Cache: Upstash Redis or managed Redis
```

### Demo Constraints

For the first demo, it is acceptable to use:

```text
mock data fallback
limited external API calls
no authentication
single demo environment
manual environment variable setup
```

---

## 17. MVP Implementation Checklist

### Backend P0

- [ ] FastAPI app initialized
- [ ] `/api/health`
- [ ] `/api/simulate`
- [ ] Zhipu AI service
- [ ] Safety service
- [ ] Entity extraction service
- [ ] PubChem connector
- [ ] UniProt connector
- [ ] ChEMBL connector
- [ ] RCSB PDB connector
- [ ] Evidence aggregator

### Frontend P0

- [ ] Next.js app initialized
- [ ] Discovery input
- [ ] Card library
- [ ] Simulation canvas
- [ ] Result dashboard
- [ ] Risk banner
- [ ] Follow-up chat basic UI

### Docs P0

- [ ] PRD
- [ ] TRD
- [ ] Demo Script
- [ ] README
- [ ] `.env.example`

---

## 18. Technical Summary

The system should be implemented as a monorepo in `YourCitizenLab/biology-api-test`, with frontend code under `/frontend`, backend code under `/backend`, and product / technical documentation under `/docs`. The backend orchestrates Zhipu AI and public scientific database connectors to generate structured, safe, concept-level discovery results for the interactive frontend.
