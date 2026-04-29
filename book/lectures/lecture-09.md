# Lecture 9 — Training a binary classification model

**Tue Feb 17, 2026 · Part 1 — Foundations · §1.3 Evaluation, training, generalization**

## What this lecture is about

L8 evaluated a fixed model. L9 turns to: how do we *train* one? The lecture opens with a real-world setup that looks like a perfectly normal ML problem but isn't — **the influenza vaccine effectiveness example.** Observational data say the vaccinated group has lower flu rates than the unvaccinated. Does the vaccine work, or is it that the kind of person who gets the flu shot is the kind of person who also avoids crowded indoor spaces, washes their hands, etc.? You can fit a beautiful classifier and answer the wrong question.

Once that hazard is in your mind, the rest of the lecture lays out the full ML training pipeline:

- **The pipeline.** Pick a loss → pick a function class → optimize empirical loss → check generalization → repeat.
- **Data splits.** Train / validation / test. Why each exists, what role each plays in estimating expected loss (callback to L6).
- **Model capacity and misspecification.** Capacity = how many functions the model class can represent. Misspecification = the right function isn't in the class. Both bite, in different ways.
- **k-Nearest Neighbors as a procedural baseline.** No training step in the usual sense; classification = "vote among the k closest training points." It is *consistent* (in the limit of infinite data, it converges to the Bayes-optimal classifier) but practically catastrophic in high dimensions.
- **The optimization view.** Training = minimize empirical risk. With logistic loss + linear model = logistic regression. With cross-entropy + neural network = the same recipe scaled up.

The companion notebook `Lecture_9.ipynb` (with its `dataset (*).jpg` images) makes the geometric intuition vivid: see how decision boundaries move as you change loss, capacity, and dataset structure.

The paradox flagged is the **Healthy Vaccinee Effect** — a confounder you should have in your peripheral vision the rest of the course.

## Why it matters

Three threads converge here:

**The pipeline is the pipeline.** Loss → function class → optimization → generalization. Almost everything you'll fit in the next 14 weeks fits this template, and the *hard* parts are picking the loss and picking the function class to match the *problem*, not running the optimizer. The optimizer is the easy part.

**kNN is more important than it looks.** Yes, you'll never deploy kNN in a real system. But kNN is the simplest model that reveals the bias-variance tradeoff (k controls capacity), domain shift (your "neighbors" aren't your neighbors anymore), high-D pathology (every point is far from every other point in 100-D), and consistency (it provably converges). It is a useful sanity-check baseline and a teaching tool that returns in L10 and L25.

**The flu-vaccine motivation is the moral of the lecture.** Fitting a classifier on observational data answers a *prediction* question well, but tells you almost nothing about *intervention*. We will dedicate L24 to formalizing this distinction — but the warning starts here.

## Things you should walk away believing

- "Train a classifier" = pick loss + function class + optimizer + generalization estimate. The four pieces are independent design choices.
- Train / validation / test do different jobs: train fits, validation chooses model/hyperparameters, test estimates expected loss. Don't conflate them.
- Capacity and misspecification are different problems with different fixes — capacity is a parameter-count knob, misspecification is "the right function isn't in your class."
- kNN is a *useful* baseline, not a toy. Fit it before you fit anything fancy.
- Observational data fitting answers a prediction question. It is not a license to claim causality.

## How this connects to the rest of the course

- L10 closes the training arc with the modern story of generalization (overfitting, inductive bias, regularization).
- L13 (neural networks) is this same pipeline with a richer function class and more careful optimization.
- L18 (EHR modeling) requires re-defining "what counts as a label" because of windows / censoring / actionability.
- L23 (survival) replaces binary classification with time-to-event when "did it happen?" hides "when did it happen?"
- L24 (causality) takes the flu-vaccine warning seriously and gives you the formal tools (DAGs, do-operator, propensity scores) to reason about it.

## Source files in this folder

- `Lecture 9.pdf` — the slides as released to students.
- `Lecture 9.pptx` — editable PowerPoint source.
- `Lecture_9.ipynb` — companion notebook with the decision-boundary visualizations used in lecture.
- `dataset*.jpg` — input figures the notebook consumes.

## To go deeper

- **Hastie, Tibshirani, Friedman, _The Elements of Statistical Learning_, Chs. 2 and 13.** ESL Ch. 2 is the cleanest single chapter on the bias-variance tradeoff anywhere. Ch. 13 is on prototypes and nearest-neighbor methods.
- **Murphy, _Probabilistic Machine Learning: An Introduction_, Chs. 4 and 16.** Modern, ML-flavored coverage of training and kNN.
- **Domingos, "A Few Useful Things to Know About Machine Learning," _CACM_ 55(10), 2012.** Twelve things every ML practitioner should internalize. Worth re-reading once a year.
- **Géron, _Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow_ (3rd ed.).** The applied companion if you want to run all of this in code.
