# Part 4 — Population, Causality, Fairness

**Lectures 23-24**

## What this part is about

Part 4 lifts the lens beyond "what happens in a single hospital's EHR / imaging system" to the population scale, and then formalizes a warning that has been threading through the whole course since L1: **prediction and intervention are different questions, and conflating them is one of the most consequential mistakes in clinical AI.**

Two lectures:

- **L23 — Population health & survival analysis** broadens the data lens to designed surveys (NHANES), cancer registries (SEER), biobanks (UK Biobank, All of Us), and clinical trials, then introduces survival analysis as the principled framework for time-to-event outcomes with censoring (Kaplan-Meier, Cox, DeepSurv, DeepHit).
- **L24 — Causality & fairness** finally writes down the prediction-vs.-intervention distinction with causal DAGs, propensity scores, and fairness criteria. The Chouldechova / Kleinberg impossibility says that two natural-sounding fairness metrics (sufficiency vs. separation) cannot both be satisfied when base rates differ — which they almost always do in health. Obermeyer et al. (2019) is the canonical case study: a fair-looking algorithm that under-served Black patients because the *label* (cost) was a biased proxy for the *target* (need).

## Goals for this part

- Map a clinical or research question to the right data source (registry, survey, biobank, trial, EHR), and identify the selection biases each carries.
- Read a Kaplan-Meier curve; interpret a Cox forest plot; recognize when binary classification at a fixed horizon is hiding survival structure.
- Read a causal DAG; distinguish chain / fork / collider; reason about when conditioning helps and when it hurts.
- Apply propensity-score weighting / matching / stratification in observational comparisons.
- State and apply the canonical fairness criteria (sufficiency vs. separation, equalized odds, calibration-within-group); explain why they're mutually incompatible at unequal base rates.
- Audit an ML pipeline for label bias (à la Obermeyer): does the label measure what we actually care about, or a proxy that disadvantages some group?

## Key takeaways for this part

- The right data source depends on the question. No source is universally best.
- Censoring and competing risks are structural, not accidental. Survival analysis is what handles them principally.
- p(Y|X) ≠ p(Y|do(X)) in general. Prediction models do not, by themselves, license intervention claims.
- Sufficiency and separation are different fairness families; they are mathematically incompatible under unequal base rates.
- Label bias is invisible to fairness criteria that only look at scores. Always ask: *what does the label measure?*

## Lectures in this part

- [L23 — Population health & survival analysis](../lectures/lecture-23.md)
- [L24 — Causality & fairness](../lectures/lecture-24.md)

## External resources for this part

**Survival analysis (L23)**

- Kaplan & Meier, "Nonparametric estimation from incomplete observations," *JASA* 53, 1958. Original; surprisingly readable.
- Cox, "Regression Models and Life-Tables," *JRSS B* 34, 1972.
- Katzman et al., "DeepSurv," *BMC Med Res Methodol* 18, 2018.
- Lee et al., "DeepHit," *AAAI* 2018.
- Bycroft et al., "The UK Biobank resource with deep phenotyping and genomic data," *Nature* 562, 2018.
- NHANES analytic guidelines (CDC) and SEER documentation (NCI).
- Coursera, *Survival Analysis in R for Public Health* (Imperial College).

**Causality & fairness (L24)**

- Pearl, Glymour & Jewell, *Causal Inference in Statistics: A Primer*, 2016. Readable intro; start here.
- Hernán & Robins, *Causal Inference: What If* (free PDF online). The applied-epidemiology lens.
- Pearl, *Causality* (2nd ed.), 2009. The full book; harder.
- Obermeyer, Powers, Vogeli & Mullainathan, "Dissecting racial bias in an algorithm used to manage the health of populations," *Science* 366, 2019. **Required reading. Twice.**
- Chouldechova, "Fair prediction with disparate impact: A study of bias in recidivism prediction instruments," *Big Data* 5, 2017.
- Kleinberg, Mullainathan, Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores," *ITCS* 2017.
- Rajkomar et al., "Ensuring Fairness in Machine Learning to Advance Health Equity," *Ann Intern Med* 169, 2018.
- Coursera, *A Crash Course in Causality* (Roy, U. Pittsburgh) — free, hands-on companion.
