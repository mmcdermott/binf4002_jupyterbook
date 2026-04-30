# L8 Study Guide — Evaluation of Binary Classification

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

## Key Terms

| Term | Definition |
|---|---|
| **Confusion Matrix** | 2×2 table of TP, FP, FN, TN counts. Every binary-classification metric derives from these four numbers. |
| **Sensitivity (Recall, TPR)** | TP / (TP + FN). Of all sick patients, how many did we flag? |
| **Specificity (TNR)** | TN / (TN + FP). Of all healthy patients, how many did we correctly clear? |
| **Precision (PPV)** | TP / (TP + FP). Of those flagged positive, how many truly are? Sensitive to class imbalance. |
| **F1 Score** | Harmonic mean of precision and recall: 2 · (P·R)/(P+R). Useful when class imbalance makes accuracy misleading. |
| **Hard classification** | A model R : x ↦ {0,1} that outputs a binary label directly. Decision boundary is fixed. |
| **Soft classification** | A model f_θ : x ↦ s ∈ ℝ that outputs a score or probability. A threshold τ then maps s → {0,1}. |
| **Bayes Optimal Classifier** | Classifier that minimizes expected loss given the *true* data distribution. For 0-1 loss: predict the class with highest posterior probability. No learnable model can beat it. |
| **Optimal Threshold** | The τ* minimizing expected loss; depends on the loss function and class priors. **Not always 0.5.** |
| **Discrimination** | Can the model separate class 1 from class 0? Measured by overlap of score distributions q₁ and q₀. |
| **Calibration** | Do output probabilities match true probabilities? Calibrated iff P(y=1 \| s=p) ≈ p for all p. |
| **AUROC** | Area Under the ROC curve. Equals P(score for a random positive > score for a random negative). Threshold-free measure of discrimination. 0.5 = random; 1.0 = perfect. |
| **Decision Curve Analysis** | Framework for evaluating clinical net benefit across a range of decision thresholds, accounting for the consequences of TP and FP decisions. |

## Discrimination vs. Calibration: Two Distinct Goals

```{admonition} Why both matter in health ML
:class: important
**Discrimination** asks: does a high score tend to go to positive cases?
**Calibration** asks: if the model says 70% risk, does the patient actually have 70% probability of the outcome?

A model can discriminate perfectly (AUROC = 1) but be miscalibrated (all probabilities shifted). In clinical decision-making — especially shared decision-making — calibration often matters *more* than discrimination because the raw probability is being used directly.
```

## The AUROC Interpretation

```{admonition} Probabilistic interpretation
:class: tip
AUROC = P(s₁ > s₀) where s₁ is a random score from a positive case and s₀ from a negative case. It equals the probability that the model ranks a randomly chosen positive case above a randomly chosen negative case. This interpretation holds regardless of threshold and class prevalence.
```

## Self-Check Questions

1. A COVID test has sensitivity 0.95 and specificity 0.90. In a population with 5% prevalence, compute the PPV and NPV.
2. Sketch the ROC curve for: (a) a random classifier, (b) a perfect classifier, (c) a typical classifier. What area does each subtend?
3. A model achieves AUROC = 0.85 but its calibration curve shows probabilities are consistently twice as high as the true rate. What are the implications for clinical use?
4. Why might you choose a threshold other than 0.5? Give an example where a low threshold (high sensitivity) is preferable and one where a high threshold (high precision) is preferable.
5. Explain the tradeoff between sensitivity and specificity in a screening test vs. a confirmatory test.

## Additional Resources

- [Fawcett — *An Introduction to ROC Analysis* (2006)](https://people.inf.elte.hu/kiss/13dwhdm/roc.pdf) — the canonical ROC paper.
- [Steyerberg et al., "Assessing the performance of prediction models" (2010)](https://pubmed.ncbi.nlm.nih.gov/20010215/) — discrimination, calibration, and clinical utility.
- [StatQuest — ROC and AUC, Clearly Explained! (YouTube)](https://www.youtube.com/watch?v=4jRBRDbJemM) — visual walkthrough.
- [MSKCC — Decision Curve Analysis](https://www.mskcc.org/departments/epidemiology-biostatistics/biostatistics/decision-curve-analysis) — the original DCA framework.
- [Van Calster et al., "Calibration: the Achilles' heel of predictive analytics," *BMC Med* 17, 2019](https://bmcmedicine.biomedcentral.com/articles/10.1186/s12916-019-1466-7).
- Pepe, *The Statistical Evaluation of Medical Tests*; Steyerberg, *Clinical Prediction Models* Chs. 15-17 — definitive textbooks.

> See also: [L8 lecture page](../lectures/lecture-08.md).
