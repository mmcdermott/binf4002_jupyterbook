# L11 Study Guide — Lab Day #1

> No lecture content. In-class Q&A and lab work for the first lab chunk (labs 0-5: ML model types). Use this study guide as a checklist for what each model class is trying to do; for full review see the [Labs](../labs/intro.md).

## Key Terms

| Term | Definition |
|---|---|
| **Logistic Regression** | Linear classifier with sigmoid output; trained by minimizing cross-entropy. The default baseline. |
| **Decision Tree** | Recursive axis-aligned splits of feature space. Interpretable; prone to overfit; invariant to monotonic feature scaling. |
| **k-Nearest Neighbors** | Predict by majority vote of the k closest training points. Non-parametric; consistent under k → ∞, k/n → 0. Highly sensitive to feature scaling. |
| **Random Forest** | Ensemble of decision trees on bootstrap samples + random feature subsets at each split. Variance-reduction via averaging. |
| **Gradient Boosting** | Additive ensemble: each new weak learner fits the residual of the previous ensemble. Strong on tabular data (XGBoost, LightGBM). |
| **Feedforward Neural Network (MLP)** | Stack of fully-connected layers with element-wise nonlinearities. Universal approximator; needs careful optimization (preview of L13). |

## Things to Practice

```{admonition} The model-type spectrum
:class: tip
Linear → tree → ensemble → neural is the canonical capacity / inductive-bias progression. Each step trades interpretability and small-sample efficiency for representational power. **Always fit at least one simple baseline (logistic regression or a single tree) before reaching for anything fancier** — both as a sanity check and as an honest comparison.
```

## Self-Check Questions

1. Why does feature scaling matter for k-NN and logistic regression but *not* for decision trees?
2. A decision tree gets 100% training accuracy and 60% test accuracy. What's happening, and what hyperparameter would you tune?
3. What is bagging? What is boosting? Which is each ensemble method (random forest vs. gradient boosting) using?
4. When does a neural network fit on tabular data with 1000 examples make sense, and when does it not?

## Additional Resources

- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) — every model in this lab chunk has a section.
- [Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.)](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) — Chs. 2-7 cover almost everything in this lab chunk.
- [Kuhn & Johnson, *Applied Predictive Modeling*](http://appliedpredictivemodeling.com/) — older but excellent on thoughtful preprocessing.
- [Chen & Guestrin, "XGBoost" (KDD 2016)](https://arxiv.org/abs/1603.02754) — the gradient-boosting engine you'll meet in lab 4.

> See also: [L11 lecture page](../lectures/lecture-11.md).
