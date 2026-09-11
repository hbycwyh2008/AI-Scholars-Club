# Model Comparison and Error Analysis Routine

Use this routine at the end of Phase 5 and whenever students compare candidate classical models.

## Comparison Rule

Models are compared only under a trustworthy common evaluation design:

- same task definition;
- same split / cross-validation folds;
- same metric;
- split-safe preprocessing;
- reproducible random state where appropriate;
- documented feature set.

A score from a different split is not a fair comparison.

## Comparison Card

For every candidate model, record:

| Dimension | Question |
|---|---|
| Validation performance | How strong and stable is the score? |
| Training performance | Is there evidence of underfitting or overfitting? |
| Error pattern | Which examples/groups fail? |
| Assumptions / bias | What structure does this model favour? |
| Preprocessing | What transformations does it require? |
| Interpretability | Can important decisions be explained? |
| Runtime / memory | Is the cost justified? |
| Robustness | How sensitive is it to data/split/parameters? |

## Error Analysis Routine

1. collect out-of-sample predictions;
2. identify the largest or most important errors;
3. create meaningful slices/groups;
4. compare error rates or residual distributions by slice;
5. inspect representative examples;
6. write a hypothesis for the failure;
7. propose **one** experiment that could test the hypothesis.

Do not jump directly from an error to a complicated model.

## Model Card Minimum

The final model card includes:

- task and intended output;
- data and split summary;
- baseline;
- candidate models compared;
- metric and results;
- error analysis;
- chosen model and rationale;
- known limitations;
- next experiment.

## Evidence

- fair model-comparison table;
- error-slice analysis;
- one tested failure hypothesis;
- final model card;
- oral defense explaining why one plausible alternative was rejected.

## Exit Check

Student can defend a model choice using validation evidence, failure patterns, cost, and limitations—not simply “this model got the highest score.”
