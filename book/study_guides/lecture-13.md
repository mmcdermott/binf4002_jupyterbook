# L13 Study Guide — Neural Networks: From Motivation to Practice

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

> This study guide consolidates the "Neural Networks supplementary lecture" content from the L7-10 study guide alongside the L13 calendar slot in this course.

## Key Terms

| Term | Definition |
|---|---|
| **Universal Approximation** | A sufficiently wide (or deep) neural network can approximate any continuous function to arbitrary precision. Justifies using NNs as a general-purpose function class. |
| **Layer** | The fundamental building block: h = σ(Wx + b). W ∈ ℝ^{d_out × d_in}, b ∈ ℝ^{d_out}, σ is a nonlinear activation. Parameter count: d_out·d_in + d_out. |
| **Activation Function** | The nonlinearity σ applied element-wise. Without it, composing layers collapses to a single linear map. ReLU, GELU, sigmoid, tanh are common. |
| **ReLU** | σ(z) = max(0, z). Default activation; simple, non-saturating, but can produce "dead neurons" (stuck at 0 for all inputs). |
| **GELU** | Gaussian Error Linear Unit. Smooth approximation of ReLU; preferred in transformers (BERT, GPT). |
| **Depth vs. Width** | Depth (more layers) is far more parameter-efficient than width (more neurons per layer) for high expressiveness in practice. |
| **Inductive Bias via Architecture** | FC/MLP: no structural prior. CNN: translation equivariance (locality). RNN: sequential ordering. Transformer: permutation equivariance with learned interactions. |
| **Xavier / Glorot Init** | Weight variance = 1/d_in (or 2/(d_in+d_out)). Designed for tanh/sigmoid. |
| **Kaiming / He Init** | Weight variance = 2/d_in. Designed for ReLU; accounts for ReLU zeroing half the neurons. |
| **Batch Normalization** | Normalizes layer inputs to zero mean and unit variance per mini-batch. Reduces internal covariate shift. |
| **Layer Normalization** | Normalizes across the feature dimension *per sample*. Preferred in transformers; works with variable sequence lengths. |
| **Residual Connection** | h_{ℓ+1} = h_ℓ + F(h_ℓ). "Skip" connections solve the degradation problem; create gradient highways; enable very deep networks (ResNet). |
| **Adam / AdamW** | Adaptive gradient optimizer with per-parameter first and second moment estimates. AdamW adds decoupled weight decay. Default for most DL; start at η = 10⁻³. |
| **Learning Rate Schedule** | Varies η during training. Warmup + cosine decay is the modern default. A constant LR violates Robbins–Monro convergence conditions. |
| **Gradient Clipping** | Caps gradient norms at a threshold (e.g., 1.0) to prevent destructive updates from gradient spikes. |
| **Gradient Accumulation** | Accumulate gradients over k micro-batches before updating, simulating a larger effective batch size when GPU memory is limited. |
| **Linear Scaling Rule** | When multiplying batch size by k, multiply LR by k (Goyal et al., 2017). Derived for SGD; breaks down for Adam at large batch sizes. |
| **Weight Decay / L2 Regularization** | Adds λ‖θ‖² to loss. Built into AdamW. Primary regularizer for most modern architectures. |
| **Dropout** | Randomly zeros neurons with probability p during training. Forces redundancy; reduces co-adaptation. p ∈ [0.1, 0.5]. |

## Why Neural Networks? Three Requirements

| Requirement | Why It Matters for Health ML |
|---|---|
| Arbitrarily expressive (universal) | Health data is high-D and nonlinear; no simple model class suffices. |
| Parametric (fixed-size θ) | Deployable in clinical systems; model size doesn't grow with the dataset. |
| Efficiently auto-differentiable | Scalable optimization via backprop; O(forward-pass) cost for gradients. |

## Architecture Encodes Assumptions (Inductive Bias)

