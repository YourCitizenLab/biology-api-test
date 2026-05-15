# Engineering Workflow & Contribution Guidelines

## 1. Purpose

This document defines the required engineering workflow for the `biology-api-test` repository.

It is intended for:

- human developers;
- Codex / AI coding agents;
- reviewers;
- technical leads;
- external collaborators.

The goal is to ensure that all design, development, review, commit, push, pull request, merge, rollback, and release activities follow a consistent professional full-stack engineering process.

Repository:

```text
https://github.com/YourCitizenLab/biology-api-test
```

Default branch:

```text
main
```

Correct local organization workspace:

```text
G:\workspace\YourCitizenLab
```

Correct local repository path:

```text
G:\workspace\YourCitizenLab\biology-api-test
```

---

## 2. Core Engineering Principles

All contributors must follow these principles:

1. **Never work directly on `main`.**
2. **Always create a feature branch for each task.**
3. **Keep each branch focused on one logical change.**
4. **Read the relevant PRD / TRD before implementation.**
5. **Write code that is testable, readable, and easy to review.**
6. **Do not commit secrets, API keys, tokens, or local environment files.**
7. **Run local checks before committing.**
8. **Use Pull Requests for all changes.**
9. **Require human review before merging.**
10. **Prefer small, incremental PRs over large unreviewable changes.**
11. **Keep the safety boundary of this project intact.**
12. **Document known limitations clearly.**
13. **Keep local paths consistent with the organization-level workspace layout.**

---

## 3. Project-Specific Safety Requirement

This project is an AI Bio/Chem Discovery Simulator. It must remain a **concept-level discovery and education tool**.

The system must not generate or expose:

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

Allowed outputs:

```text
concept-level scientific explanation
public database summaries
non-operational structure/function explanation
risk labels
confidence scores
safer alternative suggestions
educational visualizations
```

Every backend response and AI-generated result must preserve this boundary.

---

## 4. Required Documents to Read Before Development

Before starting any task, read the relevant files:

```text
README.md
docs/Engineering-Workflow.md
docs/PRD.md
docs/TRD.md
docs/Demo-Script.md
```

For implementation tasks, `docs/TRD.md` is the primary technical reference.

For UI / product behavior, `docs/PRD.md` is the primary product reference.

For demo behavior, `docs/Demo-Script.md` is the primary presentation reference.

For all Git, Codex, review, branch, commit, merge, and rollback behavior, `docs/Engineering-Workflow.md` is the source of truth.

---

## 5. Local Development Setup

### 5.1 Clone Repository Locally

Use an organization-level workspace so all repos under `YourCitizenLab` stay grouped together.

Correct local workspace:

```text
G:\workspace\YourCitizenLab
```

Correct local repo path:

```text
G:\workspace\YourCitizenLab\biology-api-test
```

HTTPS clone:

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

Alternative SSH clone:

```powershell
cd /d G:\workspace
mkdir YourCitizenLab
cd YourCitizenLab
git clone git@github.com:YourCitizenLab/biology-api-test.git
cd biology-api-test
```

If the repo already exists locally:

```powershell
cd /d G:\workspace\YourCitizenLab\biology-api-test
git status
git remote -v
```

### 5.2 Verify Git Remote

```bash
git remote -v
```

Expected remote:

```text
origin  https://github.com/YourCitizenLab/biology-api-test.git
```

or SSH equivalent:

```text
origin  git@github.com:YourCitizenLab/biology-api-test.git
```

### 5.3 Sync Local Main

Always start from an up-to-date `main`:

```bash
git checkout main
git pull origin main
```

---

## 6. Branching Strategy

### 6.1 Never Commit Directly to Main

Do not run implementation work on `main`.

Bad:

```bash
git checkout main
# edit files directly
# commit directly to main
```

Good:

```bash
git checkout main
git pull origin main
git checkout -b feature/backend-mvp-skeleton
```

### 6.2 Branch Naming Convention

Use descriptive branch names:

```text
feature/backend-mvp-skeleton
feature/zhipu-integration
feature/scientific-connectors
feature/frontend-mvp
feature/frontend-backend-integration
fix/backend-cors
fix/safety-filter-edge-case
docs/update-trd
docs/engineering-workflow
chore/update-dependencies
refactor/evidence-aggregator
```

