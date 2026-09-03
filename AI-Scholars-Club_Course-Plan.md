# AI Scholars Club — Course Plan

## 1. Course Identity

**Course Name:** AI Scholars Club  
**Audience:** Grades 10–12, school AI specialization track  
**Format:** three-year pathway, normally one 75-minute club meeting per week  
**Prerequisites:** G8 Software Design, Development & AI + G9 AP Computer Science Principles

### Course Thesis

Students should leave this course able to investigate an AI/ML problem, build and evaluate a model, explain what the model learned and failed to learn, and preserve evidence of their reasoning in a scholarly portfolio.

The course is **process-first, evidence-driven, project-based, and activity-based**. External platforms and courses are resources inside the pathway; they are not the pathway itself.

The shared learning culture matches the Full-Stack Web & AI course:

> **Learn → Practice → Rebuild → Share**

The exact number of minutes allocated to each step can change by lesson type and year band.

---

## 2. Learning Priorities

### Primary Outcomes

Students can independently or collaboratively:

1. formalise an AI/ML problem in terms of inputs, outputs, labels, task type, baseline, and evaluation metric;
2. inspect, clean, transform, visualise, and document real datasets;
3. use NumPy, Pandas, scikit-learn, and later PyTorch in reproducible workflows;
4. create and evaluate defensible baselines before tuning or increasing model complexity;
5. diagnose errors, leakage, overfitting, underfitting, class imbalance, and data-quality problems;
6. compare models using appropriate metrics and controlled experiments;
7. explain limitations, bias, stakeholder impact, and responsible-AI concerns;
8. connect computer vision to robotics and other real systems;
9. conduct a multi-stage AI project from question through evidence, model, evaluation, revision, and communication;
10. maintain a GitHub-based portfolio containing reproducible evidence rather than screenshots alone.

### Secondary Outcomes — Python and Data Fluency

Students strengthen practical fluency in:

- Python functions, conditionals, loops, strings, collections, files, and debugging;
- NumPy arrays, shapes, indexing, and vectorisation;
- Pandas selection, filtering, grouping, cleaning, and joining;
- plotting and exploratory data analysis;
- basic statistics required for ML reasoning.

Python is an enabling skill, not the identity of the club.

### Advanced Outcomes

Depending on year band and student readiness:

- PyTorch training loops and validation discipline;
- CNNs and transfer learning;
- computer vision for robotics;
- advanced model evaluation and controlled tuning;
- deployment and capstone research;
- selected advanced Python/AI algorithms.

---

## 3. What Is Not Core

The following must not displace the canonical AI pathway:

- completing an entire external Python course from beginning to end;
- completing all 85 hours of CodeHS Data Science with Python;
- completing all CS50P lectures as required pre-class viewing;
- TensorFlow-first AI demo courses when PyTorch is the club's deep-learning framework;
- competition-specific tricks before students can run and diagnose a basic ML workflow;
- NOAI / IOAI / Kaggle preparation for students who have not yet reached the required foundations.

Competitions remain optional enrichment.

---

## 4. Canonical Three-Year Pathway

| Year | Sessions | Unit | Main Evidence |
|---|---:|---|---|
| **G10 / Year A** | 1–3 | Orientation, GitHub evidence, entry diagnostic | repo setup + diagnostic gap plan |
|  | 4–7 | Python/Data Foundations | NumPy/Pandas/data-quality/EDA evidence |
|  | 8–12 | Classical ML Workflow | task card + baseline + model comparison + diagnosis |
|  | 13–18 | Responsible AI & AI Literacy | claim audit + stakeholder analysis + ethics brief |
|  | 19–24 | First Scholar Project | reproducible tabular ML project + oral defense |
| **G11 / Year B** | 25–27 | Math Bridge | vectors/matrices/gradients reasoning evidence |
|  | 28–30 | PyTorch Foundations | minimal training loop + validation evidence |
|  | 31–37 | Computer Vision + Robotics | CV model + vision-to-action demo |
|  | 38–48 | Second Modality + Applied Project | applied model + model card + showcase |
| **G12 / Year C** | 49–72 | Advanced AI, deployment, research, capstone | capstone + portfolio defense |

The session count differs from the Full-Stack course, but the design principle is the same: **a coherent pathway with external resources embedded at the point of need**.

---

## 5. Resource Strategy

### CodeHS — Data Science with Python

Use **CodeHS Data Science with Python** as the main Year A practice platform for data foundations.

Recommended use:

- assign only the lessons that support the current club mission;
- use its Basic Python Bootcamp only for students with identified gaps;
- use Pandas, data-cleaning, visualisation, statistics, regression, aggregation, and data-quality activities when they align with the current session;
- do not require completion of the full 85-hour course.

### NumPy

Teach the club's NumPy bridge directly. The club needs explicit work with arrays, shapes, indexing, and vectorisation before deeper Pandas/ML work.

### Advanced Python and AI Programming

Use selected CodeHS modules later as extension material for strong students or advanced units. It is not the Year A spine.

### CS50P

CS50P becomes an optional reference and extension resource. It is not required pre-class viewing and does not determine the club sequence.

### Andrew Ng / PyTorch / Other Resources

Use selected external material only where it supports a specific mission. The teacher-designed pathway remains canonical.

---

## 6. Classroom Design

All lessons share the same learning language as the Full-Stack Web & AI course:

```text
Learn → Practice → Rebuild → Share
```

For a normal skill lesson, this often expands to:

```text
Skill Warm-up → Entry Check → Core Pattern
→ Guided Practice → Independent Rebuild → Evidence / Share
```

Talk Robin, critique, debugging, model comparison, experiment review, or teacher conferencing may be inserted wherever they improve learning.

### Timing Rule

Do **not** force every lesson into identical minute-by-minute blocks.

- Concept-heavy lesson: more Learn + guided reasoning.
- Coding/data lesson: more Practice + Rebuild.
- Project sprint: brief Learn, long Build/Rebuild, then Share.
- Seminar/ethics lesson: evidence reading, structured discussion, claim revision, written evidence.
- Robotics lab: setup/test cycles dominate the period.

The invariant is the learning cycle, not the clock allocation.

---

## 7. Recurring AI/ML Reasoning Backbone

Students repeatedly use:

```text
problem → data → baseline → model → evaluation
→ diagnosis → controlled change → reevaluation → documentation
```

For task recognition:

```text
input → output → labels? → task type → baseline → metric
```

For evidence quality:

```text
claim → evidence → interpretation → limitation → next action
```

---

## 8. Assessment and Evidence

Watching, copying, or running supplied code is not mastery.

Students must progressively demonstrate that they can:

1. explain;
2. trace or inspect;
3. modify with reasoning;
4. rebuild without copying a complete solution;
5. debug;
6. evaluate;
7. defend decisions using evidence.

Typical evidence includes notebooks, code commits, experiment logs, model cards, error analyses, data-quality reports, short written claims, presentations, and project retrospectives.

---

## 9. Final Capstone

By the end of Year C, students complete an AI capstone that includes:

- a defensible problem statement;
- data provenance and quality analysis;
- baseline and model-selection rationale;
- reproducible implementation;
- appropriate evaluation;
- error/failure analysis;
- responsible-AI and stakeholder considerations;
- iteration based on evidence;
- GitHub history and documentation;
- final presentation and portfolio defense.

The capstone is assessed on reasoning and evidence, not merely model accuracy or demo polish.
