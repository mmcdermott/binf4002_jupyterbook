# Lecture 20 — Clinical and biomedical NLP: modeling

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Apr 2, 2026 · Part 3 — Health data modalities · §3.2 Clinical text**

## What this lecture is about

L19 told you what clinical text *is*. This lecture is about what to *do* with it. Most of clinical NLP can be organized as the answer to a series of questions: how much general-language signal do we get for free? When do we need clinical-specific pretraining? When does an LLM beat a domain-adapted small model? When does it not?

The lecture walks through the modeling toolkit in the order most projects use it.

- **The domain-mismatch problem.** A general-language model (BERT, GPT-3) was trained on Wikipedia, news, Common Crawl. Clinical notes use vocabulary, abbreviations, and conventions that those corpora barely contain. The model "speaks" English; clinical notes are a *dialect*.
- **Clinical NLP model lineage.** The progression: rule-based (regex + dictionaries) → classical ML (SVM + hand-crafted features) → general-language transformers (BERT) → biomedical/clinical pretraining (BioBERT, ClinicalBERT, PubMedBERT) → instruction-tuned LLMs (GPT-4, Med-PaLM-style). Each generation fixed something and broke something.
- **Why domain adaptation works.** Continuing pretraining on clinical text moves the model's representation toward the clinical dialect. Even a small amount of clinical pretraining markedly improves downstream performance.
- **Clinical Named Entity Recognition (NER).** Identify mentions of diseases, drugs, anatomy, etc., in text. The hardest part isn't tagging — it's *boundary detection* ("acute myocardial infarction" or just "myocardial infarction"?), *concept-normalization* (mapping the mention to UMLS / SNOMED / ICD), and *temporality* (is this a current diagnosis or a past one?).
- **Assertion and negation.** Once you've identified an entity, is it asserted, negated, hypothetical, or about a family member? NegEx (Chapman et al., 2001) is the surprisingly-still-relevant baseline. LLMs do this better but inconsistently.
- **Relation extraction and clinical information extraction.** Beyond entities: drug-disease relations, dose-frequency-route relations, temporal relations. The shift from "what's in the text" to "what is the structured information the text is *about*."
- **LLMs vs. domain-adapted models.** Per-task experiments. LLMs win on tasks with little labeled data, especially zero/few-shot. Domain-adapted small models win when you have hundreds of labels and need cheap inference. The choice depends on annotation budget, latency budget, and *how confidently you can validate the LLM's output*.
- **The annotation bottleneck.** Clinical NLP gets stuck on labels — both because expert labels are expensive and because *inter-annotator agreement* on clinical concepts is often only moderate. Two physicians can disagree on whether a note describes "sepsis." Your training labels are upper-bounded by that disagreement.
- **RAG (retrieval-augmented generation) as a practical alternative.** Don't fine-tune an LLM; let it look things up. Useful when you have a structured knowledge base (UMLS, drug references) and want grounded outputs.

## Why it matters

Three reasons this lecture is the practical core of clinical NLP:

**The LLM-vs.-small-model question is real and not obvious.** "Just use GPT-4" is a defensible answer for some tasks and a catastrophic answer for others. The lecture gives you the framework for making the choice — which depends on the *task*, the *annotation budget*, and the *deployment constraints*, not on which model is "better in general."

**Annotation is the bottleneck, not modeling.** This is the single most important practical fact about clinical NLP. The model you fit will be no better than the labels it learns from, and labels in clinical NLP are expensive, scarce, and noisy. Strategies — weak supervision, distant supervision, active learning, LLM-as-annotator — exist but each has its own pitfalls.

**Negation and assertion are *not* solved.** A clinical NLP system that doesn't explicitly model negation/assertion will get a fraction of "positive findings" exactly inverted. NegEx — a 2001 rule-based system — is *still* a reasonable baseline. That fact says something about the field.

## Things you should walk away believing

- General-language NLP doesn't transfer cleanly to clinical text. Domain pretraining is not optional for most tasks.
- The LLM-vs.-domain-adapted question is task-dependent. Decide on annotation budget, latency, validation cost, and *then* model choice.
- NER alone is not enough. You also need normalization, assertion, negation, and temporality before you can claim "the model extracts X from notes."
- Inter-annotator agreement is part of the modeling problem. If your labels disagree by 15% across annotators, no model can be more than 85% "right."
- Negation and assertion handling is non-negotiable. Use NegEx or its modern equivalents; verify on held-out data.
- RAG is often a better deployment pattern than fine-tuning when ground-truth knowledge exists in a structured form.
- LLMs hallucinate clinical facts confidently. Always evaluate against ground truth, not against "looks plausible."

