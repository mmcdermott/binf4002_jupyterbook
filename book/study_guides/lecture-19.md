# L19 Study Guide — Clinical & Biomedical Text: The Modality

## Key Terms

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

## What Makes Clinical Text Hard

```{admonition} It's documentation, not communication
:class: warning
Clinical text is produced under workflow, billing, and templating pressure — not natural language. A model that "does NLP on clinical text" needs to know it's modeling *documentation behavior*, not communication. Ignoring this leads to models that learn template completion rather than clinical reasoning.
```

## Anatomy of a Clinical Note

Most clinical notes have:

- **HPI** (History of Present Illness) — narrative of why the patient is here.
- **PMH** (Past Medical History) — list of past diagnoses; often copy-forward.
- **Medications** — current med list; templated.
- **Vitals / Labs** — structured data also in the EHR's structured tables.
- **A&P** (Assessment & Plan) — clinical reasoning and plan, where the action is.

Each section has its own conventions and its own failure modes for downstream models.

## Self-Check Questions

1. Why is "five copies of the same paragraph for the same patient" not five independent samples? What modeling decision does this affect?
2. NegEx flips the polarity of any keyword preceded by a negation phrase ("no", "denies", "rule out"). Walk through one *failure mode* of this approach.
3. MIMIC-III is the most-used open clinical-text dataset. What's the *selection effect* in MIMIC patients that limits "MIMIC-NLP performance" as a measure of "clinical NLP performance"?
4. HIPAA Safe Harbor lists 18 categories of PHI to remove. After removing all of them, can a patient still be re-identified? Give an example.
5. PubMed and clinical notes are both "biomedical text." Why are they ecosystems with different conventions, and what does that imply for transfer?

## Additional Resources

- [MIMIC-IV documentation](https://mimic.mit.edu/) — the dataset behind most clinical-NLP work; access procedure included.
- [Wang et al., "A clinical text classification paradigm using weak supervision and deep representation," *BMC Med Inform Decis Mak* 19, 2019](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-018-0723-6) — pragmatic clinical-NLP playbook.
- [Wu et al., "A survey on clinical NLP in the UK 2007-2022," *NPJ Digit Med* 5, 2022](https://www.nature.com/articles/s41746-022-00684-9) — landscape survey.
- [Steinkamp et al., "Notational difference: how EHR templates affect documentation quality," *JAMIA Open* 4, 2021](https://academic.oup.com/jamiaopen/article/4/3/ooab062/6346091) — templates with data.
- [HIPAA Privacy Rule, 45 CFR §164.514](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/) — the regulation governing de-identification.

> See also: [L19 lecture page](../lectures/lecture-19.md). Companion notebook: [`nb19_clinical_text_data.ipynb`](../lectures/nb-19-clinical-text.ipynb).
