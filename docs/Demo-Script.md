# Demo Script: Interactive AI Bio/Chem Discovery Simulator

## 1. Demo Objective

This script explains how to present the Interactive AI Bio/Chem Discovery Simulator to internal teammates, external collaborators, Jordan, or potential investors.

The demo should communicate one core message:

```text
The system turns abstract bio/chemical inspiration into an interactive, database-backed, safety-bounded discovery concept.
```

---

## 2. Demo Setup

Before demo:

1. start backend;
2. start frontend;
3. confirm environment variables are configured;
4. test the default prompt;
5. confirm high-risk safety banner works;
6. prepare a fallback mock result in case external APIs are slow.

Recommended URLs:

```text
Frontend: http://localhost:3000
Backend: http://localhost:8000
Health:   http://localhost:8000/api/health
```

---

## 3. Opening Narrative

Suggested opening:

```text
This demo is an interactive AI discovery simulator. Instead of asking users to understand complex scientific databases directly, we let them describe or visually combine biological and chemical inspirations. The AI Agent then maps those inputs to real scientific entities, calls public databases, aggregates evidence, and produces a concept-level discovery result with safety boundaries.
```

Then clarify:

```text
This is not a wet-lab protocol generator. It does not output synthesis steps, extraction methods, dosage, temperature, purification, or experimental conditions. It is designed for concept exploration, education, and early-stage discovery thinking.
```

---

## 4. Demo Scenario: Jordan Example

Use the following example:

```text
Making a new peptide out of bull, tiger, and blue scorpion.
```

Explain:

```text
This is intentionally abstract and playful. The goal is to show that the system can turn a creative prompt into a scientific exploration workflow.
```

---

## 5. Step-by-Step Walkthrough

### Step 1: Open Discovery Input

Show the home page.

Say:

```text
The user can start with a natural language idea. They do not need to know the exact scientific terminology.
```

Enter:

```text
Making a new peptide out of bull, tiger, and blue scorpion.
```

Click:

```text
Start Discovery
```

---

### Step 2: Show Entity Understanding

Expected system summary:

```text
Bull -> Bos taurus / mammalian protein reference
Tiger -> Panthera tigris / mammalian protein reference
Blue scorpion -> venom peptide / toxin-related peptide source
Peptide -> bioactive peptide scaffold
```

Say:

```text
The Agent first translates the user's creative language into scientific entities that can be searched in public databases.
```

---

### Step 3: Show Interactive Card Lab

Open the card lab.

Drag the following cards:

```text
Bull
Tiger
Blue Scorpion
Peptide
```

Say:

```text
The same workflow can also be driven visually. This makes the experience feel more like an interactive science lab or educational card board.
```

Click:

```text
Generate Candidate Concept
```

---

### Step 4: Show Agent Reasoning Panel

Expected user-visible reasoning summary:

```text
1. Understanding your input
2. Mapping to scientific entities
3. Querying public databases
4. Aggregating evidence
5. Applying safety filter
6. Generating candidate concept
```

Say:

```text
This panel is not showing hidden chain-of-thought. It shows a user-friendly summary of the steps the system is performing.
```

---

### Step 5: Show Evidence Cards

Expected evidence sources:

```text
UniProt
ChEMBL
PubChem
RCSB PDB
AlphaFold DB
EPA CompTox, if enabled
```

Say:

```text
The important point is that the AI is not only generating text. It is grounding its output in external scientific databases.
```

Click an evidence card, for example:

```text
UniProt Evidence
```

Explain:

```text
For the blue scorpion card, the system searches for toxin-related peptide and venom peptide records. This supports the interpretation of blue scorpion as a venom peptide source.
```

---

### Step 6: Show Candidate Concept

Expected result:

```text
Candidate Concept:
Scorpion-inspired disulfide-rich peptide scaffold with mammalian motif references.
```

Say:

```text
The system does not claim this is a real validated molecule. It frames it as a hypothetical scaffold concept inspired by known biological patterns.
```

---

### Step 7: Show Possible Function Direction

Expected directions:

```text
Stable peptide scaffold
Ion-channel interaction simulation
Antimicrobial peptide-like exploration
Venom peptide family similarity
Structure-function relationship exploration
```

Say:

```text
These are high-level exploration directions, not experimental instructions.
```

---

### Step 8: Show Safety Banner

Expected risk:

```text
Risk Level: High
Reason: Venom / toxin-related biological entity detected.
```

Say:

```text
Because the input includes venom-related biology, the system automatically restricts the output to concept-level explanation only.
```

Emphasize:

```text
No synthesis protocol. No extraction method. No dosage. No reaction conditions. No wet-lab steps.
```

---

### Step 9: Show Follow-up Chat

Click or ask:

```text
Can this concept be made safer?
```

Expected answer:

```text
A safer direction would avoid toxin-like functional claims and focus on non-toxic peptide scaffold stability, antimicrobial peptide databases, or general structure-function education.
```

Say:

```text
The follow-up chat keeps the same simulation context and safety constraints.
```

Then ask:

```text
Explain this for non-scientists.
```

Expected answer:

```text
The system explains the concept in plain language while preserving scientific caution.
```

---

## 6. Key Talking Points

### Product Value

```text
This makes scientific exploration more accessible by combining a playful interface with real scientific data sources.
```

### Technical Value

```text
The system combines LLM orchestration, public scientific database APIs, evidence aggregation, and safety filtering.
```

### Safety Value

```text
The system is designed around concept-level exploration and blocks operational instructions for risky biological or chemical content.
```

### Future Value

```text
This can become a foundation for AI co-scientist workflows, DeSci education, citizen science exploration, and early-stage research ideation.
```

---

## 7. Backup Demo Output

If external APIs are slow, use the following mock result:

```text
Candidate Concept:
Scorpion-Inspired Peptide Scaffold Concept

Summary:
A hypothetical bioactive peptide concept inspired by compact scorpion venom peptide scaffolds and general mammalian protein motif references.

Evidence:
- UniProt: related toxin peptide and animal protein records
- RCSB PDB: related peptide scaffold structures
- ChEMBL: related bioactivity records
- PubChem: chemical identity references where applicable

Risk:
High. Venom/toxin-related entity detected.

Safety Boundary:
Concept-level simulation only. No experimental protocol or synthesis guidance is provided.

Confidence:
Medium. The scorpion peptide scaffold direction is biologically plausible, but the proposed product is hypothetical and not experimentally validated.
```

---

## 8. Demo Closing

Suggested closing:

```text
The demo shows how an AI Agent can transform creative biological and chemical ideas into structured, evidence-backed, safety-aware discovery concepts. The immediate MVP is an interactive simulator, and the long-term direction is a safer AI co-scientist interface for DeSci, education, and early discovery workflows.
```

---

## 9. Demo Checklist

Before presenting:

- [ ] frontend starts successfully;
- [ ] backend starts successfully;
- [ ] `/api/health` returns ok;
- [ ] Zhipu API key is configured in `.env`;
- [ ] default Jordan prompt works;
- [ ] card drag-and-drop works;
- [ ] result dashboard renders;
- [ ] risk banner appears for blue scorpion / venom input;
- [ ] follow-up chat works;
- [ ] fallback mock result is ready.