| Layer Type | Inductive Bias | Health Modality | Rule of Thumb |
|---|---|---|---|
| **FC / MLP** | No structural prior | Tabular EHR, lab values | Baseline for structured data |
| **CNN** | Translation equivariance, locality | Medical images, ECG signals | First choice for images |
| **RNN / LSTM** | Sequential ordering | Clinical notes, time series | Use if order is crucial |
| **Transformer** | Permutation equivariant; learned interactions | Any; esp. notes, sequences | Fewest structural assumptions; default when unsure |

## Practical Optimization: The Full Toolkit

```{admonition} Training recipe
:class: tip
1. Choose architecture matching your data modality.
2. Initialize weights with Kaiming (ReLU) or Xavier (tanh/sigmoid).
3. Add BatchNorm (CNNs) or LayerNorm (Transformers).
4. Add residual connections if depth > 5-6.
5. Use AdamW optimizer with η = 10⁻³ as default.
6. Use cosine decay or linear-warmup + cosine-decay LR schedule.
7. Set gradient clipping to 1.0.
8. Monitor: loss, gradient norm, activation statistics, train/val gap.
9. Regularize with weight decay first; add dropout if still overfitting.
```

## Loss Functions and Their Probabilistic Interpretations

| Loss | Task | Probabilistic Interpretation |
|---|---|---|
| **Binary Cross-Entropy** | Binary classification | NLL of sigmoid output under Bernoulli model |
| **Categorical Cross-Entropy** | Multi-class | NLL of softmax output under Categorical model |
| **MSE** | Regression | NLL under Gaussian noise |
| **MAE** | Regression (robust to outliers) | NLL under Laplace noise |
| **Focal Loss** | Extreme class imbalance | Cross-entropy down-weighting easy examples |

## Self-Check Questions

1. Compute the output of a 2-layer MLP with ReLU on **x** = [1, 2, 3]ᵀ, W₁ = [[0.5, −1, 0.3], [0.2, 0.8, −0.4]], **b**₁ = [0.1, −0.2], W₂ = [[1, −1]], b₂ = [0]. Show each step.
2. Why does composing multiple linear layers without nonlinearities reduce to a single linear layer? Prove it for 2 layers.
3. Explain the vanishing gradient problem. Which activations cause it, and why does ReLU help?
4. Why does weight initialization matter? What goes wrong with all-zeros initialization?
5. A model trained on hospital A's chest X-rays has 95% accuracy but 70% on hospital B. You increase L2 regularization. Will this help? Why or why not?
6. The linear-scaling rule says to multiply LR by k when multiplying batch size by k. Under what conditions does this break down?

## Additional Resources

- [3Blue1Brown — Neural Networks (playlist)](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — best visual introduction to NN fundamentals.
- [Goodfellow et al., *Deep Learning* — Chs. 6-8](https://www.deeplearningbook.org/) — feedforward nets, training, regularization rigorously.
- [Karpathy — "Neural Networks: Zero to Hero" (YouTube playlist)](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) — builds backprop and a small transformer from scratch.
- [Karpathy — "A Recipe for Training Neural Networks" (blog)](http://karpathy.github.io/2019/04/25/recipe/) — practical debugging.
- [He et al., "Deep Residual Learning for Image Recognition" (2015)](https://arxiv.org/abs/1512.03385) — the ResNet paper.
- [Ioffe & Szegedy, "Batch Normalization" (2015)](https://arxiv.org/abs/1502.03167).
- [Loshchilov & Hutter, "AdamW" (2017)](https://arxiv.org/abs/1711.05101) — why weight decay should be decoupled from the adaptive update.
- [Smith, "A Disciplined Approach to Neural Network Hyper-Parameters" (2018)](https://arxiv.org/abs/1803.09820) — practical LR / batch tuning.

> See also: [L13 lecture page](../lectures/lecture-13.md). Companion notebook: [`nn_fundamentals_lab.ipynb`](../lectures/nb-13-nn-fundamentals.ipynb).
