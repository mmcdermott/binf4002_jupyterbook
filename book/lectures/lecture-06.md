# Lecture 6 — Probabilistic optimization: optimizing expected performance

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Feb 5, 2026 · Part 1 — Foundations · §1.1 Mathematical preliminaries**

## What this lecture is about

Last lecture we minimized fixed functions. This lecture lifts that move into the probabilistic setting: when the inputs and labels are random, "the function" is an expectation over a data-generating distribution, and we only ever see samples from that distribution. The objective we *care about* is not the average over our training set; it is the expected loss on data we haven't seen.

The lecture builds the train / test / generalization gap from first principles:

- Start with deterministic optimization (L5). The function is fixed; minimization is well-defined.
- Now make inputs and labels random variables. The "true" objective is 𝔼ₓ,ᵧ ℓ(f(x), y).
- We do not have access to that expectation. We have a sample. So we minimize the *empirical* expectation 1/n Σ ℓ(f(xᵢ), yᵢ) instead.
- Empirical-loss minimization is a sample-based approximation of what we actually want. Sometimes it works; sometimes it doesn't.

The paradox flagged is **Red-ball / Black-ball**: an example where the "obvious" expected-value reasoning fails because the prior on the urn matters more than the likelihood of the draw.

## Why it matters

This is the lecture that justifies the entire training/validation/test split that ML practitioners do reflexively. Here's the argument:

We train by minimizing empirical loss. If we use the *same* data to evaluate the model, we get an estimate of empirical loss — which is the thing we just minimized. That number is biased downward as an estimator of true (expected) loss, often dramatically. To estimate true loss we need *fresh samples* — the test set.

Held-out evaluation is not a procedural ritual. It is a statement about which expectation you're trying to estimate.

This framing also gives you the right way to think about generalization failures in health AI. "The model trained on Massachusetts EHRs underperforms in Texas" is not a mysterious bug — it is the empirical loss minimizing over the wrong measure (Massachusetts) when you actually wanted the expected loss over (Texas, or all-of-USA, or wherever you're deploying). Fixing it is not "more data" in general; it is "samples from the right distribution."

## Things you should walk away believing

- The real ML objective is *expected* loss over a data-generating distribution. The empirical loss you minimize is a sample-based estimator of that objective.
- iid sampling is the assumption that lets the empirical estimate concentrate around the true expectation. It is almost never strictly true in health.
- Your training distribution is not your deployment distribution. When they differ, "good train loss" can mean almost nothing.
- The held-out test set is an unbiased estimator of expected loss *only* if you don't peek and don't reuse it.
- "More data" is the right answer when the iid assumption holds. When the distribution itself is wrong, more data from the wrong distribution doesn't help.

## How this connects to the rest of the course

- L7 (probabilistic modeling, guest lecture) frames supervised learning as maximum likelihood — i.e., minimizing a particular expected loss.
- L9 (training a binary classifier) is L6 wired to a real optimizer and a real loss.
- L10 (generalization) is the empirical study of when the train→test gap is small or large.
- L17-L18 (EHR data) and L23 (population health) are extended studies of "the observed distribution is not the population."
- L24 (causality) is what you reach for when "different distribution" means "different intervention," not "different sample."
- The L28 recap returns to this framing as the unifying lens.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Deterministic Optimization** | Find θ* = argmin L(θ) where L is a fixed function. Perfect solutions are theoretically achievable. |
| **Probabilistic Optimization** | Find θ* = argmin 𝔼_{(x,y)~P}[L(θ; x, y)]. The loss is an expectation over a random data distribution. Perfect solutions are impossible due to irreducible randomness. |
| **iid Assumption** | Independent and identically distributed: each data sample is drawn from the same distribution, independently. The foundation for most generalization theory. |
| **Generalization** | The ability of a model optimized on training samples to perform well on new samples from the same distribution. The central challenge in ML. |
| **Bias** | Systematic error due to wrong assumptions in the learning algorithm. High bias → underfitting. 𝔼[f̂(x)] − f(x). |
| **Variance** | Error due to sensitivity to fluctuations in the training set. High variance → overfitting. 𝔼[(f̂(x) − 𝔼[f̂(x)])²]. |
| **Irreducible Error** | The noise inherent in the data-generating process. No model can reduce this. Var(ε) where y = f(x) + ε. |
| **Bias-Variance Tradeoff** | MSE = Bias² + Variance + Irreducible Error. Reducing bias tends to increase variance and vice versa. |
| **Stochastic Gradient Descent (SGD)** | Gradient descent using a random mini-batch to estimate the gradient. Efficient and introduces beneficial noise for escaping local optima. |
| **Empirical Risk Minimization** | Minimize (1/n) Σ L(θ; xᵢ, yᵢ) as a proxy for the true expected risk. The standard training objective. |

### Deterministic vs. Probabilistic Optimization

| | Deterministic | Probabilistic |
|---|---|---|
| Objective | Fixed function | Expectation over random data |
| Achievability | Perfect solution theoretically possible | Irreducible uncertainty always remains |
| Algorithms | Can be deterministic | Must incorporate stochasticity |
| Concern | No worry about unseen data | Must generalize to new samples from P |

### The Bias-Variance Decomposition

```{admonition} Key formula
:class: tip
For MSE loss:  𝔼[(y − f̂(x))²] = **Bias² + Variance + Irreducible Error**

- Bias = 𝔼[f̂(x)] − f(x)   *(systematic error)*
- Variance = 𝔼[(f̂(x) − 𝔼[f̂(x)])²]   *(sensitivity to training set)*
- Irreducible = Var(ε)   *(noise in the data-generating process)*
```

### Self-Check Questions

1. In your own words, explain why probabilistic optimization is fundamentally harder than deterministic optimization.
2. A model that memorizes training data has low bias but high variance. Explain why, using the definitions above.
3. How does averaging predictions from multiple independent models trained on subsets of data affect bias and variance?
4. Why does SGD's stochasticity sometimes help generalization compared to full-batch gradient descent?
5. Sketch the classic bias-variance tradeoff curve showing training error and test error as model complexity increases.

### Additional Resources

- [Scott Fortmann-Roe — Understanding the Bias-Variance Tradeoff](https://scott.fortmann-roe.com/docs/BiasVariance.html) — best interactive visual explanation.
- [Goodfellow et al., *Deep Learning* Ch. 5](https://www.deeplearningbook.org/contents/ml.html) — formal treatment of capacity, overfitting, and generalization.
- [Distill — A Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) — interactive visualization of model fitting and overfitting.
- [James et al., *An Introduction to Statistical Learning* (free PDF)](https://www.statlearning.com/) — Ch. 2 covers bias-variance clearly and accessibly.
- Vapnik, *Nature of Statistical Learning Theory*, Chs. 1-2; Shalev-Shwartz & Ben-David, *Understanding Machine Learning*, Chs. 2-3 — formal PAC learning.
