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
- selected advanced Python/AI algorithms;
- competition-style task recognition and rapid-baseline design.

---

## 3. What Is Not Core

The following must not displace the canonical AI pathway:

- completing an entire external Python course from beginning to end;
- completing all 85 hours of CodeHS Data Science with Python;
- completing all CS50P lectures as required pre-class viewing;
- TensorFlow-first AI demo courses when PyTorch is the club's deep-learning framework;
- competition-specific tricks before students can run and diagnose a basic ML workflow;
- NOAI / IOAI / Kaggle preparation for students who have not yet reached the required foundations.

Competitions remain optional enrichment for the general club. A qualified competition cohort may use the separate IOAI-focused route defined below.

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

### Melanie Mitchell — AI Conceptual Map

For the **IOAI-focused route**, place the existing eight-seminar *Artificial Intelligence: A Guide for Thinking Humans* sequence immediately after Course Introduction / Orientation.

Its job is not to teach coding. It gives students a conceptual map of symbolic AI, machine learning, neural networks, CV, NLP, RL, and the limits of current systems before the technical sequence begins.

### CodeHS — Data Science with Python

Use **CodeHS Data Science with Python** as the main Year A practice platform for data foundations. In the IOAI-focused route it comes **after the AI History / conceptual-map unit**.

Recommended use:

- assign only the lessons that support the current club mission;
- use its Basic Python Bootcamp only for students with identified gaps;
- use Pandas, data-cleaning, visualisation, statistics, regression, aggregation, and data-quality activities when they align with the current session;
- do not require completion of the full 85-hour course.

### NumPy

Teach the club's NumPy bridge directly. The club needs explicit work with arrays, shapes, indexing, and vectorisation before deeper Pandas/ML work.

### CodeHS — Advanced Python and AI Programming

For the **general G10–G12 club**, use selected modules as extension material for strong students or advanced units; it is not the Year A spine.

For the **IOAI-focused route**, it is a selected core bridge after data-science foundations. Prioritise:

- object-oriented programming where it improves program structure;
- libraries and packages;
- data structures and algorithmic trade-offs;
- search / graph-search ideas;
- selected AI Algorithms material;
- the classifier build/evaluation project.

Do not require the full year-long course and do not let unrelated projects delay the ML workflow phase.

### CS50P

CS50P becomes an optional reference and extension resource. It is not required pre-class viewing and does not determine the club sequence.

### ML Workflow Preparation

For the IOAI route, establish the complete applied workflow **before** the systematic Andrew Ng model sequence using selected material from:

- Andreas C. Müller — *Applied Machine Learning*;
- DataTalksClub — *Machine Learning Zoomcamp*.

Focus on problem framing, preprocessing, validation, baseline design, metrics, error analysis, feature reasoning, model comparison, and controlled tuning. Deployment/MLOps is optional for IOAI preparation.

### Andrew Ng / AAAMLP / Deep Learning / PyTorch

Use the resources in this order for the IOAI route:

```text
Andrew Ng Machine Learning Specialization
→ Approaching (Almost) Any Machine Learning Problem
→ advanced evaluation / features / tuning / ensembling
→ Andrew Ng Deep Learning Specialization
→ PyTorch
```

Andrew Ng provides the model-principles map; AAAMLP provides competition decision-making; PyTorch is the main executable deep-learning framework.

See the [IOAI Core Resource Map](05_Resources/IOAI_Core_Resource_Map.md).

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

For competition work, expand the modeling backbone to:

```text
problem / scoring rule
→ data audit
→ validation design
→ baseline
→ metric
→ error analysis
→ controlled improvement
→ reproducible comparison
→ postmortem
```

For the IOAI-focused route, use lighter problem-framing questions during the AI History unit, then begin the full six-question task-recognition routine in the Data Science unit.

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

## 9. IOAI-Focused Route

The [IOAI Core Learning Path](00_Course_Overview/IOAI_Core_Learning_Path.md) is the preferred route for a qualified competition cohort. It does not replace the general three-year club for every student.

Recommended sequence:

```text
Course Introduction / Orientation
→ Melanie Mitchell, A Guide for Thinking Humans / AI History
→ CodeHS Data Science with Python
→ CodeHS Advanced Python and AI Programming
→ ML Workflow Bootcamp (Müller + Zoomcamp)
→ Andrew Ng Machine Learning Specialization
→ Approaching (Almost) Any Machine Learning Problem
→ Evaluation / Feature Engineering / Tuning / Ensembling
→ Andrew Ng Deep Learning Specialization
→ PyTorch
→ IOAI competition projects
```

Teacher preparation and lesson plans:

- [IOAI Teacher Preparation Watchlist](09_Teacher_Planning/IOAI_Teacher_Preparation_Watchlist.md)
- [IOAI Core Lesson Plans](09_Teacher_Planning/Daily_Lesson_Plans/IOAI_Core_Pathway/README.md)
- [IOAI Core Resource Map](05_Resources/IOAI_Core_Resource_Map.md)

The formal task-recognition drills begin during Data Science and continue throughout the rest of the sequence; they are not postponed until competition season.

---

## 10. Final Capstone

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
