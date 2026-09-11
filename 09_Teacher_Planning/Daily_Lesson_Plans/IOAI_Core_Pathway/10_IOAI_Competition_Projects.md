# Unit 10 — IOAI Competition Projects

**Suggested length:** 6+ guided/timed sprints  
**Purpose:** transfer the full workflow to unfamiliar task families under realistic constraints.

Current official IOAI/NOAI rules, authorised assets, package restrictions, runtime limits, and scoring rules override all historical examples.

## Sprint Progression

| Sprint | Task style | Main constraint | Evidence |
|---:|---|---|---|
| 1 | tabular regression | valid baseline within a fixed time budget | task contract + baseline + RMSE/official metric analysis |
| 2 | tabular classification | imbalance / threshold / metric decision | CV results + error analysis |
| 3 | image classification | baseline vs transfer learning | image error gallery + model card |
| 4 | text or sequence task | preprocessing + validation discipline | baseline/deep comparison |
| 5 | unsupervised / anomaly / novel task | task must be inferred, not announced | task justification + evaluation plan |
| 6 | secured mixed mock | no step-by-step prompts; current-rule environment | final submission + experiment log + postmortem |

Add audio, multimodal, scientific-ML, or other task families when they match the active IOAI syllabus/rules.

## Competition Workflow Contract

Every sprint begins with a written plan:

```text
Problem / required output
↓
Task family
↓
Metric and scoring interpretation
↓
Data audit + leakage risks
↓
Validation strategy
↓
Simplest credible baseline
↓
Experiment queue
↓
Error analysis
↓
Controlled improvements
↓
Final fit / submission
↓
Postmortem
```

## Teacher Checkpoints

Do not tell students which model to use at the start. Ask questions such as:

- What exactly is being scored?
- What can leak from the future/group/target into training?
- What is the cheapest baseline that tells us whether the pipeline works?
- What failure pattern do you see?
- Which single experiment has the highest information value next?
- Are you improving local evidence or chasing leaderboard noise?

## Scoring Beyond Accuracy

Teacher assessment should include:

- task recognition;
- validation quality;
- reproducibility;
- experiment discipline;
- metric reasoning;
- error analysis;
- controlled iteration;
- runtime/rule compliance;
- explanation and postmortem.

A high score from an invalid or irreproducible workflow does not pass the sprint.

## Exit Gate

A student is competition-ready only after demonstrating repeated transfer across multiple task families, including at least one unseen task under time constraints, with a clean baseline, valid evaluation, reproducible experiments, error analysis, and an evidence-based next-action strategy.
