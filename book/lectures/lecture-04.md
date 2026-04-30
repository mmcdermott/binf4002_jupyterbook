# Lecture 4 — Conditioning, Bayes' rule, and information theory

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Jan 29, 2026 · Part 1 — Foundations · §1.1 Mathematical preliminaries**

## What this lecture is about

This lecture is about three closely-linked moves: how to get from a joint distribution to marginal and conditional distributions; what Bayes' rule is *really* doing (it's just a rearrangement, not magic); and how information theory gives us a way to measure uncertainty, surprise, and divergence between distributions.

We move from the law of large numbers and expectation to:

- **Marginalization.** Sum (or integrate) a joint distribution over the variable you don't want.
- **Conditioning.** Take a slice of the joint and renormalize. Conditioning is *not* filtering; it changes the distribution itself.
- **Independence and dependence.** Read off from whether the joint factorizes.
- **Bayes' rule.** A statement about a joint distribution rewritten two ways. Prior × likelihood ÷ evidence = posterior.
- **Information theory.** Entropy, KL divergence, mutual information — the tools that turn "uncertainty" into something you can write a loss against.

The paradox flagged is **St. Petersburg**, which is a stress-test for whether expectation is the right summary of a distribution at all.

## Why it matters

Two reasons this material is more than mathematical hygiene:

**Bayes' rule is the engine of every diagnostic conversation in clinical medicine.** When prevalence is 0.1% and a test has 95% sensitivity and 95% specificity, the positive predictive value is around 1.9%. That's not a curiosity — it is the entire reason "alert fatigue" is a measurable clinical phenomenon (which we'll return to in L8 and L10). If your audience for an ML system is clinicians, you need to feel Bayes-rule arithmetic in your bones, because the system's outputs will be *interpreted* through it.

**Information theory underwrites almost every loss function the course will use.** Cross-entropy decomposes as H(p, q) = H(p) + KL(p‖q): it equals the entropy of the data distribution plus the KL divergence between data and model. Because H(p) does not depend on the model, *minimizing* cross-entropy is equivalent to minimizing KL — but they are not identical objects. Negative log-likelihood averaged over a sample is a sample-based estimator of cross-entropy (it equals entropy only in the degenerate case where the model matches the truth exactly). The "perplexity" you'll see in L14 (LLMs) is exp(cross-entropy). Once you see this, the loss-function landscape of ML stops feeling like a zoo and starts feeling like one idea (KL) appearing in many costumes.

## Things you should walk away believing

- Conditional probability is renormalization, not filtering. ℙ(A|B) tells you about a different distribution than ℙ(A).
- Bayes' rule is just ℙ(A|B) ℙ(B) = ℙ(A,B) = ℙ(B|A) ℙ(A) rewritten. The "magic" is the rearrangement plus the willingness to call one of the conditionals "prior."
- Independence ⇔ joint factorizes. This is the same fact dressed up in different vocabulary across the rest of the course.
- Entropy H(X) measures expected surprise; KL(p‖q) measures how surprising q is when p is the truth; they are *not symmetric* and that asymmetry matters in ML losses.
- A "low PPV at low prevalence" is not a failure of the test — it is Bayes' rule working correctly.

## How this connects to the rest of the course

- L6's "expected loss over the data-generating distribution" is built on conditioning.
- L7 (probabilistic modeling) frames supervised learning as maximum likelihood — i.e., minimizing a KL-shaped object.
- L8 (binary-classification evaluation) reuses Bayes' rule to turn a confusion matrix into clinical claims.
- L14 (LLMs) is literally entropy minimization over next tokens.
- L17-L18 (EHR data) and L24 (causal inference) lean on conditioning constantly: "given the patient was *observed*, what does the distribution of their lab values look like?"
- L28 (recap) returns to PPV-vs.-prevalence as a deployment lens.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

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

### Key Insight: The Prior Is Not a "Belief"

```{admonition} Caution on Bayesian interpretation
:class: warning
A common misconception is that the prior P(Y) reflects a subjective belief or guess. Formally, it is the marginal distribution of Y in the joint P(X,Y). Bayesian vs. frequentist debates are philosophically interesting but should not distract from the mathematics: **Bayes' rule is a theorem, not a philosophy.**
```

### Clinical Application: Bayes in Diagnosis

```{admonition} Why base rates matter
:class: important
Bayes' rule reveals why a highly-accurate test can still yield mostly false positives when the disease is rare. If prevalence is 1%, a test with 95% sensitivity and 90% specificity has positive predictive value of only ≈ 8.7%. **Model accuracy metrics must always be interpreted in the context of class prevalence.**
```

### Self-Check Questions

1. Derive the marginal P(X) from the joint P(X,Y) for a 2×2 discrete example.
2. Derive Bayes' rule directly from the definition of conditional probability.
3. Compute the entropy of a fair coin. What distribution over a 2-outcome space *maximizes* entropy?
4. Why is KL divergence not a metric? What metric property does it fail?
5. A diagnostic test has sensitivity 0.95 and specificity 0.90; disease prevalence is 1%. Using Bayes' rule, what is P(disease | positive test)?

### Additional Resources

- [3Blue1Brown — Bayes' Theorem Visualized (YouTube)](https://www.youtube.com/watch?v=HZGCoVF3YvM) — superb visual derivation of Bayes' rule.
- [Cover & Thomas — *Elements of Information Theory*](https://www.wiley.com/en-us/Elements+of+Information+Theory-p-9780471241959) — standard textbook reference.
- [MacKay — *Information Theory, Inference, and Learning Algorithms* (free PDF)](http://www.inference.org.uk/itila/book.html) — the friendliest book that takes both information theory and Bayesian inference seriously.
- [Arbital — Bayes' Rule (interactive)](https://arbital.com/p/bayes_rule/) — progressive intro to Bayesian reasoning.
- [Seeing Theory (Brown University)](https://seeing-theory.brown.edu/) — beautiful interactive visualizations for probability concepts.
