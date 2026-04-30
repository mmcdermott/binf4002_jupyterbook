# L20 Study Guide — Clinical & Biomedical NLP: Modeling

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

## Key Terms

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

## The LLM-vs.-Domain-Adapted Question

```{admonition} The choice depends on the task, not the model
:class: tip
LLMs win on tasks with little labeled data — especially zero / few-shot. Domain-adapted small models win when you have hundreds of labels and need cheap inference. The choice depends on **annotation budget**, **latency budget**, and **how confidently you can validate the LLM's output**. There is no universal winner.
```

## Negation Is Not a Footnote

```{admonition} A pneumonia classifier without negation handling
:class: warning
…will flag every patient whose note says "no pneumonia" as positive. NegEx — a 2001 rule-based system — is *still* a reasonable baseline. That fact says something about the field. Always handle negation explicitly; verify on held-out data.
```

## Self-Check Questions

1. ClinicalBERT and BioBERT are both biomedical BERT variants. What's the difference, and when would you reach for which?
2. A clinical NER system identifies "myocardial infarction" but the patient's record actually says "history of myocardial infarction, resolved." What's the classification problem here, and which subsystem handles it?
3. Two physicians label the same 100 notes for sepsis; they agree on 75. What are the implications for any model trained on these labels?
4. RAG vs. fine-tuning: name a clinical setting where RAG is clearly the right call and one where fine-tuning is.
5. An LLM achieves 0.92 on a clinical Q&A benchmark. Walk through three deployment risks the score does *not* reflect.

## Additional Resources

- [Chapman et al., "NegEx," *J Biomed Inform* 34, 2001](https://www.sciencedirect.com/science/article/pii/S1532046401910298) — the classic; still used.
- [Alsentzer et al., "Publicly Available Clinical BERT Embeddings," *ClinicalNLP@NAACL* 2019](https://arxiv.org/abs/1904.03323) — ClinicalBERT.
- [Lee et al., "BioBERT," *Bioinformatics* 36, 2020](https://academic.oup.com/bioinformatics/article/36/4/1234/5566506).
- [Singhal et al., "Large language models encode clinical knowledge" (Med-PaLM), *Nature* 620, 2023](https://www.nature.com/articles/s41586-023-06291-2). Read the limitations carefully.
- [Zack et al., "Assessing GPT-4 to perpetuate racial and gender biases in health care," *Lancet Digital Health* 6, 2024](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(23)00226-0/fulltext) — sobering case study.
- [Lewis et al., "Retrieval-Augmented Generation," *NeurIPS* 2020](https://arxiv.org/abs/2005.11401) — the RAG paper.

> See also: [L20 lecture page](../lectures/lecture-20.md). Companion notebook: [`nb20_clinical_nlp.ipynb`](../lectures/nb-20-clinical-nlp.ipynb).
