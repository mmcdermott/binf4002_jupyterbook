# L3 Study Guide — Probability: Random Variables & Expectation

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

## Key Terms

| Term | Definition |
|---|---|
| **Probability Triple** | (Ω, Σ, P): sample space Ω (all outcomes), event space Σ (measurable subsets), probability measure P : Σ → [0,1] satisfying P(Ω)=1 and countable additivity. |
| **Random Variable** | A measurable function X : Ω → E mapping outcomes to observable values. The induced distribution over E is what we usually work with. |
| **PMF (discrete)** | Probability mass function: P(X=x) for each x. Must sum to 1. |
| **PDF (continuous)** | Probability density function: f(x) ≥ 0 with ∫ f(x) dx = 1. P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx. |
| **Expectation** | 𝔼[X] = Σ x P(X=x) (discrete) or ∫ x f(x) dx (continuous). The probability-weighted average outcome. |
| **Law of Large Numbers** | Sample averages of iid draws converge in probability to the true expectation as n → ∞. |
| **Variance** | Var(X) = 𝔼[(X − 𝔼[X])²] = 𝔼[X²] − 𝔼[X]². Measures spread around the mean. |

## Intuition: What Is a Probability Triple?

```{admonition} Coin-flip example
:class: tip
Ω = {H, T}.  Σ = {∅, {H}, {T}, {H,T}}.  P({H}) = P({T}) = ½.
The event space must be closed under complement and countable union — i.e., a σ-algebra. For most practical uses you can think of a random variable and its distribution as equivalent; the formal triple captures the rigorous foundations.
```

## Self-Check Questions

1. Verify the three axioms of a probability measure for a fair die.
2. If X ~ Uniform(0,1), compute 𝔼[X] and Var(X) from first principles.
3. Why must a PDF integrate to 1? What goes wrong if it doesn't?
4. What is the relationship between CDF and PDF?
5. A random variable maps outcomes to values — what does it mean for it to be "measurable"?

## Additional Resources

- [Harvard Stat 110 (Joe Blitzstein) — full course online](https://projects.iq.harvard.edu/stat110/home) — one of the best probability courses available.
- [Probability for Machine Learning (Brownlee)](https://machinelearningmastery.com/probability-for-machine-learning/) — applied intro; pairs well with the formal definitions.
- [StatQuest — Probability (YouTube)](https://www.youtube.com/c/joshstarmer) — short, clear videos on distributions and expectations.
- [Betancourt — Probability Theory for ML](https://betanalpha.github.io/assets/case_studies/probability_theory.html) — rigorous measure-theoretic treatment.
- Bishop, *PRML*, Ch. 1; Wasserman, *All of Statistics*, Chs. 1-3; Murphy, *PML*, Ch. 2.

> See also: [L3 lecture page](../lectures/lecture-03.md).
