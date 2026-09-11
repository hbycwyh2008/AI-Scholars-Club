# Unit 4 — ML Workflow Bootcamp

**Suggested length:** 8 × 75 minutes  
**Primary teacher sources:** Andreas C. Müller *Applied Machine Learning* + selected DataTalksClub *Machine Learning Zoomcamp* modules.  
**Purpose:** establish the end-to-end workflow **before** a model-by-model specialization.

## Unit Spine

```text
problem → data → split → baseline → metric
→ model → error analysis → controlled improvement → reevaluation
```

## Lesson Sequence

| Lesson | Main concept | Real-task activity | Required evidence |
|---:|---|---|---|
| 1. Frame the problem | target, inputs, constraints, scoring rule | convert three messy scenarios into task contracts | task cards |
| 2. Inspect before modeling | schema, distributions, missingness, suspicious columns | audit a fresh tabular dataset | data audit + risk list |
| 3. Validation first | train/validation/test, CV, groups/time, leakage | critique several valid/invalid split plans | validation decision memo |
| 4. Build the baseline | dummy/simple model, preprocessing pipeline | produce first valid regression/classification baseline | baseline notebook |
| 5. Choose the metric | regression vs classification metrics, threshold effects | compare metrics on same predictions | metric justification |
| 6. Error analysis | confusion matrix/errors/residual slices | inspect where the baseline fails | error-slice table |
| 7. Controlled improvement | feature engineering, ablation, model comparison | change exactly one meaningful factor | experiment log |
| 8. Mini end-to-end challenge | independent workflow on fresh data | timed small project | notebook + oral defense + postmortem |

## Source Alignment

### Andreas C. Müller

Use selected material on:

- machine-learning workflow and validation;
- preprocessing and pipelines;
- model evaluation;
- imbalanced data;
- feature selection / interpretation;
- parameter tuning.

### Machine Learning Zoomcamp

Use selected cases from:

- Introduction to Machine Learning;
- Machine Learning for Regression;
- Machine Learning for Classification;
- Evaluation Metrics for Classification;
- Decision Trees and Ensemble Learning.

Deployment/serverless/MLOps modules are not required for this unit.

## Non-Negotiable Teacher Rules

- Split before learning data-dependent preprocessing statistics.
- Keep a final test set untouched when the task warrants it.
- A higher training score is not evidence of improvement.
- Tuning is not the first response to weak performance.
- Students must record what changed between experiments.

## Exit Gate

On a fresh tabular task, the student independently produces:

1. task contract;
2. data audit;
3. valid validation design;
4. simple baseline;
5. appropriate metric;
6. error analysis;
7. one controlled improvement;
8. comparison and limitation statement.

If students cannot defend those eight items, they are not ready to use a larger model catalogue competitively.
