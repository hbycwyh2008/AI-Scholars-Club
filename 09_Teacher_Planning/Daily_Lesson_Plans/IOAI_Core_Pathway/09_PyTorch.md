# Unit 9 — PyTorch

**Suggested length:** 8 × 75 minutes  
**Purpose:** turn the deep-learning concept map into an independent, debuggable PyTorch workflow.

Use the existing PyTorch/DL resource bank selectively; do not require students to copy full reference notebooks.

## Lesson Sequence

| Lesson | Focus | Rebuild task | Evidence |
|---:|---|---|---|
| 1 | Tensors, shapes, dtypes, devices | reproduce NumPy-like operations and shape transformations | tensor trace |
| 2 | Dataset + DataLoader | build a small custom dataset/data pipeline | loader notebook |
| 3 | `nn.Module` + forward pass | implement and test a minimal MLP | model code + shape checks |
| 4 | loss, autograd, optimiser | perform one training step and inspect gradients | gradient/training-step trace |
| 5 | complete train/validation loop | rebuild loop from a blank file | reproducible training script |
| 6 | overfitting, regularisation, checkpoints | diagnose curves; add one controlled intervention | curve diagnosis |
| 7 | CNN / transfer learning | train a small image model or fine-tune a pretrained model | model comparison |
| 8 | independent mini-project | fresh task with no complete starter solution | notebook/script + model card + oral defense |

## Canonical PyTorch Loop

Students should be able to reconstruct this logic without a complete solution open:

```text
for epoch:
    model.train()
    for batch:
        zero gradients
        forward
        compute loss
        backward
        optimiser step

    model.eval()
    disable gradients
    compute validation metric
    log results
```

## Debugging Checklist

Require students to inspect:

- input/target shapes;
- dtype and device;
- model output shape;
- loss expectations;
- whether gradients exist where expected;
- train/eval mode;
- data split integrity;
- deterministic seeds where appropriate;
- metric code separately from loss code.

## Exit Gate

From a clean runtime and a concise task description, the student can load data, define a model, train it, validate it, diagnose at least one failure, make one controlled improvement, and explain the complete training loop.
