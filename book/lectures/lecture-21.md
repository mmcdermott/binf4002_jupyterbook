# Lecture 21 — Medical imaging: the modality

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Apr 7, 2026 · Part 3 — Health data modalities · §3.3 Medical imaging**

## What this lecture is about

Medical imaging is the canonical "deep-learning success story in healthcare," and that reputation is half-deserved. There are real successes (diabetic retinopathy screening, certain pathology workflows, some chest X-ray applications), but the field is also full of papers whose claimed performance evaporates when you change scanners, sites, or label distributions. To understand both the success and the fragility, you have to understand the *data* before the models — which is what this lecture does.

We work through the major modalities, in roughly the order students will see them in practice:

- **X-ray / radiograph.** 2D projection. Cheap, ubiquitous, often the first imaging modality a hospital uses. Chest X-rays (CXRs) are the most-published medical imaging task and have the largest open datasets.
- **CT (computed tomography).** Volumetric — a stack of 2D slices that together form a 3D volume. Each voxel has a *Hounsfield unit* representing tissue density. Different windowing (lung window, bone window, brain window) is a *display* choice, not a data-modification choice.
- **MRI.** Volumetric, like CT, but with multiple sequences (T1, T2, FLAIR, DWI, etc.) representing different tissue properties. A single "MRI study" is a multi-channel volumetric dataset, not a single image.
- **Histopathology.** *Gigapixel* whole-slide images (WSIs). One slide is 50,000 × 50,000 pixels at 20× magnification — too big to fit in any GPU. The standard ML formulation is **multi-instance learning (MIL)**: split the slide into thousands of patches, predict per-patch features, aggregate.
- **Other modalities.** Retinal fundus photography, dermatoscopy, ultrasound, OCT, mammography, endoscopy. Each has its own acquisition physics and its own data-quality profile.
- **DICOM.** The data standard. Every medical image carries metadata: scanner manufacturer, acquisition parameters, date, patient ID, study description, body part, sometimes annotations. DICOM metadata is *both* essential and dangerous (see "shortcut learning" below).
- **Why medical images are not natural images.** They are grayscale (or single-channel volumetric), have semantically-meaningful intensities (a Hounsfield unit *means* tissue density), are acquired with controlled physics, are interpreted by trained specialists, and the *clinical context* (patient history) often determines what counts as a finding.
- **Data quality issues.** Acquisition artifacts, motion blur, cropping, partial-volume effects, scanner-specific calibration drift.
- **Shortcut learning.** A pneumonia classifier learns to detect "this CXR was taken at the COVID hospital" rather than pneumonia. A fracture detector keys on the radiologist's annotation marker. These failures are not bugs in particular models; they are predictable consequences of training on data with side-channel information.

The paradox flagged is the **Garden of forking paths** — every analysis pipeline involves so many decisions (preprocessing, augmentation, train/test split, evaluation metric) that "p < 0.05" loses meaning unless those decisions are pre-registered.

## Why it matters

Three reasons this lecture is the substrate for L22:

**Medical images are not natural images.** Models pretrained on ImageNet transfer surprisingly well to some medical-imaging tasks, but the transfer is task-dependent and not guaranteed. Domain pretraining (MedSAM, RadImageNet) is sometimes better, sometimes not. You can't shortcut this lecture and just "fine-tune ResNet-50."

**Volumetric and gigapixel data force different architectures.** A 3D CT is not "a stack of 2D images"; treating it that way loses information. A whole-slide pathology image cannot be processed end-to-end on a GPU; MIL is not optional, it is forced by the data.

**Shortcut learning is *the* failure mode.** It is invisible in within-site evaluation and catastrophic at deployment. Every imaging-AI paper since 2019 has had to grapple with it. If you don't have a between-site validation, you don't have evidence the model generalizes.

## Things you should walk away believing

- 2D, volumetric, and gigapixel are different data shapes and force different architectures. CT/MRI need 3D; histopathology needs MIL.
- DICOM metadata is informative (scanner, acquisition parameters) and a shortcut hazard (study description leaks the diagnosis).
- Hounsfield units (CT) and MRI sequence type are *semantic* intensities. Don't normalize them away.
- "Normal" looks different on different scanners. Site generalization is not a nice-to-have.
- Shortcut learning is the default failure mode; demonstrate the model isn't doing it.
- Histopathology is a multi-instance problem from day one. There is no end-to-end whole-slide model.
- Acquisition artifacts and motion blur are real signals that models can latch onto, sometimes for the wrong reasons.

## How this connects to the rest of the course

- L22 (next lecture) takes the imaging-data-side problems as given and builds the modeling toolkit (transfer learning, U-Net, MIL, augmentation).
- L13 (NN) is the architectural background; CNN inductive bias is the right prior for natural images and a *useful* prior for medical images.
- L15 (foundation models) — RadImageNet, MedSAM, BiomedCLIP. Foundation models for medical imaging are an active area.
- L10 (generalization and domain shift) — multi-site generalization on imaging is the canonical example.
- L24 (fairness) — imaging models can encode demographic shortcuts (skin tone in dermatology, scanner type by site demographics).

## Source files in this folder

- `L21.pdf` — the slides as released to students. *The LaTeX source compiles to a 78-page PDF identical to this in content (verified).*
- `latex/main.tex` and `latex/figures/` — editable Beamer source, including CT.gif and brain_mri.gif animations.
- `nb21_medical_imaging_data.ipynb` — companion notebook exploring CXR datasets, CT volumetric data, DICOM metadata, and intensity / windowing operations.

## To go deeper

- **Litjens et al., "A survey on deep learning in medical image analysis," _Med Image Anal_ 42, 2017.** Older but still the cleanest map of the field.
- **Mårtensson et al., "The reliability of a deep learning model in clinical out-of-distribution MRI data: A multicohort study," _Med Image Anal_ 66, 2020.** What multi-site generalization actually looks like when you measure it.
- **DeGrave, Janizek & Lee, "AI for radiographic COVID-19 detection selects shortcuts over signal," _Nat Mach Intell_ 3, 2021.** The canonical recent shortcut-learning paper.
- **Zech et al., "Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study," _PLOS Med_ 15, 2018.** The paper that made the field take cross-site evaluation seriously.
- **DICOM Standard.** [https://www.dicomstandard.org](https://www.dicomstandard.org) — the standard reference. Skim once.
- **Pianykh, _Digital Imaging and Communications in Medicine (DICOM): A Practical Introduction and Survival Guide._** A friendlier book-form intro to DICOM if the spec is too dense.

## Study tools

- [Study guide for L21](../study_guides/lecture-21.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
