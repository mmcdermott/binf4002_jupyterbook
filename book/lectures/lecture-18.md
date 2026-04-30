# Lecture 18 — Modeling over EHR and claims data

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Mar 26, 2026 · Part 3 — Health data modalities · §3.1 EHR & claims**

## What this lecture is about

L17 told you what EHR/claims data are and how their generation breaks "iid samples from a population." This lecture asks the modeling question: **given those pathologies, what choices do you make when training a predictor?**

We deliberately keep the prediction objective to *binary classification* throughout the lecture. That isolation is a teaching choice — it lets us focus on representation and task definition without confounding them with loss-function complexity. The lecture argues that even keeping the loss "simple," the modeling problem is rich.

The lecture is built around three threads.

**Thread 1: Task definition.** A binary-classification task on EHR data is not "did the patient have outcome Y." It is a much more specific object:

- **Prediction time.** The instant from which features are computed and the future is "unknown."
- **Observation window.** The window before prediction time used to compute features.
- **Prediction window.** The window after prediction time during which the outcome is predicted.
- **Label window** vs. **action window.** The time during which a label can in principle be observed, vs. the time during which an intervention can in principle be acted on.
- **Censoring.** A patient drops out of the data before the prediction window ends. Were they fine, were they admitted elsewhere, did they die at home? You don't know.
- **Competing risks.** A patient dies of cause B before they could have outcome A. They are censored for A but in a way that is *not* random.

Every "EHR-based 30-day mortality predictor" is making a specific decision about every one of these. Two papers studying the same outcome can produce incomparable models because their windows differ.

**Thread 2: Representation.** Three families of representations for irregularly-sampled health event streams:

- **Tabularization.** Aggregate the observation window into a fixed-size feature vector (counts, means, last values). Every classical ML model works on this. You lose order, timing, and event-level detail.
- **Chunked / windowed sequences.** Bin the observation window into time intervals (hourly, daily) and produce a regular sequence. RNNs and 1D-CNNs handle this. You buy back order at the cost of binning artifacts.
- **Event streams.** Keep the events at their actual times, with their actual codes and values. Transformer-style architectures handle this. You buy back full fidelity at the cost of model complexity and a much harder training problem.

This is the same orthogonality-of-representation that L13 hinted at, applied to a specific domain.

**Thread 3: Modeling consequences.** Once you have a task and a representation, the rest of the pipeline (loss, optimizer, evaluation) inherits choices:

- Class imbalance is the default, not the exception.
- Metrics need to match the workflow: an alert-based system has very different success criteria than a triage tool.
- Leakage modes are subtle (computing a "feature" from a window that includes the label, for instance).
- Survival analysis is often the principled generalization of the binary task — but introducing it before the modality lecture would have buried the data-side issues.

The paradox flagged: implicit in the lecture is that **binary classification on EHR data is not the simple choice.** It is a choice that hides a lot of decisions.

## Why it matters

Three reasons this lecture is the make-or-break for clinical ML modeling:

**Task misdefinition is the silent killer of clinical AI projects.** A team builds a 30-day-mortality model using a 90-day observation window. Sounds fine. But three subtle leakage paths can break it: (a) "30-day mortality" measured in claims data has a 1-3 month lag (claims arrive late), so labels available retrospectively were not available at prediction time; (b) some EHR codes get back-dated by billing — a code "observed at" day -5 actually became visible at day +20; (c) for patients with a *prior* admission, a 90-day look-back on the new admission may overlap the *previous* admission's outcome window, leaking that outcome into the features. Result: a model that "works" retrospectively and silently underperforms in deployment. Most published EHR ML papers have at least one task-definition issue worth flagging.

**Representation drives what the model can possibly learn.** If you tabularize, the model can never learn from event order. If you bin into hours, the model can never see sub-hour patterns. Choosing the representation is choosing what's *expressible*. Every modeling claim is conditional on representation.

**Workflow alignment is what makes the model useful.** A perfect model that produces predictions 12 hours after the action window has closed is useless. A worse model whose predictions arrive *in time* and *with the right granularity* gets adopted.

## Things you should walk away believing

- "Binary classification on EHR" hides observation, prediction, label, and action windows; censoring; and competing risks. Make every one of those explicit.
- Representation is a modeling decision. Different representations can express different patterns.
- Tabularized → chunked → event-stream is a complexity / capacity / data-cost tradeoff, not a strict hierarchy.
- Class imbalance, leakage, and workflow misalignment are the three most common silent failures.
- Survival analysis (L23) is often the right generalization. Use it when timing matters and you can afford the modeling complexity.
- The right metric is the one that matches the clinical decision being made, not the one with the highest reported value.

## How this connects to the rest of the course

- L17 set up the data-side problems; L18 turns them into modeling decisions.
- L23 generalizes binary classification to time-to-event with censoring (Cox, modern survival models).
- L24 (causality, fairness) re-examines task definition under intervention vs. prediction.
- L15 (foundation models) — the EHR autoregressive model framing is a "foundation model over event streams" claim.
- L28 (recap) returns to "the model is never separate from the task" with the EHR pipeline as the primary example.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

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

### Three Representation Families

| Representation | Pros | Cons | Typical Architecture |
|---|---|---|---|
| **Tabularized** | Every classical ML model works; interpretable | Loses order, timing, event detail | LR, RF, GBM |
| **Chunked sequences** | Buys back order; some timing | Bin-size choice creates artifacts | RNN, 1D-CNN |
| **Event streams** | Full fidelity (timing + order + values) | Hard to train; data-hungry | Transformer over events |

### Task Definition Is the Hard Part

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

### Self-Check Questions

1. A hospital wants a 24h-readmission model run at discharge. Define: prediction time, observation window, prediction window, label window, action window. What does each imply about feature computation?
2. Why is binary-classification-at-fixed-horizon often a worse choice than survival analysis when you actually care about *when* the event happens?
3. A team uses a 90-day observation window for a 30-day mortality task. Their AUROC is 0.95. Walk through the leakage modes you would suspect.
4. Tabularized vs. event-stream: for predicting sepsis from ICU data, which would you pick, and why?
5. Class imbalance is the rule, not the exception, in EHR ML. Name three handling strategies and one drawback of each.

### Additional Resources

- [Tang et al., "Democratizing EHR analyses with FIDDLE," *JAMIA* 27, 2020](https://academic.oup.com/jamia/article/27/12/1921/5905041) — principled tabularization.
- [Choi et al., "Doctor AI: Predicting Clinical Events via RNNs," *MLHC* 2016](https://arxiv.org/abs/1511.05942) — chunked-sequences template.
- [Rajkomar et al., "Scalable and accurate deep learning with EHRs," *npj Digit Med* 1, 2018](https://www.nature.com/articles/s41746-018-0029-1) — modern EHR-FM template.
- [Lipton, Kale & Wetzel, "Modeling Missing Data in Clinical Time Series with RNNs," *MLHC* 2016](https://arxiv.org/abs/1606.04130) — treating missingness as informative.
- [Hyland et al., "Early prediction of circulatory failure in the ICU," *Nat Med* 26, 2020](https://www.nature.com/articles/s41591-020-0789-4) — workflow-aligned EHR ML done right.
- McDermott-lab work on Event Stream GPT and the MEDS ecosystem.
