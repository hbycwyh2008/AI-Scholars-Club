# AI Scholars Club — G10–G12 Core Pathway

**Status:** canonical club route  
**Audience:** Grades 10–12 students on the school **AI specialization track**  
**Duration:** 72 sessions (~24 per year, normally one 75-minute club meeting per week)  
**Prerequisites:** [G8 Full-Stack Web & AI](Prerequisite_Map_from_G8_G9.md) + [G9 AP CSP](Prerequisite_Map_from_G8_G9.md)

See also: [AI Scholars Club Course Plan](../AI-Scholars-Club_Course-Plan.md).

## What this club is

AI Scholars Club is a **three-year scholarly pathway**, not a contest cram course and not a sequence of external online courses.

Students build:

- data and ML literacy;
- reproducible modeling workflows;
- responsible-AI judgment;
- computer vision skills connected to robotics;
- advanced AI skills and a portfolio capstone.

**Competitions** (NOAI, IOAI, Kaggle) are **optional enrichment** — not the club identity.

## Shared Learning Culture

The club uses the same learning language as the Full-Stack Web & AI course:

```text
Learn → Practice → Rebuild → Share
```

A normal skill lesson may use:

```text
Skill Warm-up → Entry Check → Core Pattern
→ Guided Practice → Independent Rebuild → Evidence / Share
```

This is a **learning cycle, not a rigid minute template**. A 75-minute coding lesson, ethics seminar, robotics lab, and project sprint will divide time differently.

## Recurring Modeling Workflow

```text
problem → data → baseline → model → evaluation
→ diagnosis → controlled change → reevaluation → documentation
```

Task recognition starts with:

```text
input → output → labels? → task type → baseline → metric
```

## External Resource Rule

External courses support the pathway; they do not determine it.

- **CodeHS Data Science with Python:** targeted Year A practice for Python/data gaps, Pandas, data cleaning, visualisation, statistics, aggregation, and data quality.
- **Basic Python Bootcamp inside that CodeHS course:** remediation only after diagnostic evidence.
- **NumPy:** taught directly by the club.
- **CS50P:** optional reference/extension; no required pre-class viewing.
- **Advanced Python and AI Programming:** selected extension material, not the Year A spine.
- **Andrew Ng / PyTorch / other resources:** selected only when aligned to a mission.

---

## Year A — G10: Foundations & Responsible AI (Sessions 1–24)

### Unit A0 — Orientation, evidence, and routing (1–3)

| Session | Title | Evidence |
|---:|---|---|
| 1 | Club charter, portfolio model, and pathway | norms + one portfolio goal |
| 2 | GitHub, notebooks, AI disclosure, and evidence standards | repo setup + disclosure template |
| 3 | Diagnostic: Python, data, and computing-impact readiness | diagnostic record + gap plan |

**Routing rule:** Session 3 decides who needs Python remediation. Do not reteach the same Python sequence to the whole cohort by default.

### Unit A1 — Python & Data Foundations (4–7)

| Session | Title | Evidence | Main support |
|---:|---|---|---|
| 4 | NumPy arrays, shapes, indexing, and vectorisation | rebuilt array exercise | teacher-designed club lesson |
| 5 | Pandas selection, filtering, and grouping | EDA notebook fragment | CodeHS Data Science with Python selected practice |
| 6 | Data quality: missing values, types, duplicates, and cleaning | data-quality report | CodeHS selected practice |
| 7 | Visualisation and mini exploratory analysis | chart + written claim | CodeHS selected practice |

Students with identified Python gaps use the **Basic Python Bootcamp** inside CodeHS Data Science with Python or selected legacy Python packets before/during this unit. Strong students do not complete remedial work simply because it exists.

### Unit A2 — Classical ML Workflow (8–12)

| Session | Title | Evidence |
|---:|---|---|
| 8 | Task formalisation: input, output, labels, task, baseline, metric | task card |
| 9 | Train/validation/test thinking, baselines, and leakage checks | baseline notebook |
| 10 | Logistic regression and classification metrics | metric comparison |
| 11 | Decision trees and random forests | model comparison log |
| 12 | Model selection: diagnose before tuning | written diagnosis |

### Unit A3 — Responsible AI & AI Literacy (13–18)

**Core text:** Melanie Mitchell, selected chapters.

| Session | Title | Evidence |
|---:|---|---|
| 13 | What counts as intelligence? | seminar notes + claim audit |
| 14 | Training data, bias, and representation | case analysis |
| 15 | What did the model actually learn? | error interpretation |
| 16 | Generative AI, hallucinations, and school AI policy | policy application |
| 17 | Fairness, surveillance, and stakeholders | stakeholder map |
| 18 | Ethics workshop: defend a design decision | ethics brief |

