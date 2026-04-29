# BINF 4002 — Through-lines and mind-map structure

This file is the *connective tissue* of the course. It complements the canonical hierarchical syllabus ([`syllabus.md`](syllabus.md)) by laying out the cross-cutting threads that link lectures, the suggested mind-map hierarchy, and the external-reference clusters that the mind map can link to.

It is meant to drive a mind-map renderer (Markmap, Mermaid mindmap, Obsidian/Logseq graph view, etc.) — every node names its parent topic and children, and every through-line explicitly lists which lectures it touches so a renderer can emit cross-edges.

---

## Through-lines

These are the cross-cutting themes that *connect* lectures. Each through-line lists the lectures it appears in, so a mind-map generator can render edges between those nodes.

### TL1 — The model is never separate from the task
Same score, different decisions, depending on threshold, utility, prevalence, calibration, and workflow. Appears in: **L8** (evaluation), **L9** (training), **L17-L18** (EHR task definition), **L23** (survival vs. binary classification), **L24** (prediction vs. intervention), **L28** (course recap synthesis).

### TL2 — Data are generated, not given
Every health dataset has a measurement system, an incentive structure, and a selection mechanism. Appears in: **L1** (orientation), **L17-L18** (EHR/claims as byproducts of care/billing), **L19-L20** (clinical text as documentation), **L21-L22** (DICOM, scanners, sites), **L23** (selection into registries / biobanks / trials), **L24** (Obermeyer mechanism), **L25** (population stratification).

### TL3 — Representation is a scientific claim
Tabularizing, chunking, windowing, tokenizing, embedding, fingerprinting all impose assumptions. Appears in: **L2** (basis choice), **L13** (NN architecture as inductive bias), **L18** (tabularized vs. chunked vs. event-stream EHR), **L20** (tokenization, embeddings, RAG), **L21-L22** (2D vs. 3D vs. WSI; MIL), **L25** (PCA on genotypes), **L26** (SMILES, fingerprints), **L27** (equivariance).

### TL4 — Generalization is contextual
Generalization depends on sites, populations, workflows, time, prevalence, coding practices, scanners, interventions. Appears in: **L6** (expected vs. empirical loss), **L10** (overfitting, inductive bias, domain shift), **L17-L18** (cohort selection), **L21-L22** (multi-site generalization, garden of forking paths), **L25** (PRS transferability).

### TL5 — Modern AI does not remove classical baselines
Bayes, kNN, calibration, Cox, MSA, PSSMs, homology modeling, QSAR, docking still matter. Appears in: **L2-L7** (foundations), **L9** (kNN), **L20** (NegEx, BioBERT vs. LLM), **L23** (Cox vs. DeepSurv), **L26** (MSA, PSSM, QSAR, docking), **L27** (genomic-FM critique).

### TL6 — Deployment creates new distributions
Validated models become *part of* the data-generating process they predict over. Appears in: **L8** (calibration drift), **L17-L18** (label/action windows), **L24** (mechanism + threshold mitigation). *(The originally-planned L28 deployment lecture covered this through-line directly. It is not taught this cycle; the L28 slot is a course recap. Students wanting the deployment material should self-study Finlayson et al. (NEJM 2021) and the FDA AI/ML SaMD Action Plan (2021).)*

---

## Suggested mind-map hierarchy

The intended hierarchy for the mind map. Each level has a corresponding section in [`syllabus.md`](syllabus.md) with topic, summary, goals, takeaways, materials, and references.

```
BINF 4002 (root)
├── Part 1 — Foundations (L1-L10)
│   ├── 1.1 Mathematical preliminaries (L1-L6)
│   │   ├── L1 Orientation
│   │   ├── L2 Linear algebra
│   │   ├── L3 Probability
│   │   ├── L4 Information theory & Bayes
│   │   ├── L5 Calculus & optimization
│   │   └── L6 Probabilistic optimization
│   ├── 1.2 Probabilistic modeling (L7)
│   │   └── L7 Probabilistic modeling (Di Liu, guest)
│   └── 1.3 Evaluation, training, generalization (L8-L10)
│       ├── L8 Binary-classification evaluation (Florent Pollet)
│       ├── L9 Binary-classification training
│       └── L10 Generalization & domain shift
├── Part 2 — Modern AI & lab work (L11-L16)
│   ├── L11 Lab Day #1
│   ├── L12 Lab Day #2
│   ├── L13 Neural networks
│   ├── L14 Large language models
│   ├── L15 Foundation models
│   └── L16 Lab Day #3
├── Part 3 — Health data modalities (L17-L22)
│   ├── 3.1 EHR & claims (L17-L18)
│   │   ├── L17 EHR/claims data
│   │   └── L18 EHR/claims modeling
│   ├── 3.2 Clinical text (L19-L20)
│   │   ├── L19 Clinical text data
│   │   └── L20 Clinical NLP modeling
│   └── 3.3 Medical imaging (L21-L22)
│       ├── L21 Imaging data
│       └── L22 Imaging modeling
├── Part 4 — Population, causality, fairness (L23-L24)
│   ├── L23 Population health & survival
│   └── L24 Causality & fairness
├── Part 5 — Molecules & biological AI (L25-L27)
│   ├── L25 DNA, genetics, gene regulation
│   ├── L26 Proteins & molecules
│   └── L27 Modern biological AI
├── Part 6 — Course recap (L28)
│   └── L28 Synthesis / recap of L1-L27
└── Cross-cutting through-lines (TL1-TL6)
    ├── TL1 Model ≠ task
    ├── TL2 Data are generated
    ├── TL3 Representation is a claim
    ├── TL4 Generalization is contextual
    ├── TL5 Classical baselines persist
    └── TL6 Deployment creates new distributions
```

