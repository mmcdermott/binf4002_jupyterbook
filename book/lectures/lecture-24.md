# Lecture 24 — Causality and fairness

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Apr 16, 2026 · Part 4 — Population, causality, fairness**

## What this lecture is about

This is the lecture that finally formalizes the warning that has been threading through the whole course since L1: **prediction and intervention are different questions, and conflating them is one of the most consequential mistakes in clinical AI.** The lecture has two interlocking halves — causality and fairness — that turn out to be the same problem from two angles.

**Half 1: Causality.**

- **Causal DAGs.** A directed acyclic graph encoding qualitative causal assumptions about a data-generating process. Nodes are variables; edges are direct causal effects.
- **The do-operator.** Pearl's notation for an *intervention* — what would happen if we forced X = x rather than observed X = x. p(Y | X = x) and p(Y | do(X = x)) are different distributions in general; in observational data we only get the former.
- **Three DAG patterns.**
  - **Chain (X → Z → Y).** Z mediates X's effect on Y. Conditioning on Z blocks the path.
  - **Fork (X ← Z → Y).** Z is a common cause; without conditioning on Z, X and Y appear correlated even with no direct causal link.
  - **Collider (X → Z ← Y).** Z is a common effect. Conditioning on Z *creates* spurious correlation between X and Y. (Berkson's paradox from L17 is a collider-conditioning story.)
- **Bias gallery.** Selection bias, confounding bias, measurement error, reverse causation, ascertainment bias, immortal-time bias. Each has a DAG signature.
- **Propensity scores.** The probability of receiving treatment given covariates: e(x) = p(T = 1 | X = x). Used for matching, weighting (IPTW), and stratification. Lets you compare treatment groups in observational data *as if* they had been randomized — provided you've measured all the right confounders.
- **Causal inference challenges.** No-unmeasured-confounders is an *assumption*, not a fact. Sensitivity analysis (E-values, etc.) tells you how robust your conclusion is to a hidden confounder.

**Half 2: Fairness.**

- **Fairness definitions.** Statistical parity, equalized odds, predictive parity, calibration-within-group, individual fairness. They sound similar; they aren't equivalent.
- **Sufficiency vs. separation.** Two compact families of fairness criteria.
  - **Sufficiency** (calibration within groups): given the score, the outcome distribution is the same across groups.
  - **Separation** (equalized odds / FPR / FNR balance): given the outcome, the score distribution is the same across groups.
- **The Chouldechova / Kleinberg impossibility.** If base rates differ across groups (which they almost always do in health), you *cannot* simultaneously satisfy sufficiency and separation, except in trivial cases. A "fair" model is forced to choose which kind of fairness it satisfies.
- **The Obermeyer case study.** A widely-used commercial risk-stratification algorithm under-served Black patients because it predicted *healthcare cost* as a proxy for *health need* — and Black patients had systematically lower costs *given the same need* due to access disparities. The bias wasn't in the algorithm; it was in the *label*. Read the paper. Twice.
- **Causal fairness.** Use the DAG to ask: where in the data-generating process is the unfairness coming from? This is what unifies the two halves of the lecture — fairness analysis without causal reasoning is incomplete.
- **Subgroup evaluation.** Compute every metric (AUROC, calibration, PPV, FNR) per subgroup. Differences are diagnostic.
- **Mitigation.** Three loci: data (fix labels, fix sampling), model (constrain training to satisfy a fairness criterion), threshold (group-specific thresholds). Each has trade-offs.

## Why it matters

Three reasons this lecture sits where it does in the course:

**Most "AI fairness" papers treat fairness as a pure technical problem — pick metric, optimize against it, done.** That misses the entire mechanism story. The Obermeyer algorithm satisfied calibration; it failed because the *label* (cost) was a biased proxy for *what we cared about* (need). No technical fairness criterion would have flagged it. You need to look at the DAG.

**Causality and fairness are the same problem.** Both ask: *given observed data, what's actually going on in the world?* Both require explicit assumptions you can't get from the data alone. Both reward DAG-thinking and punish "just optimize the metric" thinking.

**The impossibility result is real and matters for deployment.** A system can be calibrated within groups *or* equalize FPR/FNR across groups, but not both. Which one is the right choice is a *value* judgment, not a technical one. ML practitioners need to be ready to have that conversation with stakeholders.

## Things you should walk away believing

- Prediction and intervention are different questions. p(Y|X) ≠ p(Y|do(X)) in general.
- DAGs are explicit assumptions. They are wrong sometimes; their explicitness lets you debug.
- Conditioning on a collider creates spurious correlation. This is *the* most common DAG mistake.
- Propensity scores are useful, not magic. They depend on having measured all confounders.
- Sufficiency and separation are different fairness families. Neither is universally "right."
- The Chouldechova / Kleinberg impossibility is real; choose which fairness you want.
- Label bias (Obermeyer) is invisible to fairness criteria that only look at scores. Always ask: *what does the label measure*?
- Mitigation has trade-offs. Group-specific thresholds can be the right answer; they can also be illegal.
- Subgroup evaluation is non-optional. Every metric, per subgroup, every time.

## How this connects to the rest of the course

- L9's flu-vaccine motivation finally gets formalized here.
- L17-L18 (EHR data) and L23 (population health) provide the substrate where these issues bite.
- L8's calibration is the "sufficiency" axis; L8's separation-into-FPR/FNR is the "separation" axis. The fairness impossibility applies to L8's metrics.
- L25 (PRS transferability) is a fairness-across-ancestry story.
- L15 (foundation models) inherits all of these issues at scale.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Causal DAG** | Directed Acyclic Graph encoding *qualitative causal assumptions*. Nodes are variables, edges are direct causal effects. Wrong sometimes; their explicitness lets you debug. |
| **do-operator** | Pearl's notation for an *intervention*: p(Y \| do(X = x)) ≠ p(Y \| X = x) in general. Observational data give the latter; we usually want the former. |
| **Chain (X → Z → Y)** | Z mediates X's effect on Y. *Conditioning on Z blocks the path.* |
| **Fork (X ← Z → Y)** | Z is a common cause; without conditioning on Z, X and Y appear correlated even with no direct link. |
| **Collider (X → Z ← Y)** | Z is a common effect. **Conditioning on Z creates spurious correlation between X and Y.** (Berkson's paradox.) |
| **Confounder** | A common cause of treatment and outcome. Failure to adjust for confounders biases observed associations. |
| **Selection bias** | Bias from non-random sampling (who's in the data depends on the variables you're studying). |
| **Propensity score** | e(x) = P(T = 1 \| X = x). Probability of receiving treatment given covariates. Used for matching, weighting (IPTW), or stratification. |
| **No unmeasured confounders** | The assumption that all confounders are measured. **An assumption, not a fact.** Sensitivity analysis (E-values) tells you how robust your conclusion is to a hidden confounder. |
| **Statistical parity** | P(Ŷ = 1 \| A = a) equal across groups. (Demographic parity.) |
| **Equalized odds (separation)** | P(Ŷ = 1 \| Y = y, A = a) = P(Ŷ = 1 \| Y = y) for all y, a. |
| **Predictive parity (sufficiency)** | P(Y = 1 \| Ŷ = p, A = a) = P(Y = 1 \| Ŷ = p) for all p, a. (Calibration within group.) |
| **Chouldechova / Kleinberg impossibility** | Sufficiency and separation cannot both hold for non-degenerate classifiers when base rates differ across groups. |
| **Obermeyer et al. (2019)** | Canonical case study: a "fair-looking" risk algorithm under-served Black patients because the *label* (cost) was a biased proxy for the *target* (need). |
| **Causal fairness** | Use a DAG to ask *where in the data-generating process the unfairness comes from*. Unifies the technical fairness criteria with mechanism analysis. |

### Prediction ≠ Intervention

```{admonition} The single most consequential confusion
:class: warning
**p(Y \| X) ≠ p(Y \| do(X))** in general. Observational ML answers the *prediction* question. It does not, by itself, license intervention claims. The whole point of causal DAGs and propensity scores is to bridge this gap *with explicit assumptions*.
```

### The Fairness Impossibility

```{admonition} Sufficiency vs. separation are mathematically incompatible
:class: warning
When base rates differ across groups (which they almost always do in health) and prediction is imperfect, you *cannot* simultaneously satisfy sufficiency (calibration within groups) and separation (equalized FPR/FNR). One must be prioritized. **Which one to prioritize is a value judgment, not a technical one.**
```

### Label Bias Is Invisible to Score-Only Fairness

```{admonition} Obermeyer in one sentence
:class: warning
A widely-used commercial risk-stratification algorithm under-served Black patients because it predicted *healthcare cost* as a proxy for *health need* — and Black patients had systematically lower costs *given the same need* due to access disparities. The bias was in the **label**, not the algorithm. Always ask: *what does the label measure?*
```

### Self-Check Questions

1. Walk through the three DAG patterns (chain, fork, collider). For each, when does *conditioning on the middle variable* help, and when does it hurt?
2. A propensity score lets you compare treatment groups in observational data *as if* they had been randomized. What assumption does that "as if" require, and what tools (e.g., E-values) check robustness to it?
3. Two physicians want a fair sepsis predictor. Physician A wants equal calibration across groups (sufficiency); Physician B wants equal FNR across groups (separation). Why can't you give them both?
4. Walk through the Obermeyer mechanism: what was the label, what was the target, why did the proxy gap produce racial harm, and how did the fix work?
5. Statistical parity, equalized odds, predictive parity: which of these does the Obermeyer algorithm *satisfy*? Which does it *violate*?

### Additional Resources

- [Pearl, Glymour & Jewell, *Causal Inference in Statistics: A Primer*](http://bayes.cs.ucla.edu/PRIMER/) — the friendliest intro; start here.
- [Hernán & Robins, *Causal Inference: What If* (free PDF)](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/) — the applied-epidemiology lens.
- [Pearl, *Causality* (2nd ed.)](http://bayes.cs.ucla.edu/BOOK-2K/) — the full book.
- [Obermeyer et al., "Dissecting racial bias in an algorithm used to manage the health of populations," *Science* 366, 2019](https://www.science.org/doi/10.1126/science.aax2342). **Required reading. Twice.**
- [Chouldechova, "Fair prediction with disparate impact" (2017)](https://arxiv.org/abs/1703.00056).
- [Kleinberg, Mullainathan, Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores," *ITCS* 2017](https://arxiv.org/abs/1609.05807).
- [Rajkomar et al., "Ensuring Fairness in ML to Advance Health Equity," *Ann Intern Med* 169, 2018](https://www.acpjournals.org/doi/10.7326/M18-1990).
- [Coursera — *A Crash Course in Causality* (Roy, Pittsburgh)](https://www.coursera.org/learn/crash-course-in-causality) — free hands-on companion.
