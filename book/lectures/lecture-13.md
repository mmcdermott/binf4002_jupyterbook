# Lecture 13 — Neural networks: from motivation to practice

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Mar 3, 2026 · Part 2 — Modern AI & lab work**

## What this lecture is about

A neural network is, at its core, the same recipe from L7: pick a function class, define a loss, optimize. What's new is that the function class is now massively expressive (a deep stack of linear maps interleaved with nonlinearities), the optimizer needs *care* (initialization, normalization, learning rate, gradient handling), and the inductive bias is encoded in the *architecture* rather than in a hand-crafted feature set.

The lecture is built in two halves.

**The first half is conceptual:** what is a neural network, why does it work, and how does it relate to the linear / kernel / tree models from labs 0-5?

- **Motivation.** Linear models can't approximate arbitrary functions. Trees and forests can but generalize poorly with high-dimensional structured inputs (images, sequences). Kernels can but scale badly. Neural networks combine *expressiveness* (universal approximation), *parametric deployment* (fixed-size model regardless of training-set size), and *automatic differentiation* (any differentiable loss + architecture is trainable).
- **Anatomy.** Layers, activations, depth, parameters. A layer is "apply a linear map, then a non-linearity." Depth lets you compose features into higher-level features.
- **Architecture as inductive bias.** This is the central conceptual move. CNNs encode "translation-equivariance and locality matter" — the right bias for natural images. RNNs encode "sequential structure matters." Transformers encode "any-to-any token interaction matters but with attention as the routing mechanism." The architecture is *not* incidental; it is the prior.
- **Loss matching task type.** Squared error → Gaussian (regression). Cross-entropy → categorical (classification). Hinge → margin-based. NLL → arbitrary parametric. The choice is informed by L7's framework.

**The second half is practical:** how do you actually train one of these without it failing silently?

- **Initialization.** Bad init → vanishing or exploding gradients → silent failure. Kaiming / Xavier / orthogonal are not interchangeable.
- **Normalization.** BatchNorm, LayerNorm, GroupNorm. They stabilize the optimization landscape.
- **Residual connections.** They let gradients flow through deep stacks; they also change what gets learned.
- **Optimizers.** SGD with momentum, Adam, AdamW. Each makes different assumptions about the loss surface.
- **Learning rate schedules.** Constant, step, cosine, warmup. Tied tightly to batch size.
- **Gradient clipping and accumulation.** When gradients spike (RNNs, large LRs); when memory limits batch size.
- **Monitoring.** Loss curves, gradient norms, weight statistics, activation distributions. A healthy training run *looks* a particular way.
- **Regularization.** Weight decay, dropout, early stopping, augmentation. Each implies a different prior.

The companion notebook `nn_fundamentals_lab.ipynb` runs MNIST experiments where you can see each of these knobs change something visible.

## Why it matters

Three reasons this lecture is the hinge of the course:

**Almost every model in Parts 3-5 is a neural network.** Clinical NLP (L20), medical imaging (L22), survival models (L23), protein language models (L27) — they are all variations on this template. If you internalize the architecture-as-inductive-bias idea here, the rest of the course becomes "what's the right inductive bias for *this* modality."

**Training mechanics are the model.** Two NNs with the same architecture trained with different learning-rate schedules will end up at different solutions. This is not a footnote; it is one of the central facts of modern ML and a reason "reproducibility crisis" exists. You need to know the optimizer is part of the model so that when you read a paper, you know which knobs to ask about.

**Monitoring is non-optional.** Expressive function classes can fit anything *including* noise — they fail silently in a way that simpler models don't. The L10 inductive-bias / generalization story has its practical face here: you have to *watch* the training run, you can't just check the final loss.

## Things you should walk away believing

- Universal approximation makes the function class powerful; the *optimizer* and *architecture* together decide what you actually learn.
- Architecture choice is a prior. Pick it for the data modality; don't default to "what worked on MNIST."
- The training pipeline (init, norm, optimizer, LR, schedule, batch, clipping, monitoring, regularization) is the model. Don't blame "training instability" — diagnose which piece broke.
- Smaller models are easier to train but encode weaker priors. Bigger models with careful inductive bias usually win once you can afford them.
- Always have a sanity baseline (linear or shallow NN) and a non-trivial loss curve in your peripheral vision while training.

