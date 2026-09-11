# Unit 2 — CodeHS Data Science with Python

**Suggested length:** 6 × 75 minutes  
**Purpose:** make data inspection and evidence-based reasoning automatic before ML begins.  
**Primary resource:** selected lessons from CodeHS *Data Science with Python*; do not require full-course completion.

## Unit Outcomes

Students can inspect an unfamiliar table, identify data-quality risks, transform and summarise data with Pandas, visualise relevant distributions/relationships, and state claims with evidence and limitations.

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
