# Lecture 28 — Course recap

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

**Date.** Thu Apr 30, 2026.

The standalone deployment lecture originally planned for this slot was **not taught this cycle**. Instead, L28 is a guided walk back through the course arc — making the cross-cutting through-lines explicit and giving you a final-exam study frame.

## The course arc in one paragraph

We started with **mathematical foundations** (L1-L10): linear algebra, probability, calculus and optimization, then the supervised-learning loop (probabilistic modeling, evaluation, training, generalization). We then introduced **modern AI methods** (L13-L15: neural networks, LLMs, foundation models) and used three in-class lab days (L11, L12, L16) to wrestle with the orthogonality of model / loss / data type on real datasets. After spring break we walked through **clinical AI** modality by modality — EHR / claims (L17-L18), clinical text (L19-L20), medical imaging (L21-L22) — pairing a "what is the data" lecture with a "how do we model it" lecture every time. Then we lifted the lens beyond a single hospital with **population health and survival analysis** (L23) and **causality and fairness** (L24), and closed with the **molecular tier** (L25-L27): DNA and gene regulation, proteins and small molecules, and modern biological AI.

## The six through-lines (TL1-TL6)

These are the cross-cutting threads. For every one, name an instance from at least three different lectures and you've internalized it.

### TL1 — The model is never separate from the task

Same score, different decisions, depending on threshold, utility, prevalence, calibration, and workflow. There is no "good model" in the abstract — only a model that is good for *this* decision in *this* context. **Touched in:** L8 (calibration / threshold / utility), L9 (loss is a proxy for the decision), L17-L18 (cohort definition and windows *are* the task), L23 (survival vs. binary at fixed horizon), L24 (prediction vs. intervention).

### TL2 — Data are generated, not given

Every health dataset has a measurement system, an incentive structure, and a selection mechanism. Patterns in the data reflect those *before* they reflect biology. **Touched in:** L17 (EHR / claims as care + billing byproducts), L18 (recording timing is itself signal), L19-L20 (clinical text is documentation), L21-L22 (DICOM metadata leaks site information), L23 (healthy-volunteer effect; selection), L24 (Obermeyer: the label was the bias), L25 (population structure in genotypes).

### TL3 — Representation is a scientific claim

Tabularizing, chunking, windowing, tokenizing, embedding, fingerprinting all impose assumptions. The choice of representation is *part of the model*, not preprocessing trivia. **Touched in:** L2 (basis choice), L13 (architecture as inductive bias), L18 (tabular vs. chunked vs. event-stream EHR), L20 (tokenization, embeddings, RAG), L21-L22 (2D vs. 3D vs. WSI; MIL forced by data size), L25 (PCA on genotypes), L26 (SMILES, ECFP fingerprints), L27 (equivariance for 3D molecules).

### TL4 — Generalization is contextual

A model that works in one place may not work in another. Generalization depends on sites, populations, workflows, time, prevalence, coding practices, scanners — not on parameter count or training-set size alone. **Touched in:** L6 (expected vs. empirical loss), L10 (inductive bias; domain shift), L17-L18 (cohort selection), L21-L22 (multi-site DICOM artifacts; CXR generalization), L25 (PRS transferability across ancestries).

### TL5 — Modern AI does not remove classical baselines

Bayes, kNN, calibration, Cox regression, multiple sequence alignment, PSSMs, homology modeling, QSAR, docking — these are still strong, often state-of-the-art for specific subproblems. New methods should be benchmarked against them, not just against the previous deep-learning paper. **Touched in:** L2-L7 (the foundations themselves), L9 (kNN as a real baseline), L20 (NegEx and ClinicalBERT vs. LLMs), L23 (Cox vs. DeepSurv), L26 (MSA, PSSMs, QSAR, docking), L27 (genomic-FM critique).

### TL6 — Deployment creates new distributions

