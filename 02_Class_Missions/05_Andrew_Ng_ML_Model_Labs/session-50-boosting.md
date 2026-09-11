# Session 50 — Boosting

## Goal

Understand sequential error correction and why boosted trees are strong tabular models.

## Learn

Contrast bagging with boosting. Use residual/error-correction intuition to explain how later weak learners focus on mistakes made by the current ensemble.

## Practice

- trace a tiny two-stage residual-correction example;
- compare random forest and boosted-tree validation results;
- inspect learning-rate / number-of-estimators trade-offs;
- discuss overfitting and runtime.

## Rebuild

Fit a boosted-tree model under the same validation setup used for earlier tree models. Change one parameter only after writing a prediction about its effect.

## Share

Explain why a score improvement may not generalise if validation is weak or tuning is repeated too aggressively.

## Evidence

- residual-correction trace;
- model comparison table;
- controlled parameter experiment;
- generalisation warning/limitation.

## Exit Check

Student can distinguish boosting from bagging and explain why boosted trees are a candidate rather than an automatic final answer.
