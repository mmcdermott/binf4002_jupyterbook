# L10 Study Guide — Training Theory: Overfitting, Inductive Bias & Limits of Learning

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

## Key Terms

| Term | Definition |
|---|---|
| **Memorization** | A model that stores exact (xᵢ, yᵢ) pairs achieves zero training loss but fails to generalize. The "lookup table" solution is always available to a sufficiently complex model. |
| **Regularization** | Any technique that constrains effective complexity to discourage memorization: L2/L1 penalties, dropout, early stopping, data augmentation. |
| **Zhang et al. (2017)** | Empirical result: deep neural networks can memorize random labels on CIFAR-10. Capacity alone does not explain generalization — modern networks *can* memorize but often choose not to. |
| **Inductive Bias** | "How easy it is to learn the right model." The implicit preference an algorithm or architecture has for certain function classes, independent of data. |
| **Double Descent** | Test error vs. model complexity can decrease, then increase (classical overfitting), then decrease again as overparameterization grows. Challenges the classical bias-variance picture. |
| **Interpolation** | A model that exactly fits all training points. Highly-overparameterized interpolating models can still generalize well (benign overfitting). |
| **Manifold Hypothesis** | Real-world high-D data (images, EHR) lies near a low-D manifold in the ambient space. Explains why neural nets generalize despite the curse of dimensionality. |
| **Distribution Shift** | Test distribution P(X,Y) differs from training distribution. No algorithm can guarantee generalization to a different distribution without assumptions. |
| **Domain Adaptation** | Techniques that aim to generalize under (bounded) distribution shift: align feature distributions, re-weight samples, learn invariant representations. |
| **Faithfulness (Explainability)** | An explanation faithfully reflects the model's true decision mechanism. Hard to verify without ground truth for model behavior. |
| **Separation (Fairness)** | P(Ŷ=1 \| Y=y, A=a) = P(Ŷ=1 \| Y=y) for all y, a. Equalized odds: model performance equal across groups conditional on the true label. |
| **Sufficiency (Fairness)** | P(Y=1 \| Ŷ=p, A=a) = P(Y=1 \| Ŷ=p) for all p, a. Calibration equal across groups. |
| **Fairness Impossibility** | Separation and sufficiency cannot both hold simultaneously for a non-degenerate classifier on a non-trivial distribution. One must be prioritized. |

## The Central Mystery: Why Does AI Generalize?

```{admonition} The $100B question
:class: warning
Zhang et al. (2017) showed that neural networks have enough capacity to memorize training data entirely, yet in practice they don't. This is unexplained by classical learning theory (VC dimension, PAC bounds), which would predict generalization failure for overparameterized models.

**Key insight:** it is not about *how many parameters* it takes to encode a model that generalizes — it is about *how easy it is to learn* such a model. Gradient descent has its own implicit inductive bias toward smooth, low-complexity solutions, even without explicit regularization.
```

## Four Sources of Inductive Bias

| Source | Example |
|---|---|
| **Fundamental learning process (SGD)** | Interpolation, double descent, implicit regularization from mini-batch noise |
| **Data structure (manifold hypothesis)** | Directions of variance and density in the data; representation learning captures this |
| **Architecture (hard structural constraints)** | CNNs enforce translation invariance; transformers enforce permutation equivariance |
| **Training objective (soft constraints)** | Auxiliary losses, pre-training objectives, contrastive losses |

## The Unsolvable Problems

```{admonition} Hard limits of learning theory — know these for health AI
:class: warning
1. **Distribution shift (without assumptions)**: If the test distribution truly differs from training, no algorithm can guarantee generalization. Mitigation: domain adaptation, invariant risk minimization, careful dataset documentation.
2. **Explainability**: Faithfulness, simplicity, stability, completeness, model-agnosticism, and counterfactual validity cannot all be simultaneously satisfied. Every explainability method makes tradeoffs.
3. **Fairness impossibility**: Separation (Ŷ ⊥ A \| Y) and sufficiency (Y ⊥ A \| Ŷ) cannot both hold for non-degenerate classifiers. Choosing which to enforce is a normative, domain-specific decision.
```

## Self-Check Questions

1. Summarize the Zhang et al. (2017) experiment in one paragraph. What does it prove, and what does it leave open?
2. Explain double descent in your own words. How does it challenge the classical bias-variance picture?
3. A CNN achieves high accuracy on hospital A's data but fails on hospital B's data. Name three possible causes and one mitigation strategy for each.
4. A model trained to predict sepsis has AUROC = 0.85 for White patients and 0.72 for Black patients. Does this violate separation, sufficiency, or both? What additional information would you need?
5. Why can't you satisfy both separation and sufficiency at once? Sketch a simple proof or counterexample.

## Additional Resources

- [Zhang et al., "Rethinking Generalization," *ICLR* 2017](https://openreview.net/forum?id=Sy8gdB9xx) — opened the modern debate on generalization in deep learning.
- [Belkin et al., "Reconciling Modern ML Practice with Bias-Variance Tradeoff" (2018)](https://arxiv.org/abs/1812.11118) — the double-descent paper.
- [Chouldechova, "Fair Prediction with Disparate Impact" (2017)](https://arxiv.org/abs/1703.00056) — original fairness-impossibility proof.
- [Lipton, "The Mythos of Model Interpretability" (2016)](https://arxiv.org/abs/1606.03490) — taxonomy of "interpretability" tradeoffs.
- [Saria & Subbaswamy, "Tutorial on Safe and Reliable ML" (2019)](https://arxiv.org/abs/1904.07204) — health-specific treatment of distribution shift and reliability.
- [D'Amour et al., "Underspecification presents challenges for credibility in modern ML," *JMLR* 23, 2022](https://www.jmlr.org/papers/v23/20-1335.html) — why two equally-trained models can behave differently in deployment.
- [Finlayson et al., "The Clinician and Dataset Shift in Artificial Intelligence," *NEJM* 385, 2021](https://www.nejm.org/doi/full/10.1056/NEJMc2104626).

> See also: [L10 lecture page](../lectures/lecture-10.md).
