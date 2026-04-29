# L9 Study Guide — Training a Binary Classification Model

## Key Terms

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

## The Problem Determines Everything

```{admonition} Central design principle
:class: tip
Data Modality → Modeling Problem → Target Loss → Encoder Class → Training Algorithm → Data Split

These choices are **not independent** — each one constrains the others. A common mistake is to choose a model first and then fit the problem around it. The correct direction is the reverse: start from the deployment use-case and work backwards.
```

## Hyperparameters vs. Parameters

| | Hyperparameters | Parameters (θ) |
|---|---|---|
| Differentiable w.r.t. loss? | Usually no | Usually yes |
| Effect on per-sample loss | Indirect | Direct |
| Tuned where | Validation set | Training set |
| Examples | k in k-NN, η, network depth | Weights W, biases b |

## k-NN: What Is Actually Being Learned?

```{admonition} k-NN is richer than it looks
:class: tip
At first glance k-NN seems parameter-free. In practice you are choosing:
- **k** (or radius r) — controls bias-variance.
- **Kernel function** — weights nearby vs. distant neighbors.
- **Distance function** — defines the geometry of "nearness" (Euclidean, cosine, learned metric).
- **Index structure** — for scalable inference.

Metric learning (learning the distance function) turns k-NN into a parametric model and is an active research area.
```

## Data Splitting in Health: Why It's Harder

```{admonition} Generalization unit mismatch is a major source of health-AI failure
:class: warning
If a patient has 10 visits and you split by sample, the model may "see" the same patient in both train and test — leaking information. If you split by patient but deploy across hospitals, you may still overestimate performance.

**Always ask: what unit of independence does my deployment assume? Split at that unit.**
```

## Self-Check Questions

1. For a readmission prediction model at a hospital network, what should the generalization unit be? Defend your choice.
2. A k-NN model achieves 99% training accuracy and 60% test accuracy. What is the likely cause? What hyperparameter change might help?
3. Why is it incorrect to tune hyperparameters on the test set? What should you do instead if you have limited data?
4. A model class cannot represent non-linear decision boundaries. Is the resulting error bias or variance? Is there a data-driven fix?
5. In what sense is k-NN "consistent"? What conditions on k and n are required?

## Additional Resources

- [Hastie, Tibshirani, Friedman, *ESL* Ch. 7 — Model Assessment and Selection](https://hastie.su.domains/ElemStatLearn/) — authoritative treatment of data splits, cross-validation, generalization.
- [Kapoor & Narayanan, "Leakage and the Reproducibility Crisis in ML-Based Science" (2022)](https://arxiv.org/abs/2207.07048) — important paper on how leakage undermines health-ML benchmarks.
- [Cover & Hart, "Nearest Neighbor Pattern Classification" (1967)](https://ieeexplore.ieee.org/document/1053964) — original proof of k-NN consistency.
- [James et al., *ISLR* Ch. 5 — Resampling Methods](https://www.statlearning.com/) — accessible cross-validation and bootstrap.
- Murphy, *PML*, Chs. 4 and 16; Domingos, "A Few Useful Things to Know About Machine Learning," *CACM* 55(10), 2012.

> See also: [L9 lecture page](../lectures/lecture-09.md).
