# L17 Study Guide — EHR & Claims Data: The Modality

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

## Key Terms

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

## The Central Claim

```{admonition} EHR data are byproducts of care, not designed measurements
:class: warning
A vital sign is in the EHR because someone took it. Someone took it because the patient was sick enough, or it was routine, or the protocol required it. **Whether a measurement exists is informative. Whether a code is recorded is informative. Whether a patient came back is informative.** None of this is iid sampling from a population distribution.
```

## Cohort Selection As a Modeling Problem

```{admonition} "Patients with diabetes" sounds simple
:class: tip
…but defining it from EHR data requires choosing: a code set (which ICD-10 codes? include E11.x but exclude E10.x?), an observation window (when?), an exclusion list (gestational diabetes? prediabetes?), a denominator (all patients in the system? those with at least one encounter?). Two reasonable definitions can yield very different cohorts and different conclusions. **Document them.**
```

## Self-Check Questions

1. Patient A has a diagnosis of hypertension with three encounters in 2024. Patient B has the same diagnosis and one encounter. Why might these patients have *systematically different* downstream outcomes that are not about disease severity?
2. Why is "missing lab value" not the same kind of missingness as "missing answer on a survey"? Give one concrete clinical example where the *fact of measurement* is more informative than its value.
3. ICD-9 → ICD-10 transition (US: October 2015) added many codes and changed the structure. What does this do to a model trained on pre-2015 data and deployed in 2025?
4. OMOP, MEDS, FHIR. Match each to: "billing-derived dataset across multiple sites," "modality-agnostic event-stream format," "API standard for clinical interoperability."
5. Berkson's paradox in one sentence: how can you avoid it when defining your study cohort?

## Additional Resources

- [The Book of OHDSI (free online)](https://book.ohdsi.org/) — OMOP CDM reference. Skim Ch. 1-5.
- [MEDS schema (GitHub)](https://github.com/Medical-Event-Data-Standard/meds) — modality-agnostic event-stream format.
- [Hripcsak & Albers, "Next-generation phenotyping of EHRs," *JAMIA* 20, 2013](https://academic.oup.com/jamia/article/20/1/117/2909002) — phenotyping foundations.
- [Wells et al., "Strategies for handling missing data in EHR-derived data," *EGEMS* 1, 2013](https://egems.academyhealth.org/articles/10.13063/2327-9214.1035) — missingness in EHRs is *not* random.
- [Beam & Kohane, "Big Data and ML in Health Care," *JAMA* 319(13), 2018](https://jamanetwork.com/journals/jama/fullarticle/2675024).

## Clinical Context

```{admonition} Who's actually in your dataset?
:class: important
Insurance status, geographic catchment, language, socioeconomic status, healthcare-seeking behavior — all select who shows up in any given EHR. The observed cohort is not the population. If you don't account for this, your model assumes they are the same.
```

> See also: [L17 lecture page](../lectures/lecture-17.md). Companion notebook: [`nb17_ehr_claims.ipynb`](../lectures/nb-17-ehr-claims.ipynb).
