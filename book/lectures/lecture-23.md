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
- **Competing risks.** A patient dies of cause B before they could die of cause A. This *violates the independent-censoring assumption* that Kaplan-Meier and standard Cox both rely on — the censoring time depends on the failure mechanism, so it is **informative censoring**. The standard remedies are cause-specific hazards or Fine-Gray subdistribution models.
- **Kaplan-Meier estimator.** A non-parametric estimator of the survival function S(t) = P(time-to-event > t). Easy to compute, easy to interpret, robust. Read by stratifying into subgroups and overlaying curves.
- **Cox proportional hazards.** The classical regression model for survival. Models the *hazard rate* as h(t|x) = h₀(t) exp(βᵀx). The "proportional hazards" assumption is the crucial caveat — it can fail, and you should test it.
- **Modern survival models.** Three different ways of relaxing Cox's assumptions: **DeepSurv** is a Cox extension proper (replaces the linear predictor βᵀx with a neural network, keeps the proportional-hazards form); **DeepHit** is *not* a Cox extension — it directly models the discrete-time joint distribution over event types and times, designed to handle competing risks; **random survival forests** (Ishwaran et al.) are a non-parametric tree-based method with survival-specific split criteria, also not a Cox extension.
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
- Censoring is the defining structural feature; competing risks make censoring *informative* and require special handling. Survival analysis is what handles both.
- Kaplan-Meier is the *first* analysis you do for any time-to-event outcome. Even if you'll fit Cox later.
- Cox is interpretable but assumes proportional hazards. Test the assumption. DeepSurv extends Cox; DeepHit and random survival forests are different approaches entirely, each relaxing different Cox assumptions at the cost of interpretability.
- Comparing treatment arms in observational data is making an *unconfoundedness* assumption (treatment is as-good-as-randomized given covariates). Propensity adjustment doesn't create unconfoundedness — it is one tool that uses it. L24 dissects this.

## How this connects to the rest of the course

- L17-L18 set up the EHR-as-byproduct claim; L23 says "and here's what you reach for when you need more."
- L24 (next lecture) takes the propensity-score preview and turns it into the full causal-inference / fairness framework.
- L7's NLL framing covers Cox: the partial likelihood is just an NLL, and DeepSurv replaces the linear predictor with a neural net.
- L25 (DNA, genetics) makes heavy use of biobank data; the healthy-volunteer effect propagates into PRS transferability.
- L8's calibration story extends to survival models: a calibrated 1-year survival prediction needs different evaluation than a calibrated binary outcome.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Registry** | Disease- or condition-specific surveillance data (SEER for cancer, ACTION for stroke, CMS Medicare claims). Designed for surveillance, not research. |
| **Designed survey** | Sampled to be representative of a population (NHANES, BRFSS, NHIS). Smaller than registries but with much richer phenotyping. |
| **Biobank** | Volunteer-consented cohort with deep phenotyping (genotypes, imaging, labs, EHR linkage). UK Biobank, All of Us, FinnGen. **Subject to healthy-volunteer effect.** |
| **Healthy-volunteer effect** | Volunteers in biobanks / longitudinal studies are systematically healthier than the general population. Generalization implications. |
| **RCT (Randomized Clinical Trial)** | Gold standard for *causal* questions; weak external validity because trial-eligible populations are narrow. |
| **Real-world data (RWD)** | Blanket FDA term covering claims, EHR-derived datasets, registries, pragmatic-trial data. |
| **Censoring (right-)** | Patient is observed event-free up to time T but their status after T is unknown. The defining feature of survival analysis. |
| **Competing risks** | Patient experiences event B (e.g., dies of cancer) before they could experience event A (e.g., recurrence). Causes **informative censoring** — violates the independent-censoring assumption. Handled by cause-specific hazards or Fine-Gray subdistribution models. |
| **Survival function S(t)** | P(T > t). Probability that the event has not occurred by time t. |
| **Hazard rate h(t)** | Instantaneous event rate at time t given survival to time t. |
| **Kaplan-Meier estimator** | Non-parametric estimate of S(t) from censored data. Easy to compute, easy to interpret. |
| **Log-rank test** | Test of equality of survival curves between groups. |
| **Cox proportional hazards** | h(t \| x) = h₀(t) exp(βᵀx). The classical regression model for survival. *Proportional* hazards is the assumption to test. |
| **DeepSurv** | Cox extension: replaces the linear predictor βᵀx with a neural network; keeps proportional hazards. |
| **DeepHit** | *Not* a Cox extension — directly models the discrete-time joint distribution over event types and times; built for competing risks. |
| **Random Survival Forests** | Non-parametric tree-based method with survival-specific split criteria (Ishwaran et al.); not a Cox extension. |
| **Simpson's paradox** | Aggregate trend reverses within subgroups. Forces a choice about aggregation. |

### Why EHR Alone Isn't Enough

```{admonition} Match the data source to the question
:class: tip
- "Does X cause Y?" → trial, or causal inference on observational data with strong assumptions.
- "How common is Z in this population?" → designed survey.
- "Who's at risk for W in the next year?" → EHR works.

**Mismatching question to data source is one of the most common errors in clinical ML papers.**
```

### Survival Analysis vs. Binary Classification

```{admonition} Many "predict 30-day mortality" papers should be predicting *time-to-mortality* with censoring
:class: warning
Forcing a binary outcome at an arbitrary horizon throws away information and creates artifacts: a patient censored at day 25 is treated identically to a patient alive at day 30. Survival analysis is the principled fix when timing matters. **Use Kaplan-Meier first, even before fitting Cox.**
```

### Self-Check Questions

1. UK Biobank participants are healthier than the general UK population. Walk through three downstream consequences for ML models trained on Biobank data.
2. A patient is censored at month 18 in a 24-month outcome study. What does censoring mean here? What's the difference between *uninformative* and *informative* censoring?
3. Cox proportional hazards assumes h(t | x) = h₀(t) exp(βᵀx). State the assumption being made and how you'd test it.
4. SEER, NHANES, and EHRs answer different kinds of questions. Match each to: "what is the lifetime risk of this cancer in this population?", "what fraction of US adults have hypertension?", "which of my hospital's patients will be readmitted?"
5. A propensity score is the probability of receiving treatment given covariates. Why is it the bridge from L23 to L24? What does it require?

### Additional Resources

- [Kaplan & Meier, "Nonparametric estimation from incomplete observations," *JASA* 53, 1958](https://www.jstor.org/stable/2281868).
- [Cox, "Regression Models and Life-Tables," *JRSS B* 34, 1972](https://www.jstor.org/stable/2985181).
- [Katzman et al., "DeepSurv," *BMC Med Res Methodol* 18, 2018](https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-018-0482-1).
- [Lee et al., "DeepHit," *AAAI* 2018](https://ojs.aaai.org/index.php/AAAI/article/view/11842).
- [Bycroft et al., "The UK Biobank resource," *Nature* 562, 2018](https://www.nature.com/articles/s41586-018-0579-z).
- [lifelines documentation](https://lifelines.readthedocs.io/) — the standard Python package; includes a great tutorial.
- [Coursera — *Survival Analysis in R for Public Health* (Imperial College)](https://www.coursera.org/learn/survival-analysis-r-public-health) — hands-on companion.
