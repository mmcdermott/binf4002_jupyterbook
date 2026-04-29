# Part 3 — Clinical AI

**Lectures 17-22**

## What this part is about

Part 3 covers the data types that arise as a byproduct of the practice of clinical care: structured EHR / claims, clinical text, and medical imaging. The naming reflects the central claim — these aren't "modalities" in some abstract sense; they are records produced *because* care happened, *by* the people delivering it, *under* the workflows and incentives of healthcare systems. Their pathologies trace back to that origin.

Each of the three threads is a paired data → modeling treatment:

- **§3.1 EHR & claims (L17-L18)** — what an EHR is, what claims data are, how care delivery and billing produce both, how cohort selection works, how OMOP / MEDS / FHIR standardize them. Then: how those pathologies translate into modeling decisions (windows, censoring, three representation families).
- **§3.2 Clinical text (L19-L20)** — clinical notes, biomedical literature, reports. Templates, copy-paste, abbreviations, negation, de-identification. Then: domain adaptation, clinical NER, assertion / negation handling, LLMs vs. ClinicalBERT, the annotation bottleneck, RAG.
- **§3.3 Medical imaging (L21-L22)** — X-ray / CT / MRI / histopathology. DICOM as both data standard and shortcut hazard. Then: transfer learning, U-Net segmentation, attention-MIL for pathology, multi-site generalization, the garden of forking paths.

## Goals for this part

- Read an EHR / claims dataset, clinical-note corpus, or imaging dataset and name what is generated, what is missing, and what is selected for.
- Pick representations (tabularized / chunked / event-stream; tokens / embeddings / RAG; 2D / 3D / WSI) with explicit awareness of what each assumes.
- Apply transfer learning, domain adaptation, U-Nets, attention-MIL, etc., where appropriate to the *data shape*, not just to "the modality."
- Spot the canonical failure modes: cohort misdefinition, label leakage, negation flipping, DICOM shortcut learning, multi-site brittleness.

## Key takeaways for this part

- Clinical data are byproducts of care delivery and billing. Their pathologies are informative *and* hazardous.
- Representation is a modeling decision, not preprocessing trivia. Tabularization, binning, tokenization, MIL each impose assumptions.
- Modality-specific architectures (CNN, U-Net, transformer-on-events) encode inductive bias that generic ML lacks.
- Multi-site generalization fails by default; demonstrate it, don't assume it.

## Lectures in this part

- [L17 — EHR & claims data (modality)](../lectures/lecture-17.md)
- [L18 — EHR & claims modeling](../lectures/lecture-18.md)
- [L19 — Clinical & biomedical text (modality)](../lectures/lecture-19.md)
- [L20 — Clinical & biomedical NLP modeling](../lectures/lecture-20.md)
- [L21 — Medical imaging (modality)](../lectures/lecture-21.md)
- [L22 — Medical imaging modeling](../lectures/lecture-22.md)

## External resources for this part

**EHR / claims (L17-L18)**

- *The Book of OHDSI* (free online) — the OMOP CDM reference. Skim Ch. 1-5.
- MEDS schema specification (Medical-Event-Data-Standard on GitHub) — modality-agnostic event-stream format.
- Hripcsak & Albers, "Next-generation phenotyping of electronic health records," *JAMIA* 20, 2013.
- Rajkomar et al., "Scalable and accurate deep learning with electronic health records," *npj Digit Med* 1, 2018.
- Tang et al., "Democratizing EHR analyses with FIDDLE," *JAMIA* 27, 2020.

**Clinical text (L19-L20)**

- Johnson, Pollard et al., "MIMIC-III, a freely accessible critical care database," *Sci Data* 3, 2016 (and the MIMIC-IV update). The substrate for almost all clinical NLP work.
- Chapman et al., "A simple algorithm for identifying negated findings and diseases in discharge summaries," *J Biomed Inform* 34, 2001 — NegEx.
- Alsentzer et al., "Publicly Available Clinical BERT Embeddings," *ClinicalNLP@NAACL* 2019.
- Lee et al., "BioBERT," *Bioinformatics* 36, 2020.
- Singhal et al., "Large language models encode clinical knowledge" (Med-PaLM), *Nature* 620, 2023.
- Zack et al., "Assessing the potential of GPT-4 to perpetuate racial and gender biases in health care," *Lancet Digital Health* 6, 2024.

**Medical imaging (L21-L22)**

- Litjens et al., "A survey on deep learning in medical image analysis," *Med Image Anal* 42, 2017.
- Ronneberger, Fischer & Brox, "U-Net," *MICCAI* 2015.
- Isensee et al., "nnU-Net," *Nat Methods* 18, 2021.
- Ilse et al., "Attention-based Deep Multiple Instance Learning," *ICML* 2018.
- DeGrave, Janizek & Lee, "AI for radiographic COVID-19 detection selects shortcuts over signal," *Nat Mach Intell* 3, 2021.
- Glocker et al., "Risk of Bias in Chest Radiography Deep Learning Foundation Models," *Radiology AI* 5, 2023.
- DICOM Standard reference: <https://www.dicomstandard.org>

**Cross-cutting**

- Coursera *AI for Medicine* specialization (deeplearning.ai) — three-course series covering diagnosis, prognosis, and treatment.
- Beam & Kohane, "Big Data and Machine Learning in Health Care," *JAMA* 319(13), 2018.
- Finlayson et al., "The Clinician and Dataset Shift in Artificial Intelligence," *NEJM* 385, 2021.
