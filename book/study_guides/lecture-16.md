# L16 Study Guide — Lab Day #3

> Last class before spring break. Lab chunks 2 (losses, labs 6-11) and 3 (data types, labs 12-16) are both in scope. No new lecture content. See the [Labs](../labs/intro.md) for full notebooks; this guide gives you the conceptual map of what each chunk teaches.

## Chunk 2 — ML Loss Types / Objectives

| Lab | Loss / Task | Probabilistic Model |
|---|---|---|
| **lab6 — Multiclass classification** | Categorical cross-entropy | Categorical / Multinomial; softmax output. |
| **lab7 — Regression** | MSE (default), MAE | Gaussian; Laplace. |
| **lab8 — Survival analysis** | Cox partial likelihood | Proportional-hazards model with right-censoring. |
| **lab9 — Probabilistic regression** | Gaussian NLL with predicted variance | Heteroscedastic Gaussian. Calibration becomes explicit. |
| **lab10 — Clustering** | Within-cluster sum of squares (k-means); GMM NLL | k-means; Gaussian mixture. |
| **lab11 — Dimensionality reduction** | PCA reconstruction error; t-SNE / UMAP objectives | Linear (PCA) vs. neighborhood-preserving (t-SNE/UMAP). |

## Chunk 3 — Data Types / Modalities

| Lab | Data Shape | Architectural Implication |
|---|---|---|
| **lab12 — Graph data** | Nodes + edges | Graph neural networks; message passing. |
| **lab13 — Ordinal sequences** | Tokens with order | RNN / transformer encoder. |
| **lab14 — Images** | 2D pixel grids | CNN with translation equivariance. |
| **lab15 — Time series** | Irregular timestamps + values | Time-series-specific losses, missingness handling. |
| **lab16 — Event streams (MEDS)** | Health event streams | Set-of-irregular-events transformer or chunked RNN. (Preview of L17-L18.) |

## Things to Practice

```{admonition} The orthogonality of model / loss / data
:class: tip
The same logistic-regression-style training loop adapts to multiclass, regression, survival — by changing the *loss*. The same architectural template adapts to images, sequences, graphs — by changing the *input encoding*. **Loss type and data type are independent ML axes; both matter.**
```

## Self-Check Questions

1. Why does survival analysis use Cox partial likelihood instead of just MSE on time-to-event? (Hint: censoring.)
2. A probabilistic regressor (lab 9) outputs both a mean and a variance. Why is this useful clinically? What's the calibration check?
3. PCA, t-SNE, and UMAP all reduce dimensions. What does each *preserve*? Which would you trust to claim "this 2D embedding shows the actual structure of the data"?
4. A whole-slide pathology image is 50,000 × 50,000 pixels. Why can't you run a CNN end-to-end on it, and what's the standard workaround?
5. MEDS-format event streams (lab 16) preserve event timestamps. Why is "discarding timestamps and tabularizing" a *real* loss, not just an inconvenience?

## Additional Resources

- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) — losses, dim reduction.
- [lifelines](https://lifelines.readthedocs.io/) — the standard Python tool for `lab8_survival_analysis`.
- [PyG (PyTorch Geometric)](https://pytorch-geometric.readthedocs.io/) — for `lab12_graph_data`.
- [MEDS schema specification (GitHub)](https://github.com/Medical-Event-Data-Standard/meds) — for `lab16`.
- [Géron, *Hands-On ML* — Chs. 14-16](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) — image / sequence / time-series chapters.

> See also: [L16 lecture page](../lectures/lecture-16.md).
