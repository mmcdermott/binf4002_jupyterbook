# Lecture 10 — Generalization, domain shift, fairness

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Feb 19, 2026 · Part 1 — Foundations · §1.3 Evaluation, training, generalization**

## What this lecture is about

This is the closer for Part 1. Now that you can train and evaluate a binary classifier, the question is: when does the trained model actually generalize, and when does it look good in validation but fail in deployment?

The lecture is organized around a few claims that each subvert the previous one:

- **Overfitting and memorization.** Classical story: high-capacity models memorize the training set; low-capacity models don't. So pick capacity carefully.
- **The modern-DL puzzle.** Deep neural networks have *more parameters than training points* and yet generalize. The classical bias-variance picture predicts they shouldn't. Zhang et al. (2017) showed they can also memorize random labels. So the classical story is at best incomplete.
- **What's actually going on: inductive bias.** A model class isn't just "what functions can be represented" — it's *which functions are easy to learn under a given optimizer*. Gradient descent on overparameterized neural networks is biased toward simple, generalizing solutions even when the model class can represent everything.
- **Regularization.** Explicit (L2, dropout, weight decay) and implicit (the optimizer's bias). Both are real, both matter.
- **kNN as a counter-example.** Local memorization, properly chosen, *can* converge to Bayes-optimal classification. That's the consistency theorem from L9 returning to make a point.
- **Negative controls.** A sanity check: shuffle labels, run training, see if you get nonzero performance. If you do, your evaluation is leaky.
- **Domain shift, explainability, fairness.** Three failure modes that the second half of the course will revisit at length. Each is a case where "good train and validation loss" doesn't mean "the model is OK."

The paradox flagged: "**overfitting is possible — it is the optimal solution to the optimization problem — but it doesn't happen.**" This is the core puzzle of modern deep learning, the paradox students should sit with.

## Why it matters

This lecture is the *transition* of the course. Part 1 has been building the formal machinery; Part 2 onwards uses it. The transition relies on three takeaways being internalized:

**Capacity is not the right way to think about generalization in modern ML.** A 100-million-parameter network is not "more overfit" than a 1-million-parameter network if the optimizer's inductive bias is good. This will matter constantly when we discuss neural networks, transformers, and foundation models in Part 2.

**Negative controls and sanity checks are basic ML hygiene, not paranoia.** "Shuffle the labels, retrain, does it still work?" is a question every reviewer should be asking, and you should be asking it of yourself before they do. We'll see real examples of papers that didn't (L21 imaging shortcut learning).

**Domain shift, explainability, and fairness are first-class.** They are not afterthoughts and they are not "ethics for ML." They are constraints on the training pipeline that, when violated, produce models that are technically excellent and practically harmful. This lecture is the one that says: that pattern is *the rule, not the exception* in health AI.

## Things you should walk away believing

- A model that *can* memorize doesn't *have* to. Inductive bias decides what it actually learns.
- "Simple model" vs. "complex model" is the wrong axis. The right axis is "which functions does the optimizer find first."
- Regularization — explicit and implicit — is part of the model, not a knob you turn at the end.
- A model that solves a puzzle without being able to do anything else (e.g., a model that fits any random labels but somehow generalizes when labels are real) is telling you something about the optimization, not about the architecture.
- Negative controls are basic hygiene. Do them before publication, not after rebuttal.
- Domain shift, explainability, and fairness are not ethical add-ons; they are reasons your validation may be lying.

## How this connects to the rest of the course

- L13 (neural networks) is essentially "here's how to make the inductive bias good in practice."
- L17-L18 (EHR data) is full of distribution-shift problems disguised as data-quality problems.
- L21-L22 (medical imaging) revisits inductive bias (CNN, U-Net, MIL) and shortcut learning as a domain-shift symptom.
- L24 (causality and fairness) formalizes the fairness questions raised here.
- L25 (PRS transferability) is a domain-shift story about populations and ancestry.
- L28 (course recap) returns to negative controls and domain shift as the things that survive the semester.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Memorization** | A model that stores exact (xᵢ, yᵢ) pairs and achieves zero training loss. *Classically* this was assumed to imply failure to generalize; the modern-DL puzzle is that overparameterized networks can interpolate the training data and still generalize well (benign overfitting). |
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

### The Central Mystery: Why Does AI Generalize?

```{admonition} The $100B question
:class: warning
Zhang et al. (2017) showed that neural networks have enough capacity to memorize training data entirely, yet in practice they don't. This is unexplained by classical learning theory (VC dimension, PAC bounds), which would predict generalization failure for overparameterized models.

**Key insight:** it is not about *how many parameters* it takes to encode a model that generalizes — it is about *how easy it is to learn* such a model. Gradient descent has its own implicit inductive bias toward smooth, low-complexity solutions, even without explicit regularization.
```

### Four Sources of Inductive Bias

| Source | Example |
|---|---|
| **Fundamental learning process (SGD)** | Interpolation, double descent, implicit regularization from mini-batch noise |
| **Data structure (manifold hypothesis)** | Directions of variance and density in the data; representation learning captures this |
| **Architecture (hard structural constraints)** | CNNs enforce translation **equivariance** at convolutional layers (pooling adds translation invariance at the readout); self-attention is permutation equivariant, and full transformers add positional encoding precisely to *break* that symmetry so order matters |
| **Training objective (soft constraints)** | Auxiliary losses, pre-training objectives, contrastive losses |

### The Unsolvable Problems

```{admonition} Hard limits of learning theory — know these for health AI
:class: warning
1. **Distribution shift (without assumptions)**: If the test distribution truly differs from training, no algorithm can guarantee generalization. Mitigation: domain adaptation, invariant risk minimization, careful dataset documentation.
2. **Explainability**: Faithfulness, simplicity, stability, completeness, model-agnosticism, and counterfactual validity cannot all be simultaneously satisfied. Every explainability method makes tradeoffs.
3. **Fairness impossibility**: Separation (Ŷ ⊥ A \| Y) and sufficiency (Y ⊥ A \| Ŷ) cannot both hold for non-degenerate classifiers. Choosing which to enforce is a normative, domain-specific decision.
```

### Self-Check Questions

1. Summarize the Zhang et al. (2017) experiment in one paragraph. What does it prove, and what does it leave open?
2. Explain double descent in your own words. How does it challenge the classical bias-variance picture?
3. A CNN achieves high accuracy on hospital A's data but fails on hospital B's data. Name three possible causes and one mitigation strategy for each.
4. A model trained to predict sepsis has AUROC = 0.85 for White patients and 0.72 for Black patients. Does this violate separation, sufficiency, or both? What additional information would you need?
5. Why can't you satisfy both separation and sufficiency at once? Sketch a simple proof or counterexample.

### Additional Resources

- [Zhang et al., "Rethinking Generalization," *ICLR* 2017](https://openreview.net/forum?id=Sy8gdB9xx) — opened the modern debate on generalization in deep learning.
- [Belkin et al., "Reconciling Modern ML Practice with Bias-Variance Tradeoff" (2018)](https://arxiv.org/abs/1812.11118) — the double-descent paper.
- [Chouldechova, "Fair Prediction with Disparate Impact" (2017)](https://arxiv.org/abs/1703.00056) — original fairness-impossibility proof.
- [Lipton, "The Mythos of Model Interpretability" (2016)](https://arxiv.org/abs/1606.03490) — taxonomy of "interpretability" tradeoffs.
- [Saria & Subbaswamy, "Tutorial on Safe and Reliable ML" (2019)](https://arxiv.org/abs/1904.07204) — health-specific treatment of distribution shift and reliability.
- [D'Amour et al., "Underspecification presents challenges for credibility in modern ML," *JMLR* 23, 2022](https://www.jmlr.org/papers/v23/20-1335.html) — why two equally-trained models can behave differently in deployment.
- [Finlayson et al., "The Clinician and Dataset Shift in Artificial Intelligence," *NEJM* 385, 2021](https://www.nejm.org/doi/full/10.1056/NEJMc2104626).
