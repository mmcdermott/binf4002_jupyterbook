# L25 Study Guide — DNA, Genetics & Gene Regulation

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

## Key Terms

| Term | Definition |
|---|---|
| **Central dogma** | DNA → RNA → protein. The information flow that ML on biological sequences ultimately models. |
| **SNP** | Single-Nucleotide Polymorphism — variation at a single base. The variant type most ML on genetics works with. |
| **Indel** | Small insertions or deletions in DNA. |
| **Structural variant / CNV** | Larger rearrangements; copy-number variants are gains/losses of large chromosomal segments. |
| **SNP array** | Microarray genotyping technology. ~1M variants, biased toward known common variants. Cheap. |
| **Whole-genome / Whole-exome sequencing** | Read all (WGS) or coding-region (WES) DNA. Far more variants, more expensive. |
| **Population structure** | Allele frequencies vary by ancestry. Top PCs of the genotype matrix correspond, almost literally, to geographic origin. |
| **Linkage disequilibrium (LD)** | Nearby variants are inherited together; correlation between adjacent SNPs. *Effective* number of independent variants is much smaller than raw count. |
| **GWAS (Genome-Wide Association Study)** | For each of ~10⁶ variants, test for association with phenotype. Effect sizes are tiny; multiple-testing burden is enormous. |
| **Genome-wide significance** | Conventional p < 5 × 10⁻⁸ (Bonferroni for ~10⁶ independent tests). |
| **Manhattan plot** | -log₁₀(p) plotted along the genome. Spikes mark associated loci. |
| **QQ plot** | Observed vs. expected p-value distribution. Diagonal = no signal; lift-off → signal *or* uncorrected confounding. |
| **Population stratification** | Confounding when both allele frequency and phenotype vary by ancestry. The first thing a GWAS reviewer checks. |
| **Polygenic risk score (PRS)** | Σⱼ βⱼ Xᵢⱼ — a weighted sum of risk alleles using GWAS effect sizes. Predicts disease risk modestly. |
| **PRS transferability** | PRS computed in one ancestry transfers poorly to others — losing 30-90% of predictive power. **A fairness story.** |
| **Gene expression** | Amount of mRNA produced from a gene. Tissue-, cell-type-, and condition-dependent. |
| **eQTL** | Expression Quantitative Trait Locus — a genetic variant associated with expression levels. Mechanistic bridge between GWAS hits and biology. |

## The Most Important Confounder

```{admonition} Population structure looks like signal until you correct for it
:class: warning
A variant whose frequency tracks ancestry will appear "associated" with any phenotype that also tracks ancestry. **Always include the first ~10 PCs of the genotype matrix as covariates** in a GWAS regression. A QQ plot that doesn't lie on the diagonal globally is the canonical sign you forgot.
```

## PRS Transferability Is a Fairness Story

```{admonition} Why this matters clinically
:class: important
GWAS samples are >80% European-ancestry. PRS computed from those GWASs predicts disease risk *worse* for non-European patients — and the gap is large. Deploying PRS clinically without acknowledging this risks widening, not closing, health disparities.
```

## Genotype Is Not Phenotype

```{admonition} Don't skip the regulatory layer
:class: tip
Most genetic effects on disease run through *expression*, *regulation*, *chromatin context*, *cell type*, *environment*. Models that map genotype directly to disease ignore the mechanism — and leave a lot on the table. eQTLs are the mechanistic bridge. GTEx and ENCODE are the substrate.
```

## Self-Check Questions

1. A QQ plot shows almost all p-values lifting off the diagonal globally. What three explanations should you consider, in order?
2. LD makes "1M variants" misleading. What is the *effective* number of independent variants in a typical European-ancestry GWAS, roughly?
3. A PRS for coronary artery disease was developed in UK Biobank (~95% European ancestry). It will be deployed in a Singaporean clinic. Walk through the failure modes you'd expect.
4. Gene expression varies by tissue and cell type. What does this mean for an "expression-prediction model" that ignores tissue context?
5. dbSNP, GTEx, ENCODE, UK Biobank: match each to "regulatory-element catalog," "common-variant catalog," "tissue-specific eQTL atlas," "phenotype-rich biobank."

## Additional Resources

- [Visscher et al., "10 Years of GWAS Discovery," *AJHG* 101, 2017](https://www.cell.com/ajhg/fulltext/S0002-9297(17)30240-9) — panoramic review.
- [Martin et al., "Clinical use of current PRSs may exacerbate health disparities," *Nat Genet* 51, 2019](https://www.nature.com/articles/s41588-019-0379-x). **Required reading.**
- [Price et al., "Principal components analysis corrects for stratification in GWAS," *Nat Genet* 38, 2006](https://www.nature.com/articles/ng1847) — the PCA-correction paper.
- [GTEx Consortium, "The GTEx Consortium atlas of genetic regulatory effects across human tissues," *Science* 369, 2020](https://www.science.org/doi/10.1126/science.aaz1776).
- [ENCODE, "Expanded encyclopaedias of DNA elements," *Nature* 583, 2020](https://www.nature.com/articles/s41586-020-2493-4).
- [Coursera — *Genomic Data Science* (Johns Hopkins)](https://www.coursera.org/specializations/genomic-data-science) — free, hands-on, multi-course companion.
- Hartl & Clark, *Principles of Population Genetics* (4th ed.) — for theoretical underpinnings.

> See also: [L25 lecture page](../lectures/lecture-25.md). Companion notebook: [`nb25_dna_genetics.ipynb`](../lectures/nb-25-dna-genetics.ipynb).
