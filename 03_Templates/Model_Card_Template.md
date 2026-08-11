# Model Card

## Intended Task

- Task family:
- Input `X`:
- Target `y` or reason no training label exists:
- Required output:
- Prediction-time boundary:

## Data

- Training data source:
- Validation / test protocol:
- Important data-quality risks:
- Leakage risks:
- Class imbalance, groups, or time-order constraints:

## Baseline

- Constant or rule baseline:
- First learned model:
- Why this baseline is defensible:

## Implementation Provenance

- Library:
- Estimator / class:
- Official documentation URL:
- Import path:
- Defaults intentionally retained:
- Parameters intentionally changed and why:
- Main preprocessing decisions:
- Documentation-to-code evidence: [use the template](Documentation_to_Code_Evidence_Template.md) when required by the Session.

## Model

- Final selected model:
- Prediction or decision rule in plain language:
- Key mathematical or algorithmic idea:
- Why this model was preferred over the baseline:

## Metric

- Primary metric:
- Why it matches the task and error costs:
- Baseline result:
- Final result:
- Threshold used, when applicable:

## Error Analysis

- Most important false-positive / false-negative / residual / cluster / anomaly pattern:
- One failed or neutral experiment:
- One controlled improvement that helped, or justified no-change decision:

## Limitations

- Model limitations:
- Data limitations:
- Distribution-shift risks:
- Conditions under which the model should not be trusted:

## Bias / Safety Considerations

- Potential affected groups or stakeholders:
- Relevant fairness, privacy, or safety issue:
- Human-review or escalation requirement, when applicable:

## Reproduction Steps

Record enough information for another student to reproduce the result without copying the original notebook:

1. environment / library versions when relevant;
2. data split or seed;
3. preprocessing pipeline;
4. estimator and constructor decisions;
5. fit / predict / transform sequence;
6. metric calculation;
7. expected baseline result range.

## Evidence Boundary

State explicitly what the reported validation result does **not** establish, such as causality, deployment safety, fairness, robustness to unseen distribution shift, or superiority outside the tested protocol.
