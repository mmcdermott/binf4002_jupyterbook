# Lecture 10 — Generalization, domain shift, fairness

**Thu Feb 19, 2026 · Part 1 — Foundations · §1.3 Evaluation, training, generalization**

## What this lecture is about

This is the closer for Part 1. Now that you can train and evaluate a binary classifier, the question is: when does the trained model actually generalize, and when does it look good in validation but fail in deployment?

The lecture is organized around a few claims that each subvert the previous one:

- **Overfitting and memorization.** Classical story: high-capacity models memorize the training set; low-capacity models don't. So pick capacity carefully.
- **The modern-DL puzzle.** Deep neural networks have *more parameters than training points* and yet generalize. The classical bias-variance picture predicts they shouldn't. Zhang et al. (2017) showed they can also memorize random labels. So the classical story is at best incomplete.
- **What's actually going on: inductive bias.** A model class isn't just "what functions can be represented" — it's *which functions are easy to learn under a given optimizer*. Gradient descent on overparameterized neural networks is biased toward simple, generalizing solutions even when the model class can represent everything.
- **Regularization.** Explicit (L2, dropout, weight decay) and implicit (the optimizer's bias). Both are real, both matter.
- **kNN as a counter-example.** Local memorization, properly chosen, *can* converge to Bayes-optimal classification. That's the consistency theorem from L9 returning to make a point.
- **Negative controls.** A sanity check: shuffle labels, run training, see if you get nonzero performance. If you do, your evaluation is leaky.
- **Domain shift, explainability, fairness.** Three failure modes that the second half of the course will revisit at length. Each is a case where "good train and validation loss" doesn't mean "the model is OK."

The paradox flagged: "**overfitting is possible — it is the optimal solution to the optimization problem — but it doesn't happen.**" This is the core puzzle of modern deep learning, the paradox students should sit with.

## Why it matters

This lecture is the *transition* of the course. Part 1 has been building the formal machinery; Part 2 onwards uses it. The transition relies on three takeaways being internalized:

**Capacity is not the right way to think about generalization in modern ML.** A 100-million-parameter network is not "more overfit" than a 1-million-parameter network if the optimizer's inductive bias is good. This will matter constantly when we discuss neural networks, transformers, and foundation models in Part 2.

**Negative controls and sanity checks are basic ML hygiene, not paranoia.** "Shuffle the labels, retrain, does it still work?" is a question every reviewer should be asking, and you should be asking it of yourself before they do. We'll see real examples of papers that didn't (L21 imaging shortcut learning).

**Domain shift, explainability, and fairness are first-class.** They are not afterthoughts and they are not "ethics for ML." They are constraints on the training pipeline that, when violated, produce models that are technically excellent and practically harmful. This lecture is the one that says: that pattern is *the rule, not the exception* in health AI.

## Things you should walk away believing

- A model that *can* memorize doesn't *have* to. Inductive bias decides what it actually learns.
- "Simple model" vs. "complex model" is the wrong axis. The right axis is "which functions does the optimizer find first."
- Regularization — explicit and implicit — is part of the model, not a knob you turn at the end.
- A model that solves a puzzle without being able to do anything else (e.g., a model that fits any random labels but somehow generalizes when labels are real) is telling you something about the optimization, not about the architecture.
- Negative controls are basic hygiene. Do them before publication, not after rebuttal.
- Domain shift, explainability, and fairness are not ethical add-ons; they are reasons your validation may be lying.

## How this connects to the rest of the course

- L13 (neural networks) is essentially "here's how to make the inductive bias good in practice."
- L17-L18 (EHR data) is full of distribution-shift problems disguised as data-quality problems.
- L21-L22 (medical imaging) revisits inductive bias (CNN, U-Net, MIL) and shortcut learning as a domain-shift symptom.
- L24 (causality and fairness) formalizes the fairness questions raised here.
- L25 (PRS transferability) is a domain-shift story about populations and ancestry.
- L28 (course recap) returns to negative controls and domain shift as the things that survive the semester.

## Source files in this folder

- `Lecture 10.pdf` — the slides as released to students.
- `Lecture 10.pptx` — editable PowerPoint source.

## To go deeper

- **Zhang et al., "Understanding deep learning requires rethinking generalization," _ICLR_ 2017.** The paper that broke the classical capacity story. Read once.
- **Belkin, Hsu, Ma & Mandal, "Reconciling modern machine-learning practice and the classical bias-variance trade-off," _PNAS_ 116(32), 2019.** The double-descent picture. The piece that gives a constructive replacement story.
- **D'Amour et al., "Underspecification presents challenges for credibility in modern machine learning," _JMLR_ 23, 2022.** Why two equally-trained models can behave differently in deployment even with identical training loss. A long but valuable read.
- **Finlayson et al., "The Clinician and Dataset Shift in Artificial Intelligence," _NEJM_ 385, 2021.** Domain shift in clinical AI, explained for clinicians. Short and excellent.
- **Geirhos et al., "Shortcut learning in deep neural networks," _Nat Mach Intell_ 2, 2020.** The taxonomy of shortcut-learning failures. Pairs well with L21.

## Study tools

- [Study guide for L10](../study_guides/lecture-10.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
