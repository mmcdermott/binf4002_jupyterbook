# Lecture 23 — Population health data and survival analysis

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Apr 14, 2026 · Part 4 — Population, causality, fairness**

## What this lecture is about

L17-L22 lived inside the EHR + clinical text + medical imaging triangle — what happens *during* care delivery. This lecture broadens the lens. Health questions often need data sources that *aren't* EHRs: registries, designed surveys, clinical trials, biobanks. And once you broaden the data, you need a tool that EHRs let you fudge: **survival analysis**, the ML/statistical framework for time-to-event outcomes with censoring.

The lecture has two halves.

**Half 1: Population health data sources.** A taxonomy.

- **Registries** (e.g., SEER for cancer, ACTION for stroke, CMS Medicare claims for elderly populations). Designed for surveillance, not research; complete on the dimensions they care about; biased toward what's reported.
- **Designed population surveys** (NHANES, BRFSS, NHIS). Sampled to be representative. Smaller than registries but with much richer phenotyping.
- **Biobanks** (UK Biobank, All of Us, FinnGen). Volunteers, consented, deeply phenotyped (genotypes, imaging, lab values, EHR linkage). Suffer the **healthy-volunteer effect** — biobank participants are systematically healthier than the general population.
- **Randomized clinical trials.** The gold standard for *causal* questions; generalize poorly because trial-eligible populations are narrow.
- **EHRs.** The lens we have spent six lectures inside; comprehensive but byproduct-shaped.
- **Real-world data.** A blanket term covering claims, EHR-derived datasets, registries, pragmatic-trial data. The new FDA frame.

We then look at *Simpson's paradox* in real data — an effect that points one direction in the population and the opposite direction within every subgroup. The classical Berkeley-admissions example, then real health-data examples (NHANES). Simpson's paradox is what *forces* you to pick a level of aggregation, and that choice is a modeling decision.

**Half 2: Survival analysis.** When the outcome of interest is *time to an event* (death, recurrence, progression, discharge), and some patients are *censored* (you don't observe the event because the study ended, they dropped out, they died of something else), classification and regression are no longer enough.

- **Censoring.** The distinguishing feature. Right-censoring (most common) means we know the patient was event-free up to time T but we don't know after that.
- **Competing risks.** A patient dies of cause B before they could die of cause A. This is *not* random censoring; it is structural.
- **Kaplan-Meier estimator.** A non-parametric estimator of the survival function S(t) = P(time-to-event > t). Easy to compute, easy to interpret, robust. Read by stratifying into subgroups and overlaying curves.
- **Cox proportional hazards.** The classical regression model for survival. Models the *hazard rate* as h(t|x) = h₀(t) exp(βᵀx). The "proportional hazards" assumption is the crucial caveat — it can fail, and you should test it.
- **Modern survival models.** DeepSurv (Cox + neural network), DeepHit (neural network for competing risks), survival forests. Extend Cox without breaking it.
- **Propensity-score preview.** A taste of what L24 will do formally with causal inference: when you compare two treatment groups in observational data, you can't just compute the difference in survival curves — you have to weight or match by propensity to treat.

## Why it matters

Three reasons this lecture matters more than its place in the syllabus suggests:

**The right data source depends on the question.** "Does X cause Y?" needs a trial, or causal inference on observational data with strong assumptions. "How common is Z in this population?" needs a designed survey. "Who's at risk for W in the next year?" can use EHR data. Mismatching question to data source is one of the most common errors in clinical ML papers.

**Binary classification can hide survival structure.** Many published "predict 30-day mortality" papers should be predicting *time-to-mortality* with censoring. Forcing a binary outcome at an arbitrary horizon throws away information and creates artifacts (patients censored at day 25 are treated the same as patients alive at day 30). Survival analysis is the principled fix.

**Healthy-volunteer effect, Simpson's paradox, and selection are not edge cases.** They are the *modal* failure modes for population-health analyses. UK Biobank participants are systematically healthier. NHANES misses non-English-speaking populations. SEER misses non-cancer patients. Every conclusion from these data sources is conditional on whose data are in them.

## Things you should walk away believing

- Data source determines what question you can answer. Pick the source for the question, not the model for the source.
- Healthy-volunteer effect is real, measurable, and biases biobank-based generalizations toward "healthier population."
- Simpson's paradox forces a choice about aggregation. The "correct" aggregation depends on the question.
- Censoring and competing risks are structural, not accidental. Survival analysis is what handles them.
- Kaplan-Meier is the *first* analysis you do for any time-to-event outcome. Even if you'll fit Cox later.
- Cox is interpretable but assumes proportional hazards. Test the assumption. Modern alternatives (DeepSurv, DeepHit) relax it at the cost of interpretability.
- Comparing treatment arms in observational data without propensity adjustment is a strong implicit assumption — the kind L24 will dissect.

## How this connects to the rest of the course

- L17-L18 set up the EHR-as-byproduct claim; L23 says "and here's what you reach for when you need more."
- L24 (next lecture) takes the propensity-score preview and turns it into the full causal-inference / fairness framework.
- L7's NLL framing covers Cox: the partial likelihood is just an NLL, and DeepSurv replaces the linear predictor with a neural net.
- L25 (DNA, genetics) makes heavy use of biobank data; the healthy-volunteer effect propagates into PRS transferability.
- L8's calibration story extends to survival models: a calibrated 1-year survival prediction needs different evaluation than a calibrated binary outcome.

## Source files in this folder

- `lecture23.pdf` — the slides as released to students. *The LaTeX source compiles to a 68-page PDF identical to this in content (verified).*
- `latex/lecture23.tex` and `latex/figures/` — editable Beamer source.
- `nb23_pophealth.ipynb` — companion notebook: NHANES missingness, Simpson's paradox demo, Kaplan-Meier on real data, Cox forest plots, DeepSurv comparison, and the propensity-score preview.

## To go deeper

- **Kaplan & Meier, "Nonparametric estimation from incomplete observations," _JASA_ 53, 1958.** The original. Surprisingly readable.
- **Cox, "Regression Models and Life-Tables," _JRSS B_ 34, 1972.** The Cox-model paper. Read for the proportional-hazards assumption.
- **Katzman et al., "DeepSurv: personalized treatment recommender system using a Cox proportional hazards deep neural network," _BMC Med Res Methodol_ 18, 2018.**
- **Lee et al., "DeepHit: A Deep Learning Approach to Survival Analysis With Competing Risks," _AAAI_ 2018.**
- **Bycroft et al., "The UK Biobank resource with deep phenotyping and genomic data," _Nature_ 562, 2018.** The dataset that makes biobank-based ML possible (and biased).
- **NHANES analytic guidelines (CDC).** Required reading if you'll touch NHANES.
- **SEER documentation (NCI).** Required for cancer-registry work.
- **Coursera _Survival Analysis in R for Public Health_ (Imperial College).** Hands-on companion course.

## Study tools

- [Study guide for L23](../study_guides/lecture-23.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
