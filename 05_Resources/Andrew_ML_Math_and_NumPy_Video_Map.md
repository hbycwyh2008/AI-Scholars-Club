# Andrew Ng ML — Free Mathematics and NumPy Video Map

**Canonical level:** L2 — Applied Machine Learning  
**Scheduled placement:** Phase 5, Sessions 41–43 (just-in-time review through Sessions 44–58)  
**Implementation:** use the same small dataset and a NumPy notebook across Sessions 41–43; no additional compulsory course or timetable block.  
**Primary lesson:** [Andrew ML Mathematics Bridge](../02_Class_Missions/05_Andrew_Ng_ML_Model_Labs/Andrew_ML_Mathematics_Bridge.md)

> **Resource rule:** Khan Academy mathematics content and the NumPy crash-course video are freely accessible resources. Assign *selected videos*, not whole calculus/linear-algebra courses. Watching a video is not mastery; collect equation-to-code evidence.

## Core free videos: when to watch

| Placement | Concept / selected video | Link | Required application / evidence |
|---|---|---|---|
| Session 41 | Vectors and spaces (selected introductory videos) — Khan Academy | [Vectors and spaces](https://en.khanacademy.org/math/linear-algebra/vectors_and_spaces/vectors) | Identify scalars, vectors, matrices, rows, columns and shapes; write a shape ledger for `X`, `y`, `w`. |
| Session 41 | NumPy Crash Course — Python Engineer (free video listing) | [NumPy Crash Course — complete video](https://www.classcentral.com/course/youtube-numpy-crash-course-complete-tutorial-117192) | Practise `np.array`, `.shape`, `.reshape()`, indexing, axes and broadcasting. Watch just the needed sections. |
| Session 42 | Vector dot product and vector length — Khan Academy | [Video: Vector Dot Product](https://www.khanacademy.org/math/linear-algebra/vectors_and_spaces/dot_cross_products/v/vector-dot-product-and-vector-length) | Compute a dot product by hand; explain `x @ w`. |
| Session 42 | Linear transformations as matrix vector products — Khan Academy | [Video: Matrix–Vector Product](https://www.khanacademy.org/v/linear-transformations-as-matrix-vector-products) | Predict output shape for `X @ w`; connect matrix multiplication to batch prediction. |
| Session 43 | Derivatives: definition and basic rules — Khan Academy | [Differential Calculus, Unit 2](https://www.khanacademy.org/math/differential-calculus/dc-diff-intro/dc-diff-calc-intro) | Explain derivative as local slope; calculate a simple derivative and its sign. |
| Session 43 | Chain rule — Khan Academy | [Differential Calculus: Chain Rule](https://www.khanacademy.org/math/differential-calculus/dc-chain) | Differentiate a composed function; explain the link to loss derivatives. |
| Session 43 | Partial derivatives, introduction — Khan Academy | [Video: Partial Derivatives](https://en.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivatives/v/partial-derivatives-introduction) | Take one partial derivative while holding the other parameter fixed. |
| Session 43 | Gradient — Khan Academy | [Video: Gradient](https://www.khanacademy.org/math/multivariable-calculus/partial_derivatives_topic/gradient) | Combine partial derivatives into a gradient; predict update direction. |
| Session 43 | Gradient Descent intuition — Khan Academy (reading) | [Gradient Descent explainer](https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/optimizing-multivariable-functions/a/what-is-gradient-descent) | Explain `w_new = w_old - learning_rate * gradient` and what happens when the rate is too large. |
| Phase 6 / DL, only when backpropagation is introduced | Multivariable chain rule — Khan Academy | [Multivariable derivatives, chain-rule section](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives) | Follow a two-stage composition / backpropagation trace. Do not require this before Session 41. |

## Andrew Ng ML alignment

| Andrew Ng topic | Mathematics + NumPy focus | Suggested use |
|---|---|---|
| Multiple Linear Regression / Vectorization | Dot product, matrix multiplication, shapes, broadcasting | Sessions 41–42 |
| Cost Function (MSE) | Residuals, squares, average, `axis` | Session 42 |
| Gradient Descent / Learning Rate | Derivative, partial derivative, gradient, chain rule | Session 43 |
| Feature Scaling | Mean, standard deviation, gradient convergence | Sessions 43 and 51; revisit during model comparison |
| Logistic Regression | Sigmoid, logarithm, composed functions | Session 44 just in time |
| Neural Networks / Backpropagation | Matrix shapes, multivariable chain rule | Sessions 47 and 59–70 |

## Compact evidence task: one dataset, three sessions

Use the **same** small linear-prediction example throughout:

```python
import numpy as np

X = np.array([[1., 2.], [3., 4.], [5., 6.]])  # (3, 2)
w = np.array([2., 3.])                       # (2,)
predictions = X @ w                         # (3,)
print(X.shape, w.shape, predictions.shape)
```

- **Session 41:** state what one row and one feature represent; report all shapes; demonstrate `reshape` and an example of broadcasting.
- **Session 42:** manually calculate one prediction, a residual, and MSE; reproduce them using NumPy.
- **Session 43:** for a supplied loss and gradient, calculate a single gradient-descent update; explain the gradient sign, learning rate, and convergence; connect the mathematical step to NumPy code.
- **Later transfer:** repeat the symbol/shape → objective → update → evaluation distinction on a new classification task.

Record the result using the [Mathematics Bridge Evidence Template](../03_Templates/Andrew_ML_Mathematics_Bridge_Evidence_Template.md) and assess with the [32-point mathematics rubric](../04_Assessment/Andrew_ML_Mathematics_Bridge_Rubric.md). The existing recommended pass gate **24/32**, with no critical shape, objective/metric or update-direction errors, is unchanged.

## Scope boundary

- NumPy array operations are **programming skills**; vector/matrix operations and calculus are **mathematical foundations**. Teach the two together by matching equations to running code.
- Do not require the full Khan Academy courses or multivariable calculus proofs.
- Do not replace the canonical L1 CodeHS programming spine or introduce a separate mathematics phase.
- Students who already demonstrate a skill can skip the corresponding support video and submit the evidence task directly.
