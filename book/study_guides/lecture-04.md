# L4 Study Guide — Probability & Information Theory

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

## Key Terms

| Term | Definition |
|---|---|
| **Joint Distribution** | P(X, Y): the probability distribution over pairs of outcomes. Captures all dependence structure between X and Y. |
| **Marginal Distribution** | P(X) = ∫ P(X,Y) dY (cont.) or Σᵧ P(X,Y=y) (disc.). Obtained by integrating/summing out the other variable. |
| **Conditional Distribution** | P(Y \| X) = P(X,Y) / P(X). The renormalized joint for a fixed value of X. |
| **Statistical Independence** | X ⊥ Y iff P(X,Y) = P(X) P(Y); equivalently P(Y \| X) = P(Y). |
| **Bayes' Rule** | P(Y \| X) = P(X \| Y) P(Y) / P(X).   Posterior = Prior × Likelihood / Evidence. |
| **Prior P(Y)** | The marginal distribution of Y before observing X. **Not** a subjective "belief" — it is the marginal of the joint. |
| **Likelihood P(X \| Y)** | Probability of observing X given Y is true. With the prior, determines the posterior. |
| **Information Content** | I(x) = −log P(x). Rare events carry more information. Units: bits (log₂) or nats (ln). |
| **Entropy** | H(X) = −Σ P(x) log P(x) = 𝔼[−log P(X)]. Average information content; measures uncertainty. |
| **KL Divergence** | D_KL(P‖Q) = Σ P(x) log (P(x)/Q(x)). Non-symmetric measure of how P differs from Q; always ≥ 0. |
| **Mutual Information** | I(X;Y) = D_KL(P(X,Y) ‖ P(X)P(Y)). How much knowing Y reduces uncertainty about X. |

## Key Insight: The Prior Is Not a "Belief"

```{admonition} Caution on Bayesian interpretation
:class: warning
A common misconception is that the prior P(Y) reflects a subjective belief or guess. Formally, it is the marginal distribution of Y in the joint P(X,Y). Bayesian vs. frequentist debates are philosophically interesting but should not distract from the mathematics: **Bayes' rule is a theorem, not a philosophy.**
```

## Clinical Application: Bayes in Diagnosis

```{admonition} Why base rates matter
:class: important
Bayes' rule reveals why a highly-accurate test can still yield mostly false positives when the disease is rare. If prevalence is 1%, a test with 95% sensitivity and 90% specificity has positive predictive value of only ≈ 8.7%. **Model accuracy metrics must always be interpreted in the context of class prevalence.**
```

## Self-Check Questions

1. Derive the marginal P(X) from the joint P(X,Y) for a 2×2 discrete example.
2. Derive Bayes' rule directly from the definition of conditional probability.
3. Compute the entropy of a fair coin. What distribution over a 2-outcome space *maximizes* entropy?
4. Why is KL divergence not a metric? What metric property does it fail?
5. A diagnostic test has sensitivity 0.95 and specificity 0.90; disease prevalence is 1%. Using Bayes' rule, what is P(disease | positive test)?

## Additional Resources

- [3Blue1Brown — Bayes' Theorem Visualized (YouTube)](https://www.youtube.com/watch?v=HZGCoVF3YvM) — superb visual derivation of Bayes' rule.
- [Cover & Thomas — *Elements of Information Theory*](https://www.wiley.com/en-us/Elements+of+Information+Theory-p-9780471241959) — standard textbook reference.
- [MacKay — *Information Theory, Inference, and Learning Algorithms* (free PDF)](http://www.inference.org.uk/itila/book.html) — the friendliest book that takes both information theory and Bayesian inference seriously.
- [Arbital — Bayes' Rule (interactive)](https://arbital.com/p/bayes_rule/) — progressive intro to Bayesian reasoning.
- [Seeing Theory (Brown University)](https://seeing-theory.brown.edu/) — beautiful interactive visualizations for probability concepts.

> See also: [L4 lecture page](../lectures/lecture-04.md).
