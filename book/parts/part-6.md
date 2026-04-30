# Part 6 — Course Recap

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

**Lecture 28**

## What this part is about

The L28 slot was originally planned as a deployment lecture (drift, feedback loops, alert fatigue, regulation). This cycle, the deployment material has been moved to optional self-study (see external resources below) and the slot is used as a **course-wide recap** — a guided walk back through the arc of the semester, with the cross-cutting through-lines (TL1-TL6 in the [concept map](../concept_map.md)) made explicit.

If you missed any earlier lectures, this is the slot where the cross-references that have been quietly accumulating get tied together into a single picture.

## Goals for this part

- Re-state the eight course-level learning objectives from the [syllabus](../syllabus.md), and identify which lectures contributed to each.
- Articulate the six course-wide through-lines (TL1-TL6) in your own words and name an instance of each from at least three different lectures.
- Identify what was *not* covered — deployment-specific topics that the optional self-study fills in.
- Walk into the final exam with an integrated picture of the course rather than 27 isolated lecture summaries.

## Key takeaways for this part

These are the same six course-wide takeaways from Level 0 of the syllabus, restated as the recap's load-bearing claims:

1. **The model is never separate from the task.** Same score, different decisions.
2. **Data are generated, not given.** Every health dataset has a measurement system, an incentive structure, and a selection mechanism.
3. **Representation is a scientific claim.** Tabularizing, chunking, windowing, tokenizing, embedding, fingerprinting all impose assumptions.
4. **Generalization is contextual.** It depends on sites, populations, workflows, time, prevalence, scanners.
5. **Modern AI does not remove classical baselines.** Bayes, kNN, calibration, Cox, MSA, PSSMs still matter.
6. **Deployment creates new distributions** (the through-line that was supposed to be L28's main subject; covered briefly in L8, L17-L18, L24, and the self-study below).

## Lectures in this part

- [L28 — Course recap / synthesis](../lectures/lecture-28.md)

## External resources for this part

**Deployment material (the dropped lecture, for self-study)**

- Finlayson et al., "The Clinician and Dataset Shift in Artificial Intelligence," *NEJM* 385, 2021. **Most accessible single piece on deployment failure modes.**
- Perdomo, Zrnic, Mendler-Dünner & Hardt, "Performative Prediction," *ICML* 2020 — the formal treatment of feedback loops.
- US FDA, "Artificial Intelligence/Machine Learning (AI/ML)-Based Software as a Medical Device (SaMD) Action Plan," 2021. The regulatory framing; relatively short.
- Sendak et al., "A path for translation of machine learning products into healthcare delivery," *EMJ Innov* 4, 2020.
- Lenert, Sakaguchi & Weir, "Rethinking the discovery of medical knowledge in the age of artificial intelligence," *Lancet Digital Health* 5, 2023.
- McKinney et al., "International evaluation of an AI system for breast cancer screening," *Nature* 577, 2020 — a contested case study worth reading alongside the critique by Haibe-Kains et al. (*Nature* 586, 2020).

**Cross-cutting course resources**

- Wiens et al., "Do no harm: a roadmap for responsible machine learning for health care," *Nat Med* 25, 2019.
- Ghassemi, Naumann, Schulam, Beam, Chen & Ranganath, "A Review of Challenges and Opportunities in Machine Learning for Health," *AMIA Joint Summits*, 2020.
- Topol, "High-performance medicine: the convergence of human and artificial intelligence," *Nat Med* 25, 2019.