Recommended prefixes:

| Prefix | Use Case |
|---|---|
| `feature/` | new feature |
| `fix/` | bug fix |
| `docs/` | documentation only |
| `chore/` | tooling, dependency, config |
| `refactor/` | code restructuring without behavior change |
| `test/` | tests only |
| `hotfix/` | urgent production fix |

### 6.3 One Branch, One Purpose

Each branch should have one clear purpose.

Good:

```text
feature/backend-mvp-skeleton
```

Bad:

```text
feature/backend-frontend-db-docs-everything
```

---

## 7. Recommended Development Sequence

The project should be developed in small stages:

```text
Task 1: Backend MVP skeleton
Task 2: Zhipu AI integration
Task 3: Scientific database connectors
Task 4: Frontend MVP
Task 5: Frontend-backend integration
Task 6: Safety filter hardening
Task 7: Deployment and demo polish
```

Each task should have its own branch and Pull Request.

---

## 8. Codex / AI Coding Agent Workflow

When using Codex or any AI coding agent, the agent must follow the same engineering rules as a human developer.

### 8.1 Required Agent Behavior

Codex must:

1. inspect the repository before editing;
2. read `README.md`, `docs/Engineering-Workflow.md`, `docs/PRD.md`, `docs/TRD.md`, and `docs/Demo-Script.md`;
3. propose an implementation plan before modifying files;
4. wait for approval when requested;
5. make changes only on a feature branch;
6. avoid modifying unrelated files;
7. run or describe tests;
8. summarize changed files;
9. ask for approval before commit if operating locally;
10. never commit secrets;
11. never push directly to `main`;
12. use `G:\workspace\YourCitizenLab\biology-api-test` as the local repo path when operating in the user's local Windows environment.

### 8.2 Standard Codex Prompt Header

Use this header for every Codex task:

```text
Context:
This repository is for the Interactive AI Bio/Chem Discovery Simulator MVP.

Repository:
https://github.com/YourCitizenLab/biology-api-test

Local organization workspace:
G:\workspace\YourCitizenLab

Local repository path:
G:\workspace\YourCitizenLab\biology-api-test

Required docs to read first:
- README.md
- docs/Engineering-Workflow.md
- docs/PRD.md
- docs/TRD.md
- docs/Demo-Script.md

Workflow:
- Do not work directly on main.
- Create a focused feature branch.
- Keep the scope limited to the task.
- Do not add real API keys.
- Do not expose secrets in frontend code.
- Run relevant tests before proposing completion.
- Ask for approval before commit/push if working locally.

Safety:
All outputs must remain concept-level only and must not include synthesis steps, wet-lab protocols, extraction methods, dosages, concentrations, temperatures, purification methods, pathogen handling, toxicity enhancement, or operational biological/chemical instructions.
```

### 8.3 Codex Task Prompt Template

```text
Task:
[Describe exactly what to implement.]

Branch:
[feature/name]

Files likely to modify:
[List expected files.]

Out of scope:
[List what Codex must not do.]

Acceptance criteria:
[List clear measurable results.]

Testing:
[List commands to run.]

Deliverables:
- changed files summary
- test results
- known limitations
- PR summary draft

Please first inspect the repository and propose an implementation plan before editing files.
```

---

## 9. Git Workflow

### 9.1 Start a New Task

```bash
git checkout main
git pull origin main
git checkout -b feature/backend-mvp-skeleton
```

### 9.2 Check Current Status

```bash
git status
```

Use this often.

### 9.3 Review Changes Locally

```bash
git diff
```

For staged changes:

```bash
git diff --cached
```

### 9.4 Stage Changes

Stage all changes:

```bash
git add .
```

Or stage specific files:

```bash
git add backend/app/main.py backend/app/routers/simulate.py
```

### 9.5 Commit Changes

Use a clear message:

```bash
git commit -m "Implement backend MVP skeleton"
```

Prefer conventional style when possible:

```text
feat: implement backend MVP skeleton
fix: handle missing Zhipu API key
chore: add environment variable template
docs: add engineering workflow
refactor: simplify evidence aggregation
```

### 9.6 Push Feature Branch

