# Lecture 16 — Lab Day #3 (last class before spring break)

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Mar 12, 2026 · Part 2 — Modern AI & lab work**

## What this class meeting was about

Third and final lab day of the semester, last class before spring break. By this point students had access to all three lab chunks:

- **Chunk 1: ML model types** (labs 0-5, released Sun Feb 22) — covered in lab days #1 and #2.
- **Chunk 2: ML loss types** (labs 6-11, released Mon Mar 2) — multiclass, regression, survival, probabilistic, clustering, dimensionality reduction.
- **Chunk 3: Data types** (labs 12-16, released Fri Mar 6) — graphs, sequences, images, time series, event streams.

Most students came in with chunk 1 finished or nearly so, working through chunks 2 and 3 in order. This lab day's folder includes labs 6-16 (the chunks that were *new* on this day; chunk 1 lives in `lecture-11-lab-day-1/labs/`).

The new labs in scope:

- **Chunk 2 — losses.**
  - `lab6_multiclass_classification` — going from binary to K-way; softmax + cross-entropy.
  - `lab7_regression` — squared error, regression metrics, prediction intervals.
  - `lab8_survival_analysis` — Cox proportional hazards as an NLL with censoring; preview of L23.
  - `lab9_probabilistic_regression` — predicting distributions, not just point estimates; calibration.
  - `lab10_clustering` — k-means, GMMs, the unsupervised side of L7's recipe.
  - `lab11_dimensionality_reduction` — PCA, t-SNE, UMAP; the representation question explicit.
- **Chunk 3 — data types.**
  - `lab12_graph_data` — graph neural networks, message passing, common pitfalls.
  - `lab13_ordinal_sequences` — sequence inputs, RNN/transformer architectures (preview of L14).
  - `lab14_images` — convolutional networks on images (preview of L21-L22).
  - `lab15_timeseries` — irregular sampling, missingness, time-series-specific losses.
  - `lab16_event_streams_MEDS` — health event streams in MEDS format (preview of L17-L18).

## Why this lab day matters for the course

Three roles for this slot:

**It bridges the foundations half and the health-data half.** The labs touch *every* data type that the modality lectures (L17-L22, L23-L27) build on. Wrestling with the generic versions before the clinical versions saves a lot of cognitive load later.

**It introduces survival analysis (lab 8) and event streams (lab 16) as warm-ups.** L23 and L17-L18 will go deep on these in clinical contexts; the labs give you the generic skeleton first, so the clinical version is "what's different about EHR" rather than "what's a Cox model."

**It demonstrates the loss / model / data-type orthogonality.** The same logistic-regression-style training loop adapts to multiclass, regression, survival — by changing the loss. The same architecture template adapts to images, sequences, graphs — by changing the input encoding. This orthogonality is the biggest single take-away of the lab program.

## What you should walk away with

- A mental table that crosses *loss type* (binary, multiclass, regression, survival, probabilistic) with *model type* (linear, tree, NN). Almost every cell is feasible; the ones that aren't are interesting.
- A working sense of when "image" / "sequence" / "graph" / "event stream" each *forces* a particular architectural choice and when it doesn't.
- First-hand experience with calibration on a probabilistic regressor (lab 9) — connecting back to L8.
- An intuition for survival analysis that L23 will formalize.
- Familiarity with the MEDS event-stream schema, which L17-L18 will build on.

## How this connects to the rest of the course

- **L17-L18** (EHR / claims) — `lab16_event_streams_MEDS` is the on-ramp.
- **L21-L22** (medical imaging) — `lab14_images` is the on-ramp.
- **L23** (population health, survival) — `lab8_survival_analysis` is the on-ramp.
- **L24** (causality, fairness) — `lab9_probabilistic_regression` and `lab11_dimensionality_reduction` provide the building blocks.
- **L25-L26** (DNA, proteins) — `lab12_graph_data` and `lab13_ordinal_sequences` provide the substrate.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Chunk 2 — ML Loss Types / Objectives

| Lab | Loss / Task | Probabilistic Model |
|---|---|---|
| **lab6 — Multiclass classification** | Categorical cross-entropy | Categorical / Multinomial; softmax output. |
| **lab7 — Regression** | MSE (default), MAE | Gaussian; Laplace. |
| **lab8 — Survival analysis** | Cox partial likelihood | Proportional-hazards model with right-censoring. |
| **lab9 — Probabilistic regression** | Gaussian NLL with predicted variance | Heteroscedastic Gaussian. Calibration becomes explicit. |
| **lab10 — Clustering** | Within-cluster sum of squares (k-means); GMM NLL | k-means; Gaussian mixture. |
| **lab11 — Dimensionality reduction** | PCA reconstruction error; t-SNE / UMAP objectives | Linear (PCA) vs. neighborhood-preserving (t-SNE/UMAP). |

### Chunk 3 — Data Types / Modalities

| Lab | Data Shape | Architectural Implication |
|---|---|---|
| **lab12 — Graph data** | Nodes + edges | Graph neural networks; message passing. |
| **lab13 — Ordinal sequences** | Tokens with order | RNN / transformer encoder. |
| **lab14 — Images** | 2D pixel grids | CNN with translation equivariance. |
| **lab15 — Time series** | Irregular timestamps + values | Time-series-specific losses, missingness handling. |
| **lab16 — Event streams (MEDS)** | Health event streams | Set-of-irregular-events transformer or chunked RNN. (Preview of L17-L18.) |

### Things to Practice

```{admonition} The orthogonality of model / loss / data
:class: tip
The same logistic-regression-style training loop adapts to multiclass, regression, survival — by changing the *loss*. The same architectural template adapts to images, sequences, graphs — by changing the *input encoding*. **Loss type and data type are independent ML axes; both matter.**
```

### Self-Check Questions

1. Why does survival analysis use Cox partial likelihood instead of just MSE on time-to-event? (Hint: censoring.)
2. A probabilistic regressor (lab 9) outputs both a mean and a variance. Why is this useful clinically? What's the calibration check?
3. PCA, t-SNE, and UMAP all reduce dimensions. What does each *preserve*? Which would you trust to claim "this 2D embedding shows the actual structure of the data"?
4. A whole-slide pathology image is 50,000 × 50,000 pixels. Why can't you run a CNN end-to-end on it, and what's the standard workaround?
5. MEDS-format event streams (lab 16) preserve event timestamps. Why is "discarding timestamps and tabularizing" a *real* loss, not just an inconvenience?

### Additional Resources

- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) — losses, dim reduction.
- [lifelines](https://lifelines.readthedocs.io/) — the standard Python tool for `lab8_survival_analysis`.
- [PyG (PyTorch Geometric)](https://pytorch-geometric.readthedocs.io/) — for `lab12_graph_data`.
- [MEDS schema specification (GitHub)](https://github.com/Medical-Event-Data-Standard/meds) — for `lab16`.
- [Géron, *Hands-On ML* — Chs. 14-16](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) — image / sequence / time-series chapters.
