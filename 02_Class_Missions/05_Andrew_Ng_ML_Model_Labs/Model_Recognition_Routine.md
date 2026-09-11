# Model Recognition Routine

Use this routine throughout Phase 5 and continue it during later competition preparation. The purpose is to make task recognition and first-pass model decisions automatic before students touch an API.

## Daily Format — 15 Minutes

Each daily set contains **5 unfamiliar scenarios**. Do not reveal the task family in the prompt.

For every scenario, students answer:

```text
1. What is the input?
2. What output is required?
3. Are labels / target values available?
4. What task family is this?
5. What is the simplest credible baseline?
6. What metric should judge success?
```

Students should also name one likely data/validation risk when the scenario gives enough information.

## Scenario Mix

Rotate across:

- classification;
- regression;
- clustering;
- dimensionality reduction;
- anomaly detection;
- recommendation / ranking;
- image, text, audio, and time-series settings;
- ambiguous real-world prompts where the correct response is to ask for missing information.

Do not write giveaway wording such as “there are no labels, so...” or “predict a category using classification.” Students infer the structure from the problem statement.

## Repeat Control

Keep the **recent repeat window at 15 scenarios**. A scenario may reappear later for retention, but not inside the recent window unless the teacher deliberately assigns remediation.

## Mastery Standard

A student reaches model-recognition mastery after **5 consecutive practice days** with:

- at least **90% overall accuracy**; and
- at least **90% accuracy on baseline + metric decisions**.

Completion of five days alone is not mastery.

After mastery, move to maintenance rather than stopping completely:

- **2 maintenance sets per week**;
- mixed task families;
- occasional current IOAI/NOAI-style scenarios;
- harder ambiguity and validation decisions.

## Secured Confirmation

Public drills are practice evidence only. Final mastery requires a **secured confirmation set** that students have not seen and cannot obtain from the public repository in advance.

## Evidence

Record for each set:

- date / set identifier;
- task-family accuracy;
- baseline-choice accuracy;
- metric-choice accuracy;
- common error pattern;
- next remediation or maintenance action.

Use the public drill bank:

- [Model Recognition Drill Index](../../04_Assessment/Model_Recognition_Drills/README.md)
- [Level 1 — Foundations](../../04_Assessment/Model_Recognition_Drills/Level_1_Foundations.md)
- [Level 2 — Mixed Tasks](../../04_Assessment/Model_Recognition_Drills/Level_2_Mixed_Tasks.md)
- [Level 3 — Competition Tasks](../../04_Assessment/Model_Recognition_Drills/Level_3_Competition_Tasks.md)

## Teacher Rule

Do not reward model-name recall by itself. A correct answer must connect the **problem structure, baseline, and metric**. If a student chooses a sophisticated model but cannot justify the task or evaluation, mark the reasoning incomplete.
