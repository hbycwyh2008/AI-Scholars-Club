# 04 — ML Workflow Bootcamp

**Suggested length:** 8 × 75 minutes  
**Primary teacher sources:** Andreas C. Müller *Applied Machine Learning* + selected DataTalksClub *Machine Learning Zoomcamp* modules.  
**Purpose:** establish the end-to-end workflow **before** a model-by-model specialization.

## Unit Spine

```text
problem → data → split → baseline → metric
→ model → error analysis → controlled improvement → reevaluation
```

## Mission Sequence

| Mission | Main concept | Required evidence | Portfolio evidence to save |
|---|---|---|---|
| WF-1 | frame the problem | task cards | project question, intended user, X/y, metric |
| WF-2 | inspect before modeling | data audit + risk list | data provenance/license, audit summary, one useful figure |
| WF-3 | validation first | validation decision memo | split rationale, leakage risks, test-set policy |
| WF-4 | build the baseline | baseline notebook | runnable baseline and environment notes |
| WF-5 | choose the metric | metric justification | metric definition and what it misses |
| WF-6 | error analysis | error-slice table | representative failure slices and interpretation |
| WF-7 | controlled improvement | experiment log | feature/model/regularization change, hypothesis, result, decision |
| WF-8 | mini end-to-end challenge | notebook + oral defense + postmortem | concise project narrative, limitations, reproducibility and reflection |

## Regularization and Feature Engineering

The bootcamp introduces the idea that fit quality and model complexity must be balanced. Where suitable, compare an unregularized or weakly regularized baseline with L1/Lasso, L2/Ridge, and Elastic Net. Explain `J(θ)=L_data(θ)+λR(θ)`, tune λ (often exposed as `alpha` or `C`) using validation/CV only, and record coefficient or feature effects. Use the task's valid model family; if linear penalties do not apply, document an appropriate complexity control. Keep the final test set untouched.

Call transformations and feature creation **Feature Engineering & Preprocessing**. Fit data-dependent transformations on training data only, preferably in a reproducible pipeline, and compare their effect on the fixed validation design.

Use the [ML Project Portfolio Evidence Template](../../03_Templates/ML_Project_Portfolio_Evidence_Template.md) to preserve evidence as the work happens.

## Source Alignment

Use selected Müller material on workflow, validation, preprocessing, evaluation, imbalance, feature selection/interpretation, and tuning. Use selected Zoomcamp regression, classification, evaluation, and tree/ensemble cases. Deployment/MLOps modules are not an IOAI prerequisite.

## Non-Negotiable Rules

- Split before learning data-dependent preprocessing statistics.
- Keep a final test set untouched when the task warrants it.
- A higher training score is not evidence of improvement.
- Tuning is not the first response to weak performance.
- Students must record what changed between experiments.
- Portfolio claims must be supported by saved, reproducible evidence.

## Detailed Teacher Plan

See [Unit 4 — ML Workflow Bootcamp](../../09_Teacher_Planning/Daily_Lesson_Plans/IOAI_Core_Pathway/04_ML_Workflow_Bootcamp.md).

## Exit Gate

On a fresh tabular task, the student independently produces a task contract, data audit, valid validation design, simple baseline, appropriate metric, error analysis, one controlled improvement, comparison, regularization/complexity-control rationale, limitation statement, and a reproducible portfolio entry.

## Next Unit

Continue to [05 — Andrew Ng ML Model Labs](../05_Andrew_Ng_ML_Model_Labs/README.md).
