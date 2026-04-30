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

## Source files in this folder

- `Lecture 6.pdf` — the slides as released to students.
- `Lecture 6 - probabilistic_optimization.pptx` — editable PowerPoint source.

## To go deeper

- **Vapnik, _The Nature of Statistical Learning Theory_, Chs. 1-2.** The classical statement of the learning problem as expected-risk minimization.
- **Shalev-Shwartz & Ben-David, _Understanding Machine Learning_, Chs. 2-3.** PAC learning in modern notation; cleaner than Vapnik to read first.
- **Bottou, Curtis & Nocedal, "Optimization Methods for Large-Scale Machine Learning," _SIAM Review_ 60(2), 2018.** The link between probabilistic optimization and the stochastic optimizers you'll actually run.
- **Murphy, _Probabilistic Machine Learning: An Introduction_, Chs. 4 and 8.** Modern ML treatment of empirical risk and its decomposition.

## Study tools

- [Study guide for L06](../study_guides/lecture-06.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
