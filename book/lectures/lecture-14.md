# Lecture 14 — Large language models: from n-grams to attention

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Mar 5, 2026 · Part 2 — Modern AI & lab work**

## What this lecture is about

This lecture takes you from "what is a language model?" to "how does a transformer-based LLM actually compute next-token probabilities, and why does it work so much better than what came before?" The arc is historical, because the historical arc is the *clearest pedagogical arc*: each generation of language models fixed a specific failure of the one before.

We open with the **Chinese Room paradox** (Searle, 1980) — a thought experiment about whether symbol manipulation without "understanding" can constitute thinking. The point of the paradox isn't to settle the philosophy; it's to put a permanent asterisk next to the word "understanding" when you talk about LLMs.

Then we walk through:

- **The language modeling objective.** Predict p(token_t | tokens_1…t-1). Simple to state, surprisingly powerful.
- **N-gram models.** Estimate p(token_t | tokens_t-n+1…t-1) by counting. Works for n=2 or 3 on small domains. Fails immediately as n grows because of *combinatorial explosion*: there are |V|^n possible n-gram contexts, and almost all of them never appear in any corpus.
- **Sparsity and back-off.** The classical fixes (Kneser-Ney, etc.) buy you another decimal point but don't solve the underlying problem.
- **Why we needed something else.** N-grams can't *generalize* across similar contexts. "The patient was admitted to the ICU on Sunday" and "The patient was admitted to the ICU on Monday" are unrelated as far as a 4-gram is concerned.
- **Embeddings and the move to continuous representations.** Word2Vec, GloVe — vectors that capture similarity, so the model can interpolate.
- **Transformers and attention.** The architectural shift that finally made next-token prediction work at scale. Attention lets every token "look at" every other token in context, learning which interactions matter for the next prediction. Self-attention + feedforward + residuals + LayerNorm = a transformer block.
- **The LLM ecosystem.** Pre-training + fine-tuning + RLHF + prompting. What's open-weight, what's API-only, what's clinical-specific.
- **Open challenges.** Hallucination, factuality, calibration, evaluation, deployment safety, cost.

The companion notebook `llm_lecture_notebook.ipynb` walks through small n-gram models, attention visualization, and sampling temperature so you can *see* what the lecture is describing.

## Why it matters

Three reasons this lecture is more than "here's how transformers work":

**Next-token prediction is a universal interface for language tasks.** Translation, summarization, classification, extraction, question-answering — all become "given this prompt, predict the continuation." That single fact is why LLMs swept across NLP applications so fast. It will also be the underlying claim of L15 (foundation models) and L20 (clinical NLP).

**Scale matters but it isn't free.** A bigger model trained on more data tends to do better, but the relationship is not linear, the cost is not free, and *failure modes do not automatically diminish with scale* — some (factual recall on common knowledge) tend to improve, while others (hallucination, miscalibration, sycophancy, biased output) often persist or get worse. The Bender et al. ("Stochastic Parrots") critique is part of this lecture for a reason.

**Fluency is not understanding.** This is the L1 epistemic-uncertainty point applied to LLMs specifically. A clinical LLM that confidently produces a fluent-but-wrong answer is *more* dangerous than one that produces an obviously-wrong answer. We will return to this in L20 when we discuss LLMs vs. domain-adapted models for clinical NLP.

## Things you should walk away believing

- A language model is a probabilistic model of next tokens given context. Everything else (translation, Q&A) is a particular way of using that model.
- N-grams fail because of sparsity in the combinatorial explosion of contexts; the remedy was learned continuous representations, not better counting.
- Attention is a routing mechanism: tokens decide which other tokens matter for the next prediction.
- A transformer block is roughly: (multi-head self-attention) → (feedforward) → with residuals and norms. The whole architecture is a stack of these blocks.
- LLMs are *epistemically hazardous*: their fluency is uncorrelated with their groundedness. Always check.
- The right baseline for "is this LLM useful" is *not* "does it sound right" — it's a real evaluation against ground truth in the application domain.

## How this connects to the rest of the course

