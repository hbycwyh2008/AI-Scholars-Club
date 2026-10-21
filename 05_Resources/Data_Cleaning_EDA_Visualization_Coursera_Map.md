# Python, Data Cleaning, EDA, and Visualization — Selected Coursera Resources

**Decision updated:** 2026-10-22  
**Purpose:** use one connected data-learning sequence before and alongside ML, with a focused cleaning supplement. This replaces the 2026-10-13 IBM-only selection.

## Recorded Resource Choice

| Role | Resource | Assigned scope |
|---|---|---|
| Python diagnostic / remediation | [DeepLearning.AI — Python for Data Analytics](https://www.coursera.org/learn/python-for-data-analytics) | Module 1 — Programming fundamentals for data analytics; assess first and assign only gaps |
| Pandas and initial EDA | Same course | Module 2 — Data structures and descriptive statistics |
| Focused cleaning supplement | [IBM — Data Analysis with Python](https://www.coursera.org/learn/data-analysis-with-python) | Module 2 — Data Wrangling; selected videos and one matching lab |
| Visualization | DeepLearning.AI — Python for Data Analytics | Module 3 — Visualization |
| Additional practice | Existing CodeHS Data Science with Python work | Select exercises for observed gaps; do not repeat demonstrated skills |

DeepLearning.AI Modules 2–3 are the main Coursera sequence. IBM Module 2 fills the explicit cleaning/preprocessing gap. Existing CodeHS basic/advanced programming resources remain available in the canonical L1 pathway; this selection does not require students to restart Python.

This choice is based on published course directories and the club's limited teaching time, not a full teaching-quality audit. Check access to assigned labs before use. Course platform workload estimates are not classroom lesson counts.

## 1. Python Readiness

Use Module 1 quiz(s) and a short independent coding task to identify gaps. The module covers Jupyter, variables, types, lists, comparisons, conditionals, loops, and calling functions.

Require students to write and explain a small program using a conditional, loop, and function. Use CodeHS practice to repair missing skills such as defining functions or using dictionaries; do not assume the module alone covers every Python prerequisite.

Students with demonstrated Kaggle/CodeHS Python skills may skip repeated instruction.

## 2. Pandas and EDA — DeepLearning.AI Module 2

Prioritise these published video topics:

- Reading CSV into Python; DataFrames; Attributes and methods;
- Selecting columns; Selecting rows;
- Sorting; Sorting by multiple columns;
- Filtering; Filtering by multiple conditions;
- Counts, sums, & histograms;
- Central tendency, variability, and skewness;
- Categorical data; Correlation;
- Segmentation by one feature; Segmentation by multiple features.

Use the corresponding Buenos Aires Subway practice labs and/or the Retail sales assignment selectively, then apply the operations to a fresh CSV.

Students must explain what each row/column means, distinguish an attribute from a method, predict an operation's result, and support findings with numerical summaries.

Teach NumPy shapes, dtypes, indexing, and vectorisation directly where needed; this course selection is not a complete NumPy course.

## 3. Cleaning Supplement — IBM Module 2

Use the Data Wrangling videos on preprocessing, missing values, formatting, normalization, binning, and categorical-to-numeric conversion. Complete one corresponding used-car or laptop-pricing lab.

Students must explain:

- missing, malformed, inconsistent, or duplicated values;
- whether a suspected outlier is an error or a valid extreme;
- why values are retained, corrected, removed, or imputed;
- before/after row counts and missing-value counts.

Normalization, scaling, and encoding are preprocessing operations; they do not by themselves establish that data is clean. Avoid automatic outlier deletion.

**ML boundary:** freeze an appropriate split before learning preprocessing parameters. Fit imputation, scaling, encoding, and feature selection on training data only; apply fitted transformations to validation/test data. EDA-driven model choices use training/development data; reserve the final test set.

## 4. Visualization — DeepLearning.AI Module 3

Use Matplotlib/Seaborn basics and selected corresponding labs:

| Published topic | Required purpose |
|---|---|
| Plotting with matplotlib | readable axes, units, and labels |
| Scatter plots | relationships between numeric variables |
| Box plots | compare centre/spread and investigate candidate outliers |
| Histograms | distributions, skew, and sensitivity to bins |
| Grouped column charts | category/group comparisons |
| Plotting with Seaborn | adapt a statistical plot to a stated question |
| Matplotlib subplots; Seaborn pairplot | select when a question needs multiple comparisons |

Select styling, annotations, and saving plots when needed for readable evidence. Defer decorative refinements and repeated chart variants.

Choose from the Flight delays and cancellations labs or the coral-reef assignment, then require new-data transfer.

## 5. Teaching Order and Deferred Content

Recommended order:

Python readiness check → Module 2 Pandas inspection/summary → IBM Module 2 cleaning → Module 3 visualization → integrated EDA → ML baseline.

Introduce basic plots alongside inspection and cleaning. Use one shared classroom dataset to reduce context switching, then change the dataset for an independent check. Select matching sections and labs rather than assigning three complete modules plus every exercise.

- **DeepLearning.AI Module 4 — Inferential Statistics:** defer until inference/regression is needed.
- **DeepLearning.AI Module 5 — Time series:** defer until a time-series task needs it. Module 5 is not the data-cleaning unit.
- **IBM Data Analysis Module 3 — EDA:** optional targeted reference if the main sequence leaves a specific gap.
- **IBM Data Visualization with Python:** optional reference; full completion is not required. Do not duplicate the main Module 3 plotting sequence. Defer Folium/maps and Plotly/Dash dashboards unless a task needs them.

## 6. Independent Transfer Task

Given an unfamiliar CSV and a stated analysis or prediction task, submit:

- a notebook that runs from a fresh kernel;
- a cleaning log: issue, evidence, action, rationale, and before/after effect;
- three question-driven plots with labels and units;
- three supported findings and their limitations;
- one justified next modelling experiment, or a further question for a non-prediction task;
- split and train-fitted preprocessing evidence when modelling is involved.

Require an individual explanation of one transformation, one cleaning decision, and one plot. Correlation does not establish causation. Course completion and chart decoration alone do not establish mastery.

## Sources and Related Materials

Course directories checked 2026-10-22:

- [DeepLearning.AI — Python for Data Analytics](https://www.coursera.org/learn/python-for-data-analytics)
- [IBM — Data Analysis with Python](https://www.coursera.org/learn/data-analysis-with-python)
- [IBM — Data Visualization with Python (optional reference)](https://www.coursera.org/learn/python-for-data-visualization)

Repository links:

- [English Video Resource Map](English_Video_Resource_Map.md)
- [IOAI Core Resource Map](IOAI_Core_Resource_Map.md)
- [Scikit-learn API Guide](Scikit_Learn_API_Guide/README.md)
- [Data-foundation class missions](../02_Class_Missions/02_CodeHS_Data_Science_with_Python/README.md)
- [Systematic EDA and split-safe cleaning task](../02_Class_Missions/07_Model_Comparison_EDA_Evaluation/session-72-split-safe-cleaning.md)

Consult this selection before assigning overlapping courses. Revisit when student evidence reveals a gap, course content changes, or access becomes unavailable.
