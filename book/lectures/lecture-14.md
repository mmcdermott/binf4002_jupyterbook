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

**Scale matters but it isn't free.** A bigger model trained on more data tends to do better, but the relationship is not linear, the cost is not free, and the failure modes (hallucination, miscalibration, biased output) get *more* prominent at scale, not less. The Bender et al. ("Stochastic Parrots") critique is part of this lecture for a reason.

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

## Source files in this folder

- `llms_lecture.pdf` — the slides as released to students. *The LaTeX source compiles to a 145-page PDF identical to this in content (verified).*
- `latex/llm_lecture.tex` and `latex/figures/` — the editable Beamer source.
- `llm_lecture_notebook.ipynb` — companion notebook: small n-gram models, attention visualization, sampling temperature.

## To go deeper

- **Vaswani et al., "Attention Is All You Need," _NeurIPS_ 2017.** The transformer paper. Read once, re-read with intent.
- **Jay Alammar, "The Illustrated Transformer" (blog).** The single best visual companion to the Vaswani paper.
- **Brown et al., "Language Models are Few-Shot Learners" (GPT-3), _NeurIPS_ 2020.** The paper that made "in-context learning" a thing.
- **Hoffmann et al., "Training Compute-Optimal Large Language Models" (Chinchilla), arXiv:2203.15556.** Why "more parameters" is not the right question; "more parameters *and* more tokens" is.
- **Bender, Gebru, McMillan-Major & Shmitchell, "On the Dangers of Stochastic Parrots," _FAccT_ 2021.** The critique. Required reading if you'll deploy any LLM near patients.
- **Jurafsky & Martin, _Speech and Language Processing_, 3rd ed. drafts (free online).** Chs. on n-gram language models and transformers.
- **Karpathy, "Let's build GPT: from scratch, in code, spelled out" (YouTube).** A 2-hour walk-through that builds a small GPT step by step. Good for the visceral feel.

## Study tools

- [Study guide for L14](../study_guides/lecture-14.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
