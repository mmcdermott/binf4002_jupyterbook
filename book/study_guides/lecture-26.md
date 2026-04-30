# L26 Study Guide — Proteins, Molecules & Structural Biology

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

## Key Terms

| Term | Definition |
|---|---|
| **Primary structure** | Amino-acid sequence of a protein. Length ~50-2000 typically. |
| **Secondary structure** | Local conformations: α-helices, β-sheets, loops. |
| **Tertiary structure** | The 3D fold of a single protein chain. |
| **Quaternary structure** | Multi-chain complexes. |
| **PDB (Protein Data Bank)** | The reference database of experimentally-determined protein structures (~200K). |
| **Protein data gap** | ~250M known protein sequences vs. ~200K experimental structures. The gap that makes structure prediction matter. |
| **MSA (Multiple Sequence Alignment)** | Aligning hundreds-to-thousands of homologous sequences. Reveals conserved positions and co-evolving pairs. The substrate for everything else. |
| **PSSM** | Position-Specific Scoring Matrix: per-position amino-acid frequencies extracted from an MSA. |
| **Coevolution** | Pairs of positions that mutate together — strongly suggestive of spatial contact. |
| **SIFT / PolyPhen** | Classical missense-variant-effect predictors using sequence conservation (SIFT) and conservation + structural features (PolyPhen). Still strong baselines. |
| **Homology modeling** | Build a 3D model by aligning to a structurally-determined homolog. Pre-AlphaFold standard. |
| **SMILES** | A linear textual encoding of a molecule (atoms + bonds). Canonical SMILES is unique. |
| **ECFP / Morgan fingerprint** | Bit-vector encoding: bit i is on iff some local substructure of radius r is present. Default small-molecule featurization. |
| **QSAR** | Quantitative Structure-Activity Relationship: predict bioactivity from structure. Random forest on fingerprints + log-activity is the canonical setup. |
| **Tanimoto similarity** | \|A ∩ B\| / \|A ∪ B\| over fingerprint bits. Standard chemical-similarity measure. |
| **Molecular docking** | Predict how a small molecule binds to a protein pocket. AutoDock Vina is the workhorse. |
| **Scaffold split** | Train/test split by chemical scaffold rather than at random. **Random splits over-estimate molecular-ML performance.** |

## Classical Methods Are Strong

```{admonition} Don't dismiss them
:class: tip
Sequence alignment, MSAs, PSSMs, fingerprints, docking, QSAR — these encode *generations* of biological knowledge into the model itself. Modern deep-learning methods compete with them only when they encode similar (or stronger) priors. **A random forest on Morgan fingerprints, evaluated with scaffold splits, is competitive with most reported deep-learning approaches** on molecular-property prediction. Not always, but often.
```

## Evaluation Matters As Much As Architecture

```{admonition} Random splits over-estimate; scaffold splits are honest
:class: warning
Molecular datasets contain many *near-duplicate* compounds (same scaffold, different decorations). Random splits put near-duplicates in both train and test, inflating apparent generalization. Scaffold splits (or stricter time-split / cluster-split evaluations) are the honest test.
```

## Self-Check Questions

1. What's the difference between a PSSM and a learned protein embedding? Why is PSSM still used in 2026?
2. SIFT scores a missense variant by sequence conservation. PolyPhen adds structural features. When would you reach for SIFT vs. PolyPhen vs. an ESM-2 zero-shot score (L27)?
3. ECFP fingerprints encode local substructure. Why do they work surprisingly well on QSAR despite ignoring 3D geometry?
4. AutoDock Vina returns a "docking score." What does it actually estimate, and what are its known failure modes?
5. A paper reports 0.85 ROC on lipophilicity prediction with random splits and 0.65 with scaffold splits. Which number should the reader take away as the model's true performance?

## Additional Resources

- [Berman et al., "The Protein Data Bank," *Nucleic Acids Res* 28, 2000](https://academic.oup.com/nar/article/28/1/235/2384399).
- [Altschul et al., BLAST, *J Mol Biol* 215, 1990](https://www.sciencedirect.com/science/article/abs/pii/S0022283605803602).
- [Adzhubei et al., PolyPhen-2, *Nat Methods* 7, 2010](https://www.nature.com/articles/nmeth0410-248).
- [Ng & Henikoff, SIFT, *Genome Res* 11, 2001](https://genome.cshlp.org/content/11/5/863).
- [Rogers & Hahn, "Extended-Connectivity Fingerprints," *J Chem Inf Model* 50, 2010](https://pubs.acs.org/doi/10.1021/ci100050t).
- [Trott & Olson, "AutoDock Vina," *J Comput Chem* 31, 2010](https://onlinelibrary.wiley.com/doi/10.1002/jcc.21334).
- [Wu et al., "MoleculeNet," *Chem Sci* 9, 2018](https://pubs.rsc.org/en/content/articlehtml/2018/sc/c7sc02664a).
- [Bento et al., "ChEMBL bioactivity database," *Nucleic Acids Res* 42, 2014](https://academic.oup.com/nar/article/42/D1/D1083/1043509) — the substrate for most QSAR work.
- [RDKit](https://www.rdkit.org/) — open-source cheminformatics toolkit; the standard tool for SMILES / fingerprints.

> See also: [L26 lecture page](../lectures/lecture-26.md). Companion notebook: [`nb26_proteins_molecules.ipynb`](../lectures/nb-26-proteins-molecules.ipynb).
