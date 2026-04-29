# Lecture 7 — Probabilistic modeling and optimization

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

## Source files in this folder

- `Lecture 7 - Di Liu (guest).pdf` — the only deliverable for this guest lecture; no editable source available.

## To go deeper

- **Bishop, _Pattern Recognition and Machine Learning_, Chs. 3-4 and Ch. 9.** Linear regression / classification through a probabilistic lens (Chs. 3-4) and mixture models / EM (Ch. 9). The single best companion for this lecture.
- **Murphy, _Probabilistic Machine Learning: An Introduction_, Chs. 8-11.** Modern, ML-oriented treatment of probabilistic models, NLL, mixture models, and EM.
- **Dempster, Laird, Rubin, "Maximum Likelihood from Incomplete Data via the EM Algorithm," _JRSS B_ 39(1), 1977.** The original EM paper. Surprisingly readable. Worth knowing the historical move.
- **Coursera / Stanford CS229 (Andrew Ng), the lecture on EM and Gaussian mixtures.** Free online, very clean derivation.
