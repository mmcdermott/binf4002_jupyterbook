# L15 Study Guide — Foundation Models

## Key Terms

| Term | Definition |
|---|---|
| **Foundation Model** | (Bommasani et al. 2021) A model trained on broad data, typically with self-supervised objectives, designed to be *adapted* to many downstream tasks. The term is broad; sharper questions follow. |
| **Single-task model** | One x → one y. Classical setup. |
| **Multi-task model** | One x → multiple y's. Shared representation, multiple heads. |
| **Transfer learning / Few-shot** | Pre-train on broad data, adapt to a new task with a small number of labeled examples. |
| **Zero-shot / Task-conditioned** | The model takes both an input x *and* a task description α; outputs without task-specific labeled data. (LLMs prompted in natural language.) |
| **Task conditioning (formal)** | A foundation model is a model that takes (x, α) as input. The "foundation" is that the model has internalized enough of the input domain *and* of task structure to handle previously-unseen α. |
| **Task distribution** | The distribution over α the model is meant to handle. Honest evaluation must sample α from this distribution. |
| **Labeled-data efficiency** | Few labels per *task* needed for adaptation. FMs often win here. |
| **Total-data efficiency** | Less data overall (pre-train + adapt) than the single-task baseline. FMs often *do not* win here. |
| **Prior-fitted networks** | A foundation model whose α is "this entire labeled tabular dataset" (e.g., TabPFN). |

## The Spectrum

```{admonition} Single-task → zero-shot
:class: tip
Single-task → multi-task → transfer/few-shot → zero-shot/task-conditioned. Each step adds adaptation flexibility at the cost of needing more / different training data and more careful evaluation. The right place on the spectrum depends on your *task distribution*.
```

## The Load-Bearing Question

```{admonition} "Foundation model over what?"
:class: warning
Always ask:
- Foundation model over **what input domain**? (English text? Clinical notes? Pathology slides? Genomes?)
- Foundation model over **what task distribution**? (Q&A? Classification? IE? All of language tasks?)
- Does it improve **labeled-data efficiency**, **total-data efficiency**, **task-accessibility**, or some combination?

A "good" FM usually wins one or two of those axes, not all three.
```

## Self-Check Questions

1. Distinguish single-task, multi-task, few-shot/transfer, and zero-shot/task-conditioned. Give a clinical example of each.
2. Why is the (x, α) framing more useful than "broad pre-training + adaptable" as a definition?
3. An LLM scores 0.85 on benchmark X. Why is that *not* a statement about all of language? What would a more honest evaluation look like?
4. Give a setting where a focused single-task model with abundant labels would *beat* a foundation model — and a setting where it wouldn't.
5. EHR autoregressive models can be cast as foundation models over event streams. What is the (x, α) decomposition? What's the task distribution?

## Additional Resources

- [Bommasani et al., "On the Opportunities and Risks of Foundation Models," arXiv:2108.07258](https://arxiv.org/abs/2108.07258) — the paper that named the term. Skim the executive summary.
- [Moor et al., "Foundation models for generalist medical AI," *Nature* 616, 2023](https://www.nature.com/articles/s41586-023-05881-4) — the clinical version of the FM argument.
- [Hollmann et al., "TabPFN," *ICLR* 2023](https://arxiv.org/abs/2207.01848) — clean example of a non-LLM foundation model.
- [Steinberg et al., "Language models are an effective representation learning technique for EHR data," *J Biomed Inform* 113, 2021](https://www.sciencedirect.com/science/article/pii/S1532046420302835) — EHR autoregressive models.

> See also: [L15 lecture page](../lectures/lecture-15.md).
