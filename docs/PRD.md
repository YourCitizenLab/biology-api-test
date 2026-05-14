# PRD: Interactive AI Bio/Chem Discovery Simulator Demo

## 1. Product Name

**Interactive AI Bio/Chem Discovery Simulator**

Chinese name: **交互式 AI 生物/化学产物探索模拟器**

---

## 2. Product Positioning

This demo is an interactive AI Agent for concept-level biological and chemical discovery exploration.

Users can explore hypothetical bio/chemical product concepts through:

- natural language input;
- drag-and-drop biological / chemical cards;
- multi-turn follow-up chat;
- evidence cards from public scientific databases;
- safety and risk explanations.

The product uses public scientific databases and an LLM orchestration layer to transform user inspiration into a traceable, evidence-backed, safety-bounded discovery concept.

This demo **does not provide wet-lab protocols, synthesis procedures, extraction steps, dosages, concentrations, temperatures, purification methods, or executable experimental instructions**.

---

## 3. Demo Goal

The demo should show that an AI Agent can:

1. understand abstract biological / chemical ideas;
2. extract and normalize entities;
3. call public scientific database APIs;
4. aggregate evidence from molecules, proteins, structures, bioactivity, and safety sources;
5. generate a concept-level candidate product;
6. explain the result through an interactive UI;
7. enforce safety boundaries for toxin, venom, pathogen, controlled chemical, or hazardous queries.

---

## 4. Target Users

| User Type | Use Case |
|---|---|
| DeSci / citizen science users | Explore scientific concepts in a low-barrier interface |
| Early-stage researchers | Quickly inspect related molecules, proteins, peptides, and structures |
| Product / investor demo viewers | Understand the AI + scientific database workflow |
| Education users | Learn relationships between biological entities, molecules, and functions |
| Startup team | Validate a future AI co-scientist / discovery simulator concept |

---

## 5. Core Demo Scenario

User input:

```text
Making a new peptide out of bull, tiger, and blue scorpion.
```

System interpretation:

```text
Bull -> mammalian protein source / Bos taurus reference
Tiger -> mammalian protein source / Panthera tigris reference
Blue scorpion -> venom peptide / toxin-related peptide source
Peptide -> bioactive peptide scaffold
```

Expected concept output:

```text
Candidate Concept:
Scorpion-inspired disulfide-rich peptide scaffold with mammalian motif references.

Possible Function Direction:
Ion-channel interaction simulation, antimicrobial peptide-like exploration, or stable peptide scaffold analysis.

Evidence:
Related protein / toxin peptide records from UniProt, structure references from RCSB PDB / AlphaFold DB, and bioactivity references from ChEMBL.

Risk:
High. Venom / toxin-related entity detected. Output is restricted to concept-level exploration only.
```

---

## 6. User Flow

### Flow A: Natural Language Discovery

1. User enters an idea in the input box.
2. System extracts biological / chemical entities.
3. System suggests related cards.
4. User starts the simulation.
5. Agent queries scientific databases.
6. Agent displays reasoning summary and evidence cards.
7. Result dashboard shows candidate concept, evidence, risk, and confidence.
8. User asks follow-up questions.

### Flow B: Drag-and-Drop Card Lab

1. User opens the interactive lab.
2. User drags cards into the simulation canvas.
3. Example cards: Bull, Tiger, Blue Scorpion, Peptide.
4. User clicks **Generate Candidate Concept**.
5. System runs the same Agent pipeline and returns a structured result.

---

## 7. Frontend Product Requirements

Frontend path:

```text
/frontend
```

Recommended stack:

```text
Next.js + React + TypeScript + Tailwind CSS + Framer Motion + React DnD
```

Required components:

```text
DiscoveryInput
CardLibrary
SimulationCanvas
AgentReasoningPanel
ResultDashboard
EvidenceDrawer
RiskBanner
FollowUpChat
```

### 7.1 Discovery Input

Allows natural language input.

Example placeholder:

```text
Describe your bio/chemical discovery idea...
```

Example prompts:

```text
Make a new peptide inspired by bull, tiger, and blue scorpion.
Explore a safer peptide scaffold inspired by venom proteins.
Find similar non-toxic antimicrobial peptide families.
```

### 7.2 Card Library

Cards should look visual and playful, similar to an educational science card board.

Card categories:

| Category | Examples |
|---|---|
| Animal Source | Bull, Tiger, Scorpion |
| Biomolecule | Peptide, Protein, Enzyme |
| Chemical Class | Alkaloid, Flavonoid, Terpene |
| Biological Function | Antimicrobial, Ion Channel, Anti-inflammatory |
| Risk Type | Venom, Toxin, Controlled Chemical |
| Database | PubChem, UniProt, ChEMBL, RCSB PDB |

