# Interactive AI Bio/Chem Discovery Simulator

This repository contains the demo implementation plan for an interactive AI Agent that helps users explore concept-level biological and chemical discovery ideas through natural language, draggable cards, public scientific database APIs, and safety-bounded AI explanations.

Repository:

```text
https://github.com/YourCitizenLab/biology-api-test
```

Correct local path:

```text
G:\workspace\YourCitizenLab\biology-api-test
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
docs/PRD.md                    # product requirements
docs/TRD.md                    # technical requirements
docs/Demo-Script.md            # demo presentation script
docs/Engineering-Workflow.md   # engineering workflow and contribution rules
```

Recommended reading order:

1. `docs/Engineering-Workflow.md`
2. `docs/PRD.md`
3. `docs/TRD.md`
4. `docs/Demo-Script.md`

For Codex or any AI coding agent, always read `docs/Engineering-Workflow.md` before making code changes.

---

## 3. Planned Architecture

```text
User
↓
Next.js Frontend
↓
FastAPI Backend
↓
DeepSeek AI Agent Service
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
│   ├── Demo-Script.md
│   └── Engineering-Workflow.md
├── frontend/
│   └── Next.js frontend application
├── backend/
│   └── FastAPI backend application
└── data/
    └── demo cards and mock evidence
```

---

## 5. Required Engineering Workflow

All contributors, including Codex or any AI coding agent, must follow this workflow:

```text
clone to G:\workspace\YourCitizenLab\biology-api-test
↓
sync main
↓
create feature branch
↓
read docs
↓
implement focused task
↓
run tests
↓
review local diff
↓
commit
↓
push feature branch
↓
open Pull Request
↓
code review
↓
squash merge to main
↓
pull latest main locally
↓
delete completed branch
```

Never commit directly to `main`.

Full rules are documented in:

```text
docs/Engineering-Workflow.md
```

---

## 6. Planned Tech Stack

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
DeepSeek API (OpenAI-compatible)
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

## 7. Environment Variables

Copy `.env.example` to `.env` locally:

```bash
cp .env.example .env
```

Then fill in local keys:

```bash
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

Never commit real API keys.

---

## 8. Planned Local Development

### Clone locally

Windows PowerShell:

```powershell
cd /d G:\workspace
mkdir YourCitizenLab
cd YourCitizenLab
git clone https://github.com/YourCitizenLab/biology-api-test.git
cd biology-api-test
```

If `YourCitizenLab` already exists:

```powershell
cd /d G:\workspace\YourCitizenLab
git clone https://github.com/YourCitizenLab/biology-api-test.git
cd biology-api-test
```

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

## 9. Planned Backend APIs

```text
GET  /api/health
POST /api/simulate
POST /api/evidence/search
POST /api/chat/follow-up
POST /api/cards/suggest
```

---

## 10. Safety Boundary

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

## 11. MVP Checklist

Backend P0:

- [ ] FastAPI app initialized
- [ ] `/api/health`
- [ ] `/api/simulate`
- [ ] DeepSeek AI service
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
- [x] Engineering Workflow
- [x] README
- [x] `.env.example`

---

## 12. Demo Story

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

---

## 13. Working MVP Local Run

### Backend

Windows PowerShell:

```powershell
cd G:\workspace\YourCitizenLab\biology-api-test\backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Health check:

```powershell
curl http://localhost:8000/api/health
```

Jordan simulation check:

```powershell
curl -X POST http://localhost:8000/api/simulate ^
  -H "Content-Type: application/json" ^
  -d "{\"input\":\"Making a new peptide out of bull, tiger, and blue scorpion.\",\"cards\":[\"Bull\",\"Tiger\",\"Blue Scorpion\",\"Peptide\"],\"mode\":\"interactive_demo\",\"output_level\":\"concept_only\"}"
```

### Frontend

Windows PowerShell:

```powershell
cd G:\workspace\YourCitizenLab\biology-api-test\frontend
npm install
npm run dev
```

Open:

```text
http://localhost:3000
```

### Environment Variables

For local development, copy `.env.example` to `.env` and keep real values local only.

```text
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

`NEXT_PUBLIC_API_BASE_URL` is safe for the browser. Do not put API keys or backend secrets in any `NEXT_PUBLIC_*` variable.

### Demo Prompt

```text
Making a new peptide out of bull, tiger, and blue scorpion.
```

Expected behavior:

- Bull and tiger map to mammalian biological references.
- Blue Scorpion maps to a venom peptide / toxin-related source.
- Peptide maps to a bioactive peptide scaffold.
- The result returns high risk and `concept_only` allowed output.

### Current MVP Limitations

- External database connectors are lightweight and use mock fallback evidence when calls fail.
- DeepSeek uses deterministic mock output when `DEEPSEEK_API_KEY` is missing.
- No production database, authentication, deployment pipeline, or saved project history yet.
- The app is restricted to concept-level educational output and does not provide operational bio/chem instructions.
