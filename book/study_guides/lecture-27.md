# L27 Study Guide — Modern Biological AI

## Key Terms

| Term | Definition |
|---|---|
| **Protein language model (pLM)** | Transformer trained with masked / autoregressive language modeling on amino-acid sequences. ESM-2 is the canonical example. |
| **ESM-2** | Lin et al. 2023. Scales: 8M to 15B parameters. Transformer-encoder in the BERT family applied to amino-acid tokens. |
| **Contact / coevolution *signal*** | Some pLM attention heads and embeddings *correlate with* structural contacts and evolutionary constraints — even from a single sequence at inference. **Not the same as** explicit MSA-derived coevolutionary couplings (DCA-style); read attention as a useful diagnostic, not a causal coupling score. |
| **Protein embedding** | A continuous representation of a protein from a pLM. Useful as input features for many downstream protein tasks. |
| **Zero-shot variant-effect prediction** | Score how unlikely a mutation is under the pLM. Often *competitive with, and on some benchmarks outperforming,* SIFT / PolyPhen. Conclusion is dataset-, split-, and endpoint-dependent — there is no blanket ranking. |
| **AlphaFold 2** | Jumper et al. 2021. Sequence + MSA → 3D structure. Combines an evoformer (transformer over residues + MSA) with a structure module. CASP14 winner. |
| **pLDDT** | Predicted Local Distance Difference Test. Per-residue confidence in [0, 100]. *Use it. Always.* Distinguishes well-predicted regions from disordered or wrong ones. |
| **AlphaFold DB** | ~200M predicted structures, free, queryable. Has rewritten what's possible for proteome-scale analysis. |
| **ESMFold** | Single-sequence structure predictor (no MSA). Faster, less accurate. Different tradeoff. |
| **Enformer** | Avsec et al. 2021. Long-context transformer over DNA, predicts tissue-specific gene expression. |
| **Evo** | Nguyen et al. 2024. Decoder-only LM over genomic sequence at million-base-pair scale. |
| **Genomic-FM controversy** | Tang & Koo (2025) argue current genomic FMs *don't actually beat* well-tuned task-specific models on regulatory-genomics benchmarks once compared fairly. |
| **Equivariant neural network** | Architecture that respects symmetries of the input (e.g., E(3)-equivariance: rotations and translations of a molecule give correspondingly transformed outputs). NequIP, MACE, EGNN. |
| **Inverse folding** | Given a protein backbone, generate a sequence that folds to it. ProteinMPNN. |
| **Generative protein design** | De-novo generation of protein structures. RFdiffusion is the canonical diffusion-based tool. |
| **Validation gap** | Computational design is cheap; *experimental* validation in the wet lab is the bottleneck and what makes a generative biology result a *result* rather than a hypothesis. |

## The Running Question

```{admonition} Do these models actually understand biology?
:class: warning
"Yes, but" — and the qualifier is the load-bearing intellectual content of the lecture. The same recipes (transformer + NLL + scale) keep winning across biological domains. That's impressive *and* a reason for caution: a recipe that wins on syntactic similarity may not capture function. Domain constraints (equivariance for 3D, MSAs for structure, long context for genomics) still dominate.
```

## pLDDT Is Not Optional

```{admonition} Trust the confidence
:class: warning
A predicted AlphaFold structure with pLDDT < 50 in a region likely indicates **disorder, low confidence, or a wrong prediction**. Treating low-pLDDT regions as ground truth is the canonical AlphaFold-DB misuse. Always plot pLDDT alongside the predicted structure.
```

## Generative Biology Requires Wet-Lab Validation

```{admonition} A computational design without experimental confirmation is a hypothesis
:class: important
Predictive models are validated against held-out test sets. Generative models — design a protein! — have to be validated *experimentally*, and almost all generation papers under-report failure rates. When reading an RFdiffusion / ProteinMPNN paper, look for: how many designs were synthesized, how many folded as predicted, how many had the intended function.
```

## Self-Check Questions

1. ESM-2 attention heads carry contact-relevant signal even though no MSA is supplied at inference. What is the right way to phrase this — "the model has discovered coevolution," "attention recovers MSA couplings," or "single-sequence statistics correlate with structural constraints"? Which framing is most accurate, and why?
2. AlphaFold 2 predictions come with pLDDT scores. Walk through the consequences of ignoring pLDDT in three downstream use cases.
3. Genomic foundation models (Enformer, Evo) face a critique that they don't outperform task-specific models. What do you think the reasonable interpretation of this critique is?
4. Equivariance for 3D molecules: state the symmetry being respected, and explain why baking it into the architecture is more efficient than learning it from data.
5. ProteinMPNN does inverse folding. Why is the inverse problem (sequence given structure) different from the forward problem (structure given sequence), and which is "harder"?

## Additional Resources

- [Lin et al., "Evolutionary-scale prediction of atomic-level protein structure" (ESM-2 / ESMFold), *Science* 379, 2023](https://www.science.org/doi/10.1126/science.ade2574).
- [Jumper et al., "Highly accurate protein structure prediction with AlphaFold," *Nature* 596, 2021](https://www.nature.com/articles/s41586-021-03819-2). The AlphaFold 2 paper.
- [Avsec et al., "Effective gene expression prediction from sequence" (Enformer), *Nat Methods* 18, 2021](https://www.nature.com/articles/s41592-021-01252-x).
- [Nguyen et al., "Sequence modeling and design from molecular to genome scale with Evo," *Science* 386, 2024](https://www.science.org/doi/10.1126/science.ado9336).
- [Dauparas et al., "Robust deep learning–based protein sequence design using ProteinMPNN," *Science* 378, 2022](https://www.science.org/doi/10.1126/science.add2187).
- [Watson et al., "De novo design of protein structure and function with RFdiffusion," *Nature* 620, 2023](https://www.nature.com/articles/s41586-023-06415-8).
- [Tang & Koo, "Evaluating the representational power of pre-trained DNA LMs for regulatory genomics," *Genome Biology* 26, 2025](https://genomebiology.biomedcentral.com/) — read alongside Enformer / Evo.
- [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk).
- [ESM Atlas](https://esmatlas.com).
- [e3nn — Euclidean neural networks library](https://docs.e3nn.org/) — for equivariant networks.

> See also: [L27 lecture page](../lectures/lecture-27.md). Companion notebook: [`nb27_modern_bio_models.ipynb`](../lectures/nb-27-modern-bio-models.ipynb).