- L13 (NN training mechanics) — every detail in this lecture's transformers is a special case of L13's recipe.
- L15 (foundation models) — frames LLMs as the prototypical foundation model and pushes the framework further.
- L20 (clinical NLP) — comes back to LLM-vs.-domain-adapted-model trade-offs in clinical settings.
- L27 (modern biological AI) — protein language models (ESM-2) and DNA foundation models (Evo) reuse the *sequence-modeling and foundation-model paradigm* of L14: tokenized sequences, self-supervised or large-scale training, transfer to downstream tasks. The architectures are *not* always literally the same as natural-language LLMs — domain constraints (long genomic context, MSA-derived inputs, 3D-equivariant heads) change the model class. Treat the connection as a paradigm analogy.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Language Model** | A probabilistic model of next-token-given-context: p(t_n \| t_{1:n-1}; θ). Everything else (translation, Q&A, summarization) becomes a particular *use* of that distribution. |
| **N-gram Model** | Estimate p(t_n \| t_{n-k+1:n-1}) by counting in a corpus. Works for k = 2 or 3 on small domains; fails immediately as k grows because of combinatorial sparsity. |
| **Tokenization** | Splitting text into tokens (words, sub-words, characters, BPE pieces). Choice of tokenizer is a representation decision (TL3). |
| **Embedding** | A dense vector representation of a token; the first thing a transformer does to its input. |
| **Self-Attention** | For each token, compute weighted combinations of all other tokens' values, with weights derived from query-key dot products. The routing mechanism. |
| **Multi-Head Attention** | Run self-attention in parallel with different learned projections, then concatenate. Lets the model attend to different relations simultaneously. |
| **Transformer Block** | (Multi-head self-attention) → residual + LayerNorm → (FFN) → residual + LayerNorm. Stack many of these. |
| **Causal vs. Bidirectional Attention** | Causal: a token can only attend to earlier tokens (decoder, GPT). Bidirectional: any-to-any (encoder, BERT). |
| **Perplexity** | exp(cross-entropy). Lower is better. The most-used LM evaluation metric. |
| **Pre-training / Fine-tuning** | Pre-train on huge unlabeled text with a self-supervised objective — *next-token-prediction* for decoder-only LMs (GPT family) or *masked-language-modeling* for encoder-only LMs (BERT, ClinicalBERT, used heavily in L20); encoder-decoder T5-style models combine both. Then fine-tune on a specific task with labeled examples. |
| **Prompting / In-context Learning** | Ask the LM a question or give few-shot examples in the input; let the model use its learned patterns to produce an answer. No weight updates. |
| **RLHF** | Reinforcement learning from human feedback: align a pre-trained LM with human preferences via a reward model + PPO. |
| **Hallucination** | An LM produces fluent text that is *factually wrong* and presented confidently. Major hazard in clinical use. |

### The Chinese Room

```{admonition} Searle's thought experiment
:class: warning
The Chinese Room asks whether symbol manipulation without "understanding" can constitute thinking. The point isn't to settle the philosophy — it's to put a permanent asterisk next to the word "understanding" when you describe LLMs. **Fluency is uncorrelated with groundedness.** A clinical LLM that confidently produces a fluent-but-wrong answer is *more* dangerous than one that produces an obviously-wrong answer.
```

### Why N-grams Fail

```{admonition} Combinatorial sparsity
:class: tip
There are |V|^n possible n-gram contexts, and almost all of them never appear in any corpus. Smoothing (Kneser-Ney etc.) buys you another decimal point but doesn't solve the underlying problem: n-grams cannot generalize across *similar* contexts. Embeddings + attention do, by interpolating in a continuous space.
```

### Self-Check Questions

1. Write the language-modeling objective formally. What is being maximized over what?
2. Why does an n-gram model with n = 5 fail catastrophically on most clinical-text corpora?
3. Walk through one transformer block: what are Q, K, V, what does softmax(QKᵀ/√d_k) V compute (where d_k is the key dimension), and what role do the residual + LayerNorm play?
4. Distinguish causal from bidirectional attention. Which would you use for: (a) clinical-note summarization with a decoder LM, (b) entity recognition with an encoder LM?
5. A clinical LLM scores 0.92 on a benchmark. Walk through what you'd verify before trusting it for live deployment. (Hint: at least three categories.)
6. Why is calibration uniquely hard for LLMs? What workarounds exist?

### Additional Resources

- [Vaswani et al., "Attention Is All You Need," *NeurIPS* 2017](https://arxiv.org/abs/1706.03762) — the transformer paper.
- [Jay Alammar, "The Illustrated Transformer" (blog)](https://jalammar.github.io/illustrated-transformer/) — best visual companion to the Vaswani paper.
- [Karpathy — "Let's build GPT: from scratch, in code, spelled out" (YouTube, ~2 hours)](https://www.youtube.com/watch?v=kCc8FmEb1nY) — visceral feel for transformers.
- [Brown et al., "Language Models are Few-Shot Learners" (GPT-3), *NeurIPS* 2020](https://arxiv.org/abs/2005.14165) — made in-context learning a thing.
- [Hoffmann et al., "Training Compute-Optimal LLMs" (Chinchilla)](https://arxiv.org/abs/2203.15556) — why "more parameters" alone is not the right question.
- [Bender, Gebru, McMillan-Major & Shmitchell, "On the Dangers of Stochastic Parrots," *FAccT* 2021](https://dl.acm.org/doi/10.1145/3442188.3445922) — required reading if deploying any LLM near patients.
- [Jurafsky & Martin, *Speech and Language Processing*, 3rd ed. drafts (free)](https://web.stanford.edu/~jurafsky/slp3/) — Chs. on n-gram LMs and transformers.
