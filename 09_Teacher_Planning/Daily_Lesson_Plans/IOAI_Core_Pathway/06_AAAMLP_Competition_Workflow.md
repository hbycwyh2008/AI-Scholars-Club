# Unit 6 — AAAMLP Competition Workflow

**Suggested length:** 6 × 75 minutes  
**Core resource:** Abhishek Thakur, *Approaching (Almost) Any Machine Learning Problem*  
**Purpose:** convert model knowledge into fast, defensible competition decisions.

AAAMLP is used here as a **problem-solving playbook**, not as the first explanation of machine-learning algorithms.

## Lesson Sequence

| Lesson | Focus | Competition-style activity | Evidence |
|---:|---|---|---|
| 1 | Problem framing + project structure | read an unfamiliar problem and write the work plan before coding | first-pass plan |
| 2 | Cross-validation strategy | choose K-fold/stratified/group/time-aware split for mixed scenarios | validation decision sheet |
| 3 | Metrics | infer what the metric rewards/punishes; identify metric-model mismatch | metric comparison |
| 4 | Categorical variables + feature engineering | design transformations without leakage | feature plan + ablation proposal |
| 5 | Feature selection + hyperparameter optimisation | decide whether to select/tune and what evidence would justify it | experiment queue |
| 6 | Ensembling + full workflow | design a final competition pipeline from baseline through ensemble | competition playbook + oral defense |

## The Pre-Code Rule

For every new task, students must write this before importing a model:

```text
Task:
Target:
Available labels:
Metric:
Validation strategy:
Leakage risks:
Baseline:
First model family:
First error analysis:
First controlled improvement:
```

## Teacher Emphasis

- Validation is a modeling decision, not a boilerplate line of code.
- A leaderboard improvement is weak evidence if local validation is unstable.
- Feature engineering must be tested with ablation, not defended by intuition alone.
- Hyperparameter optimisation should search a justified space, not every parameter.
- An ensemble must add diversity or complementary errors; averaging similar weak models is not automatically useful.

## Exit Gate

Give the student a short competition brief, dataset description, and scoring metric. Within a fixed planning window, the student must produce a coherent baseline-to-improvement plan and defend the validation strategy before coding begins.
