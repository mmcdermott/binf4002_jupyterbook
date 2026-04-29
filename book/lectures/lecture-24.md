# Lecture 24 — Causality and fairness

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

## Source files in this folder

- `lec24_causality_fairness.pdf` — the slides as released to students.
- `latex/lec24_causality_fairness.tex` — editable Beamer source. *The .tex compiles to 55 pages matching the released PDF, but figures `fig1_bias_gallery.png` ... `fig6_threshold_adjustment.png` are not bundled — they're produced by running the companion notebook. Run it before recompiling.*
- `nb24_causality_fairness.ipynb` — companion notebook: DAG examples, propensity-score illustration, fairness-metric comparison, Chouldechova impossibility demo, and a partial replication of Obermeyer et al.

## To go deeper

- **Pearl, _Causality_ (2nd ed.), Cambridge University Press, 2009.** The book. Heavy.
- **Pearl, Glymour, Jewell, _Causal Inference in Statistics: A Primer_, 2016.** The friendlier intro. Read this first.
- **Hernán & Robins, _Causal Inference: What If_ (free PDF online).** The applied epidemiology lens. Excellent.
- **Obermeyer, Powers, Vogeli & Mullainathan, "Dissecting racial bias in an algorithm used to manage the health of populations," _Science_ 366, 2019.** Required reading. Twice.
- **Chouldechova, "Fair prediction with disparate impact: A study of bias in recidivism prediction instruments," _Big Data_ 5, 2017.** The impossibility paper.
- **Kleinberg, Mullainathan, Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores," _ITCS_ 2017.** The other impossibility paper.
- **Rajkomar et al., "Ensuring Fairness in Machine Learning to Advance Health Equity," _Ann Intern Med_ 169, 2018.** A clinical-AI-applied take.
- **Coursera _A Crash Course in Causality_ (Roy, U. Pittsburgh).** Free hands-on companion.
