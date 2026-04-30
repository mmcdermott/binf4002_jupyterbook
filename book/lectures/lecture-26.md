# Lecture 26 — Proteins, molecules, and structural biology

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Thu Apr 23, 2026 · Part 5 — Molecules & biological AI**

## What this lecture is about

Before modern biological AI (L27), there is a *century* of methods for working with proteins and small molecules — sequence alignment, multiple sequence alignment (MSA), position-specific scoring matrices (PSSMs), homology modeling, QSAR, docking. This lecture is an honest tour of the classical toolkit, and the case for why those classical methods are still strong baselines that modern AI papers should be benchmarked against (a recurring theme of L27 and the course in general).

We split the lecture into two halves: proteins, then small molecules.

**Half 1: Proteins.**

- **Protein biology and structure levels.**
  - **Primary structure.** The amino-acid sequence (length 50-2000 typically).
  - **Secondary structure.** Alpha helices, beta sheets, loops.
  - **Tertiary structure.** The 3D fold of a single chain.
  - **Quaternary structure.** Multi-chain complexes.
- **Experimental structure determination.** X-ray crystallography (high resolution, requires crystallization), NMR (smaller proteins, in solution), cryo-EM (large complexes, recent revolution). Each has trade-offs.
- **The protein data gap.** ~250 million known protein sequences. ~200,000 experimentally-determined structures (PDB). The 1000× gap is the reason structure-prediction matters — and is what AlphaFold (L27) attacked.
- **Evolutionary relationships and sequence conservation.** Proteins related by descent share sequence; conserved positions indicate functional importance.
- **Sequence alignment.** Pairwise alignment (Smith-Waterman, BLAST) — find regions of similarity between two sequences. Used routinely for "what does this new sequence look like?"
- **Multiple sequence alignment (MSA).** Align hundreds-to-thousands of homologous sequences. Reveals which positions are conserved and which co-evolve. The substrate for everything else in this lecture and for AlphaFold.
- **PSSMs (Position-Specific Scoring Matrices).** Per-position amino-acid frequencies extracted from an MSA. Captures "what residue is allowed here?" Used in PSI-BLAST and earlier structure-prediction methods.
- **Coevolution.** Pairs of positions that mutate together suggest spatial contact. The 2010s breakthrough (DCA, EVfold) used coevolution to predict 3D contacts from sequence alone.
- **Variant-effect prediction.** SIFT (sequence conservation) and PolyPhen (sequence + structural features) predict whether a missense variant is likely to disrupt function. *Still strong* baselines in 2026.
- **Homology modeling.** When a structurally-determined homolog exists, build a 3D model of your protein by aligning to it. Pre-AlphaFold, the standard route to a structure.

**Half 2: Small molecules.**

- **Small molecules.** Drugs, metabolites, ligands. Typically 10-100 atoms, characterizable by 2D structure (atoms + bonds) or 3D conformation.
- **SMILES strings.** A linear textual encoding of a molecule. Canonical SMILES is unique; non-canonical is not. Easy to parse, easy to use as ML input.
- **Molecular fingerprints (ECFP / Morgan fingerprints).** Bit-vector encodings: bit i is on iff some local substructure of radius r is present. Fast similarity (Tanimoto), fast classification (random forests on fingerprints are still competitive).
- **QSAR — Quantitative Structure-Activity Relationship.** "Predict bioactivity from structure." Random forest on fingerprints + log-transformed activity readouts is the canonical setup.
- **Molecular docking.** Predict how a small molecule binds to a protein pocket. AutoDock Vina is the workhorse. Useful when you have a structure for the target.
- **The drug-discovery pipeline.** Hit identification → lead optimization → preclinical → trials. ML can help at every stage; usually it helps most at the early ones (hit-finding, virtual screening).
- **Scaffold splits.** A train/test split that *separates by chemical scaffold*, not by random sample. Random splits over-estimate generalization for molecules because similar molecules end up in both train and test. Scaffold splits are the honest evaluation.
- **The classical-baseline challenge.** A consistent finding in the molecular-ML literature: a random forest on Morgan fingerprints, evaluated with scaffold splits, is *competitive* with most reported deep-learning approaches. Not always, but often. The lecture pushes back against "deep learning solved chemistry."

