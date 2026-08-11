# Session 58 — Classical Machine-Learning Capstone

**Class duration:** 75 minutes  
**Purpose:** verify task recognition, mathematical understanding, implementation, evaluation, documentation literacy, and model limitations across Phase 5

## Required Mastery

Given an unfamiliar task, students independently:

1. identify `X`, `y`, label availability, output type, prediction-time boundary, and metric;
2. distinguish regression, classification, clustering, dimensionality reduction, anomaly detection, and recommendation;
3. choose a constant or rule baseline before an advanced model;
4. state the type and shape of the main mathematical objects;
5. explain the selected model’s prediction or decision rule;
6. complete one representative hand calculation;
7. translate the model rule into code or pseudocode;
8. locate the relevant official API and justify estimator construction without a copied end-to-end recipe;
9. design a leakage-safe validation protocol;
10. compare at least two model families under one protocol;
11. analyse errors, assumptions, costs, and failure modes;
12. reproduce the core workflow with official documentation available but tutorial/example material closed;
13. explain why good validation performance does not prove causality, human-like understanding, or deployment safety.

## Capstone Workflow

```text
read the task
→ formalise X, y, output, metric, and boundary
→ select a baseline
→ state mathematical objects and shapes
→ locate the official API
→ record constructor and preprocessing decisions
→ build a reproducible pipeline
→ evaluate under one protocol
→ compare a contrasting model
→ analyse errors and limitations
→ rebuild the core workflow
→ present the model card
```

## 75-Minute Learning Cycle

| Time | Block | Required action |
|---:|---|---|
| 0–8 | Skill Warm-Up | classify six mixed task scenarios |
| 8–15 | Talk Robin 1 | defend one baseline and one rejected model |
| 15–22 | Entry Check | complete a notation/shape/loss mini-check |
| 22–35 | Core Pattern | task → mathematics → documentation → code → evidence → limitation |
| 35–53 | Guided Practice | audit one ambiguous competition-style task |
| 53–67 | Independent Rebuild | produce a complete baseline and model card for a new task using official documentation only as implementation reference |
| 67–75 | Talk Robin 2 + Evidence | oral defence and phase-gate decision |

## Documentation Independence Rule

During the independent rebuild:

- official pandas and scikit-learn documentation are allowed;
- a student may search for the correct class, function, constructor signature, method, and parameter meaning;
- complete tutorial notebooks, copied competition solutions, and step-by-step answer recipes are not allowed as rebuild evidence;
- common syntax may be looked up, but the student must explain every major implementation decision;
- inability to identify the model family, metric, validation boundary, or leakage risk cannot be repaired by copying API syntax.

Complete the [Documentation-to-Code Evidence Template](../../03_Templates/Documentation_to_Code_Evidence_Template.md) for the baseline or selected model.

## Required Evidence

- completed [Model Recognition Routine](Model_Recognition_Routine.md);
- completed [Mathematics Bridge Evidence Template](../../03_Templates/Andrew_ML_Mathematics_Bridge_Evidence_Template.md) or equivalent capstone section;
- completed [Documentation-to-Code Evidence Template](../../03_Templates/Documentation_to_Code_Evidence_Template.md);
- baseline pipeline and validation result;
- contrasting-model comparison;
- one controlled improvement or justified no-change decision;
- error-analysis table;
- completed [Model Card](../../03_Templates/Model_Card_Template.md), including implementation provenance and evidence boundary;
- fresh-run / independent-rebuild evidence;
- oral explanation.

## Phase Gate

Students pass only when they can select and defend a classical baseline without guessing from keywords, connect the model to its mathematics and code, locate and use the official API independently, reproduce the core workflow without a copied solution, and identify the evidence boundary and likely failure modes.
