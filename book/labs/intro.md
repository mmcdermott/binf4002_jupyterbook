# Labs

Seventeen Jupyter notebooks released across the semester in three chunks. Each lab is a self-contained exercise in a particular ML model type, loss type, or data type. The labs are designed to be run on Google Colab (no local install required) and were the substrate for three in-class lab days (L11, L12, L16).

The release schedule:

- **Chunk 1 — ML model types** (released **Sun Feb 22, 2026**, used for [Lab Day #1](../lectures/lecture-11.md) and [Lab Day #2](../lectures/lecture-12.md)).
- **Chunk 2 — ML loss types / objectives** (released **Mon Mar 2, 2026**, used in [Lab Day #3](../lectures/lecture-16.md)).
- **Chunk 3 — Data types / modalities** (released **Fri Mar 6, 2026**, used in [Lab Day #3](../lectures/lecture-16.md)).

Students worked the labs in order. Solution notebooks exist for chunk 1 (in `Labs/solutions/`) but were not the primary deliverable — the lab notebooks themselves are scaffolded with reflection questions and inline explanations.

The lab notebooks below are *the released student versions* (no solutions inline). Click any lab to open it; if you want to run it yourself, use the **launch button** at the top of the notebook page (Colab and Binder when configured).

## What each lab covers

### Chunk 1 — ML model types

| Lab | Topic | Connects to |
|---|---|---|
| [Lab 0](lab0_preprocessing.ipynb) | Preprocessing, EDA, missing data, scaling, train/val/test splits | Foundation for every other lab |
| [Lab 1](lab1_logistic_regression.ipynb) | Logistic regression on the breast-cancer dataset | L9 (binary-classification training) |
| [Lab 2](lab2_decision_trees.ipynb) | Decision trees; interpretability vs. overfitting | L10 (capacity / regularization) |
| [Lab 3](lab3_knn.ipynb) | k-Nearest Neighbors; bias-variance via k | L9 (kNN consistency) |
| [Lab 4](lab4_ensemble_methods.ipynb) | Random forests and gradient boosting | L10 (variance reduction) |
| [Lab 5](lab5_neural_networks.ipynb) | First feedforward neural network | L13 (NN lecture) |

### Chunk 2 — ML loss types / objectives

| Lab | Topic | Connects to |
|---|---|---|
| [Lab 6](lab6_multiclass_classification.ipynb) | Going from binary to K-way; softmax + cross-entropy | L4 (information theory), L7 (NLL) |
| [Lab 7](lab7_regression.ipynb) | Squared error, regression metrics, prediction intervals | L7 (Gaussian NLL) |
| [Lab 8](lab8_survival_analysis.ipynb) | Cox proportional hazards as NLL with censoring | L23 (population health, survival) |
| [Lab 9](lab9_probabilistic_regression.ipynb) | Predicting distributions, calibration | L8 (calibration vs. discrimination) |
| [Lab 10](lab10_clustering.ipynb) | k-means, GMMs, the unsupervised side of L7 | L7 (mixture models) |
| [Lab 11](lab11_dimensionality_reduction.ipynb) | PCA, t-SNE, UMAP | L2 (eigenanalysis), L25 (population PCA) |

### Chunk 3 — Data types / modalities

| Lab | Topic | Connects to |
|---|---|---|
| [Lab 12](lab12_graph_data.ipynb) | Graph neural networks, message passing | L26-L27 (molecules, biological AI) |
| [Lab 13](lab13_ordinal_sequences.ipynb) | Sequence inputs; RNN/transformer architectures | L14 (LLMs) |
| [Lab 14](lab14_images.ipynb) | Convolutional networks on images | L21-L22 (medical imaging) |
| [Lab 15](lab15_timeseries.ipynb) | Irregular sampling, missingness, time-series losses | L17-L18 (EHR data) |
| [Lab 16](lab16_event_streams_MEDS.ipynb) | Health event streams in MEDS format | L17-L18 (EHR data) |

## How to run the labs

Each lab notebook has Colab-friendly boilerplate at the top and was designed to run on free Colab GPUs/TPUs. To run a lab:

1. Open the notebook page in this book (links above).
2. Click the launch icon at the top right of the notebook page (when this book is hosted on a public GitHub repo, the icon takes you to Colab or Binder with the notebook pre-loaded).
3. Run cells in order. Most labs save a pickled output that later labs may read.

If you're reading this book locally, you can also open any lab directly in Jupyter / VS Code from `Labs/notebooks/`.
