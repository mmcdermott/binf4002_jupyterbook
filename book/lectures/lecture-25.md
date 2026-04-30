# Lecture 25 — DNA, genetics, and gene regulation

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Apr 21, 2026 · Part 5 — Molecules & biological AI**

## What this lecture is about

Genetic data are the highest-dimensional, most-structured, and most population-dependent data the course will see. This lecture introduces the genome as an ML modality — what's measured, what the data look like, and why naïve "just throw a neural net at it" fails almost immediately because of population structure and multiple-testing pathologies. The lecture is dense, but the payoff is large: by the end you can read a GWAS paper, you can interpret a Manhattan plot, and you understand why polygenic risk scores transfer poorly across ancestries.

We work top-down from biology to ML.

- **Central dogma and DNA basics.** DNA → RNA → protein. ~3 billion base pairs in the human genome, ~99.5-99.9% identical across humans (the higher figure counts only SNVs; the lower includes indels and structural variants), ~4-5 million variants per individual relative to the reference (mostly SNVs plus indels). Variants come in different flavors: SNPs (single-nucleotide), indels, structural variants, copy-number variants. Most ML on genetics works with SNPs.
- **Measurement technologies.** SNP arrays (cheap, ~1M variants, biased toward known variants) vs. sequencing (more expensive, full coverage of detected variants — ~4-5M *per individual* for WGS). Population-scale catalogs that aggregate variants across many people (gnomAD, 1000 Genomes) reach 30-100M+ unique variants total — that's a *catalog* size, not a per-individual count. Modern biobanks combine arrays and sequencing.
- **Population structure.** Allele frequencies vary by ancestry. The first few principal components of a SNP matrix correspond, almost literally, to geographic origin. This is *not* a bug — it's a feature of the data — and ignoring it is one of the most common errors in genetic ML.
- **Linkage disequilibrium (LD).** Nearby variants are correlated because they're inherited together. LD structure varies by ancestry. The "effective number of independent variants" is much smaller than the raw count.
- **GWAS — Genome-Wide Association Studies.** The standard analysis: for each of ~10⁶ variants, test for association with phenotype. Effect sizes are tiny, multiple-testing burden is enormous, p-value threshold is conventionally 5 × 10⁻⁸ (Bonferroni for ~10⁶ independent tests).
- **Manhattan plots and QQ plots.** The two diagnostic plots every GWAS paper produces. Manhattan = -log₁₀(p) along the genome; QQ = observed vs. expected p-value distribution. A QQ plot that lifts off the diagonal globally suggests population stratification (uncorrected confounding) rather than real signal.
- **Population stratification correction.** Include the first 10-20 principal components of the genotype matrix as covariates in the GWAS regression. This is *the* canonical correction.
- **Polygenic risk scores (PRS).** A weighted sum of risk alleles across the genome: PRS_i = Σⱼ βⱼ Xᵢⱼ where βⱼ comes from GWAS effect sizes. PRS predicts disease risk modestly.
- **PRS transferability.** PRS computed in one ancestry transfers poorly to others — losing 30-90% of predictive power. Because GWAS samples are >80% European-ancestry, PRS clinical utility is *systematically worse* for non-European patients. This is a fairness story (link to L24).
- **Gene expression and regulation.** DNA → RNA is regulated by transcription factors, enhancers, chromatin state. Expression is *context-dependent*: tissue, cell type, time, environment.
- **eQTLs.** Expression quantitative trait loci — genetic variants associated with expression levels. Provide a mechanistic bridge between GWAS hits and actual biology.

The paradox flagged: "**first or middle principal components?**" — a teaser for which PCs to keep when correcting for population structure.

## Why it matters

Three reasons this lecture is more than "the biology you should remember from undergrad":

**Population structure is the most important confounder in genetic ML.** Two cases that look like signal are actually structure: (a) a variant whose frequency tracks ancestry will appear "associated" with any phenotype that also tracks ancestry; (b) a non-causal variant in LD with a true causal one will appear associated and will *not* generalize when LD structure differs (across populations).

**PRS transferability is a fairness problem.** The clinical use of PRS — "this patient is in the top 5% of genetic risk for X" — has different reliability for different ancestries. Deploying PRS clinically without acknowledging this risks widening, not closing, health disparities.

**Genotype is not phenotype.** Most genetic effects on disease run through *expression*, *regulation*, *context*. A variant that "causes" a disease in some sense usually does so via complex pathways. Models that ignore this layer (just-mapping-genotype-to-disease neural networks) leave a lot on the table.

