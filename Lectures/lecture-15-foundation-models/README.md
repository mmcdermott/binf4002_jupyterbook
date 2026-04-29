# Lecture 15 — Foundation models

**Tue Mar 10, 2026 · Part 2 — Modern AI & lab work**

## What this lecture is about

The phrase "foundation model" gets thrown around constantly, and the more it gets thrown, the less it means. This lecture is an honest attempt to pin it down.

We start from the **field's standard definition** (Bommasani et al., 2021): a model trained on broad data, typically with self-supervised objectives, designed to be *adapted* to many downstream tasks. That definition is broad on purpose. The lecture argues that this breadth is precisely what makes the term unhelpful in practice, and offers a sharper lens.

We walk through a spectrum:

- **Single-task models.** One x → one y. The classical setup.
- **Multi-task models.** One x → multiple y's. Shared representation, multiple heads.
- **Few-shot / transfer-learning models.** Pre-train on broad data, adapt to a new task with a small number of labeled examples.
- **Zero-shot / task-conditioned models.** The model takes both an input x *and* a task description α, and produces an output without any task-specific labeled data. This is what an LLM does when you prompt it.

The lecture's central reframe: **a foundation model is a model that takes (x, α) as input.** The "foundation" is that the model has internalized enough about the input domain and about task structure to handle previously-unseen α at inference time. That formal lens lets you ask sharp questions:

- Foundation model *over what input domain*? (English text? Clinical notes? Pathology slides? Genomes?)
- Foundation model *over what task distribution*? (Q&A? Classification? Information extraction? All of language tasks ever?)
- Does the model improve *labeled-data efficiency* (you need fewer labels per task), *total-data efficiency* (you need less data overall), *task-accessibility* (you can describe a task in natural language instead of building a labeled dataset), or some combination?

We work through examples:

- **LLMs** are foundation models over (English text, "language tasks") with task-conditioning via natural-language prompting.
- **EHR autoregressive models** can be cast as foundation models over (EHR event streams, "any future-event prediction task") — promising but unproven.
- **Prior-fitted networks** (TabPFN-style) are foundation models over (small tabular dataset, "predict y from x for this dataset") — they take an entire labeled dataset as input.

## Why it matters

Two reasons the framing in this lecture is consequential:

**It tells you when "foundation model" is the right tool and when it isn't.** If you have a fixed task with abundant labeled data and a stable distribution, a focused single-task model often beats a foundation model. If you have a task distribution where labeling is expensive or task definitions shift, foundation models win. Most published comparisons confound these settings — making the comparison framework explicit lets you read papers more sharply.

**It tells you what to evaluate.** Single-task evaluation gives you a single number on a single distribution. Foundation-model evaluation needs to be over a *distribution of tasks*, and you have to be honest about which task distribution you're sampling from. "GPT-4 scores X on benchmark Y" is a statement about Y, not about all of language. We will return to this in L20 (clinical NLP) and L27 (biological foundation models) where the over-claiming is rampant.

## Things you should walk away believing

- "Foundation model over what?" is the load-bearing question. Always ask domain *and* task distribution.
- The (x, α) framing converts the marketing term into a technical question.
- Foundation models are not automatically better than fixed single-task models on a single task with enough labels. Their distinctive value is *adaptation*, not raw performance.
- Labeled-data efficiency, total-data efficiency, and task-accessibility are different axes. A "good" foundation model usually wins one or two, not all three.
- Evaluation has to be over a task distribution. Don't accept "we tested on N benchmarks" without asking which N benchmarks and how they were chosen.

## How this connects to the rest of the course

- L14 (LLMs) is the prototypical foundation model. This lecture abstracts what makes it special.
- L20 (clinical NLP) — when does a clinical LLM beat a clinical-domain-pretrained BERT? It depends on task distribution.
- L22 (medical imaging) — domain-specific image foundation models (RadImageNet, MedSAM) are case studies.
- L27 (modern biological AI) — protein language models, DNA foundation models. Each one has to answer "foundation over what (x, α)?" in a way that the lecture sets up.

## Source files in this folder

- `FMs Lecture.pdf` — the slides as released to students.
- `FMs Lecture.pptx` — editable PowerPoint source. (No LaTeX source for this lecture.)

## To go deeper

- **Bommasani et al., "On the Opportunities and Risks of Foundation Models," arXiv:2108.07258.** The 200-page paper that named the term. You can read just the executive summary and the parts relevant to your application.
- **Moor et al., "Foundation models for generalist medical artificial intelligence," _Nature_ 616, 2023.** The clinical version of the foundation-model argument.
- **Hollmann et al., "TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second," _ICLR_ 2023.** The prior-fitted-networks paper; a clean example of a non-LLM foundation model.
- **Steinberg et al., "Language models are an effective representation learning technique for electronic health record data," _J Biomed Inform_ 113, 2021.** EHR autoregressive models as foundation models.
- **McDermott et al., "Closing the AI accountability gap: defining an end-to-end framework for internal algorithmic auditing," _FAccT_ 2020** (or current McDermott-lab preprints on EHR foundation models, depending on what's been published when you read this).
