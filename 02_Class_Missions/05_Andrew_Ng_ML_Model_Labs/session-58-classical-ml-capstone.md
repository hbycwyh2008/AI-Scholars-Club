# Session 58 — Classical ML Capstone

## Goal

Demonstrate transfer across task recognition, mathematical reasoning, modeling, evaluation, regularization, and controlled iteration. Produce a project record that can be adapted into a portfolio entry.

## Mixed Assessment

Students receive several short unfamiliar scenarios and one practical dataset. Without model names in the prompts, they must identify:

- input / output / labels;
- task family;
- valid validation design;
- simplest credible baseline;
- metric;
- candidate model families;
- likely failure modes.

## Practical Capstone

For the dataset, students independently:

1. create a task contract and data audit, including data source/license and leakage risks;
2. establish a reproducible baseline;
3. compare at least two justified classical models;
4. perform one representative mathematical trace or calculation;
5. for a suitable model, compare L1/Lasso, L2/Ridge, and Elastic Net (or justify an alternative complexity-control comparison);
6. choose regularization strength using validation or cross-validation and explain the effect on fit, coefficients, and generalization; never use the final test set to tune;
7. analyse errors;
8. make one controlled improvement;
9. write a concise model card, limitations section, and portfolio narrative.

## Oral Defense

Teacher asks students to explain why they did **not** choose one plausible alternative model or metric, what the regularization comparison showed, and what evidence would make them change their decision.

## Evidence

- mixed model-recognition assessment;
- reproducible notebook/code and clean-run instructions;
- model-comparison table;
- mathematical trace;
- regularization/complexity-control experiment log;
- error analysis;
- model card and limitations;
- short project narrative naming the student's contribution, decisions, evidence, and next step;
- oral defense notes.

Use the [ML Project Portfolio Evidence Template](../../../../03_Templates/ML_Project_Portfolio_Evidence_Template.md) to assemble the evidence.

## Exit Gate

Student passes only if the workflow is valid and defensible. A high score does not compensate for leakage, invalid evaluation, irreproducibility, or inability to explain model behaviour. The project is one evidence-rich portfolio entry, not a guarantee of admission or selection by any program.
