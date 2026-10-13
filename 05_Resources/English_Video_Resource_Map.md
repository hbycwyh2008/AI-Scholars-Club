# English Video Resource Map

## Python and Data Foundations

- **CodeHS Data Science with Python:** https://codehs.com/course/12135/overview
  - Use selected data-life-cycle, Pandas, cleaning, visualisation, statistics, aggregation, and data-quality work.
  - Do not require full-course completion for the IOAI route.
- **CodeHS Advanced Python and AI Programming:** https://codehs.com/course/27291/overview
  - Use selected OOP, libraries/packages, data structures/algorithms, AI Algorithms, and classifier-project material for the IOAI route.
- **Harvard CS50’s Introduction to Programming with Python:** https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f
  - Exact timestamp map for assigned sections: [`CS50P_edX_Timestamp_Map.md`](CS50P_edX_Timestamp_Map.md)
  - Optional remediation/reference, not the IOAI spine.

## Applied Machine-Learning Workflow — IOAI Teacher Priority

- **Andreas C. Müller — Applied Machine Learning, Columbia:** https://www.cs.columbia.edu/~amueller/comsw4995s20/
- **Müller course schedule / recordings map:** https://www.cs.columbia.edu/~amueller/comsw4995s20/schedule/
- **Applied Machine Learning notes:** https://amueller.github.io/aml/
  - Prioritise workflow, model validation, preprocessing, evaluation, imbalanced data, feature selection/interpretation, and parameter tuning.
- **DataTalksClub Machine Learning Zoomcamp:** https://github.com/DataTalksClub/machine-learning-zoomcamp
  - For IOAI, prioritise the introduction/workflow, regression, classification, evaluation metrics, and decision-trees/ensemble modules.
  - Deployment/serverless/MLOps modules are optional and should not delay competition preparation.

Use the [IOAI Teacher Preparation Watchlist](../09_Teacher_Planning/IOAI_Teacher_Preparation_Watchlist.md) for the recommended viewing order.

## Scikit-learn Library Practice — Decision Recorded 2026-10-13

- **Primary library course: Inria — Machine learning in Python with scikit-learn:** https://inria.github.io/scikit-learn-mooc/toc.html
  - Begin with The predictive modeling pipeline: estimator API, preprocessing, validation, and Pipeline. This combines videos with notebooks and exercises; not every lesson is a video.
  - Select Hyperparameter tuning and model-specific sections when needed.
- **Preferred Coursera practical alternative: IBM — Machine Learning with Python:** https://www.coursera.org/learn/machine-learning-with-python
  - Select matching model labs from Modules 2–3, evaluation/Pipeline/GridSearchCV from Module 5, and an integrated project from Module 6.
- **Optional intermediate extension: University of Michigan — Applied Machine Learning in Python:** https://www.coursera.org/learn/python-machine-learning
- **Short documentation bridge: LearnQuest — Introduction to Data Science and scikit-learn in Python:** https://www.coursera.org/learn/data-science-and-scikit-learn-in-python
  - Module 3 introduces documentation and model use; it is too short to be the complete library course.

**Recorded choice:** use Inria for library/API foundations; IBM is an alternative practical scaffold when Coursera is preferred. Do not assign all alternatives or repeat all machine-learning theory.

Exact sections, API references, and the independent model/data transfer check: [Scikit-learn API Guide](Scikit_Learn_API_Guide/README.md).

## Artificial Intelligence and Traditional Machine Learning

- **AI for Everyone on Coursera:** https://www.coursera.org/learn/ai-for-everyone
- **Machine Learning Specialization on Coursera:** https://www.coursera.org/specializations/machine-learning-introduction
- **Course 2 — Advanced Learning Algorithms:** https://www.coursera.org/learn/advanced-learning-algorithms
- **Google Machine Learning Crash Course:** https://developers.google.com/machine-learning/crash-course
- **StatQuest Video Index:** https://statquest.org/video-index/