A model in production becomes part of the data-generating process it predicts over. Calibration drifts, labels arrive late, alerts cause fatigue, access disparities widen. **Touched in:** L8 (calibration drift), L17-L18 (label / action windows), L24 (mechanism + threshold mitigation). *(The originally-planned L28 deployment lecture covered this through-line directly. It is not taught this cycle; see "Self-study" below.)*

## Lecture-to-through-line matrix

|       | TL1 | TL2 | TL3 | TL4 | TL5 | TL6 |
|-------|-----|-----|-----|-----|-----|-----|
| L2    |     |     | ✓   |     | ✓   |     |
| L3-L4 |     |     |     |     | ✓   |     |
| L6    |     |     |     | ✓   |     |     |
| L7    |     |     |     |     | ✓   |     |
| L8    | ✓   |     |     |     |     | ✓   |
| L9    | ✓   |     |     |     | ✓   |     |
| L10   |     |     |     | ✓   |     |     |
| L13   |     |     | ✓   |     |     |     |
| L17   | ✓   | ✓   |     | ✓   |     | ✓   |
| L18   | ✓   | ✓   | ✓   | ✓   |     | ✓   |
| L19-L20 |   | ✓   | ✓   |     | ✓   |     |
| L21-L22 |   | ✓   | ✓   | ✓   |     |     |
| L23   | ✓   | ✓   |     |     | ✓   |     |
| L24   | ✓   | ✓   |     |     |     | ✓   |
| L25   |     | ✓   | ✓   | ✓   |     |     |
| L26   |     |     | ✓   |     | ✓   |     |
| L27   |     |     | ✓   |     | ✓   |     |

## What was *not* covered (self-study, *not* on the exam)

The L28 slot was originally planned as a deployment lecture (drift monitoring, label delay, feedback loops, alert fatigue, regulation). **It was not taught this cycle, and is not on the final exam.** The deployment-*adjacent* material that *was* taught — calibration (L8), domain shift (L10), label/action windows (L17-L18), causal-mechanism mitigation (L24) — *is* on the exam. For your own knowledge, the deployment-*specific* material below is worth reading:

- **Finlayson et al., "The Clinician and Dataset Shift in Artificial Intelligence," _NEJM_ 385, 2021.** The single most accessible piece on clinical-AI deployment failure modes.
- **Perdomo, Zrnic, Mendler-Dünner & Hardt, "Performative Prediction," _ICML_ 2020.** Formal feedback-loop treatment.
- **US FDA, "AI/ML-Based Software as a Medical Device (SaMD) Action Plan," 2021.** The regulatory framing.
- **Sendak et al., "A path for translation of machine learning products into healthcare delivery," _EMJ Innov_ 4, 2020.**

## Final-exam study checklist

If you can answer all of these without notes, you're ready:

- [ ] State the eight course-level learning objectives and name a lecture that contributed to each.
- [ ] Articulate each of the six through-lines (TL1-TL6) in your own words.
- [ ] Pick a clinical ML scenario (e.g., 30-day hospital readmission) and walk through: task definition (windows / censoring), representation (tabular / chunked / event-stream), loss, evaluation (calibration *and* discrimination per subgroup), and at least three failure modes the course identified.
- [ ] Read a hypothetical paper that claims "AUROC 0.94 for sepsis prediction" and list five questions to ask the authors.
- [ ] Distinguish prediction from intervention; explain why two natural fairness criteria are mutually incompatible at unequal base rates.
- [ ] Critique a "foundation model" claim by asking *what input domain* and *what task distribution* it covers.
- [ ] For at least three modalities (EHR, imaging, text, survival, genetics, proteins), name one classical baseline that is still competitive in 2026.

## Materials

No new lecture deliverable. Re-read the [syllabus](../syllabus.md) and [concept map](../concept_map.md). The companion [study guides](../study_guides/intro.md) for L1-L27 are the fastest way to active-recall.

## Study tools

- [Concept map](../concept_map.md) — prerequisite graph, six through-lines, interactive mind map.
- [Syllabus](../syllabus.md) — full hierarchical content reference.
- [Study guides intro](../study_guides/intro.md) — index of all 27 per-lecture study guides.
