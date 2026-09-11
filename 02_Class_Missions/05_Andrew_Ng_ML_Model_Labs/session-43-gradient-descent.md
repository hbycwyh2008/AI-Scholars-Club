# Session 43 — Scaling, Gradients, and Gradient Descent

## Goal

Understand how feature scale, derivatives, gradients, and learning rate affect optimisation.

## Learn

Use cost curves/contours to interpret derivative sign, gradient direction, step size, convergence, oscillation, and divergence. Connect feature scaling to optimisation behaviour.

## Practice

- estimate derivative direction from a graph;
- perform two small gradient-descent updates by hand;
- predict what happens when the learning rate is too small or too large;
- compare training behaviour before and after scaling.

## Rebuild

Students implement or complete a minimal gradient-descent loop for a simple regression objective, then diagnose a deliberately poor learning-rate/scaling setup.

## Share

Defend one intervention: change learning rate, scale features, or stop training. Explain the evidence rather than saying only that the loss is “bad.”

## Evidence

- gradient/update trace;
- convergence plot or table;
- diagnosis of one failure;
- explanation of feature scaling.

## Exit Check

Student can state what the gradient means, predict update direction, and distinguish optimisation failure from poor model fit.
