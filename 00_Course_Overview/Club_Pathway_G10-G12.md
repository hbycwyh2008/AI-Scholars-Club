# AI Scholars Club — G10–G12 Core Pathway

**Status:** canonical club route (replaces competition-first 78-Session design as the default)  
**Audience:** Grades 10–12 students on the school **AI specialization track**  
**Duration:** 72 sessions (~24 per year, one 75-minute club meeting per week)  
**Prerequisites:** [G8 Full-Stack Web & AI](Prerequisite_Map_from_G8_G9.md) + [G9 AP CSP](Prerequisite_Map_from_G8_G9.md)

## What this club is

AI Scholars Club is a **three-year scholarly pathway**, not a contest cram course.

Students build:

- ML literacy and reproducible workflows
- responsible-AI judgment
- computer vision skills connected to **robotics (VEX / FIRST)**
- advanced AI topics and a **portfolio capstone**

**Competitions** (NOAI, IOAI, Kaggle) are **[optional enrichment](Competition_Enrichment_Optional.md)** — not the club identity.

## Pedagogy

Every session uses the school **75-minute seven-block** flow:

```text
Skill Warm-up → Talk Robin 1 → Entry Check → Core Pattern
→ Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence
```

Talk Robin may appear in any block when it helps learning. See `09_Teacher_Planning/75min_After_School_Club_Implementation.md`.

## Modeling workflow (recurring backbone)

```text
task formalisation → data quality → feature engineering
→ model selection / baseline → diagnosis → controlled improvement
→ documentation / postmortem
```

## Year bands

| Year | Sessions | Theme | Exit artifact |
|---|---:|---|---|
| **Year A (G10)** | 1–24 | ML foundations + responsible AI | Tabular scholar project + ethics brief |
| **Year B (G11)** | 25–48 | Deep learning + computer vision + robotics | CV / robotics vision demo |
| **Year C (G12)** | 49–72 | Advanced AI + deployment + capstone | Capstone + portfolio presentation |

---

## Year A — G10: Foundations & Responsible AI (Sessions 1–24)

### Unit A0 — Club orientation & evidence (1–2)

| Session | Title | Evidence |
|---:|---|---|
| 1 | Club charter, portfolio model, and where this sits in G6–G12 CS | Club norms + one portfolio goal |
| 2 | GitHub, notebooks, AI disclosure, and evidence standards | Repo setup + disclosure template |

### Unit A1 — Python & data refresh (3–7)

*Skip or compress based on [entry diagnostic](Prerequisite_Map_from_G8_G9.md).*

| Session | Title | Evidence |
|---:|---|---|
| 3 | Diagnostic: Python, data, and computing-impact readiness | Diagnostic record + gap plan |
| 4 | NumPy arrays, shapes, and vectorisation | Rebuilt array exercise |
| 5 | Pandas: selection, filtering, grouping | EDA notebook fragment |
| 6 | Data quality: missing values, types, duplicates | Quality report |
| 7 | Visualisation and mini exploratory analysis | Chart + written claim |

### Unit A2 — Classical ML workflow (8–12)

| Session | Title | Evidence |
|---:|---|---|
| 8 | Task formalisation: problem → data → metric | Task card |
| 9 | Splits, baselines, and leakage checks | Baseline notebook |
| 10 | Logistic regression and classification metrics | Metric comparison |
| 11 | Decision trees and random forests | Model comparison log |
| 12 | Ensembles and classical model selection | Written diagnosis |

### Unit A3 — Ethics & AI literacy (13–18)

*Core text: Melanie Mitchell, selected chapters.*

| Session | Title | Evidence |
|---:|---|---|
| 13 | What counts as intelligence? | Seminar notes + claim audit |
| 14 | Training data, bias, and representation | Case analysis |
| 15 | What did the model actually learn? | Error interpretation |
| 16 | Generative AI, hallucinations, school AI policy | Policy application |
| 17 | Fairness, surveillance, and stakeholders | Stakeholder map |
| 18 | Ethics workshop: defend a design decision | Ethics brief |

### Unit A4 — First scholar project (19–24)

| Session | Title | Evidence |
|---:|---|---|
| 19 | Project kickoff: scope, metric, model card draft | Model card v1 |
| 20 | Build sprint 1: data + baseline | Notebook + log |
| 21 | Build sprint 2: features + iteration | Change log |
| 22 | Evaluation and error analysis | Error report |
| 23 | Presentation and peer review | Oral defense + feedback |
| 24 | Year A portfolio review and Year B preview | Portfolio entry |

**Year A exit standard:** independent sklearn workflow; one completed tabular project; one ethics artifact; evidence-linked portfolio.

---

## Year B — G11: Deep Learning & Vision for Action (Sessions 25–48)

### Unit B1 — Math bridge for ML/DL (25–27)

| Session | Title | Evidence |
|---:|---|---|
| 25 | Notation, vectors, matrices, shapes | Translation exercise |
| 26 | Loss, gradients, and learning rate | Gradient sketch |
| 27 | Chain rule and composition intuition | Step-by-step derivation |

