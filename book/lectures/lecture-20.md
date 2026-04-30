# Lecture 20 — Clinical and biomedical NLP: modeling

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

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

## Source files in this folder

- `L20.pdf` — the slides as released to students. *The LaTeX source compiles to a 37-page PDF identical to this in content (verified).*
- `latex/main.tex` and `latex/figures/` — the editable Beamer source.
- `nb20_clinical_nlp.ipynb` — companion notebook with clinical NLP demonstrations: tokenization, MLM-style domain adaptation, embeddings, negation classification, RAG pipeline, and a SciBERT racial-bias case study.

## To go deeper

- **Chapman et al., "A simple algorithm for identifying negated findings and diseases in discharge summaries," _J Biomed Inform_ 34, 2001.** NegEx. The classic; still used.
- **Alsentzer et al., "Publicly Available Clinical BERT Embeddings," _ClinicalNLP@NAACL_ 2019.** ClinicalBERT.
- **Lee et al., "BioBERT: a pre-trained biomedical language representation model," _Bioinformatics_ 36, 2020.** Biomedical-domain pretraining at scale.
- **Singhal et al., "Large language models encode clinical knowledge," _Nature_ 620, 2023.** Med-PaLM. Read the limitations section carefully.
- **Zack et al., "Assessing the potential of GPT-4 to perpetuate racial and gender biases in health care," _Lancet Digital Health_ 6, 2024.** A sobering case study on bias in clinical LLMs.
- **Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," _NeurIPS_ 2020.** The original RAG paper.
- **Spasic & Nenadic, "Clinical Text Data in Machine Learning: Systematic Review," _JMIR Med Inform_ 8, 2020.** Useful survey-of-the-field.

## Study tools

- [Study guide for L20](../study_guides/lecture-20.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
