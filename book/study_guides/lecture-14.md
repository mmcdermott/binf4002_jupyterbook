# L14 Study Guide — Large Language Models: From N-grams to Attention

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

## Key Terms

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
| **Pre-training / Fine-tuning** | Pre-train on huge unlabeled text with next-token-prediction; fine-tune on a specific task with labeled examples. |
| **Prompting / In-context Learning** | Ask the LM a question or give few-shot examples in the input; let the model use its learned patterns to produce an answer. No weight updates. |
| **RLHF** | Reinforcement learning from human feedback: align a pre-trained LM with human preferences via a reward model + PPO. |
| **Hallucination** | An LM produces fluent text that is *factually wrong* and presented confidently. Major hazard in clinical use. |

## The Chinese Room

```{admonition} Searle's thought experiment
:class: warning
The Chinese Room asks whether symbol manipulation without "understanding" can constitute thinking. The point isn't to settle the philosophy — it's to put a permanent asterisk next to the word "understanding" when you describe LLMs. **Fluency is uncorrelated with groundedness.** A clinical LLM that confidently produces a fluent-but-wrong answer is *more* dangerous than one that produces an obviously-wrong answer.
```

## Why N-grams Fail

```{admonition} Combinatorial sparsity
:class: tip
There are |V|^n possible n-gram contexts, and almost all of them never appear in any corpus. Smoothing (Kneser-Ney etc.) buys you another decimal point but doesn't solve the underlying problem: n-grams cannot generalize across *similar* contexts. Embeddings + attention do, by interpolating in a continuous space.
```

## Self-Check Questions

1. Write the language-modeling objective formally. What is being maximized over what?
2. Why does an n-gram model with n = 5 fail catastrophically on most clinical-text corpora?
3. Walk through one transformer block: what are Q, K, V, what does softmax(QKᵀ/√d) V compute, and what role do the residual + LayerNorm play?
4. Distinguish causal from bidirectional attention. Which would you use for: (a) clinical-note summarization with a decoder LM, (b) entity recognition with an encoder LM?
5. A clinical LLM scores 0.92 on a benchmark. Walk through what you'd verify before trusting it for live deployment. (Hint: at least three categories.)
6. Why is calibration uniquely hard for LLMs? What workarounds exist?

## Additional Resources

- [Vaswani et al., "Attention Is All You Need," *NeurIPS* 2017](https://arxiv.org/abs/1706.03762) — the transformer paper.
- [Jay Alammar, "The Illustrated Transformer" (blog)](https://jalammar.github.io/illustrated-transformer/) — best visual companion to the Vaswani paper.
- [Karpathy — "Let's build GPT: from scratch, in code, spelled out" (YouTube, ~2 hours)](https://www.youtube.com/watch?v=kCc8FmEb1nY) — visceral feel for transformers.
- [Brown et al., "Language Models are Few-Shot Learners" (GPT-3), *NeurIPS* 2020](https://arxiv.org/abs/2005.14165) — made in-context learning a thing.
- [Hoffmann et al., "Training Compute-Optimal LLMs" (Chinchilla)](https://arxiv.org/abs/2203.15556) — why "more parameters" alone is not the right question.
- [Bender, Gebru, McMillan-Major & Shmitchell, "On the Dangers of Stochastic Parrots," *FAccT* 2021](https://dl.acm.org/doi/10.1145/3442188.3445922) — required reading if deploying any LLM near patients.
- [Jurafsky & Martin, *Speech and Language Processing*, 3rd ed. drafts (free)](https://web.stanford.edu/~jurafsky/slp3/) — Chs. on n-gram LMs and transformers.

> See also: [L14 lecture page](../lectures/lecture-14.md). Companion notebook: [`llm_lecture_notebook.ipynb`](../lectures/nb-14-llm.ipynb).
