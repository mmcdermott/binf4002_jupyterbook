# Lecture 5 — Calculus and optimization

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Feb 3, 2026 · Part 1 — Foundations · §1.1 Mathematical preliminaries**

## What this lecture is about

We are setting up the engine that runs almost every model in the course: **find the parameters that minimize a loss.** That sentence has two parts — the geometry of the loss surface and the algorithm that walks it.

The lecture covers multivariate functions geometrically (level sets, gradients, tangent surfaces), differentiation and smoothness (and where it fails), stationary points and optima, and the algorithmic landscape: random search, coordinate descent, iterative methods, and gradient descent. We also flag the way high-dimensional optimization landscapes behave very differently from the 2-D pictures everyone draws on whiteboards.

The paradox flagged is **Borel-Kolmogorov**: a paradox about how conditioning on a measure-zero event is ill-defined unless you specify how you take the limit. It's a warning that the smooth-looking move "differentiate the conditional density" hides nontrivial assumptions.

## Why it matters

In modern ML you almost never analyze the loss surface — you just throw an optimizer at it. But the optimizer is making implicit assumptions about what the surface looks like, and when those assumptions fail, you don't get a Python error — you get a model that silently doesn't train. So you need to see the geometry well enough to know when the optimizer is lying.

The high-dimensional point is the most counter-intuitive and the most important: in 2-D, "local minima" are everywhere and gradient descent gets stuck. In 10⁶-D parameter space, almost every critical point is a saddle, true local minima are rare, and the *failure mode* is not getting stuck but moving in a direction that looks promising but isn't. The course will lean on this fact later (L13: why over-parameterized neural networks generalize at all).

## Things you should walk away believing

- The gradient ∇f(x) points in the direction of steepest *ascent*. Subtract it, scaled, to descend.
- "Smoothness" is not a vibe — it has a definition (continuous derivatives), and ReLU networks violate it almost everywhere, which has real consequences.
- A stationary point is where the gradient is zero. It can be a min, a max, or a saddle. In high dimensions it is almost always a saddle.
- Random search and coordinate descent are not just historical baselines — they are the right tool when gradients are unavailable or unreliable (e.g., black-box hyperparameter tuning, certain genomic problems, RL).
- Low-dimensional pictures of optimization landscapes are misleading. Build the high-dimensional intuition early.

## How this connects to the rest of the course

- L6 lifts everything here from "minimize a fixed function" to "minimize an expected function over data" — the central ML move.
- L9 (training a binary classifier) is just empirical risk minimization wired to gradient descent.
- L10 (generalization) returns to "what is the optimizer biased toward finding?" — i.e., implicit regularization.
- L13 (neural networks) is mostly about the optimization details: initialization, normalization, learning rate schedules, gradient clipping. All of it is fighting the high-dimensional pathologies introduced here.

## Source files in this folder

- `Lecture 5.pdf` — the slides as released to students.
- `Lecture 5 - calculus_and_optimization.pptx` — editable PowerPoint source.

## To go deeper

- **Boyd & Vandenberghe, _Convex Optimization_ (free PDF), Ch. 9 (unconstrained minimization).** The standard reference for the convex case. Read this before believing any convex-relaxation argument.
- **Nocedal & Wright, _Numerical Optimization_, Chs. 2-3.** The non-convex side, written for people who actually run optimizers in practice.
- **Goodfellow, Bengio, Courville, _Deep Learning_, Ch. 4.** Optimization as ML uses it, including the high-dimensional saddle-point story.
- **Bottou, Curtis & Nocedal, "Optimization Methods for Large-Scale Machine Learning," _SIAM Review_ 60(2), 2018.** The deep dive on stochastic optimization for ML.

## Study tools

- [Study guide for L05](../study_guides/lecture-05.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
