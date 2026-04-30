# Lecture 27 — Modern biological AI

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Apr 28, 2026 · Part 5 — Molecules & biological AI**

## What this lecture is about

The past few years have produced a string of stunning results in biological AI: ESM-2 protein language models, AlphaFold 2 structure prediction, Enformer / Evo DNA foundation models, ProteinMPNN inverse folding, RFdiffusion generative protein design. This lecture is a guided tour through all of them, with one running question: *do these models actually understand biology, or are they fitting patterns that happen to be biologically interesting?*

The answer is "yes, but" — yes they're useful and often state-of-the-art, but the qualifier matters and is the load-bearing intellectual content of the lecture.

We move through five threads.

**Thread 1: Protein language models.**

- **ESM-2 (Lin et al., 2023).** Masked language modeling on a protein-sequence corpus. Transformer-encoder architecture in the BERT family, applied to amino-acid tokens. Scales: 8M to 15B parameters.
- **Attention as a contact / coevolution *signal*.** Some attention heads and learned embeddings in protein LMs *correlate with* structural contacts and evolutionary constraints, and single-sequence LMs can support contact-relevant predictions. This is **not** the same as explicitly estimating coevolutionary couplings from an MSA (DCA-style); attention should be read as a useful diagnostic signal, not as a causal coupling score.
- **Protein embeddings.** ESM-2 produces a continuous representation of any protein. Useful as input features for many downstream protein tasks.
- **Zero-shot variant-effect prediction.** Score how unlikely a mutation is under the protein LM. Often *competitive with, and on some benchmarks outperforming,* classical predictors such as SIFT and PolyPhen. The conclusion depends strongly on the benchmark, variant set, train/test leakage, and whether the endpoint is molecular fitness or clinical pathogenicity — there is no blanket ranking.
- **What protein LMs miss.** Multimer interactions, post-translational modifications, condition-specific behavior, anything outside the training distribution.

**Thread 2: AlphaFold-style structure prediction.**

- **AlphaFold 2 (Jumper et al., 2021).** Sequence + MSA → 3D structure. Combines an evoformer (transformer over residues + MSA) with a structure module (geometry-aware decoding). Won CASP14 by a large margin; the field changed.
- **pLDDT (predicted Local Distance Difference Test).** Per-residue confidence score in [0, 100]. Distinguishes "this region is well-predicted" from "this region might be wrong" or "this region is intrinsically disordered." Use it. Always.
- **AlphaFold DB.** ~214M predicted structures (as of 2025), free, queryable. Has rewritten what's possible for proteome-scale analysis.
- **ESMFold.** Fold from a single sequence — no MSA required. Faster, less accurate, but a different tradeoff.
- **AlphaFold limitations.** Disorder, large complexes, novel folds, dynamics, conformational ensembles. Don't treat the predicted structure as ground truth.

**Thread 3: DNA foundation models.**

- **The genomic-modeling challenge.** Long context (regulatory elements can be Mb away from the gene), no clean tokenization, weak per-position labels.
- **Enformer (Avsec et al., 2021).** Long-context transformer over DNA, trained to predict tissue-specific gene expression. Outperforms previous methods on regulatory variant interpretation.
- **Evo (Nguyen et al., 2024).** Decoder-only language model over genomic sequence; Evo 1 supports ~131k bp of context, with the Evo 2 follow-up extending toward ~1M bp.
- **The genomic-FM controversy.** Tang & Koo (2025) argue that current genomic foundation models *don't actually beat well-tuned task-specific models* on regulatory-genomics benchmarks once you control for fair comparison. The story is unsettled.

**Thread 4: 3D molecular models and equivariance.**

- **Why equivariance matters.** A molecule rotated or translated in space is still the *same molecule*. A model that doesn't respect those symmetries has to learn them from data — wasted capacity. Equivariant graph nets bake the symmetry into the architecture.
- **SE(3) vs. E(3).** Most modern molecular networks (NequIP, MACE) target **SE(3)-equivariance** — rotations and translations only. They deliberately *exclude* reflections, because chiral molecules (most drugs, all amino acids) are *not* invariant under reflection: a chiral molecule's mirror image is a different chemical entity, often with very different biological activity (the canonical cautionary example is thalidomide). E(3) (which adds reflections) would force the model to give the same output for a molecule and its mirror image — wrong for chirality-sensitive tasks.
- **Equivariant networks for molecular property prediction.** SchNet, EGNN, NequIP, MACE. Each enforces rotation/translation-equivariance differently; SE(3)-equivariant variants preserve chirality.
- **Why this is the right inductive bias.** It's the L13 architecture-as-prior point applied to the geometry of molecules.

