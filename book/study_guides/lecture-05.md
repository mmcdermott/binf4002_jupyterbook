# L5 Study Guide — Calculus & Optimization

## Key Terms

| Term | Definition |
|---|---|
| **Partial Derivative** | ∂f / ∂xᵢ: rate of change of f w.r.t. coordinate xᵢ, holding others fixed. Defined as the limit of (f(x+εeᵢ) − f(x))/ε as ε→0. |
| **Gradient** | ∇f(x) = [∂f/∂x₁, …, ∂f/∂xₙ]ᵀ. Points in the direction of steepest *ascent* of a real-valued function. |
| **Hessian** | H_f(x): n×n matrix of second partial derivatives. Hᵢⱼ = ∂²f / ∂xᵢ∂xⱼ. Quantifies local curvature. |
| **Smoothness** | f is smooth (C∞) if it is infinitely differentiable everywhere. A strong assumption; many ML loss surfaces are not smooth (e.g., ReLU). |
| **Stationary Point** | A point x* where ∇f(x*) = 0. Includes local minima, local maxima, and saddle points. |
| **Saddle Point** | A stationary point that is a minimum in some directions and a maximum in others. Common in high-D loss surfaces. |
| **Gradient Descent** | xₜ₊₁ = xₜ − η ∇f(xₜ). η is the learning rate. Moves opposite the gradient to minimize f. |
| **Coordinate Descent** | Update one coordinate at a time. Simpler but may converge slowly when variables are correlated. |
| **Learning Rate (η)** | Step size for gradient descent. Too large → diverge. Too small → slow convergence. Crucial hyperparameter. |
| **Convexity** | f is convex iff f(λx + (1−λ)y) ≤ λ f(x) + (1−λ) f(y). Convex functions have no local minima other than the global minimum. |

## Geometric Intuition

```{admonition} The tangent surface
:class: tip
The gradient gives the slope of the tangent hyperplane to the loss surface at a point. Gradient descent follows the steepest-downhill direction on this surface. **In high dimensions the landscape has far more saddle points than local minima** — this is helpful for neural-network training, since saddle points can often be escaped.
```

## Self-Check Questions

1. Compute the gradient of f(x,y) = x² + 3xy + y². Find all stationary points.
2. What does it mean for the Hessian to be *positive definite* at a stationary point? *Negative definite*?
3. Why can gradient descent get stuck? Name two types of problematic stationary points.
4. Sketch the loss curve for: (a) learning rate too high, (b) learning rate too low, (c) appropriate learning rate.
5. Why might coordinate descent fail on a function where variables are correlated?

## Additional Resources

- [3Blue1Brown — Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — geometric intuition for derivatives and gradients.
- [Karpathy — "Yes you should understand backprop"](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b) — builds from calculus to backprop.
- [Distill — "Why Momentum Really Works"](https://distill.pub/2017/momentum/) — visual deep dive into gradient-based optimization.
- [Goodfellow et al., *Deep Learning* Ch. 4](https://www.deeplearningbook.org/contents/numerical.html) — optimization foundations in the context of deep learning.
- Boyd & Vandenberghe, *Convex Optimization* (free PDF), Ch. 9; Nocedal & Wright, *Numerical Optimization*, Chs. 2-3 — classical references.

> See also: [L5 lecture page](../lectures/lecture-05.md). Companion notebook: [`gradient_descent.ipynb`](../../Lectures/lecture-05-calculus-optimization/gradient_descent.ipynb).