### Competition Problem-Solving Companion

- **Abhishek Thakur — Approaching (Almost) Any Machine Learning Problem:** https://github.com/abhishekkrthakur/approachingalmost
  - This is primarily a book/code companion rather than a complete official video course.
  - Use after the basic model/workflow map to develop validation, metrics, feature engineering, tuning, and ensembling decisions.

## Deep Learning

- **Deep Learning Specialization on Coursera:** https://www.coursera.org/specializations/deep-learning
- **Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization:** https://www.coursera.org/learn/deep-neural-network
- **3Blue1Brown Neural Networks:** https://www.3blue1brown.com/topics/neural-networks

## PyTorch

- **DeepLearning.AI PyTorch for Deep Learning Professional Certificate on Coursera:** https://www.coursera.org/professional-certificates/pytorch-for-deep-learning
  - **Course 1 — PyTorch: Fundamentals:** https://www.coursera.org/learn/pytorch-fundamentals
  - **Course 2 — PyTorch: Techniques and Ecosystem Tools:** https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools
  - **Course 3 — PyTorch: Advanced Architectures and Deployment:** https://www.coursera.org/learn/pytorch-advanced-architectures-and-deployment
- **PyTorch Learn the Basics:** https://docs.pytorch.org/tutorials/beginner/basics/intro.html
- **PyTorch Tutorials:** https://docs.pytorch.org/tutorials/

### PyTorch Student Use — Decision Recorded 2026-10-13

Use **PyTorch: Fundamentals** as the main implementation course alongside relevant Andrew Ng concepts. Use **Techniques and Ecosystem Tools** selectively for subsequent tuning, vision, transfer learning, and NLP work. Keep **Advanced Architectures and Deployment** optional.

Exact foundation video titles and independent rebuild evidence: [PyTorch API Guide](PyTorch_API_Guide/README.md). Students must reconstruct data loading, model, training, and validation on new data; video completion is not sufficient.

## Data and Domain Resources

- **IBM Data Analysis with Python:** https://www.coursera.org/learn/data-analysis-with-python
- **Hugging Face LLM Course:** https://huggingface.co/learn/llm-course/en/chapter1/1
- **Hugging Face Audio Course:** https://huggingface.co/learn/audio-course/en/chapter0/introduction
- **OpenCV Free Courses:** https://opencv.org/university/free-courses/
- **OpenCV Bootcamp:** https://opencv.org/university/free-opencv-course/

## Competition-Sprint Tuning Assignments

Use the exact video-title and duration map:

[`05_Resources/Hyperparameter_Tuning_Resource_Map.md`](Hyperparameter_Tuning_Resource_Map.md)

The three main tuning sources are:

1. **Course 2 — Advanced Learning Algorithms**, Week 3: Advice for Applying Machine Learning — diagnosis, model selection, bias/variance, learning curves, iterative development, and error analysis.
2. **Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization** — regularisation, Adam, learning-rate decay, search scales, and practical tuning strategy.
3. **Course 2 — PyTorch: Techniques and Ecosystem Tools**, Module 1: Hyperparameter Optimization — schedulers, tuning, Optuna, and model-efficiency trade-offs.

## Selection Rule

Use the assigned section only. A course being listed here does not mean students should complete the entire course.

For Harvard CS50’s Introduction to Programming with Python, always name the exact week, topic, and timestamp range.

For Coursera-hosted resources, use Coursera links rather than DeepLearning.AI marketing-page links.

For PyTorch, use the three-course certificate selectively: PyTorch: Fundamentals is the main foundation course; PyTorch: Techniques and Ecosystem Tools supports Round 2 computer-vision, natural-language-processing, and tuning workflows; PyTorch: Advanced Architectures and Deployment is an optional advanced extension. PyTorch official tutorials remain the API reference.

For the IOAI route, establish the applied workflow map with Müller/Zoomcamp **before** using the Andrew Ng Machine Learning Specialization as the systematic model-principles course.
