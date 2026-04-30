# Lecture 3 — Probability: random variables, expectation, joint distributions

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

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

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Probability Triple** | (Ω, Σ, P): sample space Ω (all outcomes), event space Σ (measurable subsets), probability measure P : Σ → [0,1] satisfying P(Ω)=1 and countable additivity. |
| **Random Variable** | A measurable function X : Ω → E mapping outcomes to observable values. The induced distribution over E is what we usually work with. |
| **PMF (discrete)** | Probability mass function: P(X=x) for each x. Must sum to 1. |
| **PDF (continuous)** | Probability density function: f(x) ≥ 0 with ∫ f(x) dx = 1. P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx. |
| **Expectation** | 𝔼[X] = Σ x P(X=x) (discrete) or ∫ x f(x) dx (continuous). The probability-weighted average outcome. |
| **Law of Large Numbers** | Sample averages of iid draws converge in probability to the true expectation as n → ∞. |
| **Variance** | Var(X) = 𝔼[(X − 𝔼[X])²] = 𝔼[X²] − 𝔼[X]². Measures spread around the mean. |

### Intuition: What Is a Probability Triple?

```{admonition} Coin-flip example
:class: tip
Ω = {H, T}.  Σ = {∅, {H}, {T}, {H,T}}.  P({H}) = P({T}) = ½.
The event space must be closed under complement and countable union — i.e., a σ-algebra. For most practical uses you can think of a random variable and its distribution as equivalent; the formal triple captures the rigorous foundations.
```

### Self-Check Questions

1. Verify the three axioms of a probability measure for a fair die.
2. If X ~ Uniform(0,1), compute 𝔼[X] and Var(X) from first principles.
3. Why must a PDF integrate to 1? What goes wrong if it doesn't?
4. What is the relationship between CDF and PDF?
5. A random variable maps outcomes to values — what does it mean for it to be "measurable"?

### Additional Resources

- [Harvard Stat 110 (Joe Blitzstein) — full course online](https://projects.iq.harvard.edu/stat110/home) — one of the best probability courses available.
- [Probability for Machine Learning (Brownlee)](https://machinelearningmastery.com/probability-for-machine-learning/) — applied intro; pairs well with the formal definitions.
- [StatQuest — Probability (YouTube)](https://www.youtube.com/c/joshstarmer) — short, clear videos on distributions and expectations.
- [Betancourt — Probability Theory for ML](https://betanalpha.github.io/assets/case_studies/probability_theory.html) — rigorous measure-theoretic treatment.
- Bishop, *PRML*, Ch. 1; Wasserman, *All of Statistics*, Chs. 1-3; Murphy, *PML*, Ch. 2.