## How this connects to the rest of the course

- L14 (LLMs) is the largest-scale instance of this lecture: a transformer is a stack of attention + MLP blocks, optimized with the recipe above.
- L15 (foundation models) is L14 abstracted: pre-train once, adapt to many tasks.
- L20 (clinical NLP), L22 (imaging), L25-L27 (biological AI) are domain-specific instantiations of the same recipe with different inductive biases.
- L24 (fairness) returns to "the optimizer's bias decides which fair-or-unfair solution it converges to."

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

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

### Why Neural Networks? Three Requirements

| Requirement | Why It Matters for Health ML |
|---|---|
| Arbitrarily expressive (universal) | Health data is high-D and nonlinear; no simple model class suffices. |
| Parametric (fixed-size θ) | Deployable in clinical systems; model size doesn't grow with the dataset. |
| Efficiently auto-differentiable | Scalable optimization via backprop; O(forward-pass) cost for gradients. |

### Architecture Encodes Assumptions (Inductive Bias)

| Layer Type | Inductive Bias | Health Modality | Rule of Thumb |
|---|---|---|---|
| **FC / MLP** | No structural prior | Tabular EHR, lab values | Baseline for structured data |
| **CNN** | Translation equivariance, locality | Medical images, ECG signals | First choice for images |
| **RNN / LSTM** | Sequential ordering | Clinical notes, time series | Use if order is crucial |
| **Transformer** | Permutation equivariant; learned interactions | Any; esp. notes, sequences | Fewest structural assumptions; default when unsure |

### Practical Optimization: The Full Toolkit

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

### Loss Functions and Their Probabilistic Interpretations

| Loss | Task | Probabilistic Interpretation |
|---|---|---|
| **Binary Cross-Entropy** | Binary classification | NLL of sigmoid output under Bernoulli model |
| **Categorical Cross-Entropy** | Multi-class | NLL of softmax output under Categorical model |
| **MSE** | Regression | NLL under Gaussian noise |
| **MAE** | Regression (robust to outliers) | NLL under Laplace noise |
| **Focal Loss** | Extreme class imbalance | Cross-entropy down-weighting easy examples |

### Self-Check Questions

1. Compute the output of a 2-layer MLP with ReLU on **x** = [1, 2, 3]ᵀ, W₁ = [[0.5, −1, 0.3], [0.2, 0.8, −0.4]], **b**₁ = [0.1, −0.2], W₂ = [[1, −1]], b₂ = [0]. Show each step.
2. Why does composing multiple linear layers without nonlinearities reduce to a single linear layer? Prove it for 2 layers.
3. Explain the vanishing gradient problem. Which activations cause it, and why does ReLU help?
4. Why does weight initialization matter? What goes wrong with all-zeros initialization?
5. A model trained on hospital A's chest X-rays has 95% accuracy but 70% on hospital B. You increase L2 regularization. Will this help? Why or why not?
6. The linear-scaling rule says to multiply LR by k when multiplying batch size by k. Under what conditions does this break down?

### Additional Resources

- [3Blue1Brown — Neural Networks (playlist)](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — best visual introduction to NN fundamentals.
- [Goodfellow et al., *Deep Learning* — Chs. 6-8](https://www.deeplearningbook.org/) — feedforward nets, training, regularization rigorously.
- [Karpathy — "Neural Networks: Zero to Hero" (YouTube playlist)](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) — builds backprop and a small transformer from scratch.
- [Karpathy — "A Recipe for Training Neural Networks" (blog)](http://karpathy.github.io/2019/04/25/recipe/) — practical debugging.
- [He et al., "Deep Residual Learning for Image Recognition" (2015)](https://arxiv.org/abs/1512.03385) — the ResNet paper.
- [Ioffe & Szegedy, "Batch Normalization" (2015)](https://arxiv.org/abs/1502.03167).
- [Loshchilov & Hutter, "AdamW" (2017)](https://arxiv.org/abs/1711.05101) — why weight decay should be decoupled from the adaptive update.
- [Smith, "A Disciplined Approach to Neural Network Hyper-Parameters" (2018)](https://arxiv.org/abs/1803.09820) — practical LR / batch tuning.
