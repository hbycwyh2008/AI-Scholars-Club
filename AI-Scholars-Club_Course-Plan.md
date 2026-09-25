# AI Scholars Club — Canonical Course Plan

## 1. Fixed Program Architecture

The canonical AI Scholars Club pathway is:

```text
L1 — Understand & Code
→ L2 — Build
→ L3 — Solve Unseen Problems
→ L4 — Create New Knowledge
```

This framework is competency-based rather than course-completion-based. A student advances because the required **output and evidence** are present, not because a named course or playlist was completed.

The design sequence for every level is:

```text
Input → Training → Output → Evidence → Promotion
```

### Program Rules

1. **Output determines promotion.**
2. External courses, books, videos, and platforms are inputs, not the curriculum itself.
3. A resource stays only if it materially improves the target output of its level.
4. L1 remains a low-barrier entry point.
5. L2 develops complete ML-building ability.
6. L3 develops independent unfamiliar-problem solving.
7. L4 is a research exit track and may have no qualified students in a given year.
8. Equivalent prior ability may be used to enter L2 or L3 after assessment.
9. L4 is qualification/invitation-based rather than open automatic progression.

---

## 2. L1 — AI Literacy & Python Foundations

### Identity
**Understand & Code**

### Input
- No AI background required.
- No prior Python experience required.

### Core Training

#### AI Literacy
- what AI is and is not;
- basic history and major approaches;
- AI vs ML vs deep learning;
- data, models, prediction, and simple learning-system intuition;
- basic search/problem-solving ideas;
- capabilities, limitations, hallucination, bias, privacy, and responsible use;
- simple AI task identification: input, output, and broad task type.

#### Python Foundations
- variables and expressions;
- conditionals;
- loops;
- functions;
- strings;
- lists and dictionaries;
- basic file/data handling;
- exceptions and debugging;
- simple libraries;
- basic notebook workflow;
- progressively more independent Python problem solving.

### Core Resources

#### AI Literacy Spine
- **Elements of AI** — selected sections used as the main conceptual AI-literacy spine.

#### Programming Spine
1. **CodeHS — Introduction to Python Programming**
2. **CodeHS — Advanced Python and AI Programming**

The programming order is fixed as:

```text
Introduction to Python Programming
→ Advanced Python and AI Programming
```

The following are **not** the L1 programming spine:
- CS50P;
- Web Game Programming Foundations;
- Software Design, Development & AI.

They may be used only as optional references if a specific teaching need arises.

#### AI Ideas / History Supplement
- **Melanie Mitchell — _Artificial Intelligence: A Guide for Thinking Humans_** — selected readings and discussions rather than full-book completion.

### Output
A student completing L1 can:
1. explain core AI concepts in their own words;
2. distinguish basic AI/ML/DL ideas at an introductory level;
3. write and debug basic Python programs;
4. identify the input, output, and approximate task type of a simple AI problem;
5. follow and explain a simple data → program/model → output workflow.

### Evidence
- basic Python coding task;
- AI literacy explanation, quiz, or oral check;
- simple task-identification activity;
- small integrated coding/AI artifact where appropriate.

### Promotion to L2
Promotion requires demonstrated L1 outputs. Merely completing CodeHS or Elements of AI is insufficient.

---

## 3. L2 — Applied Machine Learning

### Identity
**Build**

### Input
- L1 outputs demonstrated, or
- equivalent Python + AI-literacy readiness shown through assessment.

### Core Training
- NumPy and Pandas;
- data inspection, cleaning, and EDA;
- supervised vs unsupervised learning;
- classification, regression, and clustering foundations;
- train / validation / test discipline;
- metrics and metric selection;
- baseline design;
- scikit-learn workflow;
- basic feature engineering;
- bias/variance intuition;
- error analysis;
- reproducibility and documentation.

### Core Resources
- **Andrew Ng — Machine Learning Specialization**;
- selected data-tool practice;
- small authentic ML projects.

### Output
Given a common data problem, the student can independently execute:

```text
task identification
→ data preparation / EDA
→ baseline
→ model
→ evaluation
→ improvement
```

The student can explain why the selected metric, model, and improvement step are reasonable.

