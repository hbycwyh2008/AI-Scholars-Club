# Competition Enrichment — Optional Module

**Status:** optional add-on; **not** the default AI Scholars Club route  
**Audience:** G11–G12 students nominated by teacher after Year B minimum competency  
**Duration:** 8–12 sessions (modular)

## Purpose

Prepare motivated students for **NOAI China**, **IOAI**, or **Kaggle-style** tasks without making contest prep the club's identity.

This module reuses content from the [legacy 78-Session competition pipeline](Legacy_Competition_Pathways.md).

## Entry requirements

- Completed Year B through Session 48 (or teacher-approved equivalent)
- Portfolio shows independent rebuild at PyTorch + CV gates
- Student opts in; parent informed if school policy requires

## Module outline

| Unit | Sessions | Focus | Legacy source |
|---|---:|---|---|
| **E1** Model recognition intensive | 2 | Task-family ID, metric choice, baseline discipline | Legacy 41, 57, drills |
| **E2** Tuning & ensembling | 2 | Diagnosis-first tuning, valid stacking | Legacy 75–76 |
| **E3** Timed simulation | 2 | Mock under current official rules | Legacy 77 |
| **E4** Rule review & postmortem | 2 | Annual NOAI/IOAI/Kaggle alignment | `10_Ready_to_Teach_Pack/` |
| **E5** Extension sprints | 2–4 | Tabular / image / text / audio depth | Legacy E1–E6 + Phase 7–8 |

## Operational tools (enrichment only)

When running enrichment, teachers may use:

- `scripts/generate_daily_model_drill.py` — model-recognition practice
- `scripts/plan_learning_path.py` with `pathway` set to legacy route
- `04_Assessment/Model_Recognition_Drills/` — scenario bank

These tools are **not required** for club core members.

## Executable legacy routes

For students pursuing full competition preparation, the exact legacy routes remain documented:

- [NOAI Round 1 Compressed Path](NOAI_Round1_Compressed_Path.md) — 45 legacy sessions
- [NOAI Round 2 Project Path](NOAI_Round2_Project_Path.md) — +22 sessions
- [IOAI Full Extension Path](IOAI_Full_Extension_Path.md) — all 78 legacy sessions

**Do not** assign these routes to the whole club by default.

## Annual verification

Before each competition season:

1. Archive current official NOAI / IOAI rules locally
2. Complete `10_Ready_to_Teach_Pack/Annual_Rules_2026_Verification.md`
3. Confirm runtime, model, and submission constraints with cohort evidence
