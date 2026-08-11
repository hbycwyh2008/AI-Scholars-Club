# Tabular Regression

## Challenge

Predict a continuous target; establish a simple regression baseline, then compare it with a contrasting model family under the same validation protocol.

A suitable external rehearsal dataset is Kaggle House Prices, but the evidence requirements below apply to any tabular-regression dataset assigned by the teacher.

## Task Formalisation

Before coding, record:

- input features `X`;
- continuous target `y`;
- prediction-time boundary;
- leakage risks;
- validation design;
- primary metric and why it matches the task.

## Baseline Ladder

1. constant baseline such as training-target mean or median;
2. scikit-learn `LinearRegression` or another explicitly justified simple regression baseline;
3. one contrasting tree-based or ensemble model only after the first valid baseline is recorded.

## Documentation Rule

Use official pandas and scikit-learn documentation as implementation references. Complete the [Documentation-to-Code Evidence Template](../../03_Templates/Documentation_to_Code_Evidence_Template.md) for the first learned baseline.

Students must be able to locate the estimator import path, inspect constructor parameters, explain `fit` and `predict`, and rebuild the core workflow without a copied end-to-end notebook.

## Required Evidence

- task-recognition / data audit;
- leakage-safe validation design;
- constant baseline result;
- first valid learned baseline;
- documentation-to-code evidence;
- experiment table with one variable changed at a time;
- MAE and/or RMSE with interpretation;
- error analysis by residual magnitude, feature range, or relevant subgroup;
- one failed or neutral experiment;
- final [Model Card](../../03_Templates/Model_Card_Template.md);
- fresh independent rebuild;
- independent oral explanation.

## Primary Metric

MAE or RMSE should normally be preferred over reporting MSE alone because the result is easier to interpret in target units. Use the competition metric when the assigned task specifies one, and explain the difference.

## Controlled Improvement Rule

The student changes one major factor at a time: preprocessing, feature set, model family, or a small parameter choice. Compare each change using the same split or cross-validation protocol. Do not claim improvement from incomparable validation setups.

## Constraint

A valid baseline and output file must be produced before advanced experimentation. A higher score does not compensate for leakage, an invalid split, or inability to explain the implementation.
