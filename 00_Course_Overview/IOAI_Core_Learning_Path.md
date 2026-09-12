# IOAI Core Learning Path

**Status:** preferred IOAI-focused route for new competition-preparation cohorts  
**Purpose:** build competition-ready AI/ML problem-solving without turning the club into a checklist of external courses  
**Use with:** [teacher lesson plans](../09_Teacher_Planning/Daily_Lesson_Plans/IOAI_Core_Pathway/README.md), [resource map](../05_Resources/IOAI_Core_Resource_Map.md), and [model-recognition drills](../04_Assessment/Model_Recognition_Drills/README.md)

This route is distinct from the historical 78-session compatibility map stored in `curriculum_spec.json`.

## Ordering Principle

Students build three maps in this order:

1. **AI conceptual map** — major AI approaches, history, evidence, and limitations.
2. **ML workflow map** — data → split → baseline → metric → error analysis → controlled improvement.
3. **Model map** — major classical and deep-learning methods, their assumptions, and evaluation.

The resulting route is:

```text
Course Introduction / Orientation
→ AI History / A Guide for Thinking Humans
→ CodeHS Data Science with Python
→ CodeHS Advanced Python and AI Programming
→ ML Workflow Bootcamp
→ Andrew Ng Machine Learning Specialization
→ AAAMLP
→ Evaluation / Feature Engineering / Tuning / Ensembling
→ Andrew Ng Deep Learning Specialization
→ PyTorch
→ IOAI competition-style projects
```

**Do not place the CodeHS Python/data units before AI History in this route.**

---

## Phase 0 — Course Introduction, Orientation, and Readiness

**Current folder:** [00_Orientation_and_Evidence](../02_Class_Missions/00_Orientation_and_Evidence/README.md)

Establish the course map, evidence rules, competition context, and current student starting point. Use a short challenge and Python/data diagnostic only to identify gaps; do not turn orientation into a long remedial Python block.

**Exit gate:** students can explain the route and evidence standard, and immediate readiness gaps are identified.

---

## Phase 1 — AI History and Conceptual Map

**Current folder:** [01_AI_History_and_Thinking_Humans](../02_Class_Missions/01_AI_History_and_Thinking_Humans/README.md)  
**Core text:** Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans*.

This phase comes immediately after orientation so students first understand symbolic AI, learning-based AI, neural-network cycles, and the relationship among AI, ML, DL, CV, NLP, and RL. They also learn to separate demonstrated capability from unsupported claims.

Use light problem-framing questions:

```text
What is the problem?
What is the input?
What output would count as success?
What evidence would convince us that the system works?
```

Do not force the full baseline/model/metric routine before students have enough data and ML vocabulary.

**Exit gate:** students can place later technical topics inside a coherent AI map and audit claims with evidence and boundaries.

---

## Phase 2 — CodeHS Data Science with Python

**Current folder:** [02_CodeHS_Data_Science_with_Python](../02_Class_Missions/02_CodeHS_Data_Science_with_Python/README.md)

Use selected CodeHS lessons rather than the complete course. Prioritise the data-science life cycle, Pandas inspection/filtering/grouping, data quality, visualisation, descriptive statistics, and evidence-based claims.

Use Basic Python Bootcamp or [legacy Python packets](../02_Class_Missions/Legacy_01_CS50P_Python/README.md) only for diagnosed gaps. Teach NumPy arrays/shapes directly when needed.

From this phase onward, begin the recurring task-recognition routine:

```text
input → output → labels? → task type → baseline → metric
```

**Exit gate:** students can inspect a fresh tabular dataset and produce a reproducible data-quality/EDA report with a defensible claim and limitation.

---

## Phase 3 — CodeHS Advanced Python and AI Programming

**Current folder:** [03_CodeHS_Advanced_Python_and_AI_Programming](../02_Class_Missions/03_CodeHS_Advanced_Python_and_AI_Programming/README.md)

Select only the modules that improve IOAI readiness: OOP where useful, libraries/packages, data structures and algorithms, search, selected AI algorithms, and a classifier build/evaluation task.

**Exit gate:** students can organise a non-trivial Python program, read documentation, justify an algorithm/data-structure choice, trace search, and build/evaluate a small classifier.

---

## Phase 4 — ML Workflow Bootcamp

**Current folder:** [04_ML_Workflow_Bootcamp](../02_Class_Missions/04_ML_Workflow_Bootcamp/README.md)  
**Primary teacher resources:** Andreas C. Müller *Applied Machine Learning* + selected DataTalksClub *Machine Learning Zoomcamp* modules.

Teach the complete investigation before the full model catalogue:

```text
problem framing
→ data audit / EDA
→ valid split
→ baseline
→ metric
→ model
→ error analysis
→ controlled improvement
→ reevaluation
```

Skip deployment/MLOps unless it serves a separate objective.

**Exit gate:** students can complete a small tabular ML workflow and defend every major decision, not merely report a score.

---

## Phase 5 — Andrew Ng Machine Learning Specialization

**Current folder:** [05_Andrew_Ng_ML_Model_Labs](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/README.md)

Use Andrew Ng as the model-principles and mathematics spine: regression, classification, cost/gradient descent, regularisation, bias/variance, trees/ensembles, clustering, anomaly detection, recommenders, and practical ML advice.

For each major model require:

```text
recognise task → justify baseline/model → train → evaluate → inspect errors → state limitations
```

---

## Phase 6 — Approaching (Almost) Any Machine Learning Problem

Use Abhishek Thakur’s *Approaching (Almost) Any Machine Learning Problem* **after** students have enough model vocabulary. Focus on validation strategy, metrics, categorical variables, features, selection, optimisation, model selection, ensembling, and reproducibility.

**Exit gate:** given an unfamiliar dataset and scoring rule, students can write a defensible first-pass plan before touching the model API.

---

## Phase 7 — Evaluation, Features, Tuning, and Ensembling

Deepen metric choice, thresholding, imbalance, group/time-aware validation, leakage detection, feature engineering, ablation, learning curves, error slices, Optuna/search methods where justified, and ensemble methods.

**Rule:** no tuning before a valid baseline, split, and metric.

---

## Phase 8 — Andrew Ng Deep Learning Specialization

Build the deep-learning conceptual and optimisation map: neural-network mechanics, optimisation, regularisation, CNNs, sequence models, attention, and transferable model-development practices.

---

## Phase 9 — PyTorch

Turn deep-learning concepts into an executable workflow:

```text
tensor → Dataset/DataLoader → model → forward → loss → backward → optimiser → training loop → validation → error analysis
```

Use the existing DL/PyTorch mission bank selectively and require independent reconstruction.

---

## Phase 10 — IOAI Competition Projects

Move from guided lessons to timed unfamiliar tasks across tabular, CV, NLP, multimodal, anomaly/unsupervised, and novel-task settings as rules permit.

Every sprint preserves:

```text
problem contract → data audit → baseline → validation → metric
→ experiment log → error analysis → controlled improvement → submission → postmortem
```

Annual IOAI rules override historical examples in this repository.

## What Not to Do

- Do not bury AI History after multiple technical courses.
- Do not make CS50P the required first phase for this route.
- Do not require every hour of either CodeHS course.
- Do not make Zoomcamp deployment/MLOps an IOAI prerequisite.
- Do not tune before validation, baseline, and metric are trustworthy.
- Do not treat AAAMLP as the first algorithm textbook.
- Do not equate course completion with mastery.
- Do not award mastery for a copied notebook a student cannot rebuild, debug, evaluate, and defend.