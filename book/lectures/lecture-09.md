# Lecture 9 — Training a binary classification model

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Feb 17, 2026 · Part 1 — Foundations · §1.3 Evaluation, training, generalization**

## What this lecture is about

L8 evaluated a fixed model. L9 turns to: how do we *train* one? The lecture opens with a real-world setup that looks like a perfectly normal ML problem but isn't — **the influenza vaccine effectiveness example.** Observational data say the vaccinated group has lower flu rates than the unvaccinated. Does the vaccine work, or is it that the kind of person who gets the flu shot is the kind of person who also avoids crowded indoor spaces, washes their hands, etc.? You can fit a beautiful classifier and answer the wrong question.

Once that hazard is in your mind, the rest of the lecture lays out the full ML training pipeline:

- **The pipeline.** Pick a loss → pick a function class → optimize empirical loss → check generalization → repeat.
- **Data splits.** Train / validation / test. Why each exists, what role each plays in estimating expected loss (callback to L6).
- **Model capacity and misspecification.** Capacity = how many functions the model class can represent. Misspecification = the right function isn't in the class. Both bite, in different ways.
- **k-Nearest Neighbors as a procedural baseline.** No training step in the usual sense; classification = "vote among the k closest training points." It is *Bayes-consistent* — but only when **k → ∞ and k/n → 0** as n → ∞. Fixed-k k-NN (e.g., 1-NN) is *not* Bayes-consistent: Cover & Hart (1967) showed 1-NN converges to at most twice the Bayes error. And in high dimensions, k-NN is practically catastrophic regardless of k.
- **The optimization view.** Training = minimize empirical risk. With logistic loss + linear model = logistic regression. With cross-entropy + neural network = the same recipe scaled up.

The paradox flagged is the **Healthy Vaccinee Effect** — a confounder you should have in your peripheral vision the rest of the course.

## Why it matters

Three threads converge here:

**The pipeline is the pipeline.** Loss → function class → optimization → generalization. Almost everything you'll fit in the next 14 weeks fits this template, and the *hard* parts are picking the loss and picking the function class to match the *problem*, not running the optimizer. The optimizer is the easy part.

**kNN is more important than it looks.** Yes, you'll never deploy kNN in a real system. But kNN is the simplest model that reveals the bias-variance tradeoff (k controls capacity), domain shift (your "neighbors" aren't your neighbors anymore), high-D pathology (every point is far from every other point in 100-D), and consistency (it provably converges). It is a useful sanity-check baseline and a teaching tool that returns in L10 and L25.

**The flu-vaccine motivation is the moral of the lecture.** Fitting a classifier on observational data answers a *prediction* question well, but tells you almost nothing about *intervention*. We will dedicate L24 to formalizing this distinction — but the warning starts here.

## Things you should walk away believing

- "Train a classifier" = pick loss + function class + optimizer + generalization estimate. The four pieces are independent design choices.
- Train / validation / test do different jobs: train fits, validation chooses model/hyperparameters, test estimates expected loss. Don't conflate them.
- Capacity and misspecification are different problems with different fixes — capacity is a parameter-count knob, misspecification is "the right function isn't in your class."
- kNN is a *useful* baseline, not a toy. Fit it before you fit anything fancy.
- Observational data fitting answers a prediction question. It is not a license to claim causality.

## How this connects to the rest of the course

