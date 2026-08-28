# Teacher Start Here

## Default Route: AI Scholars Club Core

Assign the **[Club Pathway G10–G12](00_Course_Overview/Club_Pathway_G10-G12.md)** unless a student is explicitly on the optional competition track.

| Year | Sessions | Start packet |
|---|---:|---|
| G10 | 1–24 | Year A — orientation + diagnostic |
| G11 | 25–48 | Year B — math bridge + PyTorch |
| G12 | 49–72 | Year C — advanced AI + capstone |

Review [Prerequisites from G8 & G9](00_Course_Overview/Prerequisite_Map_from_G8_G9.md) before Session 1. Use **Session 3 diagnostic** to route gap-fill — do not assign the full legacy CS50P block to every student.

## Optional: Competition Enrichment

Only after Year B minimum (Session 48) and teacher nomination:

- [Competition Enrichment (optional)](00_Course_Overview/Competition_Enrichment_Optional.md)
- [Legacy competition pathways](00_Course_Overview/Legacy_Competition_Pathways.md)

## Normal Teaching Workflow

```text
confirm year band + session
→ check prerequisite / diagnostic notes
→ open Class Missions (legacy bank or year-band packet when available)
→ teach 75-minute seven-block flow
→ collect named evidence
→ update portfolio / progress record
→ schedule next session
```

Begin at [Class Missions](02_Class_Missions/README.md). Use [Legacy Session Migration Map](00_Course_Overview/Legacy_Session_Migration_Map.md) to reuse legacy packets during migration.

## Pedagogy Reference

- [75-Minute After-School Club Implementation](09_Teacher_Planning/75min_After_School_Club_Implementation.md)
- [Workflow Competency Crosswalk](00_Course_Overview/Workflow_Competency_Crosswalk.md)
- [Cohort Mastery Review Protocol](09_Teacher_Planning/Cohort_Mastery_Review_Protocol.md)

## Portfolio Gates

Club progress is tracked through **portfolio gates**, not competition mocks:

| Gate | Session |
|---|---:|
| Data quality | 7 |
| Task + baseline | 9 |
| Classical ML | 12 |
| Ethics brief | 18 |
| Year A project | 23 |
| PyTorch loop | 30 |
| Computer vision | 33 |
| Robotics vision | 37 |
| Year B showcase | 48 |
| Capstone | 70 |

## Legacy Operational Tools

For **competition enrichment only**, you may use:

```bash
python scripts/manage_student_progress.py init \
  --path student-progress/student-001.json \
  --student-id student-001 \
  --pathway noai_round1
```

```bash
python scripts/plan_learning_path.py \
  --progress student-progress/student-001.json \
  --limit 6
```

Club core members do **not** require daily model-recognition drills.

## Canonical Order (club core)

1. **Year A** — orientation, data refresh, classical ML, ethics, scholar project  
2. **Year B** — math bridge, PyTorch, CV, robotics vision, applied project  
3. **Year C** — advanced AI, responsible deployment, capstone, portfolio  

## What Changed from the Legacy Design

The repository previously defaulted to a 78-session NOAI/IOAI pipeline. That design is preserved as a **legacy resource bank** and **optional enrichment**. The club default is now the G10–G12 scholarly pathway above.

See [Legacy Competition Pathways](00_Course_Overview/Legacy_Competition_Pathways.md) for the old route documents.
