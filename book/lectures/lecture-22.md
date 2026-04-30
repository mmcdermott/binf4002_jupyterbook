# Lecture 22 — Medical imaging: modeling

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

**Thu Apr 9, 2026 · Part 3 — Health data modalities · §3.3 Medical imaging**

## What this lecture is about

Now that you understand the imaging data (L21), this lecture is about the modeling toolkit. Imaging is the domain where architectural inductive bias does the most work: a CNN's locality and translation-equivariance assumptions give you a reasonable model with very little data, and a U-Net's encoder-decoder skip-connection structure is *the* prior for medical-image segmentation.

We work through the modeling toolbox in the order most projects use it.

- **Transfer learning from ImageNet.** The default starting point. You'd think natural-image features wouldn't transfer to grayscale chest X-rays — they do, surprisingly well, especially the early layers (which learn edge and texture detectors). Later layers re-learn for the medical domain.
- **Domain-specific pretraining.** RadImageNet (CT/MRI/X-ray), MedSAM (segmentation), CheXzero. Helps when task and domain match the pretraining; can hurt when they don't.
- **Self-supervised pretraining.** Contrastive (SimCLR, MoCo) and masked-image (MAE) approaches that use unlabeled medical images. Useful when labels are scarce but unlabeled data abound.
- **Chest X-ray classification (CheXNet, DenseNet-121).** The canonical CXR pipeline: ImageNet-pretrained DenseNet, fine-tuned for multi-label CXR pathology. Read the original paper, it set the template.
- **Segmentation and U-Net.** The U-shape: encoder downsamples, decoder upsamples, skip connections preserve spatial detail. Skip connections are the key — without them, the decoder can't recover boundaries. nnU-Net is the modern auto-configured U-Net that wins most medical-segmentation challenges.
- **Segmentation losses and metrics.** Dice loss (= 1 - Dice coefficient) is the workhorse. Weighted cross-entropy when classes are imbalanced. Boundary-aware losses (HD95, focal-Tversky) for rare structures. The metric you optimize ≠ the metric you report.
- **Multi-instance learning (MIL) for pathology.** Whole-slide images are too big for end-to-end training. The MIL formulation: split into patches, encode patches, aggregate to a slide-level prediction. Attention-MIL (Ilse et al.) is the standard aggregator.
- **Modality-specific augmentation.** What's a *valid* augmentation for medical images? Random rotation makes sense for histopathology (rotation-invariant) but not for CXRs (heart is on the left). Random intensity changes can simulate scanner variation but can also break the semantic meaning of Hounsfield units. Augmentation is a domain choice.
- **Class imbalance.** Most pathology is rare. Loss reweighting, sampling strategies, and threshold tuning all matter.
- **Multi-site generalization.** The hard problem from L21. Mitigation strategies: federated learning, harmonization (ComBat for radiomics), domain-adversarial training, test-time adaptation. All have caveats.
- **Garden of forking paths in evaluation.** Pre-register your evaluation pipeline. Otherwise the choices made downstream of model training will inflate apparent performance.

## Why it matters

Three reasons this lecture is the practical core of medical-imaging ML:

**Architecture choice is the model.** A linear classifier on raw pixels won't work; a deep CNN will. A 2D CNN sliced over volumetric CT will work less well than a 3D CNN that respects the volume structure. A patch classifier on histopathology won't work; an MIL-aggregated patch classifier will. The architectural prior carries most of the modeling weight.

**Segmentation and classification have different evaluation cultures.** Classification papers report AUROC; segmentation papers report Dice. They are not interchangeable. A "great Dice on validation" can come with terrible boundary localization (HD95) — and vice versa.

**Multi-site generalization is the open problem.** A model that is excellent at one hospital and useless at another isn't a model that "didn't generalize"; it's a model whose distribution-shift properties weren't characterized. The lecture closes with this because it's the most common failure mode in practice.

## Things you should walk away believing

- ImageNet transfer is a strong default starting point even for grayscale medical images.
- Domain-specific pretraining is helpful when task and domain match. It is not a free win.
- U-Net is the right structural prior for segmentation. Skip connections are essential, not decorative.
- Dice loss + Dice score is the workhorse pair for segmentation; pick boundary-aware metrics for boundary-sensitive tasks.
- Multi-instance learning is forced by gigapixel pathology data; attention-MIL is the standard aggregator.
- Modality-specific augmentation is a *domain* choice. Don't blindly apply ImageNet augmentations.
- Multi-site generalization fails by default. Demonstrate it; don't assume it.

## How this connects to the rest of the course

- L13 (NN training mechanics) is the substrate; this lecture is the imaging-specific specialization.
- L15 (foundation models) — RadImageNet, MedSAM, BiomedCLIP are imaging foundation models worth examining through the L15 lens.
- L24 (fairness) — imaging models inherit subgroup performance gaps when trained on biased datasets.
- L10 (generalization, domain shift) — imaging is the modality where the L10 abstract claims become most concrete.
- L27 (modern biological AI) — equivariant networks for 3D molecular structure are an extension of imaging-style inductive bias to molecules.

## Source files in this folder

- `L22.pdf` — the slides as released to students. *The LaTeX source compiles to a 62-page PDF identical to this in content (verified).*
- `latex/lec22_imaging_modeling.tex` and `latex/figures/` — the editable Beamer source.
- `nb22_medical_imaging_modeling.ipynb` — companion notebook with feature-comparison, fine-tuning curves, U-Net comparison, loss comparison, MIL, augmentation ablation, and a real segmentation demo.

## To go deeper

- **Rajpurkar et al., "CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning," arXiv:1711.05225, 2017.** The CXR template-setting paper. Read once.
- **Ronneberger, Fischer & Brox, "U-Net: Convolutional Networks for Biomedical Image Segmentation," _MICCAI_ 2015.** The U-Net paper.
- **Isensee et al., "nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation," _Nat Methods_ 18, 2021.** The auto-configured U-Net that wins everything.
- **Ilse, Tomczak & Welling, "Attention-based Deep Multiple Instance Learning," _ICML_ 2018.** Attention-MIL.
- **Raghu et al., "Transfusion: Understanding Transfer Learning for Medical Imaging," _NeurIPS_ 2019.** What transfers from ImageNet, what doesn't.
- **Azizi et al., "Big Self-Supervised Models Advance Medical Image Classification," _ICCV_ 2021.** When self-supervision wins.
- **Glocker et al., "Risk of Bias in Chest Radiography Deep Learning Foundation Models," _Radiology AI_ 5, 2023.** A sober look at multi-site generalization with foundation models.

## Study tools

- [Study guide for L22](../study_guides/lecture-22.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
