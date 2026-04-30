# L24 Study Guide — Causality & Fairness

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

## Key Terms

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

## Prediction ≠ Intervention

```{admonition} The single most consequential confusion
:class: warning
**p(Y \| X) ≠ p(Y \| do(X))** in general. Observational ML answers the *prediction* question. It does not, by itself, license intervention claims. The whole point of causal DAGs and propensity scores is to bridge this gap *with explicit assumptions*.
```

## The Fairness Impossibility

```{admonition} Sufficiency vs. separation are mathematically incompatible
:class: warning
When base rates differ across groups (which they almost always do in health) and prediction is imperfect, you *cannot* simultaneously satisfy sufficiency (calibration within groups) and separation (equalized FPR/FNR). One must be prioritized. **Which one to prioritize is a value judgment, not a technical one.**
```

## Label Bias Is Invisible to Score-Only Fairness

```{admonition} Obermeyer in one sentence
:class: warning
A widely-used commercial risk-stratification algorithm under-served Black patients because it predicted *healthcare cost* as a proxy for *health need* — and Black patients had systematically lower costs *given the same need* due to access disparities. The bias was in the **label**, not the algorithm. Always ask: *what does the label measure?*
```

## Self-Check Questions

1. Walk through the three DAG patterns (chain, fork, collider). For each, when does *conditioning on the middle variable* help, and when does it hurt?
2. A propensity score lets you compare treatment groups in observational data *as if* they had been randomized. What assumption does that "as if" require, and what tools (e.g., E-values) check robustness to it?
3. Two physicians want a fair sepsis predictor. Physician A wants equal calibration across groups (sufficiency); Physician B wants equal FNR across groups (separation). Why can't you give them both?
4. Walk through the Obermeyer mechanism: what was the label, what was the target, why did the proxy gap produce racial harm, and how did the fix work?
5. Statistical parity, equalized odds, predictive parity: which of these does the Obermeyer algorithm *satisfy*? Which does it *violate*?

## Additional Resources

- [Pearl, Glymour & Jewell, *Causal Inference in Statistics: A Primer*](http://bayes.cs.ucla.edu/PRIMER/) — the friendliest intro; start here.
- [Hernán & Robins, *Causal Inference: What If* (free PDF)](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/) — the applied-epidemiology lens.
- [Pearl, *Causality* (2nd ed.)](http://bayes.cs.ucla.edu/BOOK-2K/) — the full book.
- [Obermeyer et al., "Dissecting racial bias in an algorithm used to manage the health of populations," *Science* 366, 2019](https://www.science.org/doi/10.1126/science.aax2342). **Required reading. Twice.**
- [Chouldechova, "Fair prediction with disparate impact" (2017)](https://arxiv.org/abs/1703.00056).
- [Kleinberg, Mullainathan, Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores," *ITCS* 2017](https://arxiv.org/abs/1609.05807).
- [Rajkomar et al., "Ensuring Fairness in ML to Advance Health Equity," *Ann Intern Med* 169, 2018](https://www.acpjournals.org/doi/10.7326/M18-1990).
- [Coursera — *A Crash Course in Causality* (Roy, Pittsburgh)](https://www.coursera.org/learn/crash-course-in-causality) — free hands-on companion.

> See also: [L24 lecture page](../lectures/lecture-24.md). Companion notebook: [`nb24_causality_fairness.ipynb`](../lectures/nb-24-causality-fairness.ipynb).
