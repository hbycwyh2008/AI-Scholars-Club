# 02 — Python Data Foundations, Cleaning, and Visualization

**Suggested length:** 6 × 75 minutes  
**Purpose:** make data inspection and evidence-based reasoning automatic before ML begins.  
**Primary data-learning resources (updated 2026-10-22):** DeepLearning.AI *Python for Data Analytics*, Module 2 (Pandas/descriptive statistics) and Module 3 (visualization), with IBM *Data Analysis with Python*, Module 2 (Data Wrangling), for cleaning. Use DeepLearning.AI Module 1 only for diagnosed Python gaps and retain selected CodeHS exercises for practice.

See [the selected Coursera guide](../../05_Resources/Data_Cleaning_EDA_Visualization_Coursera_Map.md) for exact topics, labs, and deferred content. The suggested six sessions are selected classroom missions, not a promise to complete all external course assignments.

This unit comes **after AI History**. Basic Python remediation is assigned only when diagnostics show a real gap; CS50P is no longer the required Phase 1 sequence.

## Unit Outcomes

Students can inspect an unfamiliar table, identify data-quality risks, transform and summarise data with Pandas, visualise relevant distributions/relationships, and state claims with evidence and limitations.

## Python Hand-Tracing Routine

Hand tracing is a core Python skill and begins before students rely on notebooks or runtime output. Use these short Python videos:

1. [Tracing program execution](https://www.khanacademy.org/computing/tesda-computational-thinking/xed777e2cccd04061:introduction/xed777e2cccd04061:program-execution/v/intro-to-tracing-program-execution) — about 5 minutes.
2. [Tracing loop execution](https://www.khanacademy.org/computing/intro-to-python-fundamentals/x5279a44ae0ab15d6:simulating-phenomena-with-loops/x5279a44ae0ab15d6:while-loops/v/tracing-loop-execution).
3. [Tracing function calls](https://www.khanacademy.org/computing/intro-to-python-fundamentals/x5279a44ae0ab15d6:playing-games-with-functions/x5279a44ae0ab15d6:function-definitions/v/tracing-function-calls).

For each short code fragment, students first predict the output and fill a trace table by hand. Track the variables that change, the loop condition/iteration where relevant, function arguments and return values, and printed output. Only then run the code and explain any mismatch.

## Mission Sequence

| Mission | Learn | Practice / Rebuild | Evidence |
|---|---|---|---|
| DS-1 | data-science life cycle: question → data → analysis → interpretation | rewrite a vague question into a testable data question | task/question card |
| DS-2 | Pandas inspection: shape, columns, dtypes, head/sample, summaries | inspect a fresh dataset without a checklist open | data-audit fragment |
| DS-3 | filtering, grouping, aggregation | answer unseen questions from the same dataset | notebook + explanations |
| DS-4 | missingness, duplicates, invalid types, suspicious values | write a cleaning plan before editing data | data-quality report |
| DS-5 | visualisation and distributions | produce plots that support or reject a claim | chart + written claim |
| DS-6 | mini EDA investigation | complete a short EDA from a fresh CSV | EDA notebook + 2-minute defense |

## Begin the Formal Task-Recognition Routine

From this unit onward, repeatedly ask:

```text
input → output → labels? → task type → baseline → metric
```

At first, simple baselines and teacher-supported metric choices are acceptable. The routine becomes more demanding later.

## Teacher Notes

- Teach NumPy arrays/shapes directly when required; CodeHS is not the only source of truth for the data stack.
- Ask students to predict what a command should return before running it.
- Require written reasons for dropping rows/columns or imputing values.
- Introduce leakage language early.
- Use the legacy Python packets only for diagnosed remediation, not as the default pathway.

## Detailed Teacher Plan

See [Unit 2 — CodeHS Data Science with Python](../../09_Teacher_Planning/Daily_Lesson_Plans/IOAI_Core_Pathway/02_CodeHS_Data_Science.md).

## Exit Gate

Given a fresh CSV, students independently state a defensible question, inspect schema and quality, identify risks, clean/aggregate appropriately, create useful visual evidence, and make one defensible claim with a limitation.

## Next Unit

Continue to [03 — CodeHS Advanced Python and AI Programming](../03_CodeHS_Advanced_Python_and_AI_Programming/README.md).
