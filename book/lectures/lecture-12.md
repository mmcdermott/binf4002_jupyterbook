# Lecture 12 — Lab Day #2

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Feb 26, 2026 · Part 2 — Modern AI & lab work**

## What this class meeting was about

Second of the two consecutive lab/Q&A days. No new lecture material. Students kept working through the first lab chunk (labs 0-5, released Sun Feb 22, covering ML model types). The second lab chunk — ML *losses* — would not release until the following Monday (Mar 2), so the labs in scope on this day are the same as on Lab Day #1.

What this day adds beyond Lab Day #1:

- **Time pressure to actually finish.** The next chunk lands Monday; carry-over is allowed but not encouraged.
- **Cross-comparison.** With a few days of work behind them, students can now compare results across model classes on the same dataset and start to *feel* the bias-variance picture from L10 rather than just believe it.
- **Clinic-style debugging.** This is the day where most students hit the "my logistic regression is doing weirdly poorly" or "my tree is at 100% training accuracy and 60% test accuracy" moments, and the in-class time is for debugging those rather than introducing new content.

## What you should walk away with

In addition to everything from Lab Day #1:

- A debugging muscle for "is this a data problem or a model problem?" — the single most useful skill in applied ML.
- A working comparison table for the six baselines (which performs best on your dataset, why, and how confident you are in that ranking).
- An understanding that *no single number* (accuracy, AUROC, F1) is the right summary of a binary classifier — connecting back to L8.

## How this connects to the rest of the course

- L13 (neural networks) is now the last NN-related lab you've seen plus the lecture you haven't. The contrast between "I trained a small NN in lab5 and it kind of worked" and "here is why architecture and optimization actually matter" is what L13 is built around.
- L16 (Lab Day #3) will pull in the loss-types chunk (lab 6-11) released the following Monday and the data-types chunk (lab 12-16) released on Mar 6; some carry-over from labs 0-5 is expected.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Common Debugging Patterns to Build

| Symptom | Common Causes |
|---|---|
| **Train acc ≫ test acc** | Overfitting — model too complex, regularization too weak, leakage between splits, or k too small in k-NN. |
| **Train acc ≈ test acc, both low** | Underfitting — model class too simple, or task fundamentally hard with the available features. |
| **Wildly variable test acc across runs** | High variance — small training set, or stochastic algorithm without seed control. |
| **Logistic regression worse than naive baseline** | Feature scaling missing, or label encoding wrong. |
| **k-NN catastrophically slow** | High dimensionality / large training set; consider approximate-NN or first dim-reduction. |
| **Tree splits look weird** | Feature has near-zero variance, or majority class dominates due to imbalance. |

### Self-Check Questions

1. You see Train AUROC = 0.95 and Test AUROC = 0.65. Walk through the causes you'd investigate, in order.
2. A lab-mate fits a logistic regression on raw Hounsfield unit values without scaling. The model "works" (AUROC 0.7) — but should they trust it? Why or why not?
3. A random forest with 100 trees does better than a single decision tree. Identify which mechanism (bagging, feature subsampling, both) is most responsible, and explain.
4. You evaluate two models with the same AUROC. Calibration plots show one is well-calibrated and one is shifted upward by 0.2 across the score range. Which is "better"? *(Trick question — discuss both senses.)*

### Additional Resources

Same as L11. In particular:

- [Domingos, "A Few Useful Things to Know About Machine Learning," *CACM* 55(10), 2012](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) — twelve practical principles.
- [Karpathy, "A Recipe for Training Neural Networks" (blog)](http://karpathy.github.io/2019/04/25/recipe/) — diagnostic mindset that generalizes to non-NN models too.