**Thread 5: Generative protein design.**

- **The shift from prediction to design.** AlphaFold predicts structure from sequence. The inverse — design a sequence that folds to a given structure — is **inverse folding**. Generating *new* structures de novo is **structure generation**.
- **ProteinMPNN (Dauparas et al., 2022).** A graph-neural-network for inverse folding. Given a backbone, what sequence will fold to it? Practical for protein engineering.
- **RFdiffusion (Watson et al., 2023).** Diffusion model over protein backbones. Generates novel structures. The first really practical de novo protein-design tool.
- **Validation requirements for designed biology.** Computational design is cheap; experimental validation is the bottleneck. Every "RFdiffusion designed N proteins" claim should be paired with "K of them folded as predicted in the wet lab."

## Why it matters

Three reasons this lecture is the conceptual capstone of the biological AI arc:

**The same paradigm (sequence-modeling, NLL, scale) keeps winning across biological domains.** ESM-2 is a transformer in the BERT family applied to protein sequences; Evo is a long-context decoder LM applied to genomes. The *paradigm reuse* is genuinely impressive — but the architectures are not literally identical to natural-language LLMs (long context, MSA-derived inputs, equivariance constraints all change the model class), and a recipe that wins on syntactic-similarity-style benchmarks may not capture function.

**Domain constraints still dominate.** Equivariance for 3D molecules. MSAs for protein structure. Long context for regulatory genomics. The architectural choices are *about* what biology forces, not about NN trends.

**Generative biology shifts the validation frame.** Predictive models are validated against held-out test sets. Generative models — design a protein! — have to be validated *experimentally* in the wet lab, and almost all generation papers under-report failure rates.

## Things you should walk away believing

- Protein language models learn statistical regularities from large protein corpora that *correlate with* structural and evolutionary constraints. Some attention heads and embeddings carry contact-relevant signal — useful — but they are not the same as explicit MSA-derived coevolutionary couplings.
- pLDDT is the AlphaFold confidence score. Use it. Don't trust low-pLDDT regions.
- Genomic foundation models are an active research area with unsettled claims. Read the critique alongside the proposals.
- Equivariant networks are the right inductive bias for 3D molecules. Most current best-in-class methods use them.
- ProteinMPNN, RFdiffusion, and friends are practical tools, not just demos. They are being used in real protein-engineering workflows.
- Generative biology requires experimental validation. A computational design without a wet-lab confirmation is a hypothesis, not a result.
- Every modern biological AI claim has a "foundation model over what?" question (callback to L15).

## How this connects to the rest of the course

