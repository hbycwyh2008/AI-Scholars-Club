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

| Mission | Main concept | Required evidence |
|---|---|---|
| WF-1 | frame the problem | task cards |
| WF-2 | inspect before modeling | data audit + risk list |
| WF-3 | validation first | validation decision memo |
| WF-4 | build the baseline | baseline notebook |
| WF-5 | choose the metric | metric justification |
| WF-6 | error analysis | error-slice table |
| WF-7 | controlled improvement | experiment log |
| WF-8 | mini end-to-end challenge | notebook + oral defense + postmortem |

## Source Alignment

Use selected Müller material on workflow, validation, preprocessing, evaluation, imbalance, feature selection/interpretation, and tuning. Use selected Zoomcamp regression, classification, evaluation, and tree/ensemble cases. Deployment/MLOps modules are not an IOAI prerequisite.

## Non-Negotiable Rules

- Split before learning data-dependent preprocessing statistics.
- Keep a final test set untouched when the task warrants it.
- A higher training score is not evidence of improvement.
- Tuning is not the first response to weak performance.
- Students must record what changed between experiments.

## Detailed Teacher Plan

See [Unit 4 — ML Workflow Bootcamp](../../09_Teacher_Planning/Daily_Lesson_Plans/IOAI_Core_Pathway/04_ML_Workflow_Bootcamp.md).

## Exit Gate

On a fresh tabular task, the student independently produces a task contract, data audit, valid validation design, simple baseline, appropriate metric, error analysis, one controlled improvement, comparison, and limitation statement.

## Next Unit

Continue to [05 — Andrew Ng ML Model Labs](../05_Andrew_Ng_ML_Model_Labs/README.md).