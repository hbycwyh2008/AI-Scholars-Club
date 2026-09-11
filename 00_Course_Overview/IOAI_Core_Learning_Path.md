# IOAI Core Learning Path

**Status:** preferred IOAI-focused route for new cohorts  
**Purpose:** build competition-ready AI/ML problem-solving without turning the club into a sequence of external courses  
**Use with:** [teacher lesson plans](../09_Teacher_Planning/Daily_Lesson_Plans/IOAI_Core_Pathway/README.md), [resource map](../05_Resources/IOAI_Core_Resource_Map.md), and the recurring [model-recognition drills](../04_Assessment/Model_Recognition_Drills/README.md)

This route does **not** replace the canonical G10–G12 club pathway for every student. It is the focused route for students preparing seriously for NOAI/IOAI or equivalent ML competitions.

## Design Principle

Students should learn three maps before being expected to solve unfamiliar competition tasks:

1. **AI conceptual map** — what major AI approaches are, why they developed, and what their limitations are.
2. **ML workflow map** — how a real problem moves from data and a baseline to evaluation, diagnosis, and controlled improvement.
3. **Model map** — how the major classical and deep-learning methods work, when they are useful, and how to evaluate them.

The competition layer comes after those maps are connected.

```text
programming + data fluency
→ AI conceptual map
→ ML workflow map
→ model principles
→ competition decision-making
→ deep learning
→ IOAI task execution
```

## Recurring Reasoning Backbone

Every ML task repeatedly returns to:

```text
problem
→ input / output / labels
→ task type
→ data audit / EDA
→ split and validation design
→ baseline
→ metric
→ model
→ error analysis
→ controlled improvement
→ reevaluation
→ documentation / postmortem
```

Task-recognition drills continue throughout the route. They are not a one-time unit.

---

## Phase 0 — Entry Diagnostic and Python Readiness

**Goal:** confirm that Python syntax is not the bottleneck.

Students should be comfortable with functions, conditionals, loops, collections, files/CSV, exceptions, and basic debugging. Use targeted remediation only where the diagnostic identifies a gap.

**Resources:** CodeHS Python review material or the legacy Python packets. CS50P remains optional reference/extension.

**Exit gate:** student can independently read, modify, debug, and explain a small Python data-processing program.

---

## Phase 1 — CodeHS Data Science with Python

**Role:** data fluency before machine learning.

Use selected CodeHS lessons rather than requiring the complete course. Prioritise:

- the data-science life cycle;
- Pandas inspection, filtering, grouping, and aggregation;
- missing values, types, duplicates, and cleaning;
- visualisation and data stories;
- descriptive statistics and distributions;
- asking statistical questions and defending claims with evidence.

NumPy arrays, shapes, indexing, and vectorisation are taught directly in the club where needed.

**Exit gate:** student can inspect an unfamiliar tabular dataset and produce a reproducible data-quality/EDA report with at least one defensible claim.

---

## Phase 2 — CodeHS Advanced Python and AI Programming

**Role:** move from basic Python to stronger algorithmic and AI-programming fluency.

Use selected modules rather than the full year-long course. Prioritise:

- object-oriented programming where it improves code organisation;
- libraries and packages;
- data structures and algorithmic trade-offs;
- search / graph-search ideas;
- selected AI Algorithms material;
- the classifier project or an equivalent teacher-designed classifier rebuild.

The adventure-game and music-player projects are optional unless they serve a specific programming objective.

**Exit gate:** student can organise a non-trivial Python program, reason about algorithm choice, use third-party libraries responsibly, and build/evaluate a small classifier.

---

## Phase 3 — AI Conceptual Map + Task Recognition

**Core text:** Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans*.

Use the existing eight-seminar sequence in [`02_Class_Missions/04_AI_History_and_Thinking_Humans`](../02_Class_Missions/04_AI_History_and_Thinking_Humans/README.md).

Alongside the reading, continue daily/weekly task-recognition practice:

```text
input → output → labels? → task type → baseline → metric
```

Students should encounter classification, regression, clustering, dimensionality reduction, anomaly detection, computer vision, NLP, and reinforcement-learning problem statements without being handed the task label in advance.

**Exit gate:** student can place an unfamiliar problem inside an AI/ML conceptual map and explain what evidence would be needed before choosing a model.

---

## Phase 4 — ML Workflow Bootcamp

**Primary teacher resources:**

- Andreas C. Müller — *Applied Machine Learning* (Columbia)
- DataTalksClub — *Machine Learning Zoomcamp* (selected modules)

This phase comes **before** the full Andrew Ng Machine Learning Specialization so students first understand what a complete ML investigation looks like.

Teach the following workflow explicitly:

1. problem framing and target definition;
2. data inspection and EDA;
3. preprocessing without leakage;
4. train/validation/test and cross-validation thinking;
5. simple baseline first;
6. metric selection;
7. error analysis;
8. feature engineering and ablation;
9. model comparison;
10. controlled tuning and documentation.

