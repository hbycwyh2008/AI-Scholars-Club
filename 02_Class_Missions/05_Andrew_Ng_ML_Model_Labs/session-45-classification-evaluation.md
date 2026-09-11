# Session 45 — Classification Evaluation

## Goal

Choose and interpret classification metrics instead of treating accuracy as universal.

## Learn

Build the confusion matrix and derive precision, recall, and F1. Introduce ROC-AUC / ranking intuition and threshold trade-offs. Connect metric choice to the cost of false positives and false negatives.

## Practice

- compute metrics from a small confusion matrix;
- compare two classifiers whose accuracy is similar but error profiles differ;
- vary the classification threshold and observe precision/recall changes;
- identify when imbalance makes accuracy weak evidence.

## Rebuild

Given predictions/probabilities from a fresh task, students choose the metric and threshold policy, then justify both from the problem statement.

## Share

One student defends a metric; a peer argues for an alternative. The class decides what task assumption would make either metric appropriate.

## Evidence

- confusion-matrix calculations;
- metric/threshold decision memo;
- short imbalance analysis;
- one failure slice.

## Exit Check

Student can select a classification metric from task consequences and explain how threshold choice changes the error trade-off.
