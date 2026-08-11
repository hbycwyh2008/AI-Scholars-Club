# Tabular Classification

## Challenge

Build a leakage-safe classifier, choose metrics that match the error costs, and analyse class-specific failures rather than reporting accuracy alone.

Suitable external rehearsal datasets include Kaggle Titanic for ordinary binary classification and Credit Card Fraud Detection for severe class imbalance.

## Task Formalisation

Before coding, record:

- input features `X`;
- label `y` and class meanings;
- class balance;
- prediction-time boundary;
- leakage risks;
- validation design;
- primary metric and the cost of false positives versus false negatives.

## Baseline Ladder

1. majority-class or simple rule baseline;
2. scikit-learn `LogisticRegression` or another explicitly justified simple classifier;
3. one contrasting tree / ensemble / distance-based classifier only after the first valid baseline is recorded.

For severe class imbalance, also compare against an anomaly-detection formulation when appropriate, but do not confuse unsupervised anomaly training with supervised classification.

## Documentation Rule

Use official pandas and scikit-learn documentation as implementation references. Complete the [Documentation-to-Code Evidence Template](../../03_Templates/Documentation_to_Code_Evidence_Template.md) for the first learned baseline.

Students must be able to locate the estimator import path, distinguish `predict` from probability/score outputs when relevant, inspect constructor parameters, and rebuild the core workflow without a copied end-to-end notebook.

## Required Evidence

- task-recognition / data audit;
- leakage-safe validation design;
- class-balance report;
- majority/rule baseline;
- first valid learned baseline;
- documentation-to-code evidence;
- confusion matrix;
- precision, recall, F1, and/or task-specific metric with interpretation;
- threshold analysis when probability scores are available;
- experiment table with one major factor changed at a time;
- class-specific error analysis;
- one failed or neutral experiment;
- final [Model Card](../../03_Templates/Model_Card_Template.md);
- fresh independent rebuild;
- independent oral explanation.

## Metric Rule

Do not default to accuracy when class imbalance or asymmetric error costs make it misleading. Choose the primary metric from the task objective, then report supporting metrics needed to understand the trade-off.

For medical-style screening or rare-event detection, explicitly discuss recall / sensitivity and the cost of missed positives. For high-cost false alarms, also discuss precision.

## Imbalanced / Anomaly Extension

When using the Credit Card Fraud dataset:

1. run a supervised classifier using `Class` as the training label;
2. run an `IsolationForest` anomaly-detection pass without using `Class` as the training target;
3. use the labels afterward to evaluate both approaches under a common confusion-matrix / precision / recall / F1 view;
4. explain why the learning setups differ even though the evaluation labels are the same.

## Controlled Improvement Rule

Change one major factor at a time: preprocessing, feature set, class weighting / threshold, model family, or a small parameter choice. Compare all changes under the same validation protocol.

## Constraint

A valid baseline and output file must be produced before advanced experimentation. A higher validation score does not compensate for leakage, metric misuse, or inability to explain the implementation.
