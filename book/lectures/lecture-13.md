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

## Source files in this folder

- `nn_lecture.pdf` — the slides as released to students. *The LaTeX source compiles to a 95-page PDF identical to this in content (verified).*
- `latex/nn_lecture.tex` and `latex/figures/` — the editable Beamer source.
- `nn_fundamentals_lab.ipynb` — companion notebook with MNIST experiments showing each of the practical knobs in action.

## To go deeper

- **Goodfellow, Bengio, Courville, _Deep Learning_, Chs. 6-8.** The standard reference. Ch. 8 specifically on optimization.
- **Karpathy, "A Recipe for Training Neural Networks" (2019, blog).** The single most useful "what to do when your network won't train" document on the internet. Read once, re-read often.
- **He et al., "Delving Deep into Rectifiers" (Kaiming init), _ICCV_ 2015.** The init story that finally let us train very deep networks.
- **Ioffe & Szegedy, "Batch Normalization," _ICML_ 2015.** The normalization paper.
- **He et al., "Deep Residual Learning for Image Recognition," _CVPR_ 2016.** Residual connections.
- **Smith, "A Disciplined Approach to Neural Network Hyper-Parameters," arXiv:1803.09820.** Practical LR/batch tuning, with a mental model for what the optimizer is doing.
- **fast.ai, _Practical Deep Learning for Coders_ (free online course).** If you want a hands-on companion that builds intuition fast.

## Study tools

- [Study guide for L13](../study_guides/lecture-13.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
