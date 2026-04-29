---
markmap:
  colorFreezeLevel: 2
  maxWidth: 320
  initialExpandLevel: 3
---

# BINF 4002 — ML for Health

## Part 1 — Foundations (L1-L10)

### 1.1 Mathematical preliminaries (L1-L6)

#### L1 Course orientation
- Tue Jan 20, 2026
- "Healthy epistemic uncertainty"
- ML for health ≠ ML on health-shaped inputs

#### L2 Linear algebra
- Tue Jan 22, 2026
- Vectors, vector spaces, linear operators
- Matrices as linear maps
- Bases / coordinatization

#### L3 Probability
- Tue Jan 27, 2026
- Probability triples
- Random variables
- Expectation
- Joint distributions

#### L4 Information theory & Bayes
- Thu Jan 29, 2026
- Marginal & conditional distributions
- Bayes' rule
- Prior, likelihood, evidence, posterior
- Entropy, KL, mutual information

#### L5 Calculus & optimization
- Tue Feb 3, 2026
- Multivariate differentiation
- Gradients, stationary points
- Random search, coordinate descent, gradient descent

#### L6 Probabilistic optimization
- Thu Feb 5, 2026
- Expected vs. empirical loss
- iid sampling
- Generalization preview

### 1.2 Probabilistic modeling (L7)

#### L7 Probabilistic modeling (Di Liu, guest)
- Tue Feb 10, 2026
- Data → model → likelihood → optimization
- NLL as a training objective
- GMMs, EM vs. gradient descent

### 1.3 Evaluation, training, generalization (L8-L10)

#### L8 Binary-classification evaluation (Florent Pollet)
- Thu Feb 12, 2026
- Confusion matrix
- Calibration vs. discrimination
- Bayes-optimal decision rule
- Decision-curve analysis
- AUROC limitations

#### L9 Binary-classification training
- Tue Feb 17, 2026
- Influenza vaccine effectiveness motivation
- Loss / optimization / overfitting control
- Data splits
- kNN and consistency

#### L10 Generalization & domain shift
- Thu Feb 19, 2026
- Memorization, capacity, regularization
- Modern-DL generalization puzzle
- Inductive bias
- Negative controls
- Domain shift, explainability, fairness

## Part 2 — Modern AI & lab work (L11-L16)

### L11 Lab Day #1
- Tue Feb 24, 2026
- Lab chunk #1: ML model types
- Labs 0-5

### L12 Lab Day #2
- Thu Feb 26, 2026
- Lab chunk #1 continued

### L13 Neural networks
- Tue Mar 3, 2026
- Architecture as inductive bias
- Init, normalization, residuals
- Optimizers, LR schedules
- Gradient clipping / accumulation
- Monitoring & regularization

### L14 Large language models
- Thu Mar 5, 2026
- Chinese Room paradox
- N-grams and sparsity
- Transformer attention
- LLM ecosystem

### L15 Foundation models
- Tue Mar 10, 2026
- Single-task → zero-shot spectrum
- Task conditioning (x, α)
- Labeled vs. total data efficiency
- EHR autoregressive models

### L16 Lab Day #3
- Thu Mar 12, 2026
- Lab chunks #2 (losses) and #3 (data types)
- Labs 6-16

## Part 3 — Health data modalities (L17-L22)

### 3.1 EHR & claims (L17-L18)

#### L17 EHR & claims data
- Tue Mar 24, 2026
- Berkson's paradox
- Coding systems (ICD, SNOMED-CT)
- Selection / cohort definition
- OMOP, MEDS, FHIR

#### L18 EHR & claims modeling
- Thu Mar 26, 2026
- Prediction / observation / label / action windows
- Censoring, competing risks
- Tabularized vs. chunked vs. event-stream

### 3.2 Clinical text (L19-L20)

#### L19 Clinical text data
- Tue Mar 31, 2026
- Notes, reports, biomedical literature
- Templates and copy-paste
- Abbreviations and negation
- De-identification (HIPAA)

#### L20 Clinical NLP modeling
- Thu Apr 2, 2026
- Domain adaptation (BioBERT, ClinicalBERT)
- Clinical NER
- Negation/assertion (NegEx)
- LLMs vs. domain-adapted models
- Annotation bottleneck

### 3.3 Medical imaging (L21-L22)

#### L21 Imaging data
- Tue Apr 7, 2026
- X-ray, CT, MRI, histopathology
- DICOM as standard and shortcut source
- Multi-instance learning for WSIs
- Shortcut learning

#### L22 Imaging modeling
- Thu Apr 9, 2026
- Transfer learning vs. domain pretraining
- DenseNet-121 for CXR
- U-Net segmentation
- Attention-MIL for pathology
- Multi-site generalization

## Part 4 — Population, causality, fairness (L23-L24)

### L23 Population health & survival
- Tue Apr 14, 2026
- Registries, NHANES, SEER, UK Biobank
- Healthy volunteer effect
- Censoring and competing risks
- Kaplan-Meier
- Cox proportional hazards
- Modern survival models

### L24 Causality & fairness
- Thu Apr 16, 2026
- Causal DAGs and do-operator
- Propensity scores
- Sufficiency vs. separation
- Chouldechova impossibility
- Obermeyer case study
- Threshold adjustment

## Part 5 — Molecules & biological AI (L25-L27)

### L25 DNA, genetics, gene regulation
- Tue Apr 21, 2026
- Central dogma
- Population structure, LD
- GWAS, multiple testing
- PRS transferability
- eQTLs

### L26 Proteins & molecules
- Thu Apr 23, 2026
- Protein structure levels
- MSA and PSSMs
- SIFT / PolyPhen
- SMILES, ECFP fingerprints
- QSAR and docking

### L27 Modern biological AI
- Tue Apr 28, 2026
- ESM-2 and protein LMs
- AlphaFold and pLDDT
- Enformer / Evo (DNA FMs)
- Equivariant 3D models
- ProteinMPNN, RFdiffusion

## Part 6 — Course recap (L28)

### L28 Synthesis / recap
- Thu Apr 30, 2026
- Re-walk through Parts 1-5
- Through-lines TL1-TL6
- Q&A
- *(Originally-planned deployment lecture is not taught this cycle.)*

## Cross-cutting through-lines

### TL1 Model ≠ task
- L8, L9, L17-L18, L23, L24

### TL2 Data are generated
- L1, L17-L18, L19-L20, L21-L22, L23, L24, L25

### TL3 Representation is a claim
- L2, L13, L18, L20, L21-L22, L25, L26, L27

### TL4 Generalization is contextual
- L6, L10, L17-L18, L21-L22, L25

### TL5 Classical baselines persist
- L2-L7, L9, L20, L23, L26, L27

### TL6 Deployment creates new distributions
- L8, L17-L18, L24
- *(self-study: Finlayson NEJM 2021, FDA SaMD Action Plan 2021)*
