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

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Clinical note** | Free-text + templated documentation in the EHR (HPI, PMH, A&P, discharge summaries). |
| **Biomedical literature** | PubMed articles, abstracts, guidelines, reviews — peer-reviewed prose. |
| **Report** | Semi-structured text: radiology, pathology, imaging-study findings. Sections + free text at the leaves. |
| **Template / Macro** | Pre-formatted note skeletons inserted by EHR shortcut tools. Most modern notes are mostly templates. |
| **Copy-paste / Note bloat** | Clinicians copy-forward from earlier notes; same paragraphs reappear across visits and patients. |
| **Abbreviation ambiguity** | "MS" = multiple sclerosis / mitral stenosis / mental status / magnesium sulfate / morphine sulfate (context-dependent). |
| **Negation / Assertion** | "No history of pneumonia" mentions pneumonia but asserts its absence. NegEx is the classical handler. |
| **De-identification** | Removing PHI per HIPAA Safe Harbor (names, dates, addresses, IDs). Required for sharing. |
| **MIMIC-III / IV** | Open-access ICU dataset from Beth Israel (MIT). The substrate for most clinical NLP research. Requires DUA training. |
| **PubMed** | NIH-maintained index of biomedical literature; ~37M+ records. The biomedical text corpus most LLMs that matter for clinical use have been pre-trained on. |
| **UMLS** | Unified Medical Language System: NIH meta-thesaurus mapping ~200 terminologies to a unified concept space. |

### What Makes Clinical Text Hard

```{admonition} It's documentation, not communication
:class: warning
Clinical text is produced under workflow, billing, and templating pressure — not natural language. A model that "does NLP on clinical text" needs to know it's modeling *documentation behavior*, not communication. Ignoring this leads to models that learn template completion rather than clinical reasoning.
```

### Anatomy of a Clinical Note

Most clinical notes have:

- **HPI** (History of Present Illness) — narrative of why the patient is here.
- **PMH** (Past Medical History) — list of past diagnoses; often copy-forward.
- **Medications** — current med list; templated.
- **Vitals / Labs** — structured data also in the EHR's structured tables.
- **A&P** (Assessment & Plan) — clinical reasoning and plan, where the action is.

Each section has its own conventions and its own failure modes for downstream models.

### Self-Check Questions

1. Why is "five copies of the same paragraph for the same patient" not five independent samples? What modeling decision does this affect?
2. NegEx flips the polarity of any keyword preceded by a negation phrase ("no", "denies", "rule out"). Walk through one *failure mode* of this approach.
3. MIMIC-III is the most-used open clinical-text dataset. What's the *selection effect* in MIMIC patients that limits "MIMIC-NLP performance" as a measure of "clinical NLP performance"?
4. HIPAA Safe Harbor lists 18 categories of PHI to remove. After removing all of them, can a patient still be re-identified? Give an example.
5. PubMed and clinical notes are both "biomedical text." Why are they ecosystems with different conventions, and what does that imply for transfer?

### Additional Resources

- [MIMIC-IV documentation](https://mimic.mit.edu/) — the dataset behind most clinical-NLP work; access procedure included.
- [Wang et al., "A clinical text classification paradigm using weak supervision and deep representation," *BMC Med Inform Decis Mak* 19, 2019](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-018-0723-6) — pragmatic clinical-NLP playbook.
- [Wu et al., "A survey on clinical NLP in the UK 2007-2022," *NPJ Digit Med* 5, 2022](https://www.nature.com/articles/s41746-022-00684-9) — landscape survey.
- [Steinkamp et al., "Notational difference: how EHR templates affect documentation quality," *JAMIA Open* 4, 2021](https://academic.oup.com/jamiaopen/article/4/3/ooab062/6346091) — templates with data.
- [HIPAA Privacy Rule, 45 CFR §164.514](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/) — the regulation governing de-identification.
