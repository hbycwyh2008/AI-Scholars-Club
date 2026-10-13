# Scikit-learn API Guide

Priority interfaces:

`train_test_split`, `Pipeline`, `StandardScaler`, `OneHotEncoder`, `LinearRegression`, `LogisticRegression`, `DecisionTreeClassifier`, `RandomForestClassifier`, `GradientBoostingClassifier`, `KMeans`, `cross_val_score`, `GridSearchCV`, and common metrics.

## Video and Practice Resource Decision — 2026-10-13

**Purpose:** teach students how to use the library and read its documentation, alongside Andrew Ng's model explanations. Do not add another complete theory course by default.

### Primary Library Course: Inria

[Machine learning in Python with scikit-learn — course contents](https://inria.github.io/scikit-learn-mooc/toc.html)

This is a mixed video, notebook, exercise, and quiz course. Not every topic is a video; assign the accompanying code and exercises as well.

| Order | Exact section | Student evidence |
|---|---|---|
| 1 | The predictive modeling pipeline: First model with scikit-learn | Explain X/y and the inputs and outputs of fit, predict, and score; rebuild a train/test example. |
| 2 | Preprocessing for numerical features; Encoding of categorical variables; Using numerical and categorical variables together | Build preprocessing appropriate to the columns; fit preprocessing only on training data. |
| 3 | Videos: Validation of a model; Visualizing scikit-learn pipelines in Jupyter. Also complete Model evaluation using cross-validation. | Explain the split and metric; build a Pipeline and compare cross-validation results. |
| 4 | Hyperparameter tuning: Set and get hyperparameters in scikit-learn; grid-search; randomized-search | Read estimator parameters, define a justified search space, and keep the final test set out of tuning. |
| 5 | Linear models; Decision tree models; Ensemble of models; Evaluating model performance | Select sections that match the current model lesson and compare against a baseline. |

API reference: [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) and [API Reference](https://scikit-learn.org/stable/api/index.html).

### Coursera Alternatives — Selective Use

- [IBM — Machine Learning with Python](https://www.coursera.org/learn/machine-learning-with-python): preferred Coursera practical companion. Use Modules 2–3 for corresponding model labs, Module 5 for evaluation and the Machine Learning Pipelines and GridSearchCV lab, and Module 6 for an integrated project. It teaches applied ML, rather than only the library API.
- [University of Michigan — Applied Machine Learning in Python](https://www.coursera.org/learn/python-machine-learning): optional further study for students with stronger Python/data skills; an intermediate applied ML course, not the default library introduction.
- [LearnQuest — Introduction to Data Science and scikit-learn in Python](https://www.coursera.org/learn/data-science-and-scikit-learn-in-python): a short documentation-use bridge. Module 3 includes Using the Scikit-Learn Docs, Loading and Analyzing datasets, and Applying Linear Regression (I). Its approximately 22 minutes of module videos are too limited to serve as the complete library course; earlier modules largely cover Python, NumPy, and Pandas.

These recommendations are based on the published syllabi, not a full teaching-quality audit. Check student access and the assigned labs before use; free enrolment does not establish free access to all materials.

## Teaching Sequence and Transfer Check

1. Watch the relevant Andrew Ng explanation to establish model intuition.
2. Complete the corresponding Inria notebook/video/exercise, or an assigned IBM lab for extra scaffolding.
3. Read the current API documentation and replace one estimator while preserving the split and evaluation method. Adapt preprocessing and parameters when the new model requires it.
4. Use an unfamiliar dataset to independently choose preprocessing, a baseline, a model, and suitable metrics; report error analysis and one controlled improvement.

Changing an import or class name alone is not evidence of understanding. Require an explanation of data shapes, parameter choices, preprocessing fit boundaries, metric meaning, and comparison fairness. Do not require migration of every Andrew Ng exercise: identify which exercises already use NumPy/scikit-learn, and preserve purposeful NumPy implementations of learning mechanisms.

See also: [English Video Resource Map](../English_Video_Resource_Map.md).
