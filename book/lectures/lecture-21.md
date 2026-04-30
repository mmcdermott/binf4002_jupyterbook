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

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **X-ray (radiograph)** | 2D projection imaging using ionizing radiation. Cheap, ubiquitous. CXR (chest X-ray) is the most-published medical-imaging task. |
| **CT (computed tomography)** | Volumetric: a stack of 2D slices forming a 3D volume. Each voxel has a *Hounsfield unit* representing tissue density. |
| **MRI** | Volumetric, multi-sequence imaging (T1, T2, FLAIR, DWI). One "study" is a multi-channel 3D dataset. |
| **Histopathology / WSI** | Whole-slide images: gigapixel digitized pathology slides (e.g., 50,000 × 50,000 pixels at 20× magnification). |
| **DICOM** | Digital Imaging and Communications in Medicine — the standard for medical-image exchange. Each image carries metadata: scanner, acquisition parameters, study description, etc. |
| **Hounsfield unit (HU)** | Quantitative scale for CT intensities; air = −1000, water = 0, bone ≈ +1000. Semantically meaningful — don't normalize them away. |
| **Windowing** | Mapping HU range → 8-bit display range (lung window, bone window, brain window). A *display* choice, not a data-modification choice. |
| **Multi-instance learning (MIL)** | A formulation for gigapixel data: split slide into patches, encode each, aggregate to a slide-level prediction. Forced by data size. |
| **Shortcut learning** | Model learns an unintended side-channel correlation (DICOM metadata, dataset artifacts) instead of the intended signal. Catastrophic at deployment. |
| **Acquisition artifact** | Motion blur, partial-volume effects, scanner-specific calibration drift, etc. Often a real signal models latch onto for the wrong reasons. |

### Why Medical Images Are Not Natural Images

```{admonition} Medical images differ from natural images in...
:class: tip
- **Channel structure**: typically grayscale or single-channel volumetric, not RGB.
- **Intensity semantics**: HU on CT means tissue density; MRI sequence is a tissue-property choice. These intensities *mean* something.
- **Acquisition physics**: controlled, parameterized, scanner-specific.
- **Interpretation**: by trained specialists, in clinical context (history, symptoms).
- **Datasets**: smaller and far more biased toward the institutions that share.

ImageNet pretraining still helps — surprisingly often — but you can't shortcut this lecture and assume "natural-image ML" transfers cleanly.
```

### Shortcut Learning Is *the* Failure Mode

```{admonition} Real examples
:class: warning
- A "pneumonia classifier" learns to detect "this CXR was taken at the COVID hospital" rather than pneumonia.
- A "fracture detector" keys on the radiologist's annotation marker.
- A "skin-cancer classifier" keys on the surgical-marker pen ink.

These are not bugs in particular models — they are predictable consequences of training on data with side-channel information. **If you don't have between-site validation, you don't have evidence the model generalizes.**
```

### Self-Check Questions

1. CT and MRI are both volumetric. Why does feeding them as a stack of independent 2D slices to a 2D CNN throw away information? What's the correct approach?
2. A whole-slide pathology image is 50,000 × 50,000 pixels. Walk through why MIL is forced by the data, not chosen.
3. DICOM metadata includes scanner manufacturer and study description. Name two ways this is *useful* for ML and two ways it's a *shortcut hazard*.
4. A pneumonia-classifier paper reports AUROC 0.95 on internal validation. What single experiment would make you trust it for deployment elsewhere? What would make you not?
5. Hounsfield units are physically meaningful. What would standardize-to-zero-mean-unit-variance do to them, and when (if ever) is that the right preprocessing?

### Additional Resources

- [Litjens et al., "A survey on deep learning in medical image analysis," *Med Image Anal* 42, 2017](https://www.sciencedirect.com/science/article/pii/S1361841517301135) — older but the cleanest map of the field.
- [DeGrave, Janizek & Lee, "AI for radiographic COVID-19 detection selects shortcuts over signal," *Nat Mach Intell* 3, 2021](https://www.nature.com/articles/s42256-021-00338-7) — the canonical recent shortcut paper.
- [Zech et al., "Variable generalization performance of a CXR pneumonia detector," *PLOS Med* 15, 2018](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002683) — the paper that made the field take cross-site evaluation seriously.
- [Mårtensson et al., "Reliability of a deep-learning model in clinical OOD MRI data," *Med Image Anal* 66, 2020](https://www.sciencedirect.com/science/article/pii/S1361841520301754).
- [DICOM Standard](https://www.dicomstandard.org) — skim once.
- [Pianykh, *Digital Imaging and Communications in Medicine: A Practical Introduction and Survival Guide*](https://link.springer.com/book/10.1007/978-3-642-10850-1) — friendlier book-form intro to DICOM.
