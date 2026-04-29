# L21 Study Guide — Medical Imaging: The Modality

## Key Terms

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

## Why Medical Images Are Not Natural Images

```{admonition} Medical images differ from natural images in...
:class: tip
- **Channel structure**: typically grayscale or single-channel volumetric, not RGB.
- **Intensity semantics**: HU on CT means tissue density; MRI sequence is a tissue-property choice. These intensities *mean* something.
- **Acquisition physics**: controlled, parameterized, scanner-specific.
- **Interpretation**: by trained specialists, in clinical context (history, symptoms).
- **Datasets**: smaller and far more biased toward the institutions that share.

ImageNet pretraining still helps — surprisingly often — but you can't shortcut this lecture and assume "natural-image ML" transfers cleanly.
```

## Shortcut Learning Is *the* Failure Mode

```{admonition} Real examples
:class: warning
- A "pneumonia classifier" learns to detect "this CXR was taken at the COVID hospital" rather than pneumonia.
- A "fracture detector" keys on the radiologist's annotation marker.
- A "skin-cancer classifier" keys on the surgical-marker pen ink.

These are not bugs in particular models — they are predictable consequences of training on data with side-channel information. **If you don't have between-site validation, you don't have evidence the model generalizes.**
```

## Self-Check Questions

1. CT and MRI are both volumetric. Why does feeding them as a stack of independent 2D slices to a 2D CNN throw away information? What's the correct approach?
2. A whole-slide pathology image is 50,000 × 50,000 pixels. Walk through why MIL is forced by the data, not chosen.
3. DICOM metadata includes scanner manufacturer and study description. Name two ways this is *useful* for ML and two ways it's a *shortcut hazard*.
4. A pneumonia-classifier paper reports AUROC 0.95 on internal validation. What single experiment would make you trust it for deployment elsewhere? What would make you not?
5. Hounsfield units are physically meaningful. What would standardize-to-zero-mean-unit-variance do to them, and when (if ever) is that the right preprocessing?

## Additional Resources

- [Litjens et al., "A survey on deep learning in medical image analysis," *Med Image Anal* 42, 2017](https://www.sciencedirect.com/science/article/pii/S1361841517301135) — older but the cleanest map of the field.
- [DeGrave, Janizek & Lee, "AI for radiographic COVID-19 detection selects shortcuts over signal," *Nat Mach Intell* 3, 2021](https://www.nature.com/articles/s42256-021-00338-7) — the canonical recent shortcut paper.
- [Zech et al., "Variable generalization performance of a CXR pneumonia detector," *PLOS Med* 15, 2018](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002683) — the paper that made the field take cross-site evaluation seriously.
- [Mårtensson et al., "Reliability of a deep-learning model in clinical OOD MRI data," *Med Image Anal* 66, 2020](https://www.sciencedirect.com/science/article/pii/S1361841520301754).
- [DICOM Standard](https://www.dicomstandard.org) — skim once.
- [Pianykh, *Digital Imaging and Communications in Medicine: A Practical Introduction and Survival Guide*](https://link.springer.com/book/10.1007/978-3-642-10850-1) — friendlier book-form intro to DICOM.

> See also: [L21 lecture page](../lectures/lecture-21.md). Companion notebook: [`nb21_medical_imaging_data.ipynb`](../lectures/nb-21-imaging-data.ipynb).
