# Machine-Learning Implementation and Project Practice Map

This map bridges model recognition and mathematical understanding into executable classical-machine-learning work. It is supporting material for the canonical Sessions; it does not create a parallel course or renumber the 78-Session pathway.

## Core Implementation Workflow

Students should learn to move from an unfamiliar task to a working baseline through the same reusable implementation skeleton:

```text
identify the task
→ identify X, y, output, and metric
→ choose a baseline model family
→ open the official documentation
→ import the estimator or tool
→ instantiate it with minimal defensible parameters
→ fit
→ predict / transform / score
→ evaluate
→ diagnose errors and limitations
→ make one controlled improvement
```

The goal is not to memorise every constructor argument. The goal is to become fast and accurate at finding the correct official API, reading the constructor signature, recognising required inputs, and using the standard `fit` / `predict` / `transform` workflow without copying an entire solution.

## Documentation Literacy

### Classical machine learning — scikit-learn

- Documentation: https://scikit-learn.org/stable/
- Getting started: https://scikit-learn.org/stable/getting_started.html
- Use for estimator imports, constructor parameters, preprocessing, model selection, metrics, pipelines, and examples.

### Tabular data — pandas

- Stable documentation: https://pandas.pydata.org/pandas-docs/stable/
- User guide: https://pandas.pydata.org/docs/user_guide/
- API reference: https://pandas.pydata.org/pandas-docs/stable/reference/
- Use for loading, filtering, grouping, missing values, joins, reshaping, dtypes, and feature-table preparation.

### Deep learning — PyTorch

- Stable documentation: https://docs.pytorch.org/docs/stable/
- Tutorials: https://docs.pytorch.org/tutorials/
- Use in Phase 6 for tensors, `nn.Module`, autograd, optimisers, data loading, and task-specific APIs.

### Required documentation evidence

When a Session requires an implementation rebuild, use the [Documentation-to-Code Evidence Template](../03_Templates/Documentation_to_Code_Evidence_Template.md). Students record the official page used, import path, constructor decisions, preprocessing contract, debugging trace, independent rebuild, metric, and one controlled improvement.

The evidence standard is deliberately different from memorisation. A student may consult official documentation, but should not require a copied end-to-end notebook to complete the core workflow.

## Selective Code-Reinforcement Courses

These are optional implementation supports. Students should use only the assigned sections that reinforce the current Session.

- **University of Michigan — Applied Machine Learning in Python:** https://www.coursera.org/learn/python-machine-learning
  - Strong fit for scikit-learn workflow, supervised versus unsupervised learning, clustering, validation, ensembles, and practical model limitations.
- **IBM — Machine Learning with Python:** https://www.coursera.org/learn/machine-learning-with-python
  - Useful for short code labs covering regression, logistic regression, KNN, trees, SVMs, clustering, validation, and end-to-end practice.
- **DataTalksClub — Machine Learning Zoomcamp:** https://github.com/DataTalksClub/machine-learning-zoomcamp
  - Complete YouTube playlist: https://www.youtube.com/playlist?list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR
  - Use self-paced material for project-oriented workflow rehearsal. The live cohort and the self-paced route use the same pre-recorded lectures; cohort deadlines and certification are not part of this curriculum requirement.

## Real-Data Project Ladder

### Project A — Regression

- **Kaggle House Prices:** https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques
- Primary use: Sessions 42–43 and later Session 57.
- Minimum evidence:
  - define `X` and `y`;
  - create a leakage-safe train/validation split;
  - run a linear-regression baseline or another explicitly justified regression baseline;
  - report MAE or RMSE;
  - identify one preprocessing or feature issue;
  - make one controlled improvement.

### Project B — Binary Classification

- **Kaggle Titanic:** https://www.kaggle.com/competitions/titanic
- Primary use: Sessions 44–45 and later Session 57.
- Minimum evidence:
  - identify label and class balance;
  - run a logistic-regression baseline;
  - produce a confusion matrix;
  - calculate and interpret accuracy plus at least one of precision, recall, or F1;
  - explain why the selected metric fits the task;
  - make one controlled improvement.

### Project C — Imbalanced Classification and Anomaly Detection

- **Kaggle Credit Card Fraud Detection:** https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- Primary use: Sessions 45 and 55.
- Two-pass use:
  1. supervised imbalanced classification using the provided `Class` label;
  2. anomaly-detection rehearsal using `IsolationForest`, treating labels as evaluation evidence rather than training targets when running the unsupervised pass.
- Minimum evidence:
  - explain why raw accuracy is misleading under severe class imbalance;
  - report precision, recall, F1, and/or a precision-recall-oriented metric;
  - compare a supervised baseline with an anomaly-detection baseline;
  - state the operational cost of false positives and false negatives.

## Session Placement

| Session | Model / workflow | Implementation practice |
|---:|---|---|
| 42 | linear regression | scikit-learn `LinearRegression`; House Prices mini-baseline |
| 44 | logistic regression | scikit-learn `LogisticRegression`; Titanic mini-baseline |
| 45 | confusion matrix and metrics | scikit-learn metrics; Titanic and fraud metric comparison |
| 48 | decision trees | scikit-learn tree API; compare with a simple linear/logistic baseline |
| 49 | random forests | scikit-learn `RandomForestClassifier` / `RandomForestRegressor`; controlled comparison |
| 51 | K-nearest neighbours | scikit-learn `KNeighborsClassifier`; scaling before distance-based modelling |
| 53 | K-means | scikit-learn `KMeans`; explicitly contrast KNN with K-means |
| 54 | PCA | scikit-learn PCA; fit only on training data before transforming validation/test data |
| 55 | anomaly detection | scikit-learn `IsolationForest`; Credit Card Fraud two-pass exercise |
| 57 | end-to-end tabular workflow | selected DataTalksClub ML Zoomcamp regression/classification/evaluation material plus Kaggle rehearsal |
| 58 | classical-ML capstone | documentation-assisted independent build; no step-by-step code recipe |

## Documentation Use Progression

### First exposure

Students are expected to use official documentation openly. Teacher prompts may name the model family but should not provide the exact import line or complete constructor. Students should record the page used and identify which constructor fields matter to the baseline.

### Guided independence

Students must locate the class or function, identify the import path, read the key parameters, and produce a minimal working model within a short time limit. At least one default parameter and one deliberately changed parameter should be explained when the model exposes meaningful choices.

### Independent rebuild

Students receive the task and dataset but not the model API. They must choose a defensible baseline, use documentation as needed, implement the workflow, and explain each major line of code. Tutorial/example notebooks are closed during the rebuild; official documentation remains available.

### Competition readiness

Common APIs should be fast to recall, but documentation remains a verification tool. Time should be spent on task formulation, leakage prevention, metric choice, error analysis, and controlled improvement rather than repeatedly rediscovering basic syntax.

## Teaching Rule

Documentation literacy is part of implementation mastery.

A student has not demonstrated mastery merely by copying a notebook that runs. The student should be able to explain:

1. what task is being solved;
2. what `X` and `y` contain;
3. why the selected baseline fits the task;
4. what `fit` is learning from;
5. what `predict`, `transform`, or `score` returns;
6. why the evaluation metric is appropriate;
7. what could cause leakage or invalid validation;
8. what the baseline cannot capture;
9. what one next improvement should be.

## Resource Selection Rule

Do not assign whole external courses by default. Assign the smallest section that supports the current Session, then require students to close the source and rebuild the workflow independently. External videos and notebooks are scaffolds; the evidence standard remains the repository's own task, implementation, evaluation, explanation, and postmortem requirements.
