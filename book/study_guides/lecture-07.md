# L7 Study Guide — Probabilistic Modeling & Optimization

> Guest lecture by Di Liu. Bridges the abstract probabilistic framework from L3-L6 to concrete ML models, deriving familiar loss functions from first principles.

## Key Terms

| Term | Definition |
|---|---|
| **Generative model** | A parametric model p(D; θ) that assigns probability to observed data D given parameters θ. Can model p(X; θ), p(Y \| X; θ), or the full joint p(Y, X; θ). |
| **Likelihood ℓ(θ)** | The probability of the observed data under the model: ℓ(θ) = p(D; θ). As a function of θ for fixed D, it measures how plausible the parameters are. |
| **Negative Log-Likelihood (NLL)** | L(θ) = − log ℓ(θ) = − log p(D; θ). The standard training objective. Minimizing NLL = maximizing likelihood. |
| **Maximum Likelihood Estimation (MLE)** | θ* = argmin L(θ) = argmax p(D; θ). Finds parameters that make the observed data most probable under the model. |
| **Conditional independence** | Assuming each (xᵢ, yᵢ) is independent given θ:  p(D; θ) = Πᵢ p(yᵢ \| xᵢ; θ). Converts a joint into a product (sum in log space). |
| **Gaussian noise model** | yᵢ = e(xᵢ; θ) + εᵢ, εᵢ ~ N(0, σ²). NLL under this model equals MSE up to constants. |
| **MSE as MLE** | Minimizing MSE = Σ(yᵢ − ŷᵢ)² is *exactly* MLE under a Gaussian noise model with constant variance. |
| **Bernoulli noise model** | For binary y ∈ {0,1}: P(Y=1 \| x; θ) = σ(e(x; θ)) where σ is the sigmoid. NLL = cross-entropy loss. |
| **Cross-entropy loss** | −Σ [yᵢ log ŷᵢ + (1−yᵢ) log (1−ŷᵢ)]. The MLE objective under a Bernoulli model for binary classification. |
| **Mixture of Experts** | A model with multiple sub-models (experts) and a gating function that assigns each input to an expert. Handles heterogeneous data (e.g., tumor subtypes). |
| **Simpson's Paradox** | A trend in combined data that disappears or reverses when data are split into subgroups. Motivates subgroup-aware modeling in health. |

## The Core Chain: Model → Likelihood → Loss

```{admonition} Every common loss is a negative log-likelihood
:class: tip
- Regression with MSE loss ⇔ Gaussian noise model (NLL)
- Binary classification with cross-entropy ⇔ Bernoulli model (NLL)
- Multi-class classification with cross-entropy ⇔ Categorical model (NLL)

**Choosing a loss is equivalent to choosing a probabilistic model for your data.** This reframing lets you reason about whether the loss assumption is appropriate for your domain.
```

## Clinical Context: Why Heterogeneity Matters

```{admonition} Tumor heterogeneity & Simpson's Paradox
:class: important
If tumors have multiple subtypes with different progression rates, a single model fits an average that may be wrong for *every* subtype. Aggregate trends can mislead when there is unmodeled subgroup structure. Mixture models, stratification, and subgroup analyses are key tools.
```

## Self-Check Questions

1. Starting from yᵢ = e(xᵢ; θ) + εᵢ, εᵢ ~ N(0, σ²), derive step-by-step that minimizing NLL is equivalent to minimizing MSE.
2. Do the same for binary labels: show that NLL under a Bernoulli model with sigmoid output equals cross-entropy.
3. If you used a Laplace noise model instead of Gaussian, what loss function would MLE give you? Why might you prefer it?
4. What does it mean for the iid assumption to be violated in a clinical dataset? Give a concrete example.
5. A dataset has 3 patient subtypes with very different prognoses. Why might a single regression model underperform, and what modeling strategies could address this?

## Additional Resources

- [Stanford CS229 Notes — Supervised Learning (MLE section)](https://cs229.stanford.edu/notes2022fall/main_notes.pdf) — rigorous derivation of MLE for linear and logistic regression.
- [Bishop, *PRML*, Ch. 3 — Linear Models for Regression](https://www.microsoft.com/en-us/research/people/cmbishop/) — Gaussian likelihood and Bayesian linear regression in depth.
- [StatQuest — Maximum Likelihood (YouTube)](https://www.youtube.com/watch?v=XepXtl9YKwc) — clear visual walkthrough of MLE.
- [Wikipedia — Simpson's Paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox) — examples including a famous clinical-trial case.
- Murphy, *PML*, Chs. 8-11 — modern ML treatment of probabilistic models, NLL, mixtures, and EM.

> See also: [L7 lecture page](../lectures/lecture-07.md).
