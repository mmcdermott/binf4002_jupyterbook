# Lecture 17 — EHR and claims data: the modality

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

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

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **EHR (Electronic Health Record)** | Clinical record system used by hospitals/clinics; contains diagnoses, procedures, medications, labs, vitals, notes, imaging. *Created by clinicians during care.* |
| **Claims data** | Billing records submitted to payers. Tells you what was *billed*, not what *happened*. More comparable across institutions because billing standards are tighter. |
| **ICD-9 / ICD-10** | International Classification of Diseases. Hierarchical disease-code system. ICD-10 is the current standard in most countries. |
| **CPT** | Current Procedural Terminology. Procedure / service codes used for billing. |
| **RxNorm** | Standardized vocabulary for clinical drugs. |
| **LOINC** | Logical Observation Identifiers Names and Codes — for labs and clinical observations. |
| **SNOMED-CT** | Systematized Nomenclature of Medicine — Clinical Terms. Comprehensive clinical terminology. |
| **OMOP CDM** | Observational Medical Outcomes Partnership Common Data Model. The OHDSI-led standard for harmonizing EHR/claims data. |
| **MEDS** | Medical-Event-Data-Standard. Modality-agnostic event-stream format (timestamp, code, value). |
| **FHIR** | Fast Healthcare Interoperability Resources — HL7 standard for clinical-data APIs. |
| **Berkson's paradox** | Conditioning on a collider (e.g., "patient was hospitalized") creates spurious correlations. The canonical EHR pitfall. |
| **Cohort selection** | Defining the population a study/model applies to (e.g., "diabetic patients ≥ 40 with a recent A1C measurement"). A modeling decision, not preprocessing. |

### The Central Claim

```{admonition} EHR data are byproducts of care, not designed measurements
:class: warning
A vital sign is in the EHR because someone took it. Someone took it because the patient was sick enough, or it was routine, or the protocol required it. **Whether a measurement exists is informative. Whether a code is recorded is informative. Whether a patient came back is informative.** None of this is iid sampling from a population distribution.
```

### Cohort Selection As a Modeling Problem

```{admonition} "Patients with diabetes" sounds simple
:class: tip
…but defining it from EHR data requires choosing: a code set (which ICD-10 codes? include E11.x but exclude E10.x?), an observation window (when?), an exclusion list (gestational diabetes? prediabetes?), a denominator (all patients in the system? those with at least one encounter?). Two reasonable definitions can yield very different cohorts and different conclusions. **Document them.**
```

### Self-Check Questions

1. Patient A has a diagnosis of hypertension with three encounters in 2024. Patient B has the same diagnosis and one encounter. Why might these patients have *systematically different* downstream outcomes that are not about disease severity?
2. Why is "missing lab value" not the same kind of missingness as "missing answer on a survey"? Give one concrete clinical example where the *fact of measurement* is more informative than its value.
3. ICD-9 → ICD-10 transition (US: October 2015) added many codes and changed the structure. What does this do to a model trained on pre-2015 data and deployed in 2025?
4. OMOP, MEDS, FHIR. Match each to: "billing-derived dataset across multiple sites," "modality-agnostic event-stream format," "API standard for clinical interoperability."
5. Berkson's paradox in one sentence: how can you avoid it when defining your study cohort?

### Additional Resources

- [The Book of OHDSI (free online)](https://book.ohdsi.org/) — OMOP CDM reference. Skim Ch. 1-5.
- [MEDS schema (GitHub)](https://github.com/Medical-Event-Data-Standard/meds) — modality-agnostic event-stream format.
- [Hripcsak & Albers, "Next-generation phenotyping of EHRs," *JAMIA* 20, 2013](https://academic.oup.com/jamia/article/20/1/117/2909002) — phenotyping foundations.
- [Wells et al., "Strategies for handling missing data in EHR-derived data," *EGEMS* 1, 2013](https://egems.academyhealth.org/articles/10.13063/2327-9214.1035) — missingness in EHRs is *not* random.
- [Beam & Kohane, "Big Data and ML in Health Care," *JAMA* 319(13), 2018](https://jamanetwork.com/journals/jama/fullarticle/2675024).

### Clinical Context

```{admonition} Who's actually in your dataset?
:class: important
Insurance status, geographic catchment, language, socioeconomic status, healthcare-seeking behavior — all select who shows up in any given EHR. The observed cohort is not the population. If you don't account for this, your model assumes they are the same.
```
