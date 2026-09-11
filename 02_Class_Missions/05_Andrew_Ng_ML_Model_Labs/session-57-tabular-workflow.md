# Session 57 — Embedded Tabular ML Workflow

## Goal

Integrate Pandas, preprocessing, validation, baseline modeling, error analysis, and one controlled improvement in a Kaggle-style tabular task.

## Learn

Review the complete workflow:

```text
task contract → data audit → split/CV → preprocessing pipeline
→ baseline → metric → error analysis → one controlled improvement
```

## Practice

Students inspect a fresh dataset and identify target, feature types, missingness, leakage risks, metric, and validation strategy before importing a model.

## Rebuild

Complete the task independently:

1. reproducible baseline;
2. split-safe preprocessing;
3. one classical model;
4. validation score;
5. error analysis;
6. exactly one justified feature/model change;
7. fair comparison.

## Share

Present the experiment as a claim: what changed, why, what evidence improved or worsened, and what should be tried next.

## Evidence

- pipeline notebook;
- validation record;
- experiment log;
- error analysis;
- one controlled improvement;
- postmortem.

## Exit Check

Student can complete a tabular workflow without leaking information or tuning randomly and can defend the next experiment from evidence.
