# Unit 7 — Evaluation, Features, Tuning, and Ensembling

**Suggested length:** 8 × 75 minutes  
**Purpose:** deepen the competition workflow after students can already produce a valid baseline.

## Lesson Sequence

| Lesson | Focus | Lab / decision task | Evidence |
|---:|---|---|---|
| 1 | Classification evaluation | confusion matrix, precision, recall, F1, ROC-AUC, PR-AUC, threshold | metric decision memo |
| 2 | Regression + other-task metrics | MAE, MSE/RMSE, R²; introduce task-specific metrics when needed | metric comparison notebook |
| 3 | Cross-validation design | stratification, groups, time, repeated CV, final holdout | split plan + leakage audit |
| 4 | Error analysis | residuals, confusion slices, subgroup/failure analysis | error-analysis report |
| 5 | Feature engineering + pipelines | encoding, scaling, interactions, transformations, split-safe pipelines | feature experiment log |
| 6 | Feature selection + ablation | remove/add feature groups under fixed validation | ablation table |
| 7 | Hyperparameter tuning | manual search → random/grid → Optuna when justified | search-space rationale + results |
| 8 | Ensembling | bagging/boosting/voting/blending/stacking; OOF logic | ensemble comparison + postmortem |

## Metric Selection Questions

Students should be able to answer:

- What kind of mistake is costly?
- Is the class distribution balanced?
- Does ranking matter more than a fixed threshold?
- Is absolute error or squared error more aligned with the task?
- Is the competition metric decomposable by row, group, time, query, image, or sequence?
- Can the local validation reproduce the scoring situation?

## Tuning Gate

Tuning is allowed only after the student can show:

1. a valid split/CV design;
2. a reproducible baseline;
3. the correct metric;
4. at least one error-analysis result;
5. a reason the chosen hyperparameter is worth searching.

## Ensembling Gate

Before combining models, students compare their validation predictions/errors. The ensemble must have a stated reason for improvement: diversity, variance reduction, complementary feature/model bias, or a task-specific advantage.

## Exit Gate

On one held-out competition-style task, the student must show a complete sequence from baseline through diagnosis, a justified feature experiment, controlled tuning, and an ensemble attempt, with an experiment log that makes every score reproducible.
