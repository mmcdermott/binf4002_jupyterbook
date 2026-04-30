# Lecture 19 — Clinical and biomedical text: the modality

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Mar 31, 2026 · Part 3 — Health data modalities · §3.2 Clinical text**

## What this lecture is about

Clinical and biomedical text is a huge, rich, and dangerous data modality. This lecture is about *what the text actually is* before we get to *how to model it* (which is L20). The point is to make you cautious and informed before you start tokenizing it.

We organize health text into three domains:

- **Clinical notes.** What clinicians write inside an EHR. Discharge summaries, progress notes, admission notes, consult notes. Heavily templated, copy-paste-rich, abbreviation-heavy, negation-heavy, written under time pressure for billing as much as for communication.
- **Biomedical literature.** PubMed articles, abstracts, clinical guidelines, systematic reviews. Structured but in a different way — peer-reviewed prose with conventions about claims and evidence.
- **Reports.** Radiology reports, pathology reports, imaging-study findings. *Semi-structured* — they have sections, conventions, structured findings — but they are still free-text at the leaves.

Then we walk through what makes clinical text hard:

- **Anatomy of a clinical note.** History of Present Illness, Past Medical History, Medications, Assessment & Plan. Each section has its own conventions, its own typical content, and its own failure modes for downstream modeling.
- **Templates and copy-paste / note bloat.** A modern note is mostly *copy-forward* from earlier visits, with small edits. The same paragraph can appear in dozens of notes for the same patient. This makes "n notes" misleading as a measure of independent text. It also corrupts label-leakage analysis (a future label can be copied backward into past notes by accident).
- **Abbreviations and ambiguity.** "MS" can be multiple sclerosis, mitral stenosis, mental status, magnesium sulfate, or morphine sulfate. Disambiguation is context-dependent and notoriously hard.
- **Negation and assertion.** "No history of pneumonia" mentions pneumonia but asserts its absence. Naïve keyword matching gets this exactly backwards. NegEx and its successors will appear in L20.
- **De-identification and access.** Clinical text is governed by HIPAA Safe Harbor; you can't share it without de-identifying first, and even de-identified text retains risk. MIMIC-III/IV (Johnson et al., MIT) is the standard public dataset; it requires DUA training and is non-trivial to obtain.
- **Mapping to ML data types.** Sequences of tokens, but with much heavier domain conventions than general English.

The paradox flagged is the **Birthday paradox** — relevant because de-identification is harder than it looks: even after stripping names, dates, and obvious identifiers, the *combination* of demographics, ZIP, and admission patterns can re-identify patients.

## Why it matters

Three reasons this lecture comes *before* clinical NLP modeling:

**Clinical text is not natural language; it's documentation.** It's produced under workflow constraints, billing pressure, and templating tools. A model trained to "do NLP on clinical text" needs to know it's modeling documentation behavior, not communication. Ignoring this leads to models that learn to predict template-completion patterns rather than clinical reasoning.

**Negation, abbreviation, and copy-paste are *the* failure modes of naïve clinical NLP.** A pneumonia classifier that doesn't handle negation will flag every patient whose note says "no pneumonia" as positive. A copy-paste-blind model trained on per-patient text will see five copies of the same paragraph as five independent samples.

**Access constraints shape the field.** Most clinical NLP research uses MIMIC-III/IV because it's the only large open dataset. That introduces its own selection effect: MIMIC patients are ICU patients at one Boston hospital. "MIMIC-NLP performance" is not "general clinical-NLP performance."

## Things you should walk away believing

- Clinical text is documentation produced under workflow and billing pressure, not communication.
- Templates and copy-paste are correlated structure, not redundant noise — they encode the workflow that produced the note.
- Negation can invert the meaning of any keyword-based feature. Always handle it explicitly.
- Abbreviations are ambiguous in a domain-specific way. Disambiguation needs context, not a static dictionary.
- De-identification is necessary, not sufficient. Even MIMIC has known re-identification risk in principle.
- Public clinical-text datasets are biased toward the institutions willing to share. Generalization beyond MIMIC is a real and open problem.
- Biomedical literature (PubMed) is a related but distinct ecosystem. Don't conflate it with clinical notes.

## How this connects to the rest of the course

- L20 (the next lecture) takes these data-side issues as given and asks: how do we model with this?
- L17-L18 (EHR / claims) is the structured-data sibling of this modality; clinical notes live *inside* the EHR alongside structured codes.
- L14 (LLMs) is the generic NLP background. The big question is whether general-language LLMs transfer to clinical text — preview of L20.
- L24 (fairness) returns to: clinical notes can encode the documenting-clinician's biases, not just objective findings.

## Source files in this folder

- `L19.pdf` — the slides as released to students. *The LaTeX source compiles to a 100-page PDF identical to this in content (verified).*
- `latex/main.tex` and `latex/figures/` — the editable Beamer source.
- `nb19_clinical_text_data.ipynb` — companion notebook exploring clinical text artifacts (note length distributions, vocabulary differences, copy-paste detection, negation prevalence, abbreviation ambiguity).

## To go deeper

- **Wang et al., "A clinical text classification paradigm using weak supervision and deep representation," _BMC Med Inform Decis Mak_ 19, 2019.** The pragmatic clinical-NLP playbook.
- **Wu et al., "A survey on clinical natural language processing in the United Kingdom from 2007 to 2022," _NPJ Digit Med_ 5, 2022.** Landscape survey, useful for sense-making.
- **Steinkamp et al., "Notational difference: how electronic health record templates affect documentation quality," _JAMIA Open_ 4, 2021.** The templates story, with data.
- **Johnson, Pollard et al., "MIMIC-III, a freely accessible critical care database," _Sci Data_ 3, 2016** (and the subsequent MIMIC-IV paper). The dataset behind most clinical NLP work, plus the access procedure.
- **Liu et al., "A scoping review of electronic health record–based clinical prediction models," _Annals of Family Medicine_ 22, 2024.** A useful summary of how clinical text is being used, and where it tends to go wrong.
- **HIPAA Privacy Rule, 45 CFR §164.514** — the regulation governing de-identification.

## Study tools

- [Study guide for L19](../study_guides/lecture-19.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
