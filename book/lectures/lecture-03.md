# Lecture 3 — Probability: random variables, expectation, joint distributions

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

**Tue Jan 27, 2026 · Part 1 — Foundations · §1.1 Mathematical preliminaries**

## What this lecture is about

Probability in this course is treated *formally* — not because the formalism is the point, but because most ML mistakes in health are smuggled in under loose probability language. The lecture introduces the probability triple (sample space Ω, event set ℱ, probability measure ℙ), random variables as functions from samples to measurable observations, expectation as the operator that connects probability to optimization, and joint distributions as the move from one variable to the relationship between two or more.

We work through discrete examples (coin flips, dice rolls) so you can see what the formal objects look like before we ever take an integral.

The lecture's paradox is the **Envelope Paradox** — a setup where naïve "expected value" reasoning gives a contradictory answer. The point of the paradox is not the puzzle; it's that "the expectation of …" is not a license to skip thinking about *which* probability measure you're integrating against.

## Why it matters

Every supervised ML algorithm minimizes an expectation. Every evaluation metric is an expectation. Every claim of the form "the model is good" is implicitly "the expected loss is small under some distribution." If you don't carefully track *which distribution*, you end up with the canonical health-AI failure mode: the model was trained and validated under one distribution and deployed under a different one, and "good performance" was a statement about the wrong measure.

This lecture also introduces the key handle for everything that comes next:

- A random variable is a *function*, not a number with hand-wavy uncertainty around it.
- An event is a structured subset of Ω (i.e., something you can ask "did this happen?" about).
- Expectation is just an inner product in function space against the probability measure.

That last bullet sounds abstract; it is the reason the course is structured as it is. It means probability sits inside the linear-algebra vocabulary from L2, and it's why information theory in L4 will feel like geometry rather than combinatorics.

## Things you should walk away believing

- A random variable is a function ω↦X(ω). When you write "X = 5" you mean the event {ω : X(ω) = 5}.
- ℙ assigns mass to events, not to individual outcomes (in continuous cases).
- 𝔼[X] = ∫ X dℙ — *which* ℙ is part of the statement.
- Joint distributions are how dependence enters; marginal and conditional distributions are derived from joints.
- Naïve expectation reasoning fails when the measure is misspecified — that is what the Envelope Paradox is teaching.

## How this connects to the rest of the course

- L4 builds conditioning, Bayes, and information theory directly on top of these objects.
- L6 (probabilistic optimization) lifts deterministic optimization from L5 into expectations over data-generating distributions.
- L7 (probabilistic modeling, guest) reads supervised ML as likelihood-based — i.e., maximum-likelihood is "minimize a particular expectation."
- L8 (binary-classification evaluation) returns to PPV / NPV / prevalence — Bayes-rule rearrangements you'll do over and over.
- L17-L18 (EHR data) is full of "the observed distribution is not the population distribution" arguments.
- L24 (causality) and L28 (recap) keep returning to "expectation under what distribution?"

## Source files in this folder

- `Lecture 3.pdf` — the slides as released to students.
- `Lecture 3 - probability.pptx` — editable PowerPoint source.

## To go deeper

- **Bishop, _Pattern Recognition and Machine Learning_, Ch. 1.** The ML-flavored probability primer.
- **Wasserman, _All of Statistics_, Chs. 1-3.** A no-nonsense reset on probability and basic statistical inference.
- **Murphy, _Probabilistic Machine Learning: An Introduction_, Ch. 2.** Tighter, more modern, ML-oriented.
- **MacKay, _Information Theory, Inference, and Learning Algorithms_ (free PDF), Chs. 2-3.** Slow, careful, opinionated; pairs well with the formalism in this lecture.

## Study tools

- [Study guide for L03](../study_guides/lecture-03.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
