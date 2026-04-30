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
- "Smoothness" is not a vibe — it has a definition (continuous derivatives), and ReLU networks fail it on a measure-zero set (the kink at z = 0). They are differentiable *almost everywhere*, but the non-smooth points still have real consequences (subgradient methods, choice of subgradient at zero, instability in line-search-based optimizers).
- A stationary point is where the gradient is zero. It can be a min, a max, or a saddle. In high dimensions it is almost always a saddle.
- Random search and coordinate descent are not just historical baselines — they are the right tool when gradients are unavailable or unreliable (e.g., black-box hyperparameter tuning, certain genomic problems, RL).
- Low-dimensional pictures of optimization landscapes are misleading. Build the high-dimensional intuition early.

## How this connects to the rest of the course

- L6 lifts everything here from "minimize a fixed function" to "minimize an expected function over data" — the central ML move.
- L9 (training a binary classifier) is just empirical risk minimization wired to gradient descent.
- L10 (generalization) returns to "what is the optimizer biased toward finding?" — i.e., implicit regularization.
- L13 (neural networks) is mostly about the optimization details: initialization, normalization, learning rate schedules, gradient clipping. All of it is fighting the high-dimensional pathologies introduced here.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Partial Derivative** | ∂f / ∂xᵢ: rate of change of f w.r.t. coordinate xᵢ, holding others fixed. Defined as the limit of (f(x+εeᵢ) − f(x))/ε as ε→0. |
| **Gradient** | ∇f(x) = [∂f/∂x₁, …, ∂f/∂xₙ]ᵀ. Points in the direction of steepest *ascent* of a real-valued function. |
| **Hessian** | H_f(x): n×n matrix of second partial derivatives. Hᵢⱼ = ∂²f / ∂xᵢ∂xⱼ. Quantifies local curvature. |
| **Smoothness** | f is smooth (C∞) if it is infinitely differentiable everywhere. ML loss surfaces frequently fail smoothness on a measure-zero set (e.g., ReLU at z = 0); they are differentiable *almost everywhere* but not C∞, which is enough to break some optimizer guarantees. |
| **Stationary Point** | A point x* where ∇f(x*) = 0. Includes local minima, local maxima, and saddle points. |
| **Saddle Point** | A stationary point that is a minimum in some directions and a maximum in others. Common in high-D loss surfaces. |
| **Gradient Descent** | xₜ₊₁ = xₜ − η ∇f(xₜ). η is the learning rate. Moves opposite the gradient to minimize f. |
| **Coordinate Descent** | Update one coordinate at a time. Simpler but may converge slowly when variables are correlated. |
| **Learning Rate (η)** | Step size for gradient descent. Too large → diverge. Too small → slow convergence. Crucial hyperparameter. |
| **Convexity** | f is convex iff f(λx + (1−λ)y) ≤ λ f(x) + (1−λ) f(y). Convex functions have no local minima other than the global minimum. |

### Geometric Intuition

```{admonition} The tangent surface
:class: tip
The gradient gives the slope of the tangent hyperplane to the loss surface at a point. Gradient descent follows the steepest-downhill direction on this surface. **In high dimensions the landscape has far more saddle points than local minima** — this is helpful for neural-network training, since saddle points can often be escaped.
```

### Self-Check Questions

1. Compute the gradient of f(x,y) = x² + 3xy + y². Find all stationary points.
2. What does it mean for the Hessian to be *positive definite* at a stationary point? *Negative definite*?
3. Why can gradient descent get stuck? Name two types of problematic stationary points.
4. Sketch the loss curve for: (a) learning rate too high, (b) learning rate too low, (c) appropriate learning rate.
5. Why might coordinate descent fail on a function where variables are correlated?

### Additional Resources

- [3Blue1Brown — Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — geometric intuition for derivatives and gradients.
- [Karpathy — "Yes you should understand backprop"](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b) — builds from calculus to backprop.
- [Distill — "Why Momentum Really Works"](https://distill.pub/2017/momentum/) — visual deep dive into gradient-based optimization.
- [Goodfellow et al., *Deep Learning* Ch. 4](https://www.deeplearningbook.org/contents/numerical.html) — optimization foundations in the context of deep learning.
- Boyd & Vandenberghe, *Convex Optimization* (free PDF), Ch. 9; Nocedal & Wright, *Numerical Optimization*, Chs. 2-3 — classical references.
