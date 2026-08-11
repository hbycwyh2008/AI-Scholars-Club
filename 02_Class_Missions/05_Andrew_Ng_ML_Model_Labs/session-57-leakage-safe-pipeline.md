# Lesson 04 — ColumnTransformer, Pipeline, and Leakage-Safe Preprocessing

**Duration:** 75 minutes

## Timeline

| Time | Block | Student output |
|---|---|---|
| 0–8 min | Skill Warm-Up | Inspect a mixed-column dataset. |
| 8–15 min | Talk Robin 1 | Explain which columns need which transformer. |
| 15–22 min | Entry Check | Choose preprocessing for numeric and categorical columns. |
| 22–35 min | Core Pattern | Teacher models ColumnTransformer inside Pipeline. |
| 35–53 min | Guided Practice | Complete supported pipeline design. |
| 53–67 min | Independent Rebuild | Rebuild pipeline plan for a new dataset. |
| 67–75 min | Talk Robin 2 + Evidence | Submit pipeline and leakage note. |

## Core Pattern

```text
Column audit → transformer groups → ColumnTransformer → Pipeline → fit on train only → validate
```

## Documentation-to-Code Evidence

Use the [Documentation-to-Code Evidence Template](../../03_Templates/Documentation_to_Code_Evidence_Template.md) for the independent rebuild.

The student must use official scikit-learn documentation to locate the APIs needed for the selected workflow, including `ColumnTransformer`, `Pipeline`, and the chosen estimator. Record:

- which columns are assigned to which transformer;
- which preprocessing objects learn state during `fit`;
- why those objects must be fitted on training data only;
- the estimator import path and constructor decisions;
- what the full pipeline receives during `fit` and `predict`;
- one concrete leakage failure that the pipeline structure prevents;
- one minimal change that is evaluated under the same validation protocol.

During the independent rebuild, a complete external notebook should not be open. Official pandas and scikit-learn documentation remain allowed.

## Evidence

Submit:

- column mapping;
- pipeline sketch/code;
- completed documentation-to-code evidence;
- one leakage-safe explanation;
- one controlled baseline comparison under the same split / validation protocol.
