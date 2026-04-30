# Lecture 4 — Conditioning, Bayes' rule, and information theory

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

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

**Information theory underwrites almost every loss function the course will use.** Cross-entropy is KL divergence between an empirical and a model distribution. Negative log-likelihood is exactly entropy when the data is the truth. The "perplexity" you'll see in L14 (LLMs) is exp(cross-entropy). Once you see this, the loss-function landscape of ML stops feeling like a zoo and starts feeling like one idea (KL) appearing in many costumes.

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

## Source files in this folder

- `Lecture 4 - information_theory.pptx` — editable Google Slides / PowerPoint source.
- `Lecture 4.pdf` — the only PDF shown to students (41 pages, exported from the PowerPoint source). An earlier 63-page Beamer/LaTeX variant existed but was not used; it is preserved inside `archive_materials.tar.xz` for reference.

## To go deeper

- **MacKay, _Information Theory, Inference, and Learning Algorithms_ (free PDF), Chs. 2-4 and 24.** The friendliest book on entropy / KL / mutual information that also takes Bayesian inference seriously.
- **Cover & Thomas, _Elements of Information Theory_, Ch. 2.** The standard, terse reference for the information-theoretic primitives.
- **Bishop, _Pattern Recognition and Machine Learning_, Chs. 1-2.** Bayesian inference and information theory in ML notation.
- **Murphy, _Probabilistic Machine Learning: An Introduction_, Chs. 2-3.** Modern ML-oriented treatment.

## Study tools

- [Study guide for L04](../study_guides/lecture-04.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
