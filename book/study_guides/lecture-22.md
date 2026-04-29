# L22 Study Guide — Medical Imaging: Modeling

## Key Terms

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

## Architecture Choice Is the Model

```{admonition} You can't shortcut the architectural prior
:class: tip
- Linear classifier on raw pixels won't work.
- Deep CNN will work — but a 2D CNN sliced over volumetric CT works less well than a 3D CNN that respects the volume.
- Patch classifier on histopathology won't work; an MIL-aggregated patch classifier will.
The architectural prior carries most of the modeling weight.
```

## Segmentation vs. Classification Cultures

```{admonition} They are not interchangeable
:class: warning
Classification papers report AUROC; segmentation papers report Dice. They measure different things. **A great Dice on validation can come with terrible boundary localization (HD95) — and vice versa.** Always look at the metric matched to the task, and ideally a boundary-aware metric for boundary-sensitive tasks.
```

## Self-Check Questions

1. ImageNet transfer is surprisingly effective for CXR classification. Why? Which layers tend to transfer well?
2. U-Net's skip connections are described as "essential, not decorative." Walk through what fails without them.
3. Dice loss is the default for segmentation. Why not just plain cross-entropy on per-pixel labels? When does Dice fail?
4. MIL with attention pooling: name one advantage over simple mean-pooling per slide.
5. A model trained on CXRs from hospital A drops in performance on hospital B. Name three mitigation strategies and the assumption each makes.

## Additional Resources

- [Rajpurkar et al., "CheXNet" (2017)](https://arxiv.org/abs/1711.05225) — the CXR template-setting paper.
- [Ronneberger, Fischer & Brox, "U-Net," *MICCAI* 2015](https://arxiv.org/abs/1505.04597).
- [Isensee et al., "nnU-Net," *Nat Methods* 18, 2021](https://www.nature.com/articles/s41592-020-01008-z).
- [Ilse, Tomczak & Welling, "Attention-based Deep MIL," *ICML* 2018](https://arxiv.org/abs/1802.04712).
- [Raghu et al., "Transfusion: Understanding Transfer Learning for Medical Imaging," *NeurIPS* 2019](https://arxiv.org/abs/1902.07208).
- [Azizi et al., "Big Self-Supervised Models Advance Medical Image Classification," *ICCV* 2021](https://arxiv.org/abs/2101.05224).
- [Glocker et al., "Risk of Bias in CXR Foundation Models," *Radiology AI* 5, 2023](https://pubs.rsna.org/doi/10.1148/ryai.230060).

> See also: [L22 lecture page](../lectures/lecture-22.md). Companion notebook: [`nb22_medical_imaging_modeling.ipynb`](../lectures/nb-22-imaging-modeling.ipynb).