### Unit B2 — PyTorch & training loops (28–30)

| Session | Title | Evidence |
|---:|---|---|
| 28 | Tensors, autograd, and training steps | Minimal training loop |
| 29 | Validation discipline and overfitting | Train/val curves |
| 30 | Regularisation and reproducibility | Seeded rerun |

### Unit B3 — Computer vision core (31–33)

| Session | Title | Evidence |
|---:|---|---|
| 31 | CNN intuition and convolution | Architecture diagram |
| 32 | Augmentation and transfer learning | Fine-tune notebook |
| 33 | CV error analysis and failure modes | Error gallery |

### Unit B4 — Vision for robotics (34–37)

| Session | Title | Evidence |
|---:|---|---|
| 34 | Camera pipeline and OpenCV basics | Capture + preprocess demo |
| 35 | Color blobs and object detection | Detection script |
| 36 | Vision → decision loop patterns | Flow diagram |
| 37 | Robotics lab: vision-guided behaviour | Robot/camera demo |

### Unit B5 — Second modality + applied project (38–48)

| Session | Title | Evidence |
|---:|---|---|
| 38 | NLP **or** audio introduction (teacher choice) | Modality notebook |
| 39 | Modality limitations and evaluation | Limitations memo |
| 40 | Applied project kickoff | Project brief |
| 41–43 | Applied project build sprints | Notebook + logs |
| 44 | Integration / robotics iteration | Demo revision |
| 45 | Evaluation and documentation | Model card v2 |
| 46 | Peer review and debugging | Review notes |
| 47 | Showcase rehearsal | Presentation draft |
| 48 | Year B showcase + portfolio update | Demo + portfolio |

**Year B exit standard:** PyTorch training loop; CV model; robotics-vision integration or equivalent applied demo.

---

## Year C — G12: Advanced AI & Capstone (Sessions 49–72)

### Unit C1 — Advanced topics (49–54)

| Session | Title | Evidence |
|---:|---|---|
| 49 | Attention and transformers (intuition) | Architecture explanation |
| 50 | Embeddings and retrieval basics | RAG sketch |
| 51 | Generative AI capabilities and limits | Claim audit |
| 52 | Advanced evaluation: EDA revisit | EDA memo |
| 53 | Feature engineering and model comparison | Comparison table |
| 54 | Error diagnosis before any tuning | Diagnosis report |

### Unit C2 — Responsible deployment (55–58)

| Session | Title | Evidence |
|---:|---|---|
| 55 | Bias testing and subgroup analysis | Test protocol |
| 56 | Documentation and reproducibility | Repro checklist |
| 57 | Stakeholder communication | One-page brief |
| 58 | Deployment ethics and school context | Risk register |

### Unit C3 — Capstone (59–70)

| Session | Title | Evidence |
|---:|---|---|
| 59 | Capstone proposal and team roles | Proposal |
| 60–65 | Capstone build sprints (6) | Weekly evidence |
| 66 | Evaluation and iteration | Eval report |
| 67 | Polish, accessibility, and README | Repo + README |
| 68 | Rehearsal and critique | Critique notes |
| 69 | Public showcase | Presentation |
| 70 | Peer and teacher review | Rubric scores |

### Unit C4 — Transition (71–72)

| Session | Title | Evidence |
|---:|---|---|
| 71 | Portfolio review and college / application narrative | Portfolio export |
| 72 | Next steps: research, internships, optional competition interest | Personal plan |

**Year C exit standard:** capstone artifact; deployment documentation; showcase presentation; complete portfolio.

---

## Portfolio gates (club core)

| Gate | Session | Requirement |
|---|---|---|
| Data quality | 7 | Named data-quality checks on a real dataset |
| Task + baseline | 9 | Written task card + baseline metric |
| Classical ML | 12 | Compared ≥2 models with diagnosis |
| Ethics | 18 | Ethics brief applied to a real case |
| Year A project | 23 | Oral defense + model card |
| PyTorch loop | 30 | Independent training loop rebuild |
| Computer vision | 33 | CV model + error analysis |
| Robotics vision | 37 | Camera → decision demo |
| Year B project | 48 | Showcase demo |
| Advanced evaluation | 54 | Diagnosis before tuning |
| Responsible deployment | 58 | Repro + stakeholder brief |
| Capstone | 70 | Rubric-passing showcase |

---

## Legacy lesson packets

Session **content files** for the old 78-Session competition pipeline remain in `02_Class_Missions/` as a **resource bank** until year-band packets are authored. See [Legacy Session Migration Map](Legacy_Session_Migration_Map.md).

## Related documents

- [Prerequisite Map from G8 & G9](Prerequisite_Map_from_G8_G9.md)
- [Competition Enrichment (optional)](Competition_Enrichment_Optional.md)
- [Learning Outcomes](Learning_Outcomes.md)
- [Legacy competition pathways](Legacy_Competition_Pathways.md)
