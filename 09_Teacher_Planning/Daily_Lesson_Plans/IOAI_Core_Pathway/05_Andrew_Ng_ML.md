# Unit 5 — Andrew Ng Machine Learning Specialization

**Suggested length:** 12 × 75 minutes plus independent Coursera study as assigned  
**Purpose:** connect model principles and mathematics to the workflow map already established in Unit 4.

External videos provide explanations; club time is used for reconstruction, transfer, diagnosis, and comparison.

## Lesson Sequence

| Lesson | Model / concept | In-class transfer | Evidence |
|---:|---|---|---|
| 1 | Linear regression, prediction, MSE | hand prediction + sklearn baseline | equation-to-code note |
| 2 | Gradient descent, scaling, learning rate | trace updates and diagnose bad scaling/rate | gradient trace |
| 3 | Multiple regression + feature reasoning | compare raw vs engineered features | experiment log |
| 4 | Logistic regression, sigmoid, log loss | probability/threshold exercise + classifier | classification notebook |
| 5 | Regularisation, bias, variance | compare underfit/overfit/regularised models | learning-curve diagnosis |
| 6 | Neural-network foundations | trace a small forward pass | shape/activation trace |
| 7 | Decision trees | split/impurity reasoning + tree baseline | tree explanation |
| 8 | Random forests + bagging | compare tree vs forest under same split | controlled comparison |
| 9 | Boosted trees | iterative correction intuition + boosted model | model comparison card |
| 10 | K-means + unsupervised evaluation questions | cluster a dataset; question whether clusters are useful | clustering memo |
| 11 | Anomaly detection + recommender ideas | threshold/density or similarity task | task/model justification |
| 12 | Applying ML: error analysis and iterative development | mixed unfamiliar task | capstone model card + defense |

## Required Pattern for Every Model

Students answer:

```text
What task is this model suitable for?
What does it assume or favour?
What preprocessing matters?
What objective/loss is being optimised?
What metric should evaluate the real task?
What failure pattern would make us change course?
What simpler baseline should it beat?
```

## Mathematics Standard

For representative models, require:

- meaning of variables and shapes;
- one hand calculation or trace;
- objective/loss intuition;
- equation-to-code translation;
- explanation of what changing an important parameter does.

Do not require detached mathematics that students cannot connect to model behaviour.

## IOAI Transfer Rule

After each 2–3 lessons, give a problem statement that does **not** name the model. Students first choose the task, baseline, metric, and validation design; only then do they choose among learned model families.

## Exit Gate

Student can compare and defend major classical model families, explain core mathematical mechanisms at the required level, and select/evaluate models inside a valid workflow rather than by API familiarity.
