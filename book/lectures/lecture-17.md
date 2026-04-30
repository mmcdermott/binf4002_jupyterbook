# Lecture 17 — EHR and claims data: the modality

**Tue Mar 24, 2026 · Part 3 — Health data modalities · §3.1 EHR & claims**

## What this lecture is about

This is the lecture where the course pivots from "ML in general" to "ML for *health data*." Electronic health records (EHRs) and claims data are the largest and most-studied data modality in clinical ML, and they are also the modality where "the data are generated, not given" hits hardest.

We open with a **statistical-trap warm-up** — a Berkson's-paradox-style example. Among hospitalized patients, two diseases that are independent in the general population can appear *negatively* correlated, simply because being hospitalized requires having one or the other (or both) seriously enough. The point: the moment you condition on "appears in the EHR," you have changed the distribution you're studying.

Then we walk through the data modality in detail:

- **What an EHR actually is.** Diagnosis codes, procedure codes, medication orders, lab results, vital signs, clinical notes (covered in L19-L20), imaging (L21-L22), demographics. Each is its own sub-modality with its own data-quality profile.
- **What claims data are, and how they differ.** Claims are *billing* records, not clinical records. They tell you what was billed, not what happened. They are also more comparable across institutions because billing standards are tighter than EHR conventions.
- **Coding systems and their hierarchies.** ICD-9/10, CPT, RxNorm, LOINC, SNOMED-CT. Each is a tree (or a DAG) with its own granularity, ambiguity, and historical revisions. "The patient has ICD-10 code I50.9" is *coarser* information than "the patient has ICD-10 code I50.21."
- **Who's actually in the data.** Insurance status, geographic catchment, language, socioeconomic status, healthcare-seeking behavior — all of these select who shows up in any given EHR. The observed cohort is not the population.
- **Health event streams.** A patient's record is a sequence of timestamped events at irregular times. The *timing* of an event (lab ordered, code recorded) is itself informative — sicker patients have more recordings.
- **Cohort selection as a modeling problem.** "Patients with diabetes" sounds simple. Defining it from EHR data requires choosing a code set, an observation window, an exclusion list, and a denominator. Two reasonable definitions can yield very different cohorts, very different conclusions, and very different models.
- **Standards and interoperability.** OMOP CDM (the OHDSI standard), MEDS (the modality-agnostic event-stream format), FHIR (the API standard). They help; they don't eliminate the problems.

The paradox flagged is the **Coastline paradox** — a question about how the apparent length of a coastline depends on the resolution at which you measure it. The same is true of "number of features in an EHR": at one level of aggregation a patient has 50 features; at another level, 50,000.

## Why it matters

Three reasons this lecture is the spine of the second half of the course:

**The data are byproducts of care, not designed measurements.** A vital sign appears in the EHR because someone took it. They took it because the patient was sick enough, or it was a routine check-in, or the protocol required it. Whether a measurement *exists* is informative. Whether a code is recorded is informative. Whether the patient came back for a follow-up is informative. None of this is iid sampling from a population distribution.

**Cohort selection is where most ML-for-EHR papers go wrong before they start.** "Predict mortality in patients with sepsis" — what counts as sepsis? Who's excluded? What window? When does the prediction time start? Two papers can claim to study the same problem and not be comparable.

**Standards (OMOP, MEDS, FHIR) are imperfect but worth investing in.** They don't make the data clean; they make it *exchangeable*. A model trained against MEDS-formatted data has a chance of running against another site's MEDS-formatted data. A model trained against an institution-specific schema does not.

## Things you should walk away believing

- The EHR is a record of care delivery and billing, not a record of biology. Patterns in it reflect both.
- Missingness, frequency-of-measurement, and code-presence are themselves data, often the most informative data.
- Cohort definitions are modeling choices. Document them. Validate them against external definitions when possible.
- The observed population is not the target population. If you don't think about this explicitly, your model will assume they are.
- Coding systems are hierarchical and revisable. ICD-10 came after ICD-9; SNOMED-CT is updated quarterly. Models that ignore this break across institutions and across time.
- OMOP, MEDS, and FHIR are worth the upfront cost. They are the closest thing the field has to a lingua franca.

## How this connects to the rest of the course

- L18 (the next lecture) takes "EHR pathology" as given and asks: *given that*, how should we model with it?
- L19-L20 (clinical text) zoom into one EHR sub-modality.
- L21-L22 (medical imaging) zoom into another.
- L23 (population health and survival) is what you reach for when EHR alone isn't enough.
- L24 (causality and fairness) returns to who's in the data and why.
- L28 (recap) revisits the EHR-as-byproduct claim.

## Source files in this folder

- `Health_Data_Modalities_EHR_Claims_Data.pdf` — the slides as released to students. *The LaTeX source compiles to a 107-page PDF identical to this in content (verified after correcting the source).*
- `latex/Lecture17_EHR_Claims.tex` and `latex/figures/` — the editable Beamer source.
- `nb17_ehr_claims.ipynb` — companion notebook exploring an EHR/claims-style dataset, illustrating the data-quality and cohort-selection issues from the lecture.

## To go deeper

- **Hripcsak & Albers, "Next-generation phenotyping of electronic health records," _JAMIA_ 20, 2013.** The classical statement of the EHR-phenotyping problem. Still relevant.
- **Wells et al., "Strategies for handling missing data in electronic health record derived data," _EGEMS_ 1, 2013.** Why missingness in EHR isn't random.
- **OHDSI Collaborative, _The Book of OHDSI_ (free online).** The full OMOP CDM reference.
- **Arnrich, Choi, Friedman et al., MEDS schema specification (GitHub).** The modality-agnostic event-stream format used in lab 16.
- **Beam, Kohane, "Big Data and Machine Learning in Health Care," _JAMA_ 319(13), 2018.** A short, opinionated piece — pairs well with this lecture's framing.
- **Blacker et al., "Towards a definition of Real-World Data," _NEJM Evid_ 2, 2023.** Useful for the "claims vs. EHR vs. registry" comparison that L23 will return to.

## Study tools

- [Study guide for L17](../study_guides/lecture-17.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
