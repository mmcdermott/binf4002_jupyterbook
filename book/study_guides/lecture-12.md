# L12 Study Guide — Lab Day #2

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

> Continued lab work on chunk 1 (labs 0-5). No new lecture content. The labs in scope are the same as L11; this guide gives you a few additional debugging-mindset prompts.

## Common Debugging Patterns to Build

| Symptom | Common Causes |
|---|---|
| **Train acc ≫ test acc** | Overfitting — model too complex, regularization too weak, leakage between splits, or k too small in k-NN. |
| **Train acc ≈ test acc, both low** | Underfitting — model class too simple, or task fundamentally hard with the available features. |
| **Wildly variable test acc across runs** | High variance — small training set, or stochastic algorithm without seed control. |
| **Logistic regression worse than naive baseline** | Feature scaling missing, or label encoding wrong. |
| **k-NN catastrophically slow** | High dimensionality / large training set; consider approximate-NN or first dim-reduction. |
| **Tree splits look weird** | Feature has near-zero variance, or majority class dominates due to imbalance. |

## Self-Check Questions

1. You see Train AUROC = 0.95 and Test AUROC = 0.65. Walk through the causes you'd investigate, in order.
2. A lab-mate fits a logistic regression on raw Hounsfield unit values without scaling. The model "works" (AUROC 0.7) — but should they trust it? Why or why not?
3. A random forest with 100 trees does better than a single decision tree. Identify which mechanism (bagging, feature subsampling, both) is most responsible, and explain.
4. You evaluate two models with the same AUROC. Calibration plots show one is well-calibrated and one is shifted upward by 0.2 across the score range. Which is "better"? *(Trick question — discuss both senses.)*

## Additional Resources

Same as L11. In particular:

- [Domingos, "A Few Useful Things to Know About Machine Learning," *CACM* 55(10), 2012](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) — twelve practical principles.
- [Karpathy, "A Recipe for Training Neural Networks" (blog)](http://karpathy.github.io/2019/04/25/recipe/) — diagnostic mindset that generalizes to non-NN models too.

> See also: [L12 lecture page](../lectures/lecture-12.md).
