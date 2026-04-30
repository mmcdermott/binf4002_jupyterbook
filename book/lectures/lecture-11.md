# Lecture 11 — Lab Day #1

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Feb 24, 2026 · Part 2 — Modern AI & lab work**

## What this class meeting was about

No new lecture material. The class slot was used for **in-class Q&A and supervised lab work**. The first chunk of labs (labs 0-5) had been released the previous Sunday (Feb 22), covering ML *model types* — the spectrum from simple linear baselines to neural networks. Students worked through the labs under instructor and TA supervision, and used the time to ask questions about the material from L1-L10 that wasn't quite settling.

The lab chunk in scope:

- **lab0_preprocessing** — data cleaning, feature scaling, train/val/test splits.
- **lab1_logistic_regression** — the canonical linear classifier.
- **lab2_decision_trees** — non-linear, interpretable, prone to overfit.
- **lab3_knn** — the k-nearest-neighbors baseline that was discussed in L9.
- **lab4_ensemble_methods** — random forests and gradient boosting; ensembling as a way to lower variance.
- **lab5_neural_networks** — first taste of feedforward networks before the real NN lecture (L13).

## Why this lab day matters for the course

Three reasons hands-on time was carved out here, *before* introducing neural networks and modern AI:

**To make the model-type spectrum tangible.** Linear → tree → ensemble → neural is the canonical progression of *function-class capacity* and *inductive bias*. Reading about it in L9-L10 isn't enough; running it on a dataset and watching where each model fails (linear underfits, deep tree overfits, random forest is hard to interpret, NN is hard to tune) makes the abstract bias-variance discussion concrete.

**To set up the loss-and-optimization mindset.** Every model in this chunk gets fitted by some form of empirical risk minimization. Watching the loss curves makes L5-L6 concrete in a way that lecture slides can't.

**To give students the muscle for lab chunk #2.** The next chunk (released Mar 2) introduces ML *loss types* — multiclass, regression, survival, probabilistic. That chunk is much harder to get right if you haven't already lived through "swap the model and re-run the same dataset."

## What you should walk away with

- A working sense of which model classes are easy to fit, which are easy to overfit, and which are easy to interpret.
- An eye for which preprocessing decisions matter (scaling matters for kNN, doesn't matter for trees, mostly matters for logistic regression).
- The reflex to *always* fit a simple baseline (logistic regression, single decision tree) before reaching for anything fancier — both for sanity-check and for ablation.
- Comfort with sklearn's standard fit / predict / score interface, which is the substrate the rest of the course's notebooks build on.

## How this connects to the rest of the course

- L13 (neural networks) presupposes you have wrestled with `lab5_neural_networks` and have at least one reflexive frustration about NN training to motivate the architectural and optimizer choices.
- L23 (population health, survival analysis) reuses the survival-analysis lab (lab8) framework.
- L24 (causality and fairness) returns to "why a logistic regression on observed labels can be both *accurate* and *unfair*."

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Logistic Regression** | Linear classifier with sigmoid output; trained by minimizing cross-entropy. The default baseline. |
| **Decision Tree** | Recursive axis-aligned splits of feature space. Interpretable; prone to overfit; invariant to monotonic feature scaling. |
| **k-Nearest Neighbors** | Predict by majority vote of the k closest training points. Non-parametric; consistent under k → ∞, k/n → 0. Highly sensitive to feature scaling. |
| **Random Forest** | Ensemble of decision trees on bootstrap samples + random feature subsets at each split. Variance-reduction via averaging. |
| **Gradient Boosting** | Additive ensemble: each new weak learner fits the residual of the previous ensemble. Strong on tabular data (XGBoost, LightGBM). |
| **Feedforward Neural Network (MLP)** | Stack of fully-connected layers with element-wise nonlinearities. Universal approximator; needs careful optimization (preview of L13). |

### Things to Practice

```{admonition} The model-type spectrum
:class: tip
Linear → tree → ensemble → neural is the canonical capacity / inductive-bias progression. Each step trades interpretability and small-sample efficiency for representational power. **Always fit at least one simple baseline (logistic regression or a single tree) before reaching for anything fancier** — both as a sanity check and as an honest comparison.
```

### Self-Check Questions

1. Why does feature scaling matter for k-NN and logistic regression but *not* for decision trees?
2. A decision tree gets 100% training accuracy and 60% test accuracy. What's happening, and what hyperparameter would you tune?
3. What is bagging? What is boosting? Which is each ensemble method (random forest vs. gradient boosting) using?
4. When does a neural network fit on tabular data with 1000 examples make sense, and when does it not?

### Additional Resources

- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) — every model in this lab chunk has a section.
- [Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.)](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) — Chs. 2-7 cover almost everything in this lab chunk.
- [Kuhn & Johnson, *Applied Predictive Modeling*](http://appliedpredictivemodeling.com/) — older but excellent on thoughtful preprocessing.
- [Chen & Guestrin, "XGBoost" (KDD 2016)](https://arxiv.org/abs/1603.02754) — the gradient-boosting engine you'll meet in lab 4.