### Unit A4 — First Scholar Project (19–24)

| Session | Title | Evidence |
|---:|---|---|
| 19 | Project kickoff: question, data, metric, model card draft | project brief + model card v1 |
| 20 | Build sprint 1: data + baseline | notebook + experiment log |
| 21 | Build sprint 2: model + controlled iteration | change log |
| 22 | Evaluation and error analysis | error report |
| 23 | Presentation and peer review | oral defense + feedback |
| 24 | Year A portfolio review | portfolio entry + retrospective |

**Year A exit standard:** independent basic sklearn workflow; one completed tabular project; one responsible-AI artifact; evidence-linked portfolio.

---

## Year B — G11: Deep Learning & Vision for Action (Sessions 25–48)

### Unit B1 — Math Bridge for ML/DL (25–27)

| Session | Title | Evidence |
|---:|---|---|
| 25 | Notation, vectors, matrices, and shapes | translation exercise |
| 26 | Loss, gradients, and learning rate | gradient sketch |
| 27 | Chain rule and composition intuition | step-by-step derivation |

### Unit B2 — PyTorch & Training Discipline (28–30)

| Session | Title | Evidence |
|---:|---|---|
| 28 | Tensors, autograd, and training steps | minimal training loop |
| 29 | Validation discipline and overfitting | train/validation curves |
| 30 | Regularisation and reproducibility | seeded rerun |

### Unit B3 — Computer Vision Core (31–33)

| Session | Title | Evidence |
|---:|---|---|
| 31 | CNN intuition and convolution | architecture diagram |
| 32 | Augmentation and transfer learning | fine-tune notebook |
| 33 | CV error analysis and failure modes | error gallery |

### Unit B4 — Vision for Robotics (34–37)

| Session | Title | Evidence |
|---:|---|---|
| 34 | Camera pipeline and OpenCV basics | capture + preprocess demo |
| 35 | Color/object detection | detection script |
| 36 | Vision → decision loop patterns | flow diagram |
| 37 | Robotics lab: vision-guided behaviour | robot/camera demo |

### Unit B5 — Second Modality + Applied Project (38–48)

| Session | Title | Evidence |
|---:|---|---|
| 38 | NLP **or** audio introduction | modality notebook |
| 39 | Modality limitations and evaluation | limitations memo |
| 40 | Applied project kickoff | project brief |
| 41–43 | Applied project build sprints | notebook + logs |
| 44 | Integration / robotics iteration | demo revision |
| 45 | Evaluation and documentation | model card v2 |
| 46 | Peer review and debugging | review notes |
| 47 | Showcase rehearsal | presentation draft |
| 48 | Year B showcase + portfolio update | demo + portfolio |

**Year B exit standard:** PyTorch training loop; CV model; robotics-vision integration or equivalent applied demo.

---

## Year C — G12: Advanced AI, Research, Deployment & Capstone (49–72)

Year C shifts from guided technique acquisition toward research-style independence.

| Sessions | Unit | Main evidence |
|---:|---|---|
| 49–53 | Advanced model/evaluation topics | controlled comparison report |
| 54–57 | Deployment, interfaces, and reproducibility | deployed or packaged model artifact |
| 58–60 | Research question, literature/evidence reading, experiment design | capstone proposal |
| 61–68 | Capstone build + experiment cycles | code, logs, evaluation, revisions |
| 69–70 | Failure analysis, responsible-AI review, documentation | final model card + limitations report |
| 71 | Portfolio and oral-defense preparation | portfolio draft |
| 72 | Capstone defense + pathway retrospective | final defense + portfolio |

**Year C exit standard:** a defensible AI capstone with reproducible code, data/model reasoning, evaluation, failure analysis, responsible-AI considerations, and oral defense.

---

## Timing Across Lesson Types

The 75-minute duration is common, but the internal timing changes by task.

| Lesson type | Typical emphasis |
|---|---|
| Concept / model reasoning | Learn + guided reasoning + short rebuild |
| Python / NumPy / Pandas lab | brief Learn + long Practice/Rebuild |
| ML experiment | baseline → run → inspect → revise → share |
| Ethics seminar | evidence reading → discussion → claim revision → writing |
| Robotics lab | setup → test → debug → retest → evidence |
| Project sprint | checkpoint → build → teacher conference → commit → share |

The constant is **Learn → Practice → Rebuild → Share**, not identical minute allocations.
