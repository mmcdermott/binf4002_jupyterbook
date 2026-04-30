# Lecture 25 — DNA, genetics, and gene regulation

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Tue Apr 21, 2026 · Part 5 — Molecules & biological AI**

## What this lecture is about

Genetic data are the highest-dimensional, most-structured, and most population-dependent data the course will see. This lecture introduces the genome as an ML modality — what's measured, what the data look like, and why naïve "just throw a neural net at it" fails almost immediately because of population structure and multiple-testing pathologies. The lecture is dense, but the payoff is large: by the end you can read a GWAS paper, you can interpret a Manhattan plot, and you understand why polygenic risk scores transfer poorly across ancestries.

We work top-down from biology to ML.

- **Central dogma and DNA basics.** DNA → RNA → protein. ~3 billion base pairs in the human genome, 99.9% identical across humans, ~3 million variants per individual. Variants come in different flavors: SNPs (single-nucleotide), indels, structural variants, copy-number variants. Most ML on genetics works with SNPs.
- **Measurement technologies.** SNP arrays (cheap, ~1M variants, biased toward known variants) vs. sequencing (more expensive, full coverage of detected variants, ~30M variants for whole genome). Modern biobanks combine both.
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
- GWAS p-values must clear ~5 × 10⁻⁸. Anything below ~10⁻⁵ is "suggestive" at best.
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

## Source files in this folder

- `lec25_dna_genetics.pdf` — the slides as released to students. *The LaTeX source compiles to a 62-page PDF identical to this in content (verified).*
- `latex/lec25_dna_genetics.tex` and `latex/figures/` — editable Beamer source.
- `nb25_dna_genetics.ipynb` — companion notebook: DNA visualizations, simulated GWAS, Manhattan plots, QQ plots, population PCA, PRS transferability demo.

## To go deeper

- **Visscher et al., "10 Years of GWAS Discovery: Biology, Function, and Translation," _AJHG_ 101, 2017.** A panoramic review by one of the field's leading methodologists.
- **Martin et al., "Clinical use of current polygenic risk scores may exacerbate health disparities," _Nat Genet_ 51, 2019.** The PRS-transferability paper. Required reading.
- **Price et al., "Principal components analysis corrects for stratification in genome-wide association studies," _Nat Genet_ 38, 2006.** The PCA-correction paper. Read it once.
- **GTEx Consortium, "The GTEx Consortium atlas of genetic regulatory effects across human tissues," _Science_ 369, 2020.** The eQTL atlas paper.
- **ENCODE Project Consortium, "Expanded encyclopaedias of DNA elements in the human and mouse genomes," _Nature_ 583, 2020.** The regulatory-element catalog.
- **Bycroft et al., "The UK Biobank resource with deep phenotyping and genomic data," _Nature_ 562, 2018.** UK Biobank.
- **Coursera _Genomic Data Science_ (Johns Hopkins).** Free, hands-on, multi-course companion.
- **Hartl & Clark, _Principles of Population Genetics_, 4th ed.** Textbook, when you want the full theoretical underpinning.

## Study tools

- [Study guide for L25](../study_guides/lecture-25.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
