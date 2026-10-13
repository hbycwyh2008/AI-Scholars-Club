# Data Cleaning, EDA, and Visualization — Selected Coursera Resources

**Decision recorded:** 2026-10-13  
**Purpose:** give students explicit data-analysis practice before and alongside model building. Use selected videos with labs rather than requiring two full courses.

## Recommended Courses

| Role | Course | Selected scope |
|---|---|---|
| Data cleaning | [IBM — Data Analysis with Python](https://www.coursera.org/learn/data-analysis-with-python) | Module 2 — Data Wrangling |
| Exploratory data analysis (EDA) | Same course | Module 3 — Exploratory Data Analysis |
| Plotting and visual diagnosis | [IBM — Data Visualization with Python](https://www.coursera.org/learn/python-for-data-visualization) | Selected videos/labs from Modules 1–2; the Seaborn video/lab in Module 3 |

The selection is based on the published course directories, not a full teaching-quality audit. Check student access and assigned labs before use. “Enroll for free” does not establish free access to every video, lab, or assessment.

## 1. Data Cleaning

Use Module 2 of Data Analysis with Python. Its six videos address preprocessing, missing values, formatting, normalization, binning, and categorical-to-numeric conversion.

Pair the videos with one of the module's used-car or laptop-pricing data-wrangling labs. Then use a new CSV for independent work.

Students must explain:

- which values are missing, malformed, inconsistent, or duplicated;
- whether a suspected outlier is an error or a valid extreme;
- why they retain, correct, remove, or impute particular values;
- the effects of each change, including row counts and missing-value counts.

**ML boundary:** freeze an appropriate split before learning preprocessing parameters. Fit imputation, scaling, encoding, and feature selection on training data only; apply the fitted transformations to validation/test data. EDA-driven model choices use training/development data; the final test set stays reserved.

Normalization, scaling, and encoding are preprocessing operations; they do not by themselves establish that a dataset is clean. Avoid automatic outlier deletion.

## 2. EDA

Use Module 3 of Data Analysis with Python. Select the videos on the purpose of EDA, descriptive statistics, grouping, and correlation, and complete a corresponding used-car or laptop-pricing EDA lab. Include the module's plotting reading.

Required evidence:

1. State a question before choosing a statistic or plot.
2. Inspect schema, missingness, distributions, and relevant groups.
3. Combine numerical summaries with plots; neither substitutes for the other.
4. Identify at least three supported findings.
5. Link one finding to a testable feature, preprocessing, split, or model hypothesis.

A correlation does not establish causation, and a small linear correlation does not exclude a nonlinear relationship. Distinguish observations from proposed explanations.

## 3. Data Visualization

Use the following exact video titles from Data Visualization with Python:

| Module | Video | Question or skill |
|---|---|---|
| 1 | Basic Plotting with Matplotlib | Construct a plot with readable axes, units, and labels. |
| 2 | Histograms | Inspect concentration, skew, multiple peaks, and truncation; examine bin sensitivity. |
| 2 | Bar Charts | Compare categories or grouped summaries. |
| 2 | Box Plots | Compare medians and spread; flag candidate outliers for investigation. |
| 2 | Scatter Plots | Examine relationships between numerical variables. |
| 2 | Plotting Directly with Matplotlib | Control plots explicitly and adapt the example to new data. |
| 3 | Seaborn and Regression Plots | Explore relationships and fitted trends. |

If students cannot yet select a chart, add the Module 1 video **Types of Plots**.

Pair these videos with the corresponding Matplotlib labs in Modules 1–2 and the regression-plot part of the Module 3 lab. The Seaborn video is approximately four minutes: it is an introduction, not comprehensive Seaborn training.

For this ML-focused unit, defer area/pie charts, waffle charts, word clouds, maps/Folium, Plotly dashboards, and Dash unless a current task requires them. This is a teacher selection rule, not a claim that these tools lack value.

## 4. Suggested Teaching Order

Data inspection → basic quality audit → split boundary where modelling is involved → justified cleaning/preprocessing → distribution plots → relationships/group comparisons → EDA conclusions → baseline and controlled next step.

Introduce basic plots alongside EDA rather than waiting until all cleaning lessons are complete. Use one shared dataset to reduce context switching, then change the dataset for the transfer check.

Existing CodeHS work remains a foundation. Use these Coursera sections to repair observed gaps or provide extra worked examples; students who already demonstrate the skills need not repeat every section.

## 5. Independent Transfer Task

Given an unfamiliar CSV and a stated analysis or prediction task, submit:

- a notebook that runs from a fresh kernel;
- a cleaning log: issue, evidence, action, rationale, and before/after effect;
- three question-driven plots with labels and units;
- three supported findings and their limitations;
- one justified next modelling experiment, or a further analysis question for a non-prediction task;
- split and train-fitted preprocessing evidence when modelling is involved.

Require an individual explanation of one cleaning decision and one plot. Code execution, chart decoration, and course completion alone do not establish mastery.

## Related Repository Materials

- [English Video Resource Map](English_Video_Resource_Map.md)
- [IOAI Core Resource Map](IOAI_Core_Resource_Map.md)
- [Scikit-learn API Guide](Scikit_Learn_API_Guide/README.md)
- [Systematic EDA and split-safe cleaning task](../02_Class_Missions/07_Model_Comparison_EDA_Evaluation/session-72-split-safe-cleaning.md)

Consult this recorded selection before reopening the same resource question. Revisit it if student evidence reveals a gap, course content changes, or access becomes unavailable.