---

## External-reference clusters

These clusters are intended as "leaf nodes" the mind map can link out to. Each lecture's `README.md` has its own focused references; the clusters here are the course-wide groupings.

### Textbooks
- Murphy, *Probabilistic Machine Learning: An Introduction* (vol 1, 2022) — closest single-volume textbook to the course's spine.
- Goodfellow, Bengio, Courville, *Deep Learning* — Chs. 2-12 cover the math foundations and modern architectures.
- Hastie, Tibshirani, Friedman, *The Elements of Statistical Learning* — classical ML.
- Bishop, *Pattern Recognition and Machine Learning* — probabilistic perspective.
- MacKay, *Information Theory, Inference, and Learning Algorithms* (free PDF) — entropy, KL, Bayesian inference.
- Boyd & Vandenberghe, *Convex Optimization* (free PDF).
- Hernán & Robins, *Causal Inference: What If* (free PDF) — causal inference for L24.
- Pearl, Glymour, Jewell, *Causal Inference in Statistics: A Primer* — DAGs.
- Strang, *Introduction to Linear Algebra* — for L2.

### Online courses
- Coursera, *AI for Medicine* specialization (deeplearning.ai) — three-course series on diagnosis, prognosis, and treatment.
- Coursera, *A Crash Course in Causality* (Roy) — companion to L24.
- Stanford CS229 (Andrew Ng) — companion to Part 1.
- fast.ai, *Practical Deep Learning for Coders* — companion to L13.
- 3Blue1Brown, *Essence of Linear Algebra* / *Essence of Calculus* — visual companions to L2 and L5.
- Jay Alammar, *The Illustrated Transformer* (blog) — companion to L14.
- Andrej Karpathy, *A Recipe for Training Neural Networks* (blog) — companion to L13.

### Health-AI papers (course-wide)
- Beam & Kohane, "Big Data and Machine Learning in Health Care," *JAMA* 319(13), 2018.
- Topol, "High-performance medicine: the convergence of human and artificial intelligence," *Nat Med* 25, 2019.
- Wiens et al., "Do no harm: a roadmap for responsible machine learning for health care," *Nat Med* 25, 2019.
- Ghassemi, Naumann, Schulam, Beam, Chen, Ranganath, "A Review of Challenges and Opportunities in Machine Learning for Health," *AMIA Joint Summits*, 2020.
- Finlayson et al., "The Clinician and Dataset Shift in Artificial Intelligence," *NEJM* 385, 2021.
- Obermeyer et al., "Dissecting racial bias in an algorithm used to manage the health of populations," *Science* 366, 2019.
- Rajkomar et al., "Scalable and accurate deep learning with electronic health records," *npj Digit Med* 1, 2018.
- Singhal et al., "Large language models encode clinical knowledge," *Nature* 620, 2023.
- Jumper et al., "Highly accurate protein structure prediction with AlphaFold," *Nature* 596, 2021.
- Lin et al., "Evolutionary-scale prediction of atomic-level protein structure" (ESM-2), *Science* 379, 2023.

### Standards / data resources
- **EHR / claims:** OMOP CDM (*Book of OHDSI*, free); MEDS schema; FHIR; MIMIC-III/IV.
- **Imaging:** DICOM Standard.
- **Population:** NHANES; SEER; UK Biobank.
- **Text:** PubMed; UMLS.
- **Molecular:** PDB; AlphaFold DB; GTEx; ENCODE.
- **Regulation:** FDA *AI/ML SaMD Action Plan* (2021).

---

## How this file relates to the rest of the project

- **[`syllabus.md`](syllabus.md)** — canonical hierarchical syllabus (course → part → section → lecture, with topic / summary / goals / takeaways / materials / references at every level).
- **[`syllabus_markmap.md`](syllabus_markmap.md)** — Markmap-formatted compact version, ready to render as an interactive mind map.
- **[`Lectures/BINF4002_IRL_syllabus.md`](Lectures/BINF4002_IRL_syllabus.md)** — earlier LLM-derived narrative synthesis (more prose, less hierarchy).
- **[`Lectures/questions.md`](Lectures/questions.md)** — open issues and verification log.
- **`mind_map.md`** *(this file)* — through-lines, suggested mind-map hierarchy, and external-reference clusters.
