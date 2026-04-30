# Lecture 7 — Probabilistic modeling and optimization

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Feb 10, 2026 · guest lecturer: Di Liu · Part 1 — Foundations · §1.2 Probabilistic modeling**

## What this lecture is about

This guest lecture by Di Liu unifies what we've built so far into a four-step recipe that will frame every supervised model in the rest of the course:

1. **Specify the data.** What is x, what is y, what are they jointly distributed over.
2. **Specify a parametric probabilistic model.** A family of conditional distributions p(y | x; θ) (supervised) or joint p(x; θ) (unsupervised), parametrized by θ.
3. **Define an objective.** Almost always a *likelihood-based* one — most commonly negative log-likelihood (NLL), 𝔼[-log p(y | x; θ)].
4. **Optimize θ.** With gradient descent (smooth differentiable objectives) or Expectation-Maximization (when latent variables make the gradient awkward).

The lecture works examples top-to-bottom of this recipe:

- **Single-expert regression.** Linear regression as Gaussian likelihood with constant variance — minimizing squared error is exactly minimizing NLL.
- **Multi-expert regression.** Mixtures of regressors, where each input x is "explained" by one of K experts. Latent variables make the model expressive but the objective non-convex.
- **Unsupervised mixture modeling.** Gaussian mixture models for subtype discovery. EM falls naturally out of the latent-variable structure.

## Why it matters

Three reasons this recipe is worth memorizing:

**It demystifies most ML losses.** Squared error → Gaussian likelihood. Cross-entropy → categorical likelihood. Logistic loss → Bernoulli likelihood. Once you see this you stop memorizing losses and start *deriving* them from probabilistic assumptions about the data. That makes you robust when you encounter a setting (survival, ordinal, count, censored, ranking) where the right loss is non-obvious.

**Latent variables let you model heterogeneity directly.** "Patients respond differently to this drug" is a mixture-of-experts statement. "There are subtypes of this disease that look similar in symptoms but differ in mechanism" is a mixture-model statement. Both come naturally out of step 2 above. We will return to this in L23 (heterogeneous treatment effects) and L24 (subgroup evaluation).

**EM vs. gradient descent is a real choice.** When the latent variable can be summed over in closed form, EM converges fast and stably. When it cannot, gradient descent (or amortized inference) is your tool. Knowing which regime you're in is something the lecture sets you up to recognize.

## Things you should walk away believing

- Most supervised losses you'll meet are NLL under some probabilistic assumption. Find the assumption and you understand the loss.
- Latent variables are how you say "the data has hidden structure I want the model to discover."
- EM is not a separate algorithm from gradient descent — it's the right tool when the latent expectation has a closed form.
- "Mixture of experts" is a structural choice, not just a fancy ensembling trick.

## How this connects to the rest of the course

- L8-L9 (binary-classification evaluation and training) walk through this exact recipe for the Bernoulli case.
- L13 (neural networks) replaces the linear regressor in step 2 with a deep network — recipe is otherwise identical.
- L23 (population health and survival analysis) plugs censoring into step 2; Cox proportional hazards is the resulting NLL.
- L24 (causality and fairness) and L25 (population stratification in genomics) lean on mixture/latent-variable thinking.
- L27 (modern biological AI) — protein language models are NLL on amino-acid sequences; ESM-2 is "step 4 done at scale."

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

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

### The Core Chain: Model → Likelihood → Loss

```{admonition} Every common loss is a negative log-likelihood
:class: tip
- Regression with MSE loss ⇔ Gaussian noise model (NLL)
- Binary classification with cross-entropy ⇔ Bernoulli model (NLL)
- Multi-class classification with cross-entropy ⇔ Categorical model (NLL)

**Choosing a loss is equivalent to choosing a probabilistic model for your data.** This reframing lets you reason about whether the loss assumption is appropriate for your domain.
```

### Clinical Context: Why Heterogeneity Matters

```{admonition} Tumor heterogeneity & Simpson's Paradox
:class: important
If tumors have multiple subtypes with different progression rates, a single model fits an average that may be wrong for *every* subtype. Aggregate trends can mislead when there is unmodeled subgroup structure. Mixture models, stratification, and subgroup analyses are key tools.
```

### Self-Check Questions

1. Starting from yᵢ = e(xᵢ; θ) + εᵢ, εᵢ ~ N(0, σ²), derive step-by-step that minimizing NLL is equivalent to minimizing MSE.
2. Do the same for binary labels: show that NLL under a Bernoulli model with sigmoid output equals cross-entropy.
3. If you used a Laplace noise model instead of Gaussian, what loss function would MLE give you? Why might you prefer it?
4. What does it mean for the iid assumption to be violated in a clinical dataset? Give a concrete example.
5. A dataset has 3 patient subtypes with very different prognoses. Why might a single regression model underperform, and what modeling strategies could address this?

### Additional Resources

- [Stanford CS229 Notes — Supervised Learning (MLE section)](https://cs229.stanford.edu/notes2022fall/main_notes.pdf) — rigorous derivation of MLE for linear and logistic regression.
- [Bishop, *PRML*, Ch. 3 — Linear Models for Regression](https://www.microsoft.com/en-us/research/people/cmbishop/) — Gaussian likelihood and Bayesian linear regression in depth.
- [StatQuest — Maximum Likelihood (YouTube)](https://www.youtube.com/watch?v=XepXtl9YKwc) — clear visual walkthrough of MLE.
- [Wikipedia — Simpson's Paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox) — examples including a famous clinical-trial case.
- Murphy, *PML*, Chs. 8-11 — modern ML treatment of probabilistic models, NLL, mixtures, and EM.
