# Unit 8 — Andrew Ng Deep Learning Specialization

**Suggested length:** 10 × 75 minutes plus selected Coursera study  
**Purpose:** build a durable deep-learning concept map before PyTorch becomes the main implementation layer.

## Lesson Sequence

| Lesson | Focus | Reconstruction / transfer | Evidence |
|---:|---|---|---|
| 1 | Neural-network map, tensors, shapes | trace dimensions through a small network | shape trace |
| 2 | Forward propagation + activations | hand-compute a tiny forward pass | calculation + explanation |
| 3 | Loss + backpropagation | trace computational dependencies and gradient direction | backprop map |
| 4 | Optimisation | compare SGD/momentum/Adam concepts; diagnose learning-rate behaviour | optimisation diagnosis |
| 5 | Regularisation | L2, dropout, data augmentation, bias/variance | controlled comparison plan |
| 6 | CNN fundamentals | convolution, padding, stride, channels, receptive fields | hand convolution + shape calculations |
| 7 | CNN architectures + transfer learning | choose train-from-scratch vs transfer approach | architecture decision memo |
| 8 | Sequence models | RNN/LSTM/sequence representation and failure modes | sequence trace |
| 9 | Attention / Transformer concepts | query-key-value and attention intuition | attention trace |
| 10 | DL development strategy | error analysis, data/model mismatch, iteration plan | deep-model experiment plan |

## Framework Rule

The conceptual source may use a different framework in demonstrations. Students are not required to become TensorFlow-first developers. Framework-specific mastery is assessed in the following PyTorch unit.

## IOAI Transfer

Every architecture lesson starts with a task question:

```text
What structure exists in the data?
What baseline should a deep model beat?
What validation design is valid?
What metric matters?
What error pattern would justify more model capacity?
```

Deep learning is not the default answer merely because the input is complex.

## Exit Gate

Student can explain the training loop conceptually, reason about tensor shapes, diagnose common optimisation/generalisation failures, and choose a plausible architecture family for image or sequence data with a baseline/evaluation plan.