```bash
git push origin feature/backend-mvp-skeleton
```

### 9.7 Create Pull Request

Create a PR from:

```text
base: main
compare: feature/backend-mvp-skeleton
```

Use GitHub web UI or GitHub CLI if available.

### 9.8 After PR Merge

Update local `main`:

```bash
git checkout main
git pull origin main
```

Delete local branch:

```bash
git branch -d feature/backend-mvp-skeleton
```

Delete remote branch when no longer needed:

```bash
git push origin --delete feature/backend-mvp-skeleton
```

---

## 10. Commit Message Rules

Good commit messages are short, specific, and action-oriented.

Recommended format:

```text
<type>: <short summary>
```

Examples:

```text
feat: implement backend MVP skeleton
feat: add Zhipu AI service wrapper
fix: prevent unsafe protocol output
fix: handle failed UniProt API response
docs: add engineering workflow
chore: update gitignore
refactor: split safety service from agent service
test: add simulate endpoint smoke test
```

Allowed types:

| Type | Meaning |
|---|---|
| `feat` | new feature |
| `fix` | bug fix |
| `docs` | documentation |
| `chore` | maintenance/config |
| `refactor` | code restructuring |
| `test` | tests |
| `style` | formatting only |
| `perf` | performance improvement |
| `ci` | CI/CD changes |

Avoid vague messages:

```text
update
fix stuff
changes
new code
final
```

---

## 11. Pull Request Rules

### 11.1 PR Size

Prefer small PRs.

A PR should ideally:

```text
focus on one task
be easy to review within 15-30 minutes
avoid unrelated formatting changes
include test evidence
include clear screenshots for UI changes
```

### 11.2 PR Title Format

Use:

```text
<type>: <summary>
```

Examples:

```text
feat: implement backend MVP skeleton
feat: add interactive card lab frontend
fix: enforce concept-only output for venom queries
docs: add engineering workflow
```

### 11.3 PR Description Template

Use this template:

```markdown
## Summary
- 
- 
- 

## Changed Files
- 
- 

## Test Plan
- [ ] 
- [ ] 

## Test Results
\```text
Paste command outputs or summarize results here.
\```

## Safety Notes
- No secrets committed.
- No unsafe wet-lab or synthesis instructions added.
- High-risk bio/chem inputs remain concept-only.

## Screenshots / Demo
Add screenshots or screen recordings for frontend changes.

## Known Limitations
- 

## Follow-up Tasks
- 
```

### 11.4 Required Review Before Merge

Every PR must be reviewed before merge.

Reviewers should check:

```text
scope matches task
code is readable
tests pass
no secrets are committed
safety boundary is preserved
frontend does not expose backend secrets
external API failures are handled gracefully
README or docs are updated if needed
```

---

## 12. Code Review Checklist

### 12.1 General Review

- [ ] Does the PR match the task scope?
- [ ] Are unrelated files avoided?
- [ ] Is the code readable and maintainable?
- [ ] Are function names clear?
- [ ] Is error handling present?
- [ ] Are edge cases handled?
- [ ] Are docs updated when behavior changes?

### 12.2 Backend Review

- [ ] FastAPI routes are typed with Pydantic schemas.
- [ ] API responses are structured and predictable.
- [ ] External API calls use timeouts.
- [ ] External API failures do not crash the entire simulation.
- [ ] Secrets are read from environment variables only.
- [ ] CORS is configured intentionally.
- [ ] Safety filtering is applied before and after LLM generation.

### 12.3 Frontend Review

- [ ] UI states handle loading, success, and error.
- [ ] Backend errors are displayed gracefully.
- [ ] API base URL uses environment variable.
- [ ] No secret API keys are included in frontend code.
- [ ] Components are reusable and not overly large.
- [ ] Accessibility is considered for buttons, inputs, and interactive cards.

### 12.4 AI / Agent Review

- [ ] Prompt includes safety boundary.
- [ ] LLM outputs are treated as untrusted until checked.
- [ ] Scientific claims are tied to evidence where possible.
- [ ] High-risk inputs return `concept_only` or `blocked` mode.
- [ ] No operational wet-lab or hazardous instructions are generated.

### 12.5 Security Review