## How this connects to the rest of the course

- L19 told you the data shape; this lecture turns it into modeling decisions.
- L14 (LLMs) provides the architectural background; this lecture is the clinical specialization.
- L15 (foundation models) — clinical LLMs are foundation models over (clinical text, "clinical NLP tasks").
- L24 (fairness) — clinical text encodes biases of documenting clinicians; cf. Zack et al. on LLMs and biased clinical reasoning.
- L17-L18 (EHR data) — clinical text is one sub-modality of the EHR; you'll often combine it with structured codes.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Domain mismatch** | A general-language model (BERT, GPT-3) was trained on Wikipedia / news / Common Crawl. Clinical text is a *dialect* the general model barely knows. |
| **Domain adaptation** | Continue pre-training on clinical / biomedical text to move the representation toward the clinical dialect. |
| **BioBERT / ClinicalBERT / PubMedBERT** | BERT variants pre-trained on biomedical / clinical corpora. Improve markedly over general-language BERT on clinical tasks. |
| **Named Entity Recognition (NER)** | Identify mentions of diseases, drugs, anatomy, etc. Hard parts: boundary detection, concept normalization, temporality. |
| **Concept normalization** | Mapping a textual mention ("DM2") to a canonical code (e.g., SNOMED-CT 44054006). |
| **Assertion / Negation classification** | Determine if a found entity is asserted, negated, hypothetical, or about a family member. NegEx (2001) is still a baseline. |
| **Relation extraction** | Beyond entities: drug-disease, dose-frequency-route, temporal relations. The shift from "what's in the text" to "what is the structured information the text is *about*." |
| **Inter-annotator agreement (IAA)** | The rate at which two human annotators agree on labels. Sets an upper bound on model performance. |
| **Annotation bottleneck** | Expert labels are expensive and scarce in clinical NLP. Annotation cost often exceeds modeling cost. |
| **RAG (Retrieval-Augmented Generation)** | Retrieve relevant passages from a knowledge base, condition the LM on them, then generate. Practical alternative to fine-tuning when ground truth lives in a structured KB. |

### The LLM-vs.-Domain-Adapted Question

```{admonition} The choice depends on the task, not the model
:class: tip
LLMs win on tasks with little labeled data — especially zero / few-shot. Domain-adapted small models win when you have hundreds of labels and need cheap inference. The choice depends on **annotation budget**, **latency budget**, and **how confidently you can validate the LLM's output**. There is no universal winner.
```

### Negation Is Not a Footnote

```{admonition} A pneumonia classifier without negation handling
:class: warning
…will flag every patient whose note says "no pneumonia" as positive. NegEx — a 2001 rule-based system — is *still* a reasonable baseline. That fact says something about the field. Always handle negation explicitly; verify on held-out data.
```

### Self-Check Questions

1. ClinicalBERT and BioBERT are both biomedical BERT variants. What's the difference, and when would you reach for which?
2. A clinical NER system identifies "myocardial infarction" but the patient's record actually says "history of myocardial infarction, resolved." What's the classification problem here, and which subsystem handles it?
3. Two physicians label the same 100 notes for sepsis; they agree on 75. What are the implications for any model trained on these labels?
4. RAG vs. fine-tuning: name a clinical setting where RAG is clearly the right call and one where fine-tuning is.
5. An LLM achieves 0.92 on a clinical Q&A benchmark. Walk through three deployment risks the score does *not* reflect.

### Additional Resources

- [Chapman et al., "NegEx," *J Biomed Inform* 34, 2001](https://www.sciencedirect.com/science/article/pii/S1532046401910298) — the classic; still used.
- [Alsentzer et al., "Publicly Available Clinical BERT Embeddings," *ClinicalNLP@NAACL* 2019](https://arxiv.org/abs/1904.03323) — ClinicalBERT.
- [Lee et al., "BioBERT," *Bioinformatics* 36, 2020](https://academic.oup.com/bioinformatics/article/36/4/1234/5566506).
- [Singhal et al., "Large language models encode clinical knowledge" (Med-PaLM), *Nature* 620, 2023](https://www.nature.com/articles/s41586-023-06291-2). Read the limitations carefully.
- [Zack et al., "Assessing GPT-4 to perpetuate racial and gender biases in health care," *Lancet Digital Health* 6, 2024](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(23)00226-0/fulltext) — sobering case study.
- [Lewis et al., "Retrieval-Augmented Generation," *NeurIPS* 2020](https://arxiv.org/abs/2005.11401) — the RAG paper.
