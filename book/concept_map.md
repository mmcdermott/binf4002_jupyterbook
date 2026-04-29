# Course concept map

**How this page is meant to work.** The course covered 28 class meetings and a lot of material. This page is the "step back" view — how the lectures connect, which ideas thread through the semester, and where to look in the syllabus when you want to follow a thread.

If you're studying for the final, work this page top-to-bottom: the prerequisite map → the six through-lines → the interactive mind map at the bottom. Each section answers a different question.

---

## How lectures build on each other

The directed graph below shows *prerequisites*. An arrow from L_i to L_j means "L_j leans heavily on the ideas L_i introduced." If a lecture is feeling shaky, follow the arrows backward to find what to review first.

```{mermaid}
flowchart LR
  classDef foundation fill:#e0f2fe,stroke:#0369a1,color:#0c4a6e
  classDef modernAI fill:#fef3c7,stroke:#b45309,color:#7c2d12
  classDef modality fill:#dcfce7,stroke:#15803d,color:#14532d
  classDef pop fill:#fce7f3,stroke:#be185d,color:#831843
  classDef bio fill:#ede9fe,stroke:#6d28d9,color:#4c1d95
  classDef recap fill:#f5f5f4,stroke:#57534e,color:#1c1917

  L1[L1 Orientation]:::foundation
  L2[L2 Linear algebra]:::foundation
  L3[L3 Probability]:::foundation
  L4[L4 Bayes & info theory]:::foundation
  L5[L5 Calculus & optimization]:::foundation
  L6[L6 Probabilistic optimization]:::foundation
  L7[L7 Probabilistic modeling]:::foundation
  L8[L8 Eval — binary classification]:::foundation
  L9[L9 Train — binary classification]:::foundation
  L10[L10 Generalization & domain shift]:::foundation

  L13[L13 Neural networks]:::modernAI
  L14[L14 LLMs]:::modernAI
  L15[L15 Foundation models]:::modernAI

  L17[L17 EHR data]:::modality
  L18[L18 EHR modeling]:::modality
  L19[L19 Clinical text data]:::modality
  L20[L20 Clinical NLP]:::modality
  L21[L21 Imaging data]:::modality
  L22[L22 Imaging modeling]:::modality

  L23[L23 Population health & survival]:::pop
  L24[L24 Causality & fairness]:::pop

  L25[L25 DNA & genetics]:::bio
  L26[L26 Proteins & molecules]:::bio
  L27[L27 Modern biological AI]:::bio

  L28[L28 Course recap]:::recap

  L2 --> L5
  L3 --> L4
  L4 --> L6
  L5 --> L6
  L6 --> L7
  L6 --> L9
  L7 --> L9
  L8 --> L9
  L9 --> L10
  L10 --> L13
  L2 --> L13
  L13 --> L14
  L14 --> L15

  L7 --> L17
  L4 --> L17
  L17 --> L18
  L8 --> L18
  L17 --> L19
  L14 --> L20
  L19 --> L20
  L13 --> L21
  L21 --> L22
  L17 --> L23
  L7 --> L23
  L23 --> L24
  L4 --> L24
  L23 --> L25
  L2 --> L25
  L25 --> L26
  L26 --> L27
  L13 --> L27
  L15 --> L27

  L10 --> L28
  L24 --> L28
  L27 --> L28
```

**How to read it.** Foundations (blue) flow into modern AI (yellow), into health-data modalities (green), into population/causality (pink), into biological AI (purple), all converging at the recap (gray). The dependency graph is dense in places — L2 (linear algebra) feeds L5, L13, and L25; L4 (Bayes) feeds L6, L17, and L24 — because those ideas really do reappear that many times.

---

## Six through-lines that thread the whole course

Six big ideas reappear in many lectures, often in quite different forms. For each through-line below: *what the idea is*, *which lectures it touches*, and *how it shows up in each*. Use these as study scaffolds — pick one, walk through every lecture it touches, and see how the same point gets re-used at different scales.

### TL1 — The model is never separate from the task

Same score, different decisions, depending on threshold, utility, prevalence, calibration, and workflow. There is no "good model" in the abstract — only a model that's good for *this* decision in *this* context.

```{mermaid}
graph LR
  TL1((TL1 Model ≠ task))
  TL1 --- L8[L8 Calibration / threshold / utility]
  TL1 --- L9[L9 Loss is a proxy for the decision]
  TL1 --- L17[L17 Cohort definition is the task]
  TL1 --- L18[L18 Windows / censoring / actionability]
  TL1 --- L23[L23 Survival vs. binary at fixed horizon]
  TL1 --- L24[L24 Prediction ≠ intervention]
  TL1 --- L28[L28 Synthesis: all the above]
```

### TL2 — Data are generated, not given

Every health dataset has a measurement system, an incentive structure, and a selection mechanism. Patterns in the data reflect those before they reflect biology.

