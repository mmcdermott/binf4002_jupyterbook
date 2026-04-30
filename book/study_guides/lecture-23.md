# L23 Study Guide — Population Health & Survival Analysis

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

## Key Terms

| Term | Definition |
|---|---|
| **Registry** | Disease- or condition-specific surveillance data (SEER for cancer, ACTION for stroke, CMS Medicare claims). Designed for surveillance, not research. |
| **Designed survey** | Sampled to be representative of a population (NHANES, BRFSS, NHIS). Smaller than registries but with much richer phenotyping. |
| **Biobank** | Volunteer-consented cohort with deep phenotyping (genotypes, imaging, labs, EHR linkage). UK Biobank, All of Us, FinnGen. **Subject to healthy-volunteer effect.** |
| **Healthy-volunteer effect** | Volunteers in biobanks / longitudinal studies are systematically healthier than the general population. Generalization implications. |
| **RCT (Randomized Clinical Trial)** | Gold standard for *causal* questions; weak external validity because trial-eligible populations are narrow. |
| **Real-world data (RWD)** | Blanket FDA term covering claims, EHR-derived datasets, registries, pragmatic-trial data. |
| **Censoring (right-)** | Patient is observed event-free up to time T but their status after T is unknown. The defining feature of survival analysis. |
| **Competing risks** | Patient experiences event B (e.g., dies of cancer) before they could experience event A (e.g., recurrence). Censored for A in a *non-random* way. |
| **Survival function S(t)** | P(T > t). Probability that the event has not occurred by time t. |
| **Hazard rate h(t)** | Instantaneous event rate at time t given survival to time t. |
| **Kaplan-Meier estimator** | Non-parametric estimate of S(t) from censored data. Easy to compute, easy to interpret. |
| **Log-rank test** | Test of equality of survival curves between groups. |
| **Cox proportional hazards** | h(t \| x) = h₀(t) exp(βᵀx). The classical regression model for survival. *Proportional* hazards is the assumption to test. |
| **DeepSurv / DeepHit** | Neural extensions: replace the linear predictor in Cox with an MLP (DeepSurv), or model competing risks directly (DeepHit). |
| **Simpson's paradox** | Aggregate trend reverses within subgroups. Forces a choice about aggregation. |

## Why EHR Alone Isn't Enough

```{admonition} Match the data source to the question
:class: tip
- "Does X cause Y?" → trial, or causal inference on observational data with strong assumptions.
- "How common is Z in this population?" → designed survey.
- "Who's at risk for W in the next year?" → EHR works.

**Mismatching question to data source is one of the most common errors in clinical ML papers.**
```

## Survival Analysis vs. Binary Classification

```{admonition} Many "predict 30-day mortality" papers should be predicting *time-to-mortality* with censoring
:class: warning
Forcing a binary outcome at an arbitrary horizon throws away information and creates artifacts: a patient censored at day 25 is treated identically to a patient alive at day 30. Survival analysis is the principled fix when timing matters. **Use Kaplan-Meier first, even before fitting Cox.**
```

## Self-Check Questions

1. UK Biobank participants are healthier than the general UK population. Walk through three downstream consequences for ML models trained on Biobank data.
2. A patient is censored at month 18 in a 24-month outcome study. What does censoring mean here? What's the difference between *uninformative* and *informative* censoring?
3. Cox proportional hazards assumes h(t | x) = h₀(t) exp(βᵀx). State the assumption being made and how you'd test it.
4. SEER, NHANES, and EHRs answer different kinds of questions. Match each to: "what is the lifetime risk of this cancer in this population?", "what fraction of US adults have hypertension?", "which of my hospital's patients will be readmitted?"
5. A propensity score is the probability of receiving treatment given covariates. Why is it the bridge from L23 to L24? What does it require?

## Additional Resources

- [Kaplan & Meier, "Nonparametric estimation from incomplete observations," *JASA* 53, 1958](https://www.jstor.org/stable/2281868).
- [Cox, "Regression Models and Life-Tables," *JRSS B* 34, 1972](https://www.jstor.org/stable/2985181).
- [Katzman et al., "DeepSurv," *BMC Med Res Methodol* 18, 2018](https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-018-0482-1).
- [Lee et al., "DeepHit," *AAAI* 2018](https://ojs.aaai.org/index.php/AAAI/article/view/11842).
- [Bycroft et al., "The UK Biobank resource," *Nature* 562, 2018](https://www.nature.com/articles/s41586-018-0579-z).
- [lifelines documentation](https://lifelines.readthedocs.io/) — the standard Python package; includes a great tutorial.
- [Coursera — *Survival Analysis in R for Public Health* (Imperial College)](https://www.coursera.org/learn/survival-analysis-r-public-health) — hands-on companion.

> See also: [L23 lecture page](../lectures/lecture-23.md). Companion notebook: [`nb23_pophealth.ipynb`](../lectures/nb-23-pophealth.ipynb).
