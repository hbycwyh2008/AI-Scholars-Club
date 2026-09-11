# Phase 5 Mathematics Intuition Map

Use this map for just-in-time mathematics during Sessions 41–58. The goal is not to finish a separate mathematics course; it is to understand enough mathematics to predict model behaviour, connect equations to code, and diagnose errors.

## Model-to-Mathematics Map

| Model / topic | Mathematics to make visible | Student should be able to do |
|---|---|---|
| linear regression | weighted sums, dot products, residuals, MSE | compute one prediction and loss |
| gradient descent | slope, derivative, partial derivative, gradient, learning rate | predict update direction and diagnose overshoot |
| logistic regression | sigmoid, probability, logarithm intuition, threshold | convert a logit to probability and explain threshold effects |
| regularisation | magnitude, L1/L2 intuition, bias/variance | predict effect of stronger/weaker regularisation |
| neural networks | matrices, composition, activations, shape flow | trace a small forward pass |
| decision trees | proportions, impurity, entropy | compare two candidate splits |
| random forests | sampling, averaging, variance reduction | explain why diverse trees can stabilise prediction |
| boosting | residual/error correction, weighted updates | trace a tiny sequential correction |
| KNN | Euclidean distance, scale | calculate neighbours and explain scaling |
| SVM | geometry, distance to boundary, margin | identify support points and margin intuition |
| K-means | distance, centroid/mean, iteration | perform one assignment/update cycle |
| PCA | centring, projection, variance direction | explain projection and information loss |
| anomaly detection | mean, variance/density intuition, threshold | reason about unusualness and false alarms |
| recommenders | vectors, dot products, similarity, latent factors | compute a simple similarity score |

## Repeated Translation Pattern

```text
task
→ mathematical objects + shapes
→ model equation/rule
→ objective/loss
→ parameter/model update
→ evaluation metric
→ code
→ observed behaviour
```

## Evidence

For each major model, require at least one of:

- hand calculation;
- shape ledger;
- graph/geometric explanation;
- equation-to-code translation;
- parameter-effect prediction made before running code.

The student should also state what the mathematics **does not** prove—for example, low training loss does not prove generalisation.

## Remediation Rule

When a student is stuck, identify the specific missing bridge: notation, shape, algebra/function behaviour, graph reading, probability, distance, gradient, or model objective. Repair that bridge using the current model rather than assigning broad detached mathematics chapters.