### 7.3 Result Dashboard

Must include:

1. Candidate Concept;
2. Entity Mapping;
3. Evidence Cards;
4. Possible Function Direction;
5. Safety & Risk;
6. Confidence Score;
7. Suggested Follow-up Questions.

---

## 8. Backend Product Requirements

Backend path:

```text
/backend
```

Recommended stack:

```text
FastAPI + Python + Pydantic + HTTPX + Zhipu AI SDK + Redis + PostgreSQL
```

Required backend APIs:

```text
POST /api/simulate
POST /api/evidence/search
POST /api/chat/follow-up
POST /api/cards/suggest
GET /api/health
```

Backend responsibilities:

1. receive frontend requests;
2. call Zhipu AI for entity extraction and explanation generation;
3. call public scientific databases;
4. aggregate evidence;
5. run safety filters;
6. return structured JSON to the frontend.

---

## 9. Scientific Database APIs

### P0 APIs

| Database | Purpose |
|---|---|
| PubChem | compound identity, SMILES, molecular properties |
| UniProt | protein / peptide sequence, organism, functional annotation |
| ChEMBL | bioactivity, target, assay, drug-like molecules |
| RCSB PDB | experimental 3D structures and metadata |

### P1 APIs

| Database | Purpose |
|---|---|
| AlphaFold DB | predicted protein structures |
| EPA CompTox | toxicity, hazard, environmental risk |
| Rhea | biochemical reactions and enzyme-related pathways |

### P2 Data Sources

| Source | Purpose |
|---|---|
| Open Reaction Database | local reaction-template evidence |
| BRENDA | enzyme data and kinetics |
| USPTO reactions | reaction prediction / retrosynthesis research dataset |

---

## 10. Zhipu AI Integration

Zhipu AI is used as the Agent reasoning and language layer. It should not replace scientific databases.

Responsibilities:

```text
Entity extraction
Query planning
Result summarization
Candidate concept generation
Follow-up chat
Safety-aware explanation
```

API Key must be loaded from environment variables only:

```bash
ZHIPU_API_KEY=your_zhipu_api_key_here
```

The frontend must never directly access the Zhipu API key.

---

## 11. Safety Boundaries

### 11.1 Prohibited Outputs

The system must not provide:

```text
real synthesis steps
wet-lab protocol
extraction method
dosage
concentration
temperature
reaction time
purification method
pathogen handling
methods to enhance toxicity
methods to evade regulation or detection
controlled substance preparation
hazardous biological or chemical operational instructions
```

### 11.2 Allowed Outputs

The system may provide:

```text
concept-level scientific explanation
public database summaries
non-operational structure/function explanation
risk labels
confidence scores
safer alternative suggestions
educational visualizations
```

### 11.3 Risk Levels

| Level | Trigger | Output Strategy |
|---|---|---|
| Low | ordinary molecules / proteins | normal concept output |
| Medium | bioactive molecules / drug targets | add caution and uncertainty |
| High | venom, toxin, controlled chemical, pathogen | concept-only output, no methods |
| Blocked | requests for harmful synthesis or enhancement | refuse and redirect to safety education |

---

## 12. MVP Scope

### P0

- natural language input;
- drag-and-drop cards;
- `/api/simulate`;
- Zhipu AI integration;
- PubChem connector;
- UniProt connector;
- ChEMBL connector;
- RCSB PDB connector;
- result dashboard;
- safety filter;
- follow-up chat.

### P1

- AlphaFold connector;
- EPA CompTox connector;
- Rhea connector;
- evidence drawer;
- confidence score;
- Redis cache;
- demo history.

### P2

- ORD local dataset;
- Neo4j knowledge graph;
- pgvector semantic search;
- 3D structure viewer;
- account system;
- saved projects;
- exportable reports.

---

## 13. Success Metrics

| Metric | Target |
|---|---|
| Entity extraction success | > 80% |
| External API success | > 90% |
| Result generation time | < 10 seconds |
| Cached result generation | < 3 seconds |
| High-risk safety trigger | 100% |
| No experimental protocol leakage | 100% |
| Demo supports Jordan example | Yes |
| Drag-and-drop card interaction | Yes |
| Multi-turn follow-up chat | Yes |

---

## 14. Repository Requirement

All implementation code must be stored in:

```text
https://github.com/YourCitizenLab/biology-api-test
```

Recommended monorepo structure:

```text
/frontend   # Next.js frontend
/backend    # FastAPI backend
/docs       # PRD, TRD, demo script
/data       # demo cards and mock evidence
```

---

## 15. One-Sentence Product Summary

This demo turns a user's biological or chemical inspiration into an interactive, database-backed, safety-bounded discovery concept through AI Agent orchestration and visual scientific evidence cards.
