# Lecture 8 — Evaluating a binary classification model

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

## Source files in this folder

- `Lecture 8 - Florent Pollet (guest).pdf` — the canonical guest deck released to students.
- `Lecture 8 - binary_classification_evaluation.pptx` — earlier draft of the lecture; kept for reference but Florent's deck is what was delivered.

## To go deeper

- **Pepe, _The Statistical Evaluation of Medical Tests for Classification and Prediction._** The textbook. Long, careful, definitive.
- **Steyerberg, _Clinical Prediction Models_, Chs. 15-17.** The applied-clinical version of the same material.
- **Vickers & Elkin, "Decision-curve analysis: a novel method for evaluating prediction models," _Med Decis Making_ 26(6), 2006.** The original DCA paper. Read it once, you'll never forget what net benefit means.
- **Van Calster et al., "Calibration: the Achilles' heel of predictive analytics," _BMC Med_ 17, 2019.** A short, punchy argument for why calibration is more often what's wrong than discrimination.
- **Saito & Rehmsmeier, "The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets," _PLOS ONE_, 2015.** Useful when prevalence is low.
