# IOAI Core Resource Map

This map identifies the **role** of each major external resource in the IOAI-focused pathway. External courses support a teacher-designed mission; completing an external course is not the learning objective.

See: [IOAI Core Learning Path](../00_Course_Overview/IOAI_Core_Learning_Path.md).

| Resource | Main role in this pathway | Use | Usually skip / de-emphasise |
|---|---|---|---|
| **Melanie Mitchell — Artificial Intelligence: A Guide for Thinking Humans** | AI conceptual map immediately after course introduction | selected/complete reading through the existing 8-seminar sequence | treating the book as a coding textbook |
| **CodeHS Data Science with Python** | data fluency | selected Pandas, cleaning, visualisation, statistics, aggregation, data-quality work | full 85-hour completion |
| **CodeHS Advanced Python and AI Programming** | stronger Python + algorithms + AI-programming bridge | OOP, libraries/packages, data structures/algorithms, AI Algorithms, classifier project | projects unrelated to the current IOAI objective unless needed for programming practice |
| **Andreas C. Müller — Applied Machine Learning** | rigorous applied ML workflow | validation, preprocessing, evaluation, imbalance, feature selection, model selection, tuning | watching every lecture before students begin real tasks |
| **DataTalksClub — Machine Learning Zoomcamp** | realistic end-to-end examples | introduction/workflow, regression, classification, evaluation, trees/ensembles | deployment/MLOps as an IOAI prerequisite |
| **Andrew Ng — Machine Learning Specialization** | model principles + mathematics | core specialization, especially regression/classification, trees, clustering, anomaly detection, practical ML advice | passive video completion without transfer labs |
| **Abhishek Thakur — Approaching (Almost) Any Machine Learning Problem** | competition decision-making | validation, metrics, features, selection, tuning, ensembling, reproducibility | using it before students understand basic models and workflow |
| **Andrew Ng — Deep Learning Specialization** | deep-learning conceptual map | neural networks, optimisation, CNNs, sequence models, attention-related concepts | framework-specific memorisation |
| **PyTorch** | executable deep-learning workflow | tensors, Dataset/DataLoader, modules, autograd, training/validation loops, CNN/sequence/attention implementations | copying complete notebooks without reconstruction |
| **Official IOAI/NOAI materials** | target alignment | current syllabus, current rules, authorised assets, task reproductions | assuming previous-year rules are still valid |

## Official / Primary Links

### AI Conceptual Map

- Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans* — use with the repository's eight-seminar AI History sequence.

### CodeHS

- Data Science with Python: https://codehs.com/course/12135/overview
- Advanced Python and AI Programming: https://codehs.com/course/27291/overview
- High School Python Pathway: https://codehs.com/course/pathway/37

### ML Workflow

- Andreas C. Müller, Applied Machine Learning course: https://www.cs.columbia.edu/~amueller/comsw4995s20/
- Andreas C. Müller, course schedule: https://www.cs.columbia.edu/~amueller/comsw4995s20/schedule/
- Applied Machine Learning notes: https://amueller.github.io/aml/
- DataTalksClub Machine Learning Zoomcamp: https://github.com/DataTalksClub/machine-learning-zoomcamp

### Machine Learning Principles

- Andrew Ng Machine Learning Specialization: https://www.coursera.org/specializations/machine-learning-introduction
- Abhishek Thakur AAAMLP repository: https://github.com/abhishekkrthakur/approachingalmost

### Deep Learning and PyTorch

- Andrew Ng Deep Learning Specialization: https://www.coursera.org/specializations/deep-learning
- DeepLearning.AI PyTorch for Deep Learning Professional Certificate: https://www.coursera.org/professional-certificates/pytorch-for-deep-learning
- PyTorch Learn the Basics: https://docs.pytorch.org/tutorials/beginner/basics/intro.html
- PyTorch Tutorials: https://docs.pytorch.org/tutorials/

## Implementation Resource Decisions — 2026-10-13

These choices supplement the existing pathway with library practice; they do not replace its workflow bootcamp or require completing every listed course.

- **scikit-learn:** use [Inria MOOC](https://inria.github.io/scikit-learn-mooc/toc.html) for API/workflow foundations. [IBM Machine Learning with Python](https://www.coursera.org/learn/machine-learning-with-python) is the preferred Coursera practical alternative. Michigan is optional further study; LearnQuest is only a short documentation bridge. See [Scikit-learn API Guide](Scikit_Learn_API_Guide/README.md) for selected sections and transfer evidence.
- **PyTorch:** use [PyTorch: Fundamentals](https://www.coursera.org/learn/pytorch-fundamentals) as the main framework foundation. Select Course 2 for subsequent applications/tuning; Course 3 remains optional. See [PyTorch API Guide](PyTorch_API_Guide/README.md) for viewing order and independent rebuild requirements.
- **Assessment:** follow a worked example, read documentation to adapt a model/API, then solve a new-data task independently. Explain inputs/outputs, preprocessing, validation, metrics, and one controlled improvement.

Consult these recorded decisions before reopening the same resource-selection question. Revisit them when learner evidence reveals a gap, access changes, or the course/API changes materially.

## Teacher Selection Rule

For every assigned external resource, record:

1. **exact lesson/module/section**;
2. **why it is needed now**;
3. **student evidence after using it**;
4. **what students must rebuild or explain without the source open**.

A resource is justified only if it improves the current mission.

## IOAI Resource Sequence

```text
Course Introduction / Orientation
→ Mitchell / AI History conceptual map
→ CodeHS Data Science
→ CodeHS Advanced Python and AI
→ Müller / Zoomcamp workflow bootcamp
→ Andrew Ng ML
→ AAAMLP
→ evaluation / features / tuning / ensemble practice
→ Andrew Ng DL
→ PyTorch
→ current IOAI competition tasks
```

The formal task-recognition drill begins during Data Science and continues throughout the remaining pathway.
