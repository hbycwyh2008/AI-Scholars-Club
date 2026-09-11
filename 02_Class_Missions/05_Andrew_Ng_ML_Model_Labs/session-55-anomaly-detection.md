# Session 55 — Anomaly Detection

## Goal

Understand anomaly scoring, distribution intuition, threshold selection, and rare-event evaluation.

## Learn

Frame anomaly detection as identifying unusual observations rather than ordinary balanced classification. Review mean/variance intuition, score distributions, thresholds, and the difficulty of evaluating rare positives.

## Practice

- inspect normal vs unusual feature values;
- vary an anomaly threshold and track false alarms/misses;
- compare an unsupervised/semi-supervised anomaly approach with a supervised classifier when labels exist;
- discuss contamination and distribution shift.

## Rebuild

Students receive a small anomaly scenario and must choose the evaluation plan before fitting a detector.

## Share

Explain which error is more costly and why a threshold that looks good on one dataset may fail after distribution shift.

## Evidence

- threshold decision;
- anomaly-score/error table;
- evaluation rationale;
- failure/shift limitation.

## Exit Check

Student can distinguish anomaly detection from ordinary classification and justify threshold/evaluation choices for a rare-event task.
