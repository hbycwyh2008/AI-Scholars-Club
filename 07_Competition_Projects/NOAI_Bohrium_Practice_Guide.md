# NOAI / Bohrium Competition Practice Guide

This guide selects Bohrium tasks that support the AI Scholars Club pathway. The goal is not to complete every competition on Bohrium. Use the NOAI tasks as the main practice set; use other AI4S tasks only when they match a skill being taught.

## Recommended Entry Points

| Priority | Practice | Link | How to use it |
|---|---|---|---|
| 1 | **NOAI 2026** | [Bohrium NOAI 2026 competition](https://www.bohrium.com/competitions/8821838186) | Official NOAI task series for practice. Read the task and run/train locally first. The competition page notes that remote evaluation may be paid; local practice is available. |
| 2 | **NOAI 2025 Teaching Test (NOAI 2024 tasks)** | [Bohrium competitions](https://www.bohrium.com/competitions) | In the list, open “NOAI2025 教学测试（NOAI2024 真题）”. It contains four prior NOAI China-stage tasks. |
| 3 | **NOAI China-stage task index** | [AI Olympiad Problem Checklist](https://checklist.sota-ai.org/) | Select NOAI China and a year, then open Round 2. Community summaries link to statements, baselines, datasets, and some editorials. Use the contest statement as the authoritative task specification. |
| 4 | **Official IOAI Education Hub** | [IOAI Education Hub](https://ioai-official.org/resources/) | Open the China — NOAI 2024 and China — NOAI 2025 sections for official task repositories and related materials. |
| 5 | **Superconductor critical-temperature prediction** | [Bohrium competitions](https://www.bohrium.com/competitions) | Search the competition list for “超导体临界温度预测”. Use as a lower-stakes tabular regression exercise after the ML workflow unit. |
| 6 | **CNS drug screening and optimization** | [Bohrium competitions](https://www.bohrium.com/competitions) | Search for “中枢神经系统药物研发”. Optional later practice; students may need to learn some domain context, so it is not an early required task. |

## Placement in the Club

### After data cleaning and EDA (L2)

Start with a small, supervised tabular task. Students should inspect the target and columns, identify missing values and possible leakage, define a validation split, establish a simple baseline, and report an appropriate metric. This is an early diagnostic and workflow exercise, not a full competition simulation.

Related project folders:
- [Tabular Regression](01-tabular-regression/README.md)
- [Tabular Classification](02-tabular-classification/README.md)

### After the ML workflow is established (L2 → L3)

Use one NOAI 2024 task from the teaching test. Require students to run the baseline, make one justified change, compare on validation data, create the required submission, and explain what changed. Do not grade leaderboard score alone.

### After PyTorch and modality-specific training (L3)

Use NOAI 2026 and the remaining NOAI tasks as unfamiliar challenges. Select tasks that match the students' current modality skills; do not assign every task at once.

Related project folders:
- [Image Classification](03-image-classification/README.md)
- [Audio Classification](04-audio-classification/README.md)
- [Text Classification](05-text-classification/README.md)
- [Unsupervised Image Analysis](06-unsupervised-image-analysis/README.md)
- [Open-Ended AI Challenge](07-open-ended-ai-challenge/README.md)

## Skills to Teach and Assess

| Skill | Students should be able to… |
|---|---|
| Data audit | Inspect file shapes, column types, target labels, missing/duplicate records, class balance, and suspicious features before training. |
| Validation design | Create a train/validation split that fits the data; use chronological splits for time-dependent data; prevent leakage; keep the test set out of model selection. |
| Baselines and metrics | Build a simple baseline; select a metric that matches the task; compare models on the same validation data; interpret errors by class or subgroup when relevant. |
| Tabular modeling | Build leakage-safe preprocessing pipelines; handle categorical and numeric features; compare a small set of appropriate models; tune only after a baseline is reliable. |
| PyTorch workflow | Read and modify a supplied notebook: tensor shapes, dataset/dataloader, model, loss, optimizer, training/evaluation loop, inference, and output generation. |
| Modality-specific methods | For image tasks, understand transforms and CNNs; for text, basic tokenization/vectorization and classification; for audio, features such as spectrograms; for time series, preserve temporal order. Add only the modality needed by the selected task. |
| Experiment discipline | Change one factor at a time, record the hypothesis and validation result, control random seeds where possible, and avoid tuning to a public leaderboard. |
| Submission and reproducibility | Follow the exact file/interface specification, run the notebook from a clean start, save a usable artifact, and record environment, metric, and limitations. |

## A Repeatable Practice Protocol

1. Read the task statement and write down the target, permitted inputs, metric, time/compute limits, and submission format.
2. Inspect the provided data and baseline before changing code.
3. Run the baseline end to end and save its validation score.
4. Propose one change with a reason; keep the validation protocol fixed.
5. Compare the result to the baseline and explain whether the evidence supports the change.
6. Generate and validate the required submission files.
7. Write a short postmortem: what worked, what failed, what may be leakage, and what to try next.

## Scope Boundary

Bohrium lists many competitions, including research-grade scientific challenges. Those are not all required club content. Prioritize NOAI tasks and introductory tabular tasks; add advanced scientific, drug-discovery, or large-model challenges only when they match a defined learning outcome.

This practice guide supports competition preparation. It does not replace the L1–L4 prerequisites or imply that completing a course or task guarantees qualification.
