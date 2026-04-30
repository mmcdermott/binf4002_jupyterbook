# Lecture 22 — Medical imaging: modeling

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

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

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Transfer learning** | Start from ImageNet (or domain) pre-trained weights, fine-tune on the target task. The default starting point in medical imaging. |
| **Domain-specific pretraining** | Pre-train on a medical-imaging corpus (RadImageNet, MedSAM). Helps when task and domain match. |
| **Self-supervised pretraining** | Use unlabeled images (contrastive: SimCLR, MoCo; masked-image: MAE) to learn representations. |
| **DenseNet-121** | The canonical CXR-classification backbone (Rajpurkar et al., CheXNet). Dense skip connections. |
| **U-Net** | Encoder-decoder with *skip connections* between corresponding levels. The default segmentation architecture. |
| **Skip connection** | Direct path from encoder layer ℓ to decoder layer L−ℓ; preserves spatial detail through the bottleneck. **Essential, not decorative.** |
| **Dice loss / Dice coefficient** | 2·\|A∩B\| / (\|A\|+\|B\|). Standard segmentation loss / metric. |
| **HD95** | 95th-percentile Hausdorff distance — boundary-aware segmentation metric. |
| **MIL aggregator** | Function that pools per-patch predictions to a slide-level decision (max, mean, attention-MIL). Attention-MIL (Ilse et al. 2018) is the standard. |
| **Augmentation** | Synthetic transformations (rotation, flip, brightness) applied during training. Choice must respect the data: rotations OK on histopathology, *not* on CXR (heart is on the left). |
| **Multi-site generalization** | Deployment across hospitals / scanners / populations. Fails by default unless demonstrated. |
| **Garden of forking paths** | Many implicit decisions in the analysis pipeline (preprocessing, splits, augmentation, evaluation metric). Inflates apparent performance unless pre-registered. |
| **nnU-Net** | Self-configuring U-Net pipeline (Isensee et al. 2021). Wins most medical-segmentation challenges. |

### Architecture Choice Is the Model

```{admonition} You can't shortcut the architectural prior
:class: tip
- Linear classifier on raw pixels won't work.
- Deep CNN will work — but a 2D CNN sliced over volumetric CT works less well than a 3D CNN that respects the volume.
- Patch classifier on histopathology won't work; an MIL-aggregated patch classifier will.
The architectural prior carries most of the modeling weight.
```

### Segmentation vs. Classification Cultures

```{admonition} They are not interchangeable
:class: warning
Classification papers report AUROC; segmentation papers report Dice. They measure different things. **A great Dice on validation can come with terrible boundary localization (HD95) — and vice versa.** Always look at the metric matched to the task, and ideally a boundary-aware metric for boundary-sensitive tasks.
```

### Self-Check Questions

1. ImageNet transfer is surprisingly effective for CXR classification. Why? Which layers tend to transfer well?
2. U-Net's skip connections are described as "essential, not decorative." Walk through what fails without them.
3. Dice loss is the default for segmentation. Why not just plain cross-entropy on per-pixel labels? When does Dice fail?
4. MIL with attention pooling: name one advantage over simple mean-pooling per slide.
5. A model trained on CXRs from hospital A drops in performance on hospital B. Name three mitigation strategies and the assumption each makes.

### Additional Resources

- [Rajpurkar et al., "CheXNet" (2017)](https://arxiv.org/abs/1711.05225) — the CXR template-setting paper.
- [Ronneberger, Fischer & Brox, "U-Net," *MICCAI* 2015](https://arxiv.org/abs/1505.04597).
- [Isensee et al., "nnU-Net," *Nat Methods* 18, 2021](https://www.nature.com/articles/s41592-020-01008-z).
- [Ilse, Tomczak & Welling, "Attention-based Deep MIL," *ICML* 2018](https://arxiv.org/abs/1802.04712).
- [Raghu et al., "Transfusion: Understanding Transfer Learning for Medical Imaging," *NeurIPS* 2019](https://arxiv.org/abs/1902.07208).
- [Azizi et al., "Big Self-Supervised Models Advance Medical Image Classification," *ICCV* 2021](https://arxiv.org/abs/2101.05224).
- [Glocker et al., "Risk of Bias in CXR Foundation Models," *Radiology AI* 5, 2023](https://pubs.rsna.org/doi/10.1148/ryai.230060).