Use Zoomcamp regression and classification cases as concrete end-to-end examples. Skip deployment/MLOps material unless it serves a separate course goal.

**Exit gate:** student can complete a small tabular ML workflow and defend every major decision, not merely report a score.

---

## Phase 5 — Andrew Ng Machine Learning Specialization

**Role:** supply the model principles and mathematics that sit inside the workflow map.

Prioritise:

- linear and logistic regression;
- cost functions and gradient descent;
- regularisation, bias, variance, and generalisation;
- neural-network foundations;
- decision trees, random forests, and boosted trees;
- clustering and anomaly detection;
- recommender-system ideas;
- advice for applying ML, including error analysis and iterative development.

For each major model, require one transfer task:

```text
recognise suitable task
→ justify baseline/model
→ train
→ evaluate with the right metric
→ inspect errors
→ state limitations
```

**Exit gate:** student can explain the mechanism, assumptions, evaluation logic, and practical role of the major classical model families.

---

## Phase 6 — Approaching (Almost) Any Machine Learning Problem

**Core resource:** Abhishek Thakur, *Approaching (Almost) Any Machine Learning Problem* (AAAMLP).

This is not used as the first ML textbook. It is used after students have enough model vocabulary to turn knowledge into competition decisions.

Focus on:

- problem/task framing;
- cross-validation strategy;
- evaluation metrics;
- categorical variables and feature engineering;
- feature selection;
- hyperparameter optimisation;
- model selection and ensembling;
- reproducible competition workflow.

**Exit gate:** given an unfamiliar dataset and scoring rule, student can write a defensible first-pass plan before touching the model API.

---

## Phase 7 — Evaluation, Features, Tuning, and Ensembling

Deepen the competition workflow with controlled experiments:

- classification, regression, ranking/other task metrics as relevant;
- threshold selection and class imbalance;
- cross-validation design, groups, and time-aware splits;
- leakage detection;
- feature engineering and ablation;
- learning curves and error slices;
- Grid Search / Random Search / Optuna where justified;
- bagging, boosting, voting, blending, and stacking;
- experiment logs and reproducibility.

**Rule:** no tuning before a valid baseline, split, and metric.

**Exit gate:** student can diagnose why a model is weak and choose a controlled next experiment rather than random parameter search.

---

## Phase 8 — Andrew Ng Deep Learning Specialization

**Role:** build the deep-learning conceptual and optimisation map before framework-specific fluency becomes the focus.

Prioritise neural-network mechanics, optimisation, regularisation, CNNs, sequence models, attention, and transferable model-development practices.

**Exit gate:** student can reason about tensors/shapes, forward propagation, backpropagation, optimisation, overfitting, and architecture choice at the conceptual level.

---

## Phase 9 — PyTorch

Turn deep-learning concepts into an executable workflow:

```text
tensor
→ Dataset / DataLoader
→ model
→ forward pass
→ loss
→ backward pass
→ optimiser
→ training loop
→ validation
→ error analysis
```

Use the existing PyTorch/DL mission bank selectively. Require students to rebuild a training loop without copying a complete reference implementation.

**Exit gate:** student can train, validate, debug, and explain a small PyTorch model from a clean runtime.

---

## Phase 10 — IOAI Competition Projects

Move from guided lessons to timed, unfamiliar tasks.

Students rotate through task families such as:

- tabular regression;
- tabular classification;
- image classification / computer vision;
- text classification / NLP;
- audio or multimodal tasks where rules permit;
- unsupervised or anomaly-detection tasks;
- novel-task rapid-baseline challenges.

Every sprint must preserve:

```text
problem contract
→ data audit
→ baseline
→ validation
→ metric
→ experiment log
→ error analysis
→ controlled improvement
→ final submission
→ postmortem
```

Annual IOAI rules always override historical examples in this repository.

---

## Recommended Ordering

```text
Python readiness
→ CodeHS Data Science with Python
→ CodeHS Advanced Python and AI Programming
→ Mitchell + continuing Task Recognition
→ ML Workflow Bootcamp (Müller + Zoomcamp)
→ Andrew Ng Machine Learning Specialization
→ AAAMLP
→ Evaluation / Feature Engineering / Tuning / Ensembling
→ Andrew Ng Deep Learning Specialization
→ PyTorch
→ IOAI competition-style projects
```

Mitchell reading and task-recognition drills may run in parallel with the data/programming phases when the cohort is ready.

## What Not to Do

- Do not require every hour of either CodeHS course.
- Do not make Zoomcamp deployment/MLOps a prerequisite for IOAI.
- Do not start hyperparameter tuning before the validation design is trustworthy.
- Do not turn AAAMLP into an algorithm-first textbook.
- Do not equate watching a course with mastery.
- Do not award mastery for a copied notebook that the student cannot rebuild, debug, evaluate, and defend.