- [ ] No `.env` committed.
- [ ] No API keys committed.
- [ ] No tokens in logs.
- [ ] No secrets returned to frontend.
- [ ] Inputs are validated.
- [ ] Errors do not leak internal stack traces in production mode.

---

## 13. Testing Requirements

### 13.1 Backend Smoke Tests

From repository root or backend folder:

```bash
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Health check:

```bash
curl http://localhost:8000/api/health
```

Simulate test:

```bash
curl -X POST http://localhost:8000/api/simulate ^
  -H "Content-Type: application/json" ^
  -d "{\"input\":\"Making a new peptide out of bull, tiger, and blue scorpion.\",\"cards\":[\"Bull\",\"Tiger\",\"Blue Scorpion\",\"Peptide\"],\"mode\":\"interactive_demo\",\"output_level\":\"concept_only\"}"
```

Expected result includes:

```text
candidate_concept
entities
evidence
risk
follow_up_questions
confidence_score
```

### 13.2 Frontend Smoke Tests

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:3000
```

Verify:

- [ ] homepage loads;
- [ ] user can submit the Jordan prompt;
- [ ] card lab loads;
- [ ] result dashboard renders;
- [ ] risk banner appears for venom/toxin-related input;
- [ ] follow-up chat works.

### 13.3 Required Test Evidence in PR

Every PR should include:

```text
commands run
pass/fail status
screenshots for UI changes
known failures or skipped tests
```

---

## 14. Environment and Secret Management

### 14.1 Required Rule

Never commit real secrets.

Forbidden files:

```text
.env
.env.local
.env.production
```

Use:

```text
.env.example
```

for placeholders only.

### 14.2 Required Variables

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

### 14.3 Frontend Secret Rule

Frontend variables beginning with `NEXT_PUBLIC_` are visible to the browser.

Therefore:

```text
Never put API keys, tokens, or secrets in NEXT_PUBLIC_* variables.
```

Allowed:

```bash
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

Not allowed:

```bash
NEXT_PUBLIC_ZHIPU_API_KEY=...
```

---

## 15. Dependency Management

### 15.1 Backend

Track dependencies in:

```text
backend/requirements.txt
```

When adding a dependency:

1. explain why it is needed in the PR;
2. avoid unnecessary large frameworks;
3. prefer stable, widely used packages;
4. ensure local install works.

### 15.2 Frontend

Track dependencies in:

```text
frontend/package.json
```

When adding frontend packages:

1. avoid unnecessary UI libraries if Tailwind can handle it;
2. check package maintenance status;
3. avoid packages that expose security concerns;
4. update lockfile if generated.

---

## 16. External API Connector Rules

All external database connectors must:

1. live under `backend/app/connectors/`;
2. use timeouts;
3. return normalized JSON;
4. handle errors gracefully;
5. avoid leaking raw internal exceptions to frontend;
6. include source names in evidence results;
7. allow the simulation to continue if one source fails.

Required P0 connectors:

```text
PubChem
UniProt
ChEMBL
RCSB PDB
```

P1 connectors:

```text
AlphaFold DB
EPA CompTox
Rhea
```

---

## 17. AI / LLM Output Rules

Zhipu AI or any future LLM provider must be called from backend only.

The frontend must never call LLM providers directly.

All LLM output must pass safety checks before returning to frontend.

The system prompt must include project safety rules.

LLM output should distinguish:

```text
database-backed evidence
scientific inference
hypothetical concept generation
```

---

## 18. Merge Strategy

### 18.1 Preferred Merge Method

Use:

```text
Squash and merge
```

for most feature branches.

Reason:

```text
keeps main history clean
turns many small development commits into one meaningful main commit
makes rollback easier
```

### 18.2 When to Use Merge Commit

Use merge commits only when preserving detailed branch history is important.

### 18.3 When to Use Rebase

Use rebase locally to keep a clean branch, but do not rewrite shared history after others have based work on the branch.

---

## 19. Pull, Rebase, and Conflict Handling

### 19.1 Before Starting Work

```bash
git checkout main
git pull origin main
git checkout -b feature/name
```

### 19.2 If Main Changes During Work

Option A: merge main into branch:

```bash
git checkout feature/name
git fetch origin
git merge origin/main
```

Option B: rebase branch on main:

```bash
git checkout feature/name
git fetch origin
git rebase origin/main
```

Use rebase only if comfortable resolving conflicts.

### 19.3 Conflict Resolution Rules

When resolving conflicts:

1. understand both sides before editing;
2. preserve safety rules;
3. run tests after resolving;
4. mention conflicts in PR if they were significant.

---

## 20. Rollback and Revert Strategy

### 20.1 Revert a Bad Commit on Main

Prefer `git revert` over force-push on shared branches.

```bash
git checkout main
git pull origin main
git revert <commit_sha>
git push origin main
```

### 20.2 Revert a Merged PR

Use GitHub's **Revert** button if available, or revert the squash commit locally.

### 20.3 Never Force Push Main

Do not run:

```bash
git push --force origin main
```

unless explicitly approved by the technical lead for an exceptional recovery case.

---

## 21. Release and Deployment Workflow

For MVP demo, releases may be informal, but the recommended path is:

```text
feature branch
↓
Pull Request
↓
review
↓
merge to main
↓
deploy staging/demo environment
↓
smoke test
↓
present demo
```

For future production workflow:

```text
main -> staging -> production
```

Potential hosting:

```text
Frontend: Vercel
Backend: Render / Railway / Fly.io / AWS ECS
Database: Supabase Postgres / managed PostgreSQL
Cache: Upstash Redis / managed Redis
```

---

## 22. Documentation Rules

Update documentation when:

```text
new endpoint is added
API schema changes
environment variable changes
safety behavior changes
local setup changes
external API connector changes
frontend workflow changes
```

Relevant files:

```text
README.md
docs/PRD.md
docs/TRD.md
docs/Demo-Script.md
docs/Engineering-Workflow.md
```

---

## 23. Definition of Done

A task is done only when:

- [ ] implementation matches scope;
- [ ] relevant docs were read;
- [ ] code is on a feature branch;
- [ ] no secrets are committed;
- [ ] safety boundary is preserved;
- [ ] tests or smoke checks were run;
- [ ] changed files are summarized;
- [ ] known limitations are documented;
- [ ] PR is created;
- [ ] PR is reviewed;
- [ ] PR is merged into `main`;
- [ ] local `main` is updated with `git pull origin main`.

---

## 24. Recommended First Task Prompt for Codex

Use this for the first backend task:

```text
Context:
This repository is for the Interactive AI Bio/Chem Discovery Simulator MVP.

Repository:
https://github.com/YourCitizenLab/biology-api-test

Local organization workspace:
G:\workspace\YourCitizenLab

Local development path:
G:\workspace\YourCitizenLab\biology-api-test

Workflow:
Do not work directly on main. Create branch feature/backend-mvp-skeleton from latest main. Read README.md, docs/Engineering-Workflow.md, docs/PRD.md, docs/TRD.md, and docs/Demo-Script.md first.

Task:
Implement Task 1 only: backend MVP skeleton.

Create a FastAPI backend under /backend with:
- GET /api/health
- POST /api/simulate
- POST /api/evidence/search
- POST /api/chat/follow-up
- POST /api/cards/suggest

Use mock evidence for now.

Out of scope:
- Do not implement frontend yet.
- Do not implement full external database API calls yet.
- Do not add real API keys.
- Do not modify main directly.
- Do not push directly to main.

Safety:
All outputs must be concept-level only and must not include synthesis steps, extraction methods, dosages, concentrations, temperatures, reaction times, purification methods, pathogen handling, toxicity enhancement, or operational biological/chemical instructions.

Acceptance criteria:
1. Backend starts with: cd backend && uvicorn app.main:app --reload --port 8000
2. GET /api/health returns status ok.
3. POST /api/simulate with the Jordan prompt returns candidate_concept, entities, evidence, risk, follow_up_questions, and confidence_score.
4. Blue scorpion / venom input returns high risk and concept_only mode.

Before editing files, inspect the repository and propose an implementation plan.
```

---

## 25. Summary

The required workflow is:

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
open PR
↓
code review
↓
squash merge to main
↓
pull latest main locally
↓
delete completed branch
```

This workflow should be followed by both human developers and AI coding agents throughout the project.
