# Unit 2 — Python Data Foundations, Cleaning, and Visualization

**Suggested length:** 6 × 75 minutes  
**Purpose:** make data inspection and evidence-based reasoning automatic before ML begins.  
**Primary data-learning resources (updated 2026-10-22):** DeepLearning.AI *Python for Data Analytics*, Module 2 (Pandas/descriptive statistics) and Module 3 (visualization), with IBM *Data Analysis with Python*, Module 2 (Data Wrangling), for cleaning. Use DeepLearning.AI Module 1 only for diagnosed Python gaps and retain selected CodeHS exercises for practice.

See [the selected Coursera guide](../../../05_Resources/Data_Cleaning_EDA_Visualization_Coursera_Map.md) for exact topics, labs, and deferred content. The suggested six sessions are selected classroom missions, not a promise to complete all external course assignments.

## Unit Outcomes

Students can inspect an unfamiliar table, identify data-quality risks, transform and summarise data with Pandas, visualise relevant distributions/relationships, and state claims with evidence and limitations.

## Selected Resource Alignment

| Classroom focus | Assigned resource |
|---|---|
| Python readiness | DeepLearning.AI Module 1 quiz/selected gaps; CodeHS remediation |
| Pandas inspection, summaries, filtering, grouping | DeepLearning.AI Module 2 selected videos and labs |
| Missing values, formatting, preprocessing | IBM Data Analysis Module 2 selected videos and one lab |
| Matplotlib/Seaborn and plot interpretation | DeepLearning.AI Module 3 selected videos and labs |
| Independent EDA | new CSV; no full worked solution |

Defer DeepLearning.AI Module 4 (Inferential Statistics) and Module 5 (Time series). IBM visualization/EDA remains an optional targeted reference.

## Lesson Sequence

| Lesson | Learn | Practice | Rebuild | Share / Evidence |
|---:|---|---|---|---|
| 1. Data-science life cycle | question → data → analysis → interpretation | distinguish good/bad statistical questions | rewrite a vague question into a testable data question | task/question card |
| 2. Pandas inspection | shape, columns, dtypes, head/sample, descriptive summaries | inspect a teacher dataset | inspect a new dataset without a checklist open | data-audit fragment |
| 3. Filtering, grouping, aggregation | selection, Boolean masks, groupby, aggregation | answer guided questions | answer three unseen questions from the same dataset | notebook + explanations |
| 4. Data quality | missingness, duplicates, invalid types, suspicious values | locate problems in a dirty table | write a cleaning plan before editing data | data-quality report |
| 5. Visualisation and distributions | choose chart by question; centre/spread/outliers | create and critique plots | produce two plots that support or reject a claim | chart + written claim |
| 6. Mini EDA investigation | connect question, audit, transformations, plots, limitations | teacher conference | complete a short EDA from a fresh CSV | EDA notebook + 2-minute defense |

## Begin the Formal Task-Recognition Routine

From this unit onward, repeatedly ask students to answer:

```text
input → output → labels? → task type → baseline → metric
```

At first, accept simple baselines and teacher-supported metric choices. The routine becomes more demanding as the ML workflow and model phases add vocabulary and experience.

## Teacher Notes

- Teach NumPy arrays/shapes directly when required; CodeHS is not the only source of truth for the data stack.
- Ask students to predict what a command should return before running it.
- Require written reasons for dropping rows/columns or imputing values.
- Introduce leakage language early: a transformation can be technically correct and still be invalid if it uses information from the wrong split.

## Exit Gate

Give students a fresh CSV. Without step-by-step instructions, they must:

1. state the question they can answer;
2. inspect schema and quality;
3. identify at least two risks or limitations;
4. perform appropriate cleaning/aggregation;
5. create useful visual evidence;
6. make one defensible claim and one limitation statement.

Students who cannot do this independently remain in data-foundation practice before entering the ML workflow bootcamp.
