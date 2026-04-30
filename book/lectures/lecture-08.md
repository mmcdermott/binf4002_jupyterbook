# Lecture 8 — Evaluating a binary classification model

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Feb 12, 2026 · guest lecturer: Florent Pollet · Part 1 — Foundations · §1.3 Evaluation, training, generalization**

## What this lecture is about

We have a fixed binary classifier and want to evaluate it. That sounds easy until you sit down to do it: which metric, on which threshold, against which utility, with what calibration assumption, in what prevalence regime? This lecture is the careful version of that question.

Florent walks through the classifier-evaluation toolkit:

- **Hard classification.** Confusion matrix. Sensitivity / specificity / PPV / NPV / accuracy / F1 / etc. Each metric is a different summary of the confusion matrix and answers a different question.
- **Soft classification.** Models output a *score*, not a label. The threshold turns the score into a label, and the threshold is a *decision*, not a property of the model.
- **Calibration vs. discrimination.** A model can rank patients well (good discrimination, AUROC ≈ 1) while being miscalibrated (its scores aren't probabilities anyone should trust). They are different failure modes that the literature constantly conflates.
- **Bayes-optimal classifiers.** Given a utility / cost structure, what is the threshold that minimizes expected loss? Often *not* 0.5.
- **Decision-curve analysis (Vickers & Elkin).** Plot net benefit vs. threshold probability. The closest thing to "is the model clinically useful" that the field has produced.
- **AUROC and its limitations.** Useful but incomplete. Hides class-imbalance effects, prevalence effects, and calibration entirely.

The paradox flagged is **Simpson's paradox** — the same direction reversed at the subgroup level vs. the aggregate level. A working AUROC at the population level can mask that the model performs *worse than chance* on a subgroup.

## Why it matters

Most published health-AI failures aren't model-architecture failures; they are evaluation failures. The model was real but the evaluation wasn't a useful answer to a clinical question. Examples:

- A pneumonia classifier with AUROC 0.95 — but its decision threshold means catching pneumonia at the cost of one false alarm per real case, which clinicians ignore (alert fatigue).
- A sepsis predictor with great discrimination — but uncalibrated, so probability of 0.7 means one thing in one hospital and a different thing in another.
- A risk model that "performed well in validation" — measured by AUROC on a balanced sample, then deployed at 1% prevalence where PPV collapses.

Every one of these is the same mistake at root: forgetting that "the metric I just reported" answers a different question than "does this help patients."

## Things you should walk away believing

- The confusion matrix is the substrate; every metric is a particular projection of it. Pick the projection that matches the decision being made.
- Soft scores → hard decisions requires a threshold, and the threshold is a clinical-utility statement.
- AUROC is threshold-free and prevalence-free. That sounds great until you realize you make decisions *with* a threshold *at* a prevalence — both of which AUROC pretends not to know about.
- Discrimination ≠ calibration. A perfectly-discriminating but miscalibrated model can still be clinically useless.
- Bayes-optimal threshold = ratio of misclassification costs. If false negatives are 9× more costly than false positives, the threshold should be ~ 0.1, not 0.5.
- Decision-curve analysis is your friend when reviewers ask "is this clinically useful?"

## How this connects to the rest of the course

- L9 (training a classifier) presupposes you know what "good" means — that's L8.
- L10 (generalization) returns to "calibration drifts at deployment time" as a leading failure mode.
- L17-L18 (EHR data) and L24 (fairness) keep returning to subgroup metrics — separate confusion matrices per subgroup, then ask if any of them is unacceptable.
- L23 (population health, survival) extends evaluation to censored and time-to-event outcomes.
- L28 (course recap) ends with a reprise of the L8 toolkit applied at deployment time.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

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

### Discrimination vs. Calibration: Two Distinct Goals

```{admonition} Why both matter in health ML
:class: important
**Discrimination** asks: does a high score tend to go to positive cases?
**Calibration** asks: if the model says 70% risk, does the patient actually have 70% probability of the outcome?

A model can discriminate perfectly (AUROC = 1) but be miscalibrated (all probabilities shifted). In clinical decision-making — especially shared decision-making — calibration often matters *more* than discrimination because the raw probability is being used directly.
```

### The AUROC Interpretation

```{admonition} Probabilistic interpretation
:class: tip
AUROC = P(s₁ > s₀) where s₁ is a random score from a positive case and s₀ from a negative case. It equals the probability that the model ranks a randomly chosen positive case above a randomly chosen negative case. This interpretation holds regardless of threshold and class prevalence.
```

### Self-Check Questions

1. A COVID test has sensitivity 0.95 and specificity 0.90. In a population with 5% prevalence, compute the PPV and NPV.
2. Sketch the ROC curve for: (a) a random classifier, (b) a perfect classifier, (c) a typical classifier. What area does each subtend?
3. A model achieves AUROC = 0.85 but its calibration curve shows probabilities are consistently twice as high as the true rate. What are the implications for clinical use?
4. Why might you choose a threshold other than 0.5? Give an example where a low threshold (high sensitivity) is preferable and one where a high threshold (high precision) is preferable.
5. Explain the tradeoff between sensitivity and specificity in a screening test vs. a confirmatory test.

### Additional Resources

- [Fawcett — *An Introduction to ROC Analysis* (2006)](https://people.inf.elte.hu/kiss/13dwhdm/roc.pdf) — the canonical ROC paper.
- [Steyerberg et al., "Assessing the performance of prediction models" (2010)](https://pubmed.ncbi.nlm.nih.gov/20010215/) — discrimination, calibration, and clinical utility.
- [StatQuest — ROC and AUC, Clearly Explained! (YouTube)](https://www.youtube.com/watch?v=4jRBRDbJemM) — visual walkthrough.
- [MSKCC — Decision Curve Analysis](https://www.mskcc.org/departments/epidemiology-biostatistics/biostatistics/decision-curve-analysis) — the original DCA framework.
- [Van Calster et al., "Calibration: the Achilles' heel of predictive analytics," *BMC Med* 17, 2019](https://bmcmedicine.biomedcentral.com/articles/10.1186/s12916-019-1466-7).
- Pepe, *The Statistical Evaluation of Medical Tests*; Steyerberg, *Clinical Prediction Models* Chs. 15-17 — definitive textbooks.
