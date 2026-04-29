# Part 2 — Modern AI & Lab Work

**Lectures 11-16**

## What this part is about

Part 2 is the bridge between the formal foundations of Part 1 and the clinical-AI material in Part 3. It introduces three ideas — neural networks, large language models, and foundation models — that *use* the foundations and *power* almost every model in the second half of the course. It also includes three in-class lab days for hands-on practice with the lab notebooks.

The calendar arc is interleaved: lab → lab → NN → LLMs → FMs → lab. The lab days are not an afterthought; they're where students wrestle with the orthogonality of *model type*, *loss type*, and *data type* on actual datasets, which is what makes the modality lectures of Part 3 land.

The three lecture lectures in this part:

- **L13 — Neural networks** generalizes the optimization arc of Part 1 to expressive parametric function classes. Architecture as inductive bias; init / normalization / residuals / optimizers / monitoring as the model's "training mechanics" rather than implementation trivia.
- **L14 — Large language models** instantiates next-token prediction at scale via transformer attention. Same formal recipe as L7 (data → parametric model → NLL → optimize), but with the function class being a transformer and the objective being the language-modeling loss.
- **L15 — Foundation models** abstracts what L14 is doing: a model that takes (input *x*, task *α*) as input and is trained to handle a *distribution* of tasks rather than a single one. Provides a principled lens for critiquing "foundation model" claims in the rest of the course.

## Goals for this part

- Read a deep neural network as a stack of linear maps interleaved with nonlinearities, with architecture encoding inductive bias.
- Diagnose training failures: vanishing/exploding gradients, saturated activations, miscalibrated learning rate, batch-size pathologies.
- State the language-modeling objective; explain why attention beats n-grams; critique fluent-but-ungrounded LLM output.
- Critique a "foundation model" claim by asking *what input domain* and *what task distribution* it covers.
- Comfortably reach for a particular model / loss / data type combo from labs 0-16 when given a clinical ML problem statement.

## Key takeaways for this part

- A neural network is the optimization arc of Part 1, scaled up via differentiable programming. The training mechanics *are* the model.
- LLMs train on a single simple objective but exhibit broad task behavior through scale and prompting. Fluency ≠ understanding.
- "Foundation model over what?" is the load-bearing question. Total data efficiency and labeled data efficiency are different things.
- Loss type and data type are independent ML axes. Both matter.

## Lectures and labs in this part

- [L11 — Lab Day #1](../lectures/lecture-11.md) (chunk 1: ML model types — labs 0-5)
- [L12 — Lab Day #2](../lectures/lecture-12.md) (continued chunk 1)
- [L13 — Neural networks](../lectures/lecture-13.md)
- [L14 — Large language models](../lectures/lecture-14.md)
- [L15 — Foundation models](../lectures/lecture-15.md)
- [L16 — Lab Day #3](../lectures/lecture-16.md) (chunks 2 and 3: losses + data types — labs 6-16)

The 17 lab notebooks are also indexed under the **[Labs](../labs/intro.md)** part of this book.

## External resources for this part

- Goodfellow, Bengio, Courville, *Deep Learning*, Chs. 6-12 — the standard reference for L13.
- Vaswani et al., "Attention Is All You Need," *NeurIPS* 2017 — the transformer paper.
- Jay Alammar, "The Illustrated Transformer" (blog) — visual companion to the Vaswani paper.
- Andrej Karpathy, "A Recipe for Training Neural Networks" (blog) — practical L13 companion.
- Andrej Karpathy, "Let's build GPT: from scratch, in code, spelled out" (YouTube, ~2 hours) — visceral feel for transformers.
- Bender, Gebru, McMillan-Major & Shmitchell, "On the Dangers of Stochastic Parrots," *FAccT* 2021 — required reading if deploying any LLM near patients.
- Bommasani et al., "On the Opportunities and Risks of Foundation Models," arXiv:2108.07258 — the paper that named "foundation model."
- Moor et al., "Foundation models for generalist medical artificial intelligence," *Nature* 616, 2023 — clinical version of the foundation-model argument.
- fast.ai, *Practical Deep Learning for Coders* (free online course) — hands-on companion to L13.
- scikit-learn user guide and Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.) — the applied companion for the labs.
