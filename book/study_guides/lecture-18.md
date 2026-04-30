# L18 Study Guide — Modeling over EHR & Claims Data

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

## Key Terms

| Term | Definition |
|---|---|
| **Prediction time** | The instant from which features are computed and the future is unknown. |
| **Observation window** | Window *before* prediction time used to compute features. |
| **Prediction window** | Window *after* prediction time during which the outcome is predicted. |
| **Label window** | The time during which a label can in principle be observed. |
| **Action window** | The time during which an intervention can in principle be acted on. |
| **Censoring** | Patient drops out of data before the prediction window ends. Were they fine, admitted elsewhere, or did they die at home? You don't know. |
| **Competing risks** | Patient experiences event B before they could experience event A. They are censored for A in a *non-random* way. |
| **Tabularization** | Aggregate the observation window into a fixed-size feature vector (counts, means, last values). Loses order, timing, event-level detail. |
| **Chunked / Windowed sequences** | Bin the observation window into time intervals (hourly, daily); produce a regular sequence. RNNs / 1D-CNNs handle this. |
| **Event streams** | Keep events at their actual times with their actual codes/values. Transformer-style architectures handle this. |
| **Leakage** | Information from the prediction window contaminating the feature window — a constant hazard in EHR modeling. |
| **Workflow alignment** | The model's predictions must arrive *at the right time*, *with the right granularity*, and *for the right action* to be useful clinically. |

## Three Representation Families

| Representation | Pros | Cons | Typical Architecture |
|---|---|---|---|
| **Tabularized** | Every classical ML model works; interpretable | Loses order, timing, event detail | LR, RF, GBM |
| **Chunked sequences** | Buys back order; some timing | Bin-size choice creates artifacts | RNN, 1D-CNN |
| **Event streams** | Full fidelity (timing + order + values) | Hard to train; data-hungry | Transformer over events |

## Task Definition Is the Hard Part

```{admonition} "30-day mortality prediction" hides a lot
:class: warning
Specify:
- **Prediction time** (admission? 24h post-admission? at discharge?)
- **Observation window** (how far back? including this admission's labs?)
- **Prediction window** (calendar 30 days from prediction time? from discharge?)
- **Censoring rule** (lost-to-follow-up = alive? = unknown?)
- **Competing risks** (death from B vs. death from A modeled separately?)

Two papers studying the "same outcome" can produce incomparable models because their windows differ. Make every choice explicit.
```

## Self-Check Questions

1. A hospital wants a 24h-readmission model run at discharge. Define: prediction time, observation window, prediction window, label window, action window. What does each imply about feature computation?
2. Why is binary-classification-at-fixed-horizon often a worse choice than survival analysis when you actually care about *when* the event happens?
3. A team uses a 90-day observation window for a 30-day mortality task. Their AUROC is 0.95. Walk through the leakage modes you would suspect.
4. Tabularized vs. event-stream: for predicting sepsis from ICU data, which would you pick, and why?
5. Class imbalance is the rule, not the exception, in EHR ML. Name three handling strategies and one drawback of each.

## Additional Resources

- [Tang et al., "Democratizing EHR analyses with FIDDLE," *JAMIA* 27, 2020](https://academic.oup.com/jamia/article/27/12/1921/5905041) — principled tabularization.
- [Choi et al., "Doctor AI: Predicting Clinical Events via RNNs," *MLHC* 2016](https://arxiv.org/abs/1511.05942) — chunked-sequences template.
- [Rajkomar et al., "Scalable and accurate deep learning with EHRs," *npj Digit Med* 1, 2018](https://www.nature.com/articles/s41746-018-0029-1) — modern EHR-FM template.
- [Lipton, Kale & Wetzel, "Modeling Missing Data in Clinical Time Series with RNNs," *MLHC* 2016](https://arxiv.org/abs/1606.04130) — treating missingness as informative.
- [Hyland et al., "Early prediction of circulatory failure in the ICU," *Nat Med* 26, 2020](https://www.nature.com/articles/s41591-020-0789-4) — workflow-aligned EHR ML done right.
- McDermott-lab work on Event Stream GPT and the MEDS ecosystem.

> See also: [L18 lecture page](../lectures/lecture-18.md).
