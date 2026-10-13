# PyTorch API Guide

Priority interfaces:

`Tensor`, `Dataset`, `DataLoader`, `nn.Module`, common layers, loss functions, `autograd`, `optim.Adam`, `optim.AdamW`, device movement, model save/load, and mixed precision.

## Coursera Video Resource Decision — 2026-10-13

**Primary implementation course:** [DeepLearning.AI — PyTorch for Deep Learning Professional Certificate](https://www.coursera.org/professional-certificates/pytorch-for-deep-learning).

| Course | Priority and selected scope | Required student evidence |
|---|---|---|
| [PyTorch: Fundamentals](https://www.coursera.org/learn/pytorch-fundamentals) | Main foundation. Begin with Getting Started with PyTorch and The PyTorch Workflow; continue with Data Management in PyTorch as projects require it. | Independently build data loading, a model, training, and validation on an unfamiliar dataset. |
| [PyTorch: Techniques and Ecosystem Tools](https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools) | Select later for hyperparameter optimisation, TorchVision, transfer learning, and NLP ecosystem practice. | Make a controlled improvement and justify it with validation evidence. |
| [PyTorch: Advanced Architectures and Deployment](https://www.coursera.org/learn/pytorch-advanced-architectures-and-deployment) | Optional extension for advanced architectures and deployment when the task needs them. Do not require full completion as a beginner prerequisite. | Explain and evaluate the selected architecture or deployment change. |

### Foundation Viewing Order

1. **Getting Started with PyTorch:** The ML Pipeline; Building a Simple Neural Network; Activation Functions; Tensors; Tensor Math and Broadcasting.
2. **The PyTorch Workflow:** the data/model pipeline videos; Loss; Optimizers and Gradients; Device Management; the two image-classification videos. Complete the accompanying classifier lab.
3. **Data Management in PyTorch:** use for custom datasets, transforms, and dataset splitting when moving to new data.

Pair corresponding Andrew Ng Deep Learning concepts with PyTorch practice; students need not finish the whole specialization before coding. Keep concept explanations and framework implementation as distinct learning objectives.

### Independent Rebuild and Transfer

From a fresh notebook, students must load and split data, construct a Dataset/DataLoader and nn.Module, run an explicit training loop, validate without gradient tracking, and report a suitable metric. They must explain tensor shapes, loss, gradient clearing/backpropagation/optimizer steps, and train/eval mode. Then change the dataset or a justified model component, run again, and explain the effect.

Use [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) and [official tutorials](https://docs.pytorch.org/tutorials/) as current implementation references. Course completion or copied notebook execution alone is not the transfer check.

See the [Andrew DL to PyTorch Pairing Map](../../02_Class_Missions/06_Andrew_Ng_DL_PyTorch/Andrew_DL_to_PyTorch_Map.md) and [English Video Resource Map](../English_Video_Resource_Map.md). Recommendations use the published syllabus; verify access and assigned labs before classroom use.
