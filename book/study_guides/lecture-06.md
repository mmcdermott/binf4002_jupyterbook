# L6 Study Guide — Probabilistic Optimization & Bias-Variance

## Key Terms

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

## Deterministic vs. Probabilistic Optimization

| | Deterministic | Probabilistic |
|---|---|---|
| Objective | Fixed function | Expectation over random data |
| Achievability | Perfect solution theoretically possible | Irreducible uncertainty always remains |
| Algorithms | Can be deterministic | Must incorporate stochasticity |
| Concern | No worry about unseen data | Must generalize to new samples from P |

## The Bias-Variance Decomposition

```{admonition} Key formula
:class: tip
For MSE loss:  𝔼[(y − f̂(x))²] = **Bias² + Variance + Irreducible Error**

- Bias = 𝔼[f̂(x)] − f(x)   *(systematic error)*
- Variance = 𝔼[(f̂(x) − 𝔼[f̂(x)])²]   *(sensitivity to training set)*
- Irreducible = Var(ε)   *(noise in the data-generating process)*
```

## Self-Check Questions

1. In your own words, explain why probabilistic optimization is fundamentally harder than deterministic optimization.
2. A model that memorizes training data has low bias but high variance. Explain why, using the definitions above.
3. How does averaging predictions from multiple independent models trained on subsets of data affect bias and variance?
4. Why does SGD's stochasticity sometimes help generalization compared to full-batch gradient descent?
5. Sketch the classic bias-variance tradeoff curve showing training error and test error as model complexity increases.

## Additional Resources

- [Scott Fortmann-Roe — Understanding the Bias-Variance Tradeoff](https://scott.fortmann-roe.com/docs/BiasVariance.html) — best interactive visual explanation.
- [Goodfellow et al., *Deep Learning* Ch. 5](https://www.deeplearningbook.org/contents/ml.html) — formal treatment of capacity, overfitting, and generalization.
- [Distill — A Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) — interactive visualization of model fitting and overfitting.
- [James et al., *An Introduction to Statistical Learning* (free PDF)](https://www.statlearning.com/) — Ch. 2 covers bias-variance clearly and accessibly.
- Vapnik, *Nature of Statistical Learning Theory*, Chs. 1-2; Shalev-Shwartz & Ben-David, *Understanding Machine Learning*, Chs. 2-3 — formal PAC learning.

> See also: [L6 lecture page](../lectures/lecture-06.md). Companion notebook: [`Probabilistic_Optimization.ipynb`](../../Lectures/lecture-06-probabilistic-optimization/Probabilistic_Optimization.ipynb).
