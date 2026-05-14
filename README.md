# Interactive AI Bio/Chem Discovery Simulator

This repository contains the demo implementation plan for an interactive AI Agent that helps users explore concept-level biological and chemical discovery ideas through natural language, draggable cards, public scientific database APIs, and safety-bounded AI explanations.

Repository:

```text
https://github.com/YourCitizenLab/biology-api-test
```

---

## 1. Product Summary

The demo turns a user's abstract biological or chemical inspiration into a structured, database-backed, safety-aware discovery concept.

Example prompt:

```text
Making a new peptide out of bull, tiger, and blue scorpion.
```

Expected output:

```text
A scorpion-inspired peptide scaffold concept with mammalian motif references, supported by public database evidence and restricted to concept-level explanation only.
```

This project is **not** a wet-lab protocol generator. It does not provide synthesis steps, extraction methods, dosage, concentration, temperature, purification methods, or other operational experimental instructions.

---

## 2. Documentation

Project documents are stored under `/docs`:

```text
docs/PRD.md          # product requirements
docs/TRD.md          # technical requirements
docs/Demo-Script.md  # demo presentation script
```

Recommended reading order:

1. `docs/PRD.md`
2. `docs/TRD.md`
3. `docs/Demo-Script.md`

---

## 3. Planned Architecture

```text
User
↓
Next.js Frontend
↓
FastAPI Backend
↓
Zhipu AI Agent Service
↓
Scientific Database Connectors
↓
Evidence Aggregator
↓
Safety Filter
↓
Interactive Result Dashboard
```

---

## 4. Planned Repository Structure

```text
biology-api-test/
├── README.md
├── .gitignore
├── .env.example
├── docs/
│   ├── PRD.md
│   ├── TRD.md
│   └── Demo-Script.md
├── frontend/
│   └── Next.js frontend application
├── backend/
│   └── FastAPI backend application
└── data/
    └── demo cards and mock evidence
```

---

## 5. Planned Tech Stack

### Frontend

```text
Next.js
React
TypeScript
Tailwind CSS
Framer Motion
React DnD
```

### Backend

```text
FastAPI
Python
Pydantic
HTTPX
Zhipu AI SDK
Redis
PostgreSQL
```

### External Scientific Databases

P0:

```text
PubChem
UniProt
ChEMBL
RCSB PDB
```

P1:

```text
AlphaFold DB
EPA CompTox
Rhea
```

P2:

```text
Open Reaction Database
BRENDA
USPTO reaction dataset
```

---

## 6. Environment Variables

Copy `.env.example` to `.env` locally:

```bash
cp .env.example .env
```

Then fill in local keys:

```bash
ZHIPU_API_KEY=your_zhipu_api_key_here
```

Never commit real API keys.

---

## 7. Planned Local Development

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

URLs:

```text
Frontend: http://localhost:3000
Backend:  http://localhost:8000
Health:   http://localhost:8000/api/health
```

---

## 8. Planned Backend APIs

```text
GET  /api/health
POST /api/simulate
POST /api/evidence/search
POST /api/chat/follow-up
POST /api/cards/suggest
```

---

## 9. Safety Boundary

The system must not output:

```text
real synthesis steps
wet-lab protocols
extraction methods
dosage
concentration
temperature
reaction time
purification methods
pathogen handling
methods to enhance toxicity
methods to evade regulation or detection
controlled substance preparation
hazardous biological or chemical operational instructions
```

The system may output:

```text
concept-level scientific explanation
public database summaries
non-operational structure/function explanation
risk labels
confidence scores
safer alternative suggestions
educational visualizations
```

---

## 10. MVP Checklist

Backend P0:

- [ ] FastAPI app initialized
- [ ] `/api/health`
- [ ] `/api/simulate`
- [ ] Zhipu AI service
- [ ] safety service
- [ ] entity extraction service
- [ ] PubChem connector
- [ ] UniProt connector
- [ ] ChEMBL connector
- [ ] RCSB PDB connector
- [ ] evidence aggregator

Frontend P0:

- [ ] Next.js app initialized
- [ ] discovery input
- [ ] card library
- [ ] simulation canvas
- [ ] result dashboard
- [ ] risk banner
- [ ] follow-up chat basic UI

Docs P0:

- [x] PRD
- [x] TRD
- [x] Demo Script
- [x] README
- [x] `.env.example`

---

## 11. Demo Story

The primary demo should use the Jordan example:

```text
Making a new peptide out of bull, tiger, and blue scorpion.
```

The system should explain:

```text
Bull and tiger are interpreted as mammalian biological references.
Blue scorpion is interpreted as a venom peptide / toxin-related source.
Peptide is interpreted as a bioactive peptide scaffold.
```

The output should remain concept-level and include a high-risk safety warning because venom/toxin-related biology is involved.
