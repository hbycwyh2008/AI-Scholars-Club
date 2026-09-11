# Classical ML Workflow Routine

Use this routine when Phase 5 moves from learning individual models to solving a complete tabular task.

## Workflow

```text
problem / scoring rule
→ input, output, labels, task family
→ data audit + leakage risks
→ validation design
→ simplest credible baseline
→ preprocessing pipeline
→ metric
→ model
→ error analysis
→ one controlled improvement
→ fair reevaluation
→ documentation
```

## Before Modeling

Students must write:

- target and prediction unit;
- task family;
- metric and what it rewards or penalises;
- split / cross-validation design;
- leakage risks;
- baseline;
- first model family and why it is reasonable.

## During Modeling

Every experiment records:

1. what changed;
2. why it changed;
3. what stayed fixed;
4. validation result;
5. runtime or complexity change when relevant;
6. what the result implies for the next experiment.

Do not tune multiple dimensions at once unless the lesson explicitly studies search methods.

## Error Analysis

Students inspect errors before adding complexity. Depending on the task, inspect:

- residual size and direction;
- false positives / false negatives;
- subgroup or feature slices;
- rare categories;
- missing-data patterns;
- outliers;
- train/validation distribution differences.

## Evidence

- task contract;
- data audit;
- validation justification;
- reproducible baseline;
- experiment log;
- error-analysis artifact;
- one controlled improvement;
- short postmortem.

## Exit Check

A student passes this routine only if another person can rerun the workflow and understand why each major decision was made. A higher score from an invalid split or undocumented change does not count as improvement.
