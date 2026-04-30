# Part 1 — Mathematical & ML Foundations

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Lectures 1-10**

## What this part is about

Part 1 builds the language the rest of the course is conducted in. By the end of L10 you should be able to read most ML papers in the rest of the syllabus, recognize their objects (vectors, distributions, gradients, losses, expected vs. empirical risk), and have an opinion about whether their evaluation answers a useful question.

It is split into three threads:

- **§1.1 Mathematical preliminaries (L1-L6)** — vectors and linear operators (L2); probability and information theory (L3-L4); calculus and optimization deterministic and probabilistic (L5-L6). The math is treated formally, not because the formalism is the point, but because most ML mistakes in health are smuggled in under loose probability language.
- **§1.2 Probabilistic modeling (L7)** — Di Liu's guest lecture unifying supervised and unsupervised learning under a single recipe: data → parametric model → likelihood-based objective → optimization. Most losses you'll encounter in the rest of the course are NLLs under different probabilistic assumptions.
- **§1.3 Evaluation, training, generalization (L8-L10)** — the canonical supervised-learning loop. L8 evaluates a fixed binary classifier; L9 trains one; L10 closes the arc with generalization, inductive bias, regularization, domain shift, explainability, and fairness as gating concerns.

## Goals for this part

- Manipulate vectors, matrices, distributions, gradients, and likelihoods fluently.
- Set up an empirical risk minimization problem and reason about expected vs. empirical loss.
- Evaluate a fixed classifier with calibration, discrimination, decision-curve analysis, Bayes-optimal thresholds.
- Train a classifier; use data splits, regularization, inductive bias.
- Recognize when ML is the wrong tool (domain shift, fairness constraints, mismatched validation).

## Key takeaways for this part

- ML is sampling + optimization + bias control. Each piece can fail independently.
- Loss functions are *proxies*, not the decision you care about.
- Generalization is not parameter-count; it's about which solutions the optimization is biased toward.
- Calibration ≠ discrimination. Both are real failure modes; AUROC alone tells you about neither well at low prevalence.

## Lectures in this part

- [L1 — Course orientation](../lectures/lecture-01.md)
- [L2 — Linear algebra](../lectures/lecture-02.md)
- [L3 — Probability](../lectures/lecture-03.md)
- [L4 — Information theory & Bayesian probability](../lectures/lecture-04.md)
- [L5 — Calculus & optimization](../lectures/lecture-05.md)
- [L6 — Probabilistic optimization](../lectures/lecture-06.md)
- [L7 — Probabilistic modeling (Di Liu, guest)](../lectures/lecture-07.md)
- [L8 — Binary-classification evaluation (Florent Pollet, guest)](../lectures/lecture-08.md)
- [L9 — Binary-classification training](../lectures/lecture-09.md)
- [L10 — Generalization, domain shift, fairness recap](../lectures/lecture-10.md)

## External resources for this part

- Goodfellow, Bengio, Courville, *Deep Learning* (free online), Chs. 2-9 — the cleanest single-volume map of the foundations material.
- Murphy, *Probabilistic Machine Learning: An Introduction* (vol 1, 2022), Chs. 2-13 — the closest single-textbook to this course's spine.
- Hastie, Tibshirani, Friedman, *The Elements of Statistical Learning* (free online), Chs. 1-9 — the classical statistical-learning lens.
- Bishop, *Pattern Recognition and Machine Learning*, Chs. 1-4 — Bayesian flavor.
- 3Blue1Brown, *Essence of Linear Algebra* and *Essence of Calculus* — visual companions for L2 and L5.
- MacKay, *Information Theory, Inference, and Learning Algorithms* (free PDF), Chs. 2-4 and 24 — for L4.
- Boyd & Vandenberghe, *Convex Optimization* (free PDF), Ch. 9 — for L5.
- Pepe, *The Statistical Evaluation of Medical Tests for Classification and Prediction* — the canonical reference for L8.
- Steyerberg, *Clinical Prediction Models*, Chs. 15-17 — applied-clinical complement to L8.
- Coursera / Stanford CS229 (Andrew Ng) — free online, covers most of Part 1 hands-on.
- Domingos, "A Few Useful Things to Know About Machine Learning," *CACM* 55(10), 2012 — twelve principles every ML practitioner should internalize.