- L25 (DNA, genetics) and L26 (proteins, molecules) are the substrate.
- L14 (LLMs) provides the *paradigm* (sequence modeling, NLL, scale, transfer); modern biological AI reuses this paradigm but the architectures are domain-specific (long-context, MSA-aware, 3D-equivariant).
- L15 (foundation models) — every system in this lecture is a foundation model claim; ask the L15 questions.
- L13 (NN architecture as inductive bias) — equivariant networks are the cleanest example.
- L24 (fairness) — biological AI inherits training-data biases (Eurocentric genome data; PDB skewed toward soluble proteins).
- L10 (generalization) — out-of-distribution failures are the rule for biological generative models.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Protein language model (pLM)** | Transformer trained with masked / autoregressive language modeling on amino-acid sequences. ESM-2 is the canonical example. |
| **ESM-2** | Lin et al. 2023. Scales: 8M to 15B parameters. Transformer-encoder in the BERT family applied to amino-acid tokens. |
| **Contact / coevolution *signal*** | Some pLM attention heads and embeddings *correlate with* structural contacts and evolutionary constraints — even from a single sequence at inference. **Not the same as** explicit MSA-derived coevolutionary couplings (DCA-style); read attention as a useful diagnostic, not a causal coupling score. |
| **Protein embedding** | A continuous representation of a protein from a pLM. Useful as input features for many downstream protein tasks. |
| **Zero-shot variant-effect prediction** | Score how unlikely a mutation is under the pLM. Often *competitive with, and on some benchmarks outperforming,* SIFT / PolyPhen. Conclusion is dataset-, split-, and endpoint-dependent — there is no blanket ranking. |
| **AlphaFold 2** | Jumper et al. 2021. Sequence + MSA → 3D structure. Combines an evoformer (transformer over residues + MSA) with a structure module. CASP14 winner. |
| **pLDDT** | Predicted Local Distance Difference Test. Per-residue confidence in [0, 100]. *Use it. Always.* Distinguishes well-predicted regions from disordered or wrong ones. |
| **AlphaFold DB** | ~214M predicted structures (as of 2025), free, queryable. Has rewritten what's possible for proteome-scale analysis. |
| **ESMFold** | Single-sequence structure predictor (no MSA). Faster, less accurate. Different tradeoff. |
| **Enformer** | Avsec et al. 2021. Long-context transformer over DNA, predicts tissue-specific gene expression. |
| **Evo** | Nguyen et al. 2024. Decoder-only LM over genomic sequence; Evo 1 ~131k bp context, Evo 2 extends toward ~1M bp. |
| **Genomic-FM controversy** | Tang & Koo (2025) argue current genomic FMs *don't actually beat* well-tuned task-specific models on regulatory-genomics benchmarks once compared fairly. |
| **Equivariant neural network** | Architecture that respects symmetries of the input. Most molecular networks (NequIP, MACE, EGNN) target **SE(3)-equivariance** — rotations and translations only — because chirality breaks reflection symmetry; E(3) would add reflections, which is *wrong* for chiral molecules (thalidomide etc.). |
| **Inverse folding** | Given a protein backbone, generate a sequence that folds to it. ProteinMPNN. |
| **Generative protein design** | De-novo generation of protein structures. RFdiffusion is the canonical diffusion-based tool. |
| **Validation gap** | Computational design is cheap; *experimental* validation in the wet lab is the bottleneck and what makes a generative biology result a *result* rather than a hypothesis. |

### The Running Question

```{admonition} Do these models actually understand biology?
:class: warning
"Yes, but" — and the qualifier is the load-bearing intellectual content of the lecture. The same recipes (transformer + NLL + scale) keep winning across biological domains. That's impressive *and* a reason for caution: a recipe that wins on syntactic similarity may not capture function. Domain constraints (equivariance for 3D, MSAs for structure, long context for genomics) still dominate.
```

### pLDDT Is Not Optional

```{admonition} Trust the confidence
:class: warning
A predicted AlphaFold structure with pLDDT < 50 in a region likely indicates **disorder, low confidence, or a wrong prediction**. Treating low-pLDDT regions as ground truth is the canonical AlphaFold-DB misuse. Always plot pLDDT alongside the predicted structure.
```

### Generative Biology Requires Wet-Lab Validation

```{admonition} A computational design without experimental confirmation is a hypothesis
:class: important
Predictive models are validated against held-out test sets. Generative models — design a protein! — have to be validated *experimentally*, and almost all generation papers under-report failure rates. When reading an RFdiffusion / ProteinMPNN paper, look for: how many designs were synthesized, how many folded as predicted, how many had the intended function.
```

### Self-Check Questions

1. ESM-2 attention heads carry contact-relevant signal even though no MSA is supplied at inference. What is the right way to phrase this — "the model has discovered coevolution," "attention recovers MSA couplings," or "single-sequence statistics correlate with structural constraints"? Which framing is most accurate, and why?
2. AlphaFold 2 predictions come with pLDDT scores. Walk through the consequences of ignoring pLDDT in three downstream use cases.
3. Genomic foundation models (Enformer, Evo) face a critique that they don't outperform task-specific models. What do you think the reasonable interpretation of this critique is?
4. Equivariance for 3D molecules: state the symmetry being respected, explain why baking it into the architecture is more efficient than learning it from data, and explain why most molecular networks target SE(3) and not E(3).
5. ProteinMPNN does inverse folding. Why is the inverse problem (sequence given structure) different from the forward problem (structure given sequence), and which is "harder"?

### Additional Resources

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
