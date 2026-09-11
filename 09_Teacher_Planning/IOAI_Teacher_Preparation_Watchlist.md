# IOAI Teacher Preparation Watchlist

This is the teacher-preparation sequence for the [IOAI Core Learning Path](../00_Course_Overview/IOAI_Core_Learning_Path.md). It is deliberately selective: establish the AI conceptual map first, then the workflow map, then the model map, then competition decision-making.

## Stage 0 — AI Conceptual Map

Before the technical workflow sequence, review the eight-seminar Mitchell arc used with students:

- what counts as intelligence;
- symbolic AI versus learning-based AI;
- neural networks and the history of connectionism;
- computer vision;
- what models actually learn;
- reinforcement learning;
- language understanding;
- common sense, abstraction, analogy, and current limitations.

Teacher takeaway: be able to draw a coherent map connecting AI, ML, deep learning, CV, NLP, and RL without reducing AI to a list of algorithms.

This is why the student pathway places AI History immediately after Course Introduction.

---

## Stage A — Build the ML Workflow Map

Complete these before teaching the Andrew Ng ML phase.

| Order | Source | Focus to watch/study | Teacher takeaway |
|---:|---|---|---|
| 1 | Andreas C. Müller — Applied Machine Learning | course introduction + machine-learning workflow | what an applied ML investigation looks like end to end |
| 2 | Andreas C. Müller | supervised learning, model complexity, model validation | why training score is not enough |
| 3 | Andreas C. Müller | preprocessing | scaling, encoding, missing values, pipelines, leakage risk |
| 4 | Andreas C. Müller | model evaluation | train/validation/test, cross-validation, model selection |
| 5 | Andreas C. Müller | calibration + imbalanced data | why accuracy can be misleading |
| 6 | Andreas C. Müller | feature selection / interpretation | feature reasoning and controlled removal |
| 7 | Andreas C. Müller | parameter tuning | tuning inside a valid validation design |
| 8 | ML Zoomcamp | regression case | see a realistic regression workflow from data to metric |
| 9 | ML Zoomcamp | classification + evaluation | see a realistic classification workflow and metric decisions |
| 10 | ML Zoomcamp | decision trees + ensemble learning | compare tree families and tune only after a baseline |

### What to skip on the first pass

Do not delay Andrew Ng ML in order to finish every Müller lecture or Zoomcamp module. Skip Zoomcamp deployment/serverless/MLOps material for this stage.

### Teacher mastery check

Before moving on, be able to explain and teach this from memory:

```text
problem
→ task / target
→ data audit + EDA
→ split / validation
→ baseline
→ metric
→ model
→ error analysis
→ controlled improvement
→ reevaluation
```

You should also be able to identify at least four forms of leakage or invalid evaluation.

---

## Stage B — Andrew Ng Machine Learning Specialization

Now study the specialization systematically. For each major model, maintain a teacher note with:

- suitable task types;
- assumptions / inductive bias;
- required preprocessing;
- loss/objective intuition;
- metric choices;
- common failure modes;
- one simple baseline comparison;
- one classroom transfer task.

Recommended teaching emphasis:

1. linear regression;
2. logistic regression;
3. gradient descent and regularisation;
4. bias/variance and iterative development;
5. neural-network foundations;
6. decision trees, random forests, boosted trees;
7. clustering;
8. anomaly detection;
9. recommender-system ideas;
10. advice for applying ML and error analysis.

Do not treat completion certificates as teacher readiness. The readiness test is whether you can diagnose a student model and explain the next experiment.

---

## Stage C — AAAMLP as the Competition Playbook

After the Andrew ML model map is established, use Abhishek Thakur's *Approaching (Almost) Any Machine Learning Problem* as the competition-thinking layer.

Study in this order:

1. supervised vs unsupervised problem framing;
2. cross-validation;
3. evaluation metrics;
4. structuring ML projects;
5. categorical variables;
6. feature engineering;
7. feature selection;
8. hyperparameter optimisation;
9. ensembling;
10. reproducibility / serving material only where relevant.

For every chapter, convert one idea into a short IOAI-style decision drill.

---

## Stage D — Deep Learning and PyTorch

Then move to:

```text
Andrew Ng Deep Learning Specialization
→ PyTorch fundamentals
→ complete training/validation loop
→ CNN
→ transfer learning
→ sequence/text models
→ attention/transformer mechanisms
→ domain-specific IOAI tasks
```

The goal is not to learn TensorFlow first and then translate syntax. Use Andrew Ng for conceptual structure and PyTorch for the executable framework.

---

## Stage E — Competition Coaching Practice

Once the above map is established, teacher preparation should become task-centred rather than course-centred.

For every practice dataset, prepare a one-page coaching record:

```text
What is the task?
What is the scoring metric?
What split is valid?
What is the simplest credible baseline?
What failure modes should students inspect?
What is the first controlled improvement?
What experiment should NOT be run yet?
```

Use the current official IOAI/NOAI rules and authorised assets for scored simulations.

## Primary Links

- Müller course: https://www.cs.columbia.edu/~amueller/comsw4995s20/
- Müller schedule: https://www.cs.columbia.edu/~amueller/comsw4995s20/schedule/
- Müller notes: https://amueller.github.io/aml/
- ML Zoomcamp: https://github.com/DataTalksClub/machine-learning-zoomcamp
- Andrew Ng ML: https://www.coursera.org/specializations/machine-learning-introduction
- AAAMLP: https://github.com/abhishekkrthakur/approachingalmost
- Andrew Ng DL: https://www.coursera.org/specializations/deep-learning
- PyTorch tutorials: https://docs.pytorch.org/tutorials/
