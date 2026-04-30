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

## Source files in this folder

- `labs/` — the six lab notebooks (labs 0-5) as released.
- `solutions/` — instructor solution notebooks for the same labs.

## To go deeper

- **scikit-learn user guide.** The single most useful online reference for the model-type chunk. Everything in labs 0-5 maps to a section.
- **Géron, _Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow_ (3rd ed.).** The applied companion textbook. Chs. 2-7 cover almost everything in this lab chunk.
- **Kuhn & Johnson, _Applied Predictive Modeling_.** Older but excellent, especially for thoughtful preprocessing.

## Study tools

- [Study guide for L11](../study_guides/lecture-11.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