```{mermaid}
graph LR
  TL2((TL2 Data are generated))
  TL2 --- L1[L1 The course's central stance]
  TL2 --- L17[L17 EHR / claims as care + billing byproducts]
  TL2 --- L18[L18 Recording timing is itself signal]
  TL2 --- L19[L19 Clinical text is documentation]
  TL2 --- L20[L20 Annotation labels carry biases]
  TL2 --- L21[L21 DICOM metadata leaks site information]
  TL2 --- L22[L22 Multi-site generalization fails]
  TL2 --- L23[L23 Healthy-volunteer effect; selection]
  TL2 --- L24[L24 Obermeyer: the label was the bias]
  TL2 --- L25[L25 Population structure in genotypes]
```

### TL3 — Representation is a scientific claim

Tabularizing, chunking, windowing, tokenizing, embedding, fingerprinting all impose assumptions. The choice of representation is part of the model, not preprocessing trivia.

```{mermaid}
graph LR
  TL3((TL3 Representation is a claim))
  TL3 --- L2[L2 Basis choice = representation choice]
  TL3 --- L13[L13 Architecture as inductive bias]
  TL3 --- L18[L18 Tabular vs. chunked vs. event stream]
  TL3 --- L20[L20 Tokenization, embeddings, RAG]
  TL3 --- L21[L21 2D vs. 3D vs. WSI as data shape]
  TL3 --- L22[L22 MIL forced by gigapixel data]
  TL3 --- L25[L25 PCA on genotypes]
  TL3 --- L26[L26 SMILES, ECFP fingerprints]
  TL3 --- L27[L27 Equivariance for 3D molecules]
```

### TL4 — Generalization is contextual

A model that works in one place may not work in another. Generalization depends on sites, populations, workflows, time, prevalence, coding practices, scanners — not on parameter count or training-set size alone.

```{mermaid}
graph LR
  TL4((TL4 Generalization is contextual))
  TL4 --- L6[L6 Expected vs. empirical loss]
  TL4 --- L10[L10 Inductive bias; domain shift]
  TL4 --- L17[L17 Cohort selection]
  TL4 --- L18[L18 Workflow alignment]
  TL4 --- L21[L21 Multi-site DICOM artifacts]
  TL4 --- L22[L22 Multi-site CXR generalization]
  TL4 --- L25[L25 PRS transferability across ancestries]
```

### TL5 — Modern AI does not remove classical baselines

Bayes, kNN, calibration, Cox regression, multiple sequence alignment, PSSMs, homology modeling, QSAR, docking — these are still strong, often state-of-the-art for specific subproblems. New methods should be benchmarked against them, not just against the previous deep-learning paper.

```{mermaid}
graph LR
  TL5((TL5 Classical baselines persist))
  TL5 --- L2[L2 Linear algebra is forever]
  TL5 --- L3[L3 Probability primitives]
  TL5 --- L4[L4 Bayes' rule arithmetic]
  TL5 --- L7[L7 NLL is still the right objective]
  TL5 --- L9[L9 kNN as a real baseline]
  TL5 --- L20[L20 NegEx and ClinicalBERT vs. LLMs]
  TL5 --- L23[L23 Cox vs. DeepSurv]
  TL5 --- L26[L26 MSA, PSSMs, QSAR, docking]
  TL5 --- L27[L27 Genomic-FM critique]
```

### TL6 — Deployment creates new distributions

A model in production becomes part of the data-generating process it predicts over. Calibration drifts, labels arrive late, alerts cause fatigue, access disparities widen.

```{mermaid}
graph LR
  TL6((TL6 Deployment creates new distributions))
  TL6 --- L8[L8 Calibration drift]
  TL6 --- L17[L17 Cohort shift over time]
  TL6 --- L18[L18 Label / action windows]
  TL6 --- L24[L24 Mechanism + threshold mitigation]
  TL6 -.- self[Self-study: Finlayson NEJM 2021,<br/>FDA AI/ML SaMD Action Plan 2021]
```

> *L28 was originally going to be a deployment lecture; it became a recap this cycle. The TL6 thread is therefore lighter than the others. The "self-study" branch above is what to read on your own to fill the gap.*

---

## Interactive mind map

Below is the same syllabus, rendered as a zoom/pan/expand interactive mind map. Click a node to expand or collapse its children; drag to pan; scroll to zoom. The mind map and the syllabus share a single source — if the syllabus changes, the mind map updates.

<iframe src="concept_mindmap.html"
        width="100%" height="650"
        style="border: 1px solid #d4d4d8; border-radius: 6px;"
        loading="lazy"
        title="Interactive course mind map">
</iframe>

<p style="font-size: 0.9em; color: #666;">
  Standalone version (better on small screens):
  <a href="concept_mindmap.html" target="_blank">open the mind map full-screen ↗</a>
</p>

---

## What this page is for, and what it is not

**For:** taking a step back at the end of the semester, finding the through-line for a topic, mapping a concept to the lectures where it appears, and reviewing for the final.

**Not for:** discovering new content. Each box, edge, and link points back to a lecture or notebook page that has the actual material. Use this page as a *index*, not as a *replacement* for the lectures.