- L10 closes the training arc with the modern story of generalization (overfitting, inductive bias, regularization).
- L13 (neural networks) is this same pipeline with a richer function class and more careful optimization.
- L18 (EHR modeling) requires re-defining "what counts as a label" because of windows / censoring / actionability.
- L23 (survival) replaces binary classification with time-to-event when "did it happen?" hides "when did it happen?"
- L24 (causality) takes the flu-vaccine warning seriously and gives you the formal tools (DAGs, do-operator, propensity scores) to reason about it.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **ML Pipeline** | The full sequence: problem definition → data split → loss specification → model class choice → training algorithm → evaluation. Every choice interacts with every other. |
| **Data Split** | Partition into train / validation / test. **Must reflect deployment**: splitting by patient vs. by sample vs. by site gives different generalization assessments. |
| **Generalization Unit** | The unit of independence your model must generalize over (sample, patient, clinic, institution). Determines how data must be split to avoid leakage. |
| **Data Leakage** | Information from the test set (or future) entering the training process, creating artificially optimistic evaluation. |
| **Hyperparameter** | Configuration of the learning algorithm not directly differentiable from the loss (e.g., k in k-NN, learning rate, architecture size). Tuned on validation set. |
| **Parameter (θ)** | Differentiable quantities learned by optimizing the training loss (e.g., neural-net weights). Fitted on training set. |
| **k-Nearest Neighbors (k-NN)** | Non-parametric: predict the label of x by majority vote (or average) of the k training points nearest to x. k is a hyperparameter; the distance function and kernel are choices. |
| **Model Capacity / Complexity** | Richness of the function class. High capacity → low bias, high variance. Low capacity → high bias, low variance. |
| **Consistent Learning** | An algorithm is consistent if its error converges to the Bayes error as n → ∞. k-NN with k → ∞ and k/n → 0 is consistent. |
| **NLL Loss** | Canonical loss derived from a probabilistic model of the data. Binary → cross-entropy. Continuous → MSE under Gaussian. |
| **Model Misspecification** | When the true data-generating process cannot be expressed by the chosen model class. Results in irreducible bias regardless of data size. |

### The Problem Determines Everything

```{admonition} Central design principle
:class: tip
Data Modality → Modeling Problem → Target Loss → Encoder Class → Training Algorithm → Data Split

These choices are **not independent** — each one constrains the others. A common mistake is to choose a model first and then fit the problem around it. The correct direction is the reverse: start from the deployment use-case and work backwards.
```

### Hyperparameters vs. Parameters

| | Hyperparameters | Parameters (θ) |
|---|---|---|
| Differentiable w.r.t. loss? | Usually no | Usually yes |
| Effect on per-sample loss | Indirect | Direct |
| Tuned where | Validation set | Training set |
| Examples | k in k-NN, η, network depth | Weights W, biases b |

### k-NN: What Is Actually Being Learned?

```{admonition} k-NN is richer than it looks
:class: tip
At first glance k-NN seems parameter-free. In practice you are choosing:
- **k** (or radius r) — controls bias-variance.
- **Kernel function** — weights nearby vs. distant neighbors.
- **Distance function** — defines the geometry of "nearness" (Euclidean, cosine, learned metric).
- **Index structure** — for scalable inference.

Metric learning (learning the distance function) turns k-NN into a parametric model and is an active research area.
```

### Data Splitting in Health: Why It's Harder

```{admonition} Generalization unit mismatch is a major source of health-AI failure
:class: warning
If a patient has 10 visits and you split by sample, the model may "see" the same patient in both train and test — leaking information. If you split by patient but deploy across hospitals, you may still overestimate performance.

**Always ask: what unit of independence does my deployment assume? Split at that unit.**
```

### Self-Check Questions

1. For a readmission prediction model at a hospital network, what should the generalization unit be? Defend your choice.
2. A k-NN model achieves 99% training accuracy and 60% test accuracy. What is the likely cause? What hyperparameter change might help?
3. Why is it incorrect to tune hyperparameters on the test set? What should you do instead if you have limited data?
4. A model class cannot represent non-linear decision boundaries. Is the resulting error bias or variance? Is there a data-driven fix?
5. In what sense is k-NN "consistent"? What conditions on k and n are required?

### Additional Resources

- [Hastie, Tibshirani, Friedman, *ESL* Ch. 7 — Model Assessment and Selection](https://hastie.su.domains/ElemStatLearn/) — authoritative treatment of data splits, cross-validation, generalization.
- [Kapoor & Narayanan, "Leakage and the Reproducibility Crisis in ML-Based Science" (2022)](https://arxiv.org/abs/2207.07048) — important paper on how leakage undermines health-ML benchmarks.
- [Cover & Hart, "Nearest Neighbor Pattern Classification" (1967)](https://ieeexplore.ieee.org/document/1053964) — original proof of k-NN consistency.
- [James et al., *ISLR* Ch. 5 — Resampling Methods](https://www.statlearning.com/) — accessible cross-validation and bootstrap.
- Murphy, *PML*, Chs. 4 and 16; Domingos, "A Few Useful Things to Know About Machine Learning," *CACM* 55(10), 2012.
