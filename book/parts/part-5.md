# Part 5 — Molecules & Biological AI

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

**Lectures 25-27**

## What this part is about

Part 5 is the molecular tier of the course: DNA → proteins/molecules → modern biological AI. The arc is intentional. L25 establishes the population-genetics substrate (variants, GWAS, regulation) that genomic AI builds on. L26 is an honest tour of the *classical* protein and small-molecule toolkit (sequence alignment, MSAs, PSSMs, fingerprints, docking, QSAR) — the strong baselines that any modern method should be benchmarked against. L27 then tours modern biological AI (ESM-2, AlphaFold, Enformer, Evo, equivariant networks, ProteinMPNN, RFdiffusion) with the running question: *do these models actually understand biology, or are they fitting patterns that happen to be biologically interesting?*

The answer is "yes, but" — and the qualifier is the load-bearing intellectual content of the part.

## Goals for this part

- Read a Manhattan plot and a QQ plot; reason about LD and population stratification; explain why polygenic risk scores transfer poorly across ancestries.
- Build a SMILES → ECFP fingerprint → random-forest baseline; defend a scaffold split; critique a deep-learning paper that claims to "beat classical X."
- Critique an ESM-2 / AlphaFold / Evo claim by asking what task and what evaluation. Use pLDDT correctly. Recognize where genomic foundation models still don't beat task-specific models.
- Sketch an inverse-folding + experimental-validation pipeline. Treat a generative biology paper as a hypothesis until wet-lab validation arrives.

## Key takeaways for this part

- Genetic data are high-D, structured, and population-dependent. Population stratification is the single most important confounder.
- PRS transferability is poor across ancestries — and this matters clinically because it widens, not closes, health disparities.
- Classical methods (MSA, PSSM, SIFT/PolyPhen, ECFP, docking, QSAR) exploit decades of biological knowledge. They are strong baselines; modern methods compete with them only when they encode similar (or stronger) priors.
- Modern biological AI re-uses the transformer + NLL + scale recipe in domain costume. Domain constraints (equivariance for 3D molecules, MSAs for protein structure, long context for genomics) still dominate.
- Generative biology is *cheap*; experimental validation is the bottleneck. A computational design without wet-lab confirmation is a hypothesis, not a result.

## Lectures in this part

- [L25 — DNA, genetics, gene regulation](../lectures/lecture-25.md)
- [L26 — Proteins, molecules, structural biology](../lectures/lecture-26.md)
- [L27 — Modern biological AI](../lectures/lecture-27.md)

## External resources for this part

**Genetics (L25)**

- Visscher et al., "10 Years of GWAS Discovery: Biology, Function, and Translation," *AJHG* 101, 2017.
- Martin et al., "Clinical use of current polygenic risk scores may exacerbate health disparities," *Nat Genet* 51, 2019. **Required reading.**
- Price et al., "Principal components analysis corrects for stratification in genome-wide association studies," *Nat Genet* 38, 2006.
- GTEx Consortium, "The GTEx Consortium atlas of genetic regulatory effects across human tissues," *Science* 369, 2020.
- ENCODE Project Consortium, "Expanded encyclopaedias of DNA elements," *Nature* 583, 2020.
- Coursera *Genomic Data Science* (Johns Hopkins) — free, multi-course, hands-on companion.

**Proteins & molecules (L26)**

- Berman et al., "The Protein Data Bank," *Nucleic Acids Res* 28, 2000.
- Altschul et al., BLAST, *J Mol Biol* 215, 1990.
- Adzhubei et al., PolyPhen-2, *Nat Methods* 7, 2010 — and Ng & Henikoff, SIFT, *Genome Res* 11, 2001.
- Rogers & Hahn, "Extended-Connectivity Fingerprints," *J Chem Inf Model* 50, 2010 — Morgan/ECFP fingerprints.
- Trott & Olson, "AutoDock Vina," *J Comput Chem* 31, 2010 — the docking workhorse.
- Wu et al., "MoleculeNet: a benchmark for molecular machine learning," *Chem Sci* 9, 2018.

**Modern biological AI (L27)**

- Lin et al., "Evolutionary-scale prediction of atomic-level protein structure" (ESM-2 / ESMFold), *Science* 379, 2023.
- Jumper et al., "Highly accurate protein structure prediction with AlphaFold," *Nature* 596, 2021.
- Avsec et al., "Effective gene expression prediction from sequence by integrating long-range interactions" (Enformer), *Nat Methods* 18, 2021.
- Nguyen et al., "Sequence modeling and design from molecular to genome scale with Evo," *Science* 386, 2024.
- Dauparas et al., "Robust deep learning–based protein sequence design using ProteinMPNN," *Science* 378, 2022.
- Watson et al., "De novo design of protein structure and function with RFdiffusion," *Nature* 620, 2023.
- Tang & Koo, "Evaluating the representational power of pre-trained DNA language models for regulatory genomics," *Genome Biology* 26, 2025 — the genomic-FM critique. Read alongside Enformer / Evo.

**AlphaFold DB and resources for hands-on exploration**

- AlphaFold Protein Structure Database — <https://alphafold.ebi.ac.uk>
- ESM Atlas — <https://esmatlas.com>
- RCSB PDB tutorials — <https://www.rcsb.org/learn>