## Things you should walk away believing

- Genetic data are high-D, structured, and population-dependent.
- Population structure looks like signal until you correct for it. PCA-correction is canonical.
- LD makes "number of variants" misleading. The effective dimensionality is much smaller.
- GWAS p-values must clear ~5 × 10⁻⁸ for genome-wide significance. Anything between ~5 × 10⁻⁸ and ~10⁻⁵ is "suggestive" at best (smaller p-values are more significant).
- A QQ plot that doesn't lie on the diagonal is the first thing a reviewer will check.
- PRS transferability is poor across ancestries, and this matters clinically.
- Gene regulation, expression, and eQTLs are the *mechanistic* layer between genotype and phenotype.
- Public databases (dbSNP, GTEx, ENCODE, UK Biobank) are the substrate for almost all current genetic ML.

## How this connects to the rest of the course

- L26 (proteins, molecules) builds on the molecular biology established here.
- L27 (modern biological AI) covers DNA foundation models (Enformer, Evo) — the deep-learning extensions of GWAS and gene-regulation modeling.
- L24 (fairness) — PRS transferability is a textbook causal-fairness story.
- L23 (population health) — UK Biobank and other biobanks are the substrate for GWAS at scale.
- L2 (linear algebra) — population PCA is literally an eigendecomposition of the centered genotype covariance matrix.
- L4 (information theory / multiple testing) — GWAS multiple-testing correction is the largest such correction the course will see.

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

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

### The Most Important Confounder

```{admonition} Population structure looks like signal until you correct for it
:class: warning
A variant whose frequency tracks ancestry will appear "associated" with any phenotype that also tracks ancestry. **Always include the first ~10 PCs of the genotype matrix as covariates** in a GWAS regression. A QQ plot that doesn't lie on the diagonal globally is the canonical sign you forgot.
```

### PRS Transferability Is a Fairness Story

```{admonition} Why this matters clinically
:class: important
GWAS samples are >80% European-ancestry. PRS computed from those GWASs predicts disease risk *worse* for non-European patients — and the gap is large. Deploying PRS clinically without acknowledging this risks widening, not closing, health disparities.
```

### Genotype Is Not Phenotype

```{admonition} Don't skip the regulatory layer
:class: tip
Most genetic effects on disease run through *expression*, *regulation*, *chromatin context*, *cell type*, *environment*. Models that map genotype directly to disease ignore the mechanism — and leave a lot on the table. eQTLs are the mechanistic bridge. GTEx and ENCODE are the substrate.
```

### Self-Check Questions

1. A QQ plot shows almost all p-values lifting off the diagonal globally. What three explanations should you consider, in order?
2. LD makes "1M variants" misleading. What is the *effective* number of independent variants in a typical European-ancestry GWAS, roughly?
3. A PRS for coronary artery disease was developed in UK Biobank (~95% European ancestry). It will be deployed in a Singaporean clinic. Walk through the failure modes you'd expect.
4. Gene expression varies by tissue and cell type. What does this mean for an "expression-prediction model" that ignores tissue context?
5. dbSNP, GTEx, ENCODE, UK Biobank: match each to "regulatory-element catalog," "common-variant catalog," "tissue-specific eQTL atlas," "phenotype-rich biobank."

### Additional Resources

- [Visscher et al., "10 Years of GWAS Discovery," *AJHG* 101, 2017](https://www.cell.com/ajhg/fulltext/S0002-9297(17)30240-9) — panoramic review.
- [Martin et al., "Clinical use of current PRSs may exacerbate health disparities," *Nat Genet* 51, 2019](https://www.nature.com/articles/s41588-019-0379-x). **Required reading.**
- [Price et al., "Principal components analysis corrects for stratification in GWAS," *Nat Genet* 38, 2006](https://www.nature.com/articles/ng1847) — the PCA-correction paper.
- [GTEx Consortium, "The GTEx Consortium atlas of genetic regulatory effects across human tissues," *Science* 369, 2020](https://www.science.org/doi/10.1126/science.aaz1776).
- [ENCODE, "Expanded encyclopaedias of DNA elements," *Nature* 583, 2020](https://www.nature.com/articles/s41586-020-2493-4).
- [Coursera — *Genomic Data Science* (Johns Hopkins)](https://www.coursera.org/specializations/genomic-data-science) — free, hands-on, multi-course companion.
- Hartl & Clark, *Principles of Population Genetics* (4th ed.) — for theoretical underpinnings.