## Why it matters

Three reasons this lecture is the right setup for L27:

**Classical methods exploit strong domain structure.** Sequence alignment, MSAs, PSSMs, fingerprints, docking — all of these encode *generations* of biological knowledge into the model itself. Modern deep-learning methods compete with these only when they encode similar (or stronger) priors.

**Evaluation matters as much as architecture.** Scaffold splits, conservation-aware evaluation, MSA-aware benchmarks — these are the difference between an over-optimistic claim and an honest one. The same architecture can look great or terrible depending on the split.

**Domain knowledge isn't optional.** A protein-prediction model that doesn't use MSA information is *throwing away* the strongest signal in the field. A small-molecule model that doesn't use fingerprints or 3D structure is doing it the hard way.

## Things you should walk away believing

- Biological sequences and molecules have strong structure (evolution, conservation, chemistry) that classical methods exploit. Don't dismiss them.
- MSA-derived features (PSSMs, conservation, coevolution) are the strongest single source of signal in protein modeling.
- SIFT / PolyPhen are still legitimate variant-effect baselines in 2026.
- SMILES / fingerprints / random forests are still legitimate small-molecule baselines.
- Random splits over-estimate molecular-ML performance; scaffold splits are the honest evaluation.
- Docking is a useful tool, not a black box. Know its assumptions before you trust the score.
- The PDB has ~200K structures; sequence databases have hundreds of millions. The gap is the reason structure prediction (L27) matters.
- "Deep learning beats classical X" claims should be checked with proper splits and proper baselines.

## How this connects to the rest of the course

- L25 set up DNA / RNA / population genetics; this lecture moves to the protein and small-molecule layers.
- L27 (next lecture) extends this with deep learning — protein language models (ESM-2), AlphaFold-style structure prediction, equivariant 3D models, generative protein design.
- L15 (foundation models) — protein LMs are foundation models over (protein sequence, ?), and the "?" is non-obvious.
- L24 (causality, fairness) — drug-discovery models inherit biases of their training data (which compounds were measured, which assays were used).
- L10's domain-shift story applies: scaffold splits expose lack of generalization; random splits hide it.

## Source files in this folder

- `lec26_proteins_molecules.pdf` — the slides as released to students. *The LaTeX source compiles to a 56-page PDF identical to this in content (verified).*
- `latex/lec26_proteins_molecules.tex` and `latex/figures/` — editable Beamer source.
- `nb26_proteins_molecules.ipynb` — companion notebook: protein structure visualization, MSA + conservation, PSSM construction, fingerprint similarity, scaffold-split demo, drug-property prediction, docking visualization.

## To go deeper

- **Berman et al., "The Protein Data Bank," _Nucleic Acids Res_ 28, 2000.** The original PDB paper.
- **Altschul et al., "Basic local alignment search tool (BLAST)," _J Mol Biol_ 215, 1990.** Sequence alignment foundation.
- **Adzhubei et al., "A method and server for predicting damaging missense mutations" (PolyPhen-2), _Nat Methods_ 7, 2010.**
- **Ng & Henikoff, "Predicting deleterious amino acid substitutions" (SIFT), _Genome Res_ 11, 2001.**
- **Rogers & Hahn, "Extended-Connectivity Fingerprints," _J Chem Inf Model_ 50, 2010.** Morgan/ECFP fingerprints.
- **Trott & Olson, "AutoDock Vina," _J Comput Chem_ 31, 2010.** The docking workhorse.
- **Wu et al., "MoleculeNet: a benchmark for molecular machine learning," _Chem Sci_ 9, 2018.** Standardized molecular ML benchmarks.
- **Bento et al., "The ChEMBL bioactivity database: an update," _Nucleic Acids Res_ 42, 2014.** The substrate for most QSAR work.
- **Coursera _Drug Discovery_ specialization (UC San Diego).** Decent companion course.

## Study tools

- [Study guide for L26](../study_guides/lecture-26.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
