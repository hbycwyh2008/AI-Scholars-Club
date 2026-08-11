# Documentation-to-Code Evidence Template

Use this template when a Session requires documentation-assisted implementation. The goal is to prove that a student can use an official API reference to build and explain a working baseline without copying a complete solution.

## 1. Task Formalisation

- Task family:
- Input `X`:
- Target `y`, or why no training label exists:
- Required output:
- Primary metric:
- Prediction-time boundary or leakage risk:

## 2. Baseline Choice

- Baseline model or method:
- Why it is a defensible first model:
- Simpler constant or rule baseline for comparison:

## 3. Official Documentation Trace

- Library:
- Class or function:
- Official documentation URL:
- Import path:
- Constructor parameters inspected:
- Main method used after construction (`fit`, `predict`, `transform`, `predict_proba`, `score`, or other):

Record only the documentation needed to justify the implementation.

## 4. Constructor Decision Record

### Defaults intentionally kept

| Parameter | Default | Why keeping it is reasonable |
|---|---|---|
| | | |

### Parameters intentionally changed

| Parameter | Value used | Why changed | Expected effect |
|---|---|---|---|
| | | | |

## 5. Preprocessing Contract

- Numeric features:
- Categorical features:
- Missing-value handling:
- Scaling required? Why or why not?
- Encoding required? Why or why not?
- Which preprocessing steps must be fitted on training data only?

## 6. Minimal Working Implementation

Record the smallest workflow that demonstrates:

```text
import
→ split / preprocess
→ instantiate
→ fit
→ predict / transform
→ evaluate
```

## 7. API-to-Concept Explanation

Explain in your own words:

1. What information does `fit(...)` learn from in this task?
2. What does the relevant prediction or transformation method return?
3. Which mathematical or algorithmic idea from the Session corresponds to the model behaviour?
4. Why is the chosen metric appropriate?

## 8. Debugging Trace

- First error, warning, or incorrect result:
- Likely cause:
- Documentation section or error message used to diagnose it:
- Fix:
- What changed after the fix:

## 9. Independent Rebuild Check

After the first successful run, close tutorial/example material and rebuild the core workflow with only official documentation available.

- Rebuild succeeded: yes / no
- What still required lookup:
- What should be recalled faster next time:

## 10. Baseline Result and One Controlled Improvement

- Baseline metric:
- Main limitation observed:
- One controlled change:
- New metric:
- Did the change help? Why or why not?

## 11. Evidence Boundary

State one thing the result does not prove, such as causality, deployment safety, absence of distribution shift, fairness, or superiority outside the tested validation protocol.

## Completion Standard

The student can explain the model choice, find the correct official API, justify the constructor, run a leakage-safe baseline, interpret the metric, and rebuild the core workflow using documentation without copying an end-to-end solution.
