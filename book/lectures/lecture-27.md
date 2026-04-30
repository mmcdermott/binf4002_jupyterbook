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
- **AlphaFold DB.** ~200M predicted structures, free, queryable. Has rewritten what's possible for proteome-scale analysis.
- **ESMFold.** Fold from a single sequence — no MSA required. Faster, less accurate, but a different tradeoff.
- **AlphaFold limitations.** Disorder, large complexes, novel folds, dynamics, conformational ensembles. Don't treat the predicted structure as ground truth.

**Thread 3: DNA foundation models.**

- **The genomic-modeling challenge.** Long context (regulatory elements can be Mb away from the gene), no clean tokenization, weak per-position labels.
- **Enformer (Avsec et al., 2021).** Long-context transformer over DNA, trained to predict tissue-specific gene expression. Outperforms previous methods on regulatory variant interpretation.
- **Evo (Nguyen et al., 2024).** Decoder-only language model over genomic sequence at scale (millions of base pairs of context).
- **The genomic-FM controversy.** Tang & Koo (2025) argue that current genomic foundation models *don't actually beat well-tuned task-specific models* on regulatory-genomics benchmarks once you control for fair comparison. The story is unsettled.

**Thread 4: 3D molecular models and equivariance.**

- **Why equivariance matters.** A molecule rotated in space is still the *same molecule*. A model that doesn't respect rotation has to learn it from data — wasted capacity. Equivariant neural networks (E(3)-equivariant graph nets) bake the symmetry into the architecture.
- **Equivariant networks for molecular property prediction.** SchNet, EGNN, NequIP, MACE. Each enforces rotation-equivariance differently.
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

## Source files in this folder

- `lec27_modern_bio_ai.pdf` — the slides as released to students. *The LaTeX source compiles to a 57-page PDF identical to this in content (verified).*
- `latex/lec27_modern_bio_ai.tex` and `latex/figures/` — editable Beamer source.
- `nb27_modern_bio_models.ipynb` — companion notebook: ESM-2 embeddings, contact prediction, AlphaFold demos, DNA foundation-model evaluation, equivariance illustration, ProteinMPNN walk-through.

## To go deeper

- **Lin et al., "Evolutionary-scale prediction of atomic-level protein structure" (ESM-2 / ESMFold), _Science_ 379, 2023.**
- **Jumper et al., "Highly accurate protein structure prediction with AlphaFold," _Nature_ 596, 2021.** The AlphaFold 2 paper.
- **Avsec et al., "Effective gene expression prediction from sequence by integrating long-range interactions" (Enformer), _Nat Methods_ 18, 2021.**
- **Nguyen et al., "Sequence modeling and design from molecular to genome scale with Evo," _Science_ 386, 2024.**
- **Dauparas et al., "Robust deep learning–based protein sequence design using ProteinMPNN," _Science_ 378, 2022.**
- **Watson et al., "De novo design of protein structure and function with RFdiffusion," _Nature_ 620, 2023.**
- **Tang & Koo, "Evaluating the representational power of pre-trained DNA language models for regulatory genomics," _Genome Biology_ 26, 2025.** The genomic-FM critique. Read alongside Enformer / Evo.
- **Geiger et al., "e3nn: Euclidean neural networks," arXiv:2207.09453.** The equivariance toolkit.
- **Coursera/edX courses on _Computational Structural Biology_ and _Drug Discovery_ — multiple options for hands-on companions.**

## Study tools

- [Study guide for L27](../study_guides/lecture-27.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
