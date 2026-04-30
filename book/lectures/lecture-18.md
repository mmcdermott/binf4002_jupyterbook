# Lecture 18 — Modeling over EHR and claims data

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

**Task misdefinition is the silent killer of clinical AI projects.** A team builds a 30-day-mortality model using a 90-day observation window. Sounds fine. But "30-day mortality" measured in claims data has a 1-3 month lag (claims arrive late), and the 90-day observation window includes information from after some patients' admission for the predicted outcome. Result: a model that "works" in retrospective evaluation and silently underperforms in deployment. Most published EHR ML papers have at least one task-definition issue worth flagging.

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

## Source files in this folder

- `lecture18_modeling_ehr_claims.pdf` — the slides as released to students. *The LaTeX source compiles to a 114-page PDF identical to this in content (verified).*
- `latex/lecture18_modeling_ehr_claims.tex`, `latex/curiosity_figure.png`, `latex/everyquery_fig.jpg` — the editable Beamer source plus the two figures it uses.
- *(No companion notebook for this lecture.)*

## To go deeper

- **Tang et al., "Democratizing EHR analyses with FIDDLE," _JAMIA_ 27, 2020.** The principled tabularization framework. Read once if you'll ever tabularize an EHR.
- **Choi et al., "Doctor AI: Predicting Clinical Events via Recurrent Neural Networks," _MLHC_ 2016.** The chunked-sequences-on-EHR canonical paper. Showed that RNNs on event streams can outperform tabularized baselines.
- **Rajkomar et al., "Scalable and accurate deep learning with electronic health records," _npj Digit Med_ 1, 2018.** The Google paper that became the template for modern EHR foundation-model claims.
- **McDermott et al., "Event Stream GPT: A Data Pre-processing and Modeling Library for Generative, Pre-trained Transformers over Continuous-time Sequences of Complex Events" (and current McDermott-lab work on EHR transformers).** The full event-stream representation in current research practice.
- **Lipton, Kale & Wetzel, "Modeling Missing Data in Clinical Time Series with RNNs," _MLHC_ 2016.** Treating missingness as informative.
- **Hyland et al., "Early prediction of circulatory failure in the intensive care unit using machine learning," _Nat Med_ 26, 2020.** A workflow-aligned EHR ML paper that gets the task definition right.

## Study tools

- [Study guide for L18](../study_guides/lecture-18.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