### Evidence
- one complete reproducible ML project/notebook;
- model and metric rationale;
- error analysis;
- short written or oral defense.

### Promotion to L3
The student must be able to build a complete ML pipeline with decreasing teacher scaffolding.

---

## 4. L3 — Advanced AI & Competition

### Identity
**Solve Unseen Problems**

### Input
- independent L2 ML pipeline ability, or
- equivalent readiness demonstrated through assessment.

### Core Training
- deep-learning foundations;
- PyTorch;
- CNNs;
- sequence models, attention, and Transformer foundations;
- applied CV and NLP;
- feature engineering;
- model selection;
- hyperparameter tuning, including tools such as Optuna;
- ensembling;
- advanced error analysis;
- validation strategy;
- Kaggle / IOAI-style unfamiliar tasks;
- competition workflow and postmortem analysis.

### Core Resources
- **Andrew Ng — Deep Learning Specialization** (selected);
- **PyTorch**;
- selected CV/NLP resources;
- Kaggle / IOAI-style tasks and internal unseen challenges.

### Output
Given an unfamiliar AI/ML problem, the student can independently execute:

```text
task recognition
→ baseline
→ model / feature selection
→ tuning
→ ensembling or another justified improvement
→ validation
→ explanation of decisions
```

### Evidence
- blind/unseen challenge or competition-style project;
- reproducible repo/notebook;
- decision log;
- comparison of controlled experiments;
- presentation or postmortem.

### Promotion to L4
L4 entry is not automatic. Students must demonstrate unusually strong independence, technical readiness, and sustained evidence from L3.

---

## 5. L4 — AI Research

### Identity
**Create New Knowledge**

### Input
- strong L3 performance;
- sufficient coding and mathematical readiness;
- independent learning ability;
- readiness to read research papers critically.

L4 is **qualification/invitation-based**. If no student meets the standard in a given year, L4 does not run.

### Core Training
- research-question formulation;
- paper reading;
- literature positioning;
- reproduction;
- baseline design;
- experimental design;
- ablation;
- evidence analysis;
- research writing;
- research presentation.

### Paper Selection Rule

Students do **not** read papers for volume and do not follow a “100 papers” target.

Priority goes to **landmark papers that changed a research paradigm, method family, or experimental practice**. Supporting papers are added only when needed for a research task.

Possible support resources include:
- original landmark papers;
- selected paper-reading explanations;
- selected CS231n / CS224N material when relevant to the student's research direction.

### Output
A student completing L4 can:

```text
identify a research question
→ reproduce a prior result
→ propose a small modification or hypothesis
→ design an experiment
→ analyse results
→ produce a research-style report / poster / presentation
```

### Evidence
- paper-reading records;
- reproduction repo;
- modified experiment;
- experimental results and analysis;
- research-style final report, poster, or presentation.

---

## 6. Recurring Reasoning Backbones

### L1
```text
input → process/model → output
```

### L2
```text
task → data → baseline → model → evaluation
→ diagnosis → improvement → reevaluation
```

### L3
```text
problem / scoring rule
→ data audit
→ validation design
→ baseline
→ metric
→ error analysis
→ controlled improvement
→ tuning / ensemble when justified
→ reproducible comparison
→ postmortem
```

### L4
```text
research question
→ prior work
→ reproducible baseline
→ hypothesis
→ controlled experiment
→ analysis
→ limitation
→ next question
```

---

## 7. Assessment Philosophy

Watching, copying, or running supplied code is not mastery.

Evidence should progressively require students to:
1. explain;
2. trace or inspect;
3. modify with reasoning;
4. rebuild without a complete supplied solution;
5. debug;
6. evaluate;
7. defend decisions using evidence;
8. transfer skills to an unfamiliar task.

---

## 8. Relationship to Existing Repository Materials

Existing G10–G12, session-based, NOAI, IOAI, and competition documents remain useful as **implementation resources and historical planning artifacts**.

They do not override this canonical progression:

```text
L1 — Understand & Code
L2 — Build
L3 — Solve Unseen Problems
L4 — Create New Knowledge
```

When an older document conflicts with the Input / Output / Evidence rules in this file, this file is the canonical program definition.
