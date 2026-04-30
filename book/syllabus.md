# BINF 4002 — Machine Learning for Health
## Syllabus (Spring 2026)

```{warning}
**This page was drafted with the help of generative AI and has not been fully reviewed by course staff.** Treat it as a study aid, not a primary source — the released slide decks, notebooks, and lecture recordings are authoritative. See the [home page](intro.md) for the full caveat.
```

This is the **canonical syllabus** for BINF 4002. It is a hierarchical content map: every level — course → part → section → lecture — has the same structure:

- **Topic** — what this level is about, in one sentence.
- **Summary** — 1-3 sentences expanding the topic.
- **Goals / learning objectives** — what students should be able to *do* after this level.
- **Key takeaways** — the load-bearing claims a student should walk away with.
- **Materials** — pointers into `Lectures/lecture-NN-topic/` folders.
- **External references** — textbooks, courses, papers, blog posts.

The dates given for each lecture are the calendar slot in BINF 4002 Spring 2026.

> Companion file:
> - [`concept_map.md`](concept_map.md) — interactive mind map plus a cross-lecture concept map showing how the six course-wide through-lines (TL1-TL6) thread the lectures together. **Start here when you sit down to review.**

---

## Lectures at a glance

| #  | Date         | Topic                                                                                       |
|----|--------------|---------------------------------------------------------------------------------------------|
| 1  | Tue Jan 20   | [Course orientation](lectures/lecture-01.md)                                                |
| 2  | Thu Jan 22   | [Linear algebra](lectures/lecture-02.md)                                                    |
| 3  | Tue Jan 27   | [Probability](lectures/lecture-03.md)                                                       |
| 4  | Thu Jan 29   | [Information theory & Bayesian probability](lectures/lecture-04.md)                         |
| 5  | Tue Feb 3    | [Calculus & optimization](lectures/lecture-05.md)                                           |
| 6  | Thu Feb 5    | [Probabilistic optimization](lectures/lecture-06.md)                                        |
| 7  | Tue Feb 10   | [Probabilistic modeling (Di Liu, guest)](lectures/lecture-07.md)                            |
| 8  | Thu Feb 12   | [Binary-classification evaluation (Florent Pollet, guest)](lectures/lecture-08.md)          |
| 9  | Tue Feb 17   | [Binary-classification training](lectures/lecture-09.md)                                    |
| 10 | Thu Feb 19   | [Generalization, domain shift, fairness recap](lectures/lecture-10.md)                      |
| 11 | Tue Feb 24   | [Lab Day #1](lectures/lecture-11.md)                                                        |
| 12 | Thu Feb 26   | [Lab Day #2](lectures/lecture-12.md)                                                        |
| 13 | Tue Mar 3    | [Neural networks](lectures/lecture-13.md)                                                   |
| 14 | Thu Mar 5    | [Large language models](lectures/lecture-14.md)                                             |
| 15 | Tue Mar 10   | [Foundation models](lectures/lecture-15.md)                                                 |
| 16 | Thu Mar 12   | [Lab Day #3 (last class before spring break)](lectures/lecture-16.md)                       |
| —  | Mar 17 / 19  | *Spring break (no class)*                                                                   |
| 17 | Tue Mar 24   | [EHR & claims data (modality)](lectures/lecture-17.md)                                      |
| 18 | Thu Mar 26   | [EHR & claims data (modeling)](lectures/lecture-18.md)                                      |
| 19 | Tue Mar 31   | [Clinical & biomedical text (modality)](lectures/lecture-19.md)                             |
| 20 | Thu Apr 2    | [Clinical & biomedical NLP (modeling)](lectures/lecture-20.md)                              |
| 21 | Tue Apr 7    | [Medical imaging (modality)](lectures/lecture-21.md)                                        |
| 22 | Thu Apr 9    | [Medical imaging (modeling)](lectures/lecture-22.md)                                        |
| 23 | Tue Apr 14   | [Population health & survival analysis](lectures/lecture-23.md)                             |
| 24 | Thu Apr 16   | [Causality & fairness](lectures/lecture-24.md)                                              |
| 25 | Tue Apr 21   | [DNA, genetics, gene regulation](lectures/lecture-25.md)                                    |
| 26 | Thu Apr 23   | [Proteins, molecules, structural biology](lectures/lecture-26.md)                           |
| 27 | Tue Apr 28   | [Modern biological AI](lectures/lecture-27.md)                                              |
| 28 | Thu Apr 30   | [Course recap / synthesis](lectures/lecture-28.md)                                          |

---

# Level 0 — The course

## Topic
Machine learning for health, taught from mathematical foundations through modern AI and the major clinical and biological data modalities. Deployment is treated as a *through-line* surfaced through other lectures (calibration, domain shift, label/action windows, fairness mechanisms); the standalone deployment lecture originally planned for L28 was **not taught this cycle** and is flagged for self-study (see [L28](lectures/lecture-28.md)).

## Summary
BINF 4002 builds the mathematical and statistical machinery of ML (vectors, probability, optimization, evaluation, generalization), then connects that machinery to modern neural and foundation-model methods, then walks modality by modality through the data and modeling problems of health AI: EHR/claims, clinical text, medical imaging, population health, causality and fairness, genomics, proteins/molecules, modern biological AI. The recurring move across the course is to map a modality onto generic ML, identify where that mapping breaks in health, and trace the breakage to task definition, representation, modeling, and evaluation.

## Goals / learning objectives
After this course, students should be able to:
1. Express health prediction problems as mathematical objects (inputs, outputs, losses, distributions, optimization problems).
2. Choose, train, and evaluate ML models with explicit awareness of capacity, regularization, calibration, discrimination, and clinical utility.
3. Translate health data — EHR events, clinical text, images, registries, genotypes, proteins, small molecules — into ML representations while naming what is lost.
4. Identify the data-generating process behind any health dataset (care delivery, billing, measurement, biology, selection, access) and reason about how it shapes models.
5. Distinguish prediction from intervention; reason mechanistically about fairness; recognize when fairness metrics are mutually incompatible.
6. Critique foundation-model claims by asking what domain and task distribution a model actually covers.
7. Recognize *deployment-adjacent* phenomena introduced through other lectures — calibration drift (L8), domain shift (L10), label/action windows (L17-L18), fairness mechanisms (L24). The standalone topics of drift monitoring, label delay, feedback loops, alert fatigue, and FDA SaMD regulation were *not taught* this cycle; see [L28](lectures/lecture-28.md) for self-study pointers.
8. Hold scientific skepticism about benchmarks, model performance, and deployment claims.

## Key takeaways
1. **The model is never separate from the task.** Same score, different decisions, depending on threshold, utility, prevalence, calibration, workflow.
2. **Data are generated, not given.** Every health dataset has a measurement system, an incentive structure, and a selection mechanism.
3. **Representation is a scientific claim.** Tabularizing, chunking, windowing, tokenizing, embedding, fingerprinting all impose assumptions.
4. **Generalization is contextual.** It depends on sites, populations, workflows, time, prevalence, coding practices, scanners, interventions, and post-deployment feedback.
5. **Modern AI does not remove classical baselines.** Bayes, kNN, calibration, Cox, MSA, PSSMs, homology modeling, QSAR, docking still matter.
6. **Deployment creates new distributions.** Validated models become *part of* the data-generating process they predict over.

## Materials
The full set of `lecture-NN-topic/` folders below, plus `Labs/Labs_export.zip` for in-class lab work and `archive/` for raw/historical files.

## External references — overall
- Beam & Kohane, "Big Data and Machine Learning in Health Care," *JAMA* 319(13), 2018.
- Topol, "High-performance medicine: the convergence of human and artificial intelligence," *Nat Med* 25, 2019.
- Ghassemi, Naumann, Schulam, Beam, Chen, Ranganath, "A Review of Challenges and Opportunities in Machine Learning for Health," *AMIA Joint Summits*, 2020.
- Finlayson et al., "The Clinician and Dataset Shift in Artificial Intelligence," *NEJM* 385, 2021.
- Wiens et al., "Do no harm: a roadmap for responsible machine learning for health care," *Nat Med* 25, 2019.
- Coursera: *AI for Medicine* specialization (deeplearning.ai) — three-course series covering diagnosis, prognosis, and treatment.
- Murphy, *Probabilistic Machine Learning: An Introduction* (vol 1, 2022) — the closest single-volume textbook to this course's spine.

---

# Part 1 — Mathematical & ML foundations  (Lectures 1-10)

## Topic
The language and machinery of ML: linear algebra, probability, calculus, optimization, probabilistic modeling, and the evaluation/training/generalization triad for supervised learning.

## Summary
Part 1 establishes the formal substrate the rest of the course rests on. Vectors and matrices give representations; probability and information theory give random variables, conditioning, Bayes, and entropy; calculus and optimization give gradients and minimization; probabilistic modeling unifies likelihood-based learning. The block closes with binary-classification evaluation, training, and generalization — the canonical supervised-learning loop.

## Goals
- Manipulate vectors, matrices, distributions, gradients, and likelihoods fluently.
- Set up an empirical risk minimization problem and reason about expected vs. empirical loss.
- Evaluate a fixed classifier with calibration, discrimination, decision-curve analysis, and Bayes-optimality.
- Train a classifier; use data splits, regularization, and inductive bias.
- Recognize when ML is the wrong tool (domain shift, fairness, mismatched validation).

## Key takeaways
- ML is sampling + optimization + bias control. Each piece can fail independently.
- Loss functions are *proxies*, not the decision you care about.
- Generalization is not parameter-count; it's about which solutions the optimization is biased toward.

## Materials
`lecture-01-orientation/` through `lecture-10-generalization-domain-shift/`.

## External references — Part 1
- Goodfellow, Bengio, Courville, *Deep Learning*, Chs. 2-9.
- Murphy, *Probabilistic Machine Learning: An Introduction* — Chs. 2-13.
- Hastie, Tibshirani, Friedman, *The Elements of Statistical Learning*, Chs. 1-9.
- Bishop, *Pattern Recognition and Machine Learning*, Chs. 1-4.
- Coursera / Stanford CS229 — Andrew Ng's Machine Learning course.

---

## Section 1.1 — Mathematical preliminaries (L1-L6)

### Topic
Linear algebra, probability, information theory, calculus, deterministic optimization, and probabilistic optimization.

### Summary
Six lectures setting the formal groundwork. L2 introduces vectors and linear operators as the language of representations; L3-L4 develop probability, conditioning, Bayes' rule, and information theory; L5 introduces multivariate calculus and deterministic optimization; L6 generalizes to expected loss over data-generating distributions.

### Goals
- Compute and reason with linear maps, expectations, conditional distributions, gradients.
- State and use Bayes' rule fluently.
- Derive empirical risk minimization from probabilistic optimization.

### Key takeaways
- Coordinatization, conditioning, and gradients are *moves*, not facts.
- Empirical loss is a sampled approximation of expected loss.

### Materials
L2-L6 folders. Companion notebooks: `gradient_descent.ipynb` (L5), `Probabilistic_Optimization.ipynb` (L6).

### External references
- 3Blue1Brown, *Essence of Linear Algebra* video series.
- MacKay, *Information Theory, Inference, and Learning Algorithms* (free PDF).
- Boyd & Vandenberghe, *Convex Optimization* (free PDF).
- Nocedal & Wright, *Numerical Optimization*.

---

### Lecture 1 — Course orientation

- **Date.** Tue Jan 20, 2026.
- **Topic.** Course logistics and the goals of an ML/AI for health class.
- **Summary.** First-day deck. Why this course starts with math, why durable intuition matters more than tool-of-the-month, and why ML for health needs both ML fundamentals and health-specific epistemic caution.
- **Goals.** Understand expectations, the course's emphasis on intuition, and the idea that ML for health ≠ generic ML on health-shaped inputs.
- **Key takeaways.** "Healthy epistemic uncertainty" is an explicit objective; conceptual understanding outlives any specific tool.
- **Materials.** `lecture-01-orientation/Lecture 1.pdf`, `Lecture 1 - Intros_and_overview.pptx`.
- **External references.** Beam & Kohane (*JAMA* 2018); Topol (*Nat Med* 2019).

---

### Lecture 2 — Linear algebra: vectors, vector spaces, linear operators, matrices

- **Date.** Thu Jan 22, 2026.
- **Topic.** Linear algebra as the representational language of ML.
- **Summary.** Builds vectors → vector spaces → linear operators → matrices → bases → matrix multiplication. Points students toward eigen/SVD/matrix calculus for self-study.
- **Goals.** Distinguish abstract vectors from coordinate representations; read a matrix as the coordinate form of a linear map; understand basis change.
- **Key takeaways.** A matrix is not a table; it is a linear operator written in a chosen basis. Representation choice determines what the model can see.
- **Subsections.**
  - Why linear algebra in ML.
  - Linearity, linear combinations, vector spaces.
  - Linear operators, matrices, matrix multiplication.
  - Bases and coordinatization.
  - Pointers: eigenanalysis, SVD, matrix calculus, matrix exponentials.
- **Materials.** `lecture-02-linear-algebra/Lecture 2.pdf`, `Lecture 2 - linear_algebra.pptx`.
- **External references.** Strang, *Introduction to Linear Algebra*; 3Blue1Brown; Goodfellow et al. Ch. 2.

---

### Lecture 3 — Probability: random variables, expectation, joint distributions

- **Date.** Tue Jan 27, 2026.
- **Topic.** Formal probability — sample spaces, events, measures, random variables, expectation, joint distributions.
- **Summary.** Probability triples (Ω, F, P) → discrete examples → random variables as functions on Ω → expectation as the bridge to ML loss → joint distributions. Paradox flagged: Envelope.
- **Goals.** Reason about a random variable as a function, not a number. Use expectation as the operator that connects probability to objectives.
- **Key takeaways.** RVs are functions; events are structured subsets; expectation is the bridge to losses.
- **Subsections.**
  - Probability triples and discrete examples.
  - Random variables as measurable functions.
  - Expectation.
  - Joint random variables.
- **Materials.** `lecture-03-probability/Lecture 3.pdf`, `Lecture 3 - probability.pptx`.
- **External references.** Bishop *PRML* Ch. 1; Wasserman *All of Statistics* Chs. 1-3; Murphy *PML* Ch. 2.

---

### Lecture 4 — Conditioning, Bayes' rule, and information theory

- **Date.** Thu Jan 29, 2026.
- **Topic.** Conditioning, marginalization, Bayes, Bayesian inference, information theory.
- **Summary.** Marginal vs. conditional distributions, independence, Bayes' rule, prior/posterior/likelihood/evidence, then entropy / KL / mutual information for the loss-function and language-modeling later. Paradox flagged: St. Petersburg.
- **Goals.** Derive Bayes' rule; interpret Bayesian quantities; use information-theoretic measures.
- **Key takeaways.** Conditioning is renormalization, not filtering. Bayes' rule is rearrangement of a joint. Information theory underwrites cross-entropy losses.
- **Subsections.**
  - LLN and expectation refresher.
  - Marginal and conditional distributions, independence.
  - Bayes' rule and Bayesian statistics (prior/likelihood/evidence/posterior).
  - Information theory: entropy, KL, mutual information; geometric/statistical intuition.
- **Materials.** `lecture-04-information-theory/Lecture 4 - information_theory.pptx` (Google Slides → PowerPoint source); `Lecture 4.pdf` (41-page PowerPoint-exported PDF — the only version shown to students).
- **External references.** MacKay Chs. 2-4 and 24; Cover & Thomas Ch. 2; Bishop *PRML* Chs. 1-2.

---

### Lecture 5 — Calculus and optimization

- **Date.** Tue Feb 3, 2026.
- **Topic.** Multivariate calculus and deterministic optimization.
- **Summary.** Functions on Rⁿ → derivatives, gradients, smoothness → stationary points and optima → optimization algorithms (random search, coordinate descent, gradient descent) and how high-dimensional landscapes differ from 2-D pictures. Paradox: Borel-Kolmogorov.
- **Goals.** Compute gradients; reason geometrically about optima; pick an appropriate optimizer for a problem.
- **Key takeaways.** The gradient points uphill; optimization is geometry; high-D ≠ low-D intuition.
- **Subsections.**
  - Multivariate differentiation; smoothness.
  - Gradients, tangent surfaces, stationary points.
  - Random search, coordinate descent, gradient descent.
  - Low-D vs. high-D landscapes.
- **Materials.** `lecture-05-calculus-optimization/Lecture 5.pdf`, `Lecture 5 - calculus_and_optimization.pptx`, `gradient_descent.ipynb`.
- **External references.** Boyd & Vandenberghe Ch. 9; Nocedal & Wright Chs. 2-3; Goodfellow et al. Ch. 4.

---

### Lecture 6 — Probabilistic optimization

- **Date.** Thu Feb 5, 2026.
- **Topic.** Optimizing expected loss when inputs and labels are random.
- **Summary.** Lifts L5 from deterministic to probabilistic objectives. Training data are samples from a distribution; the real goal is expected loss on future samples; this is the train/test/generalization gap. Paradox: Red-ball Black-ball.
- **Goals.** Distinguish empirical from expected loss; reason about iid sampling and generalization.
- **Key takeaways.** ML is optimizing an expectation observed only through samples. Empirical risk minimization is an *estimate* of the real objective.
- **Subsections.**
  - Random inputs and labels; expected objectives.
  - Empirical data as iid samples.
  - Static vs. sampled functions.
  - Generalization preview.
- **Materials.** `lecture-06-probabilistic-optimization/Lecture 6.pdf`, `Lecture 6 - probabilistic_optimization.pptx`, `Probabilistic_Optimization.ipynb`.
- **External references.** Vapnik, *Nature of Statistical Learning Theory* Chs. 1-2; Shalev-Shwartz & Ben-David Chs. 2-3; Bottou, Curtis & Nocedal, *SIAM Review* 2018.

---

## Section 1.2 — Probabilistic modeling and supervised learning (L7)

### Lecture 7 — Probabilistic modeling and optimization (guest: Di Liu)

- **Date.** Tue Feb 10, 2026.
- **Topic.** A unified probabilistic ML workflow: data → model → likelihood objective → optimization.
- **Summary.** Guest lecture. Casts regression and classification as likelihood-based probabilistic models; introduces multi-expert regression and unsupervised mixture models with EM vs. gradient descent.
- **Goals.** Frame ML training as NLL minimization; choose between EM and gradient descent.
- **Key takeaways.** Most supervised losses are NLLs under a probabilistic assumption. Latent variables let you model heterogeneous populations.
- **Subsections.**
  - Data notation: supervised vs. unsupervised.
  - Parametric probabilistic models; NLL.
  - Single- and multi-expert regression.
  - GMMs; EM vs. gradient descent.
- **Materials.** `lecture-07-probabilistic-modeling/Lecture 7 - Di Liu (guest).pdf` — guest deck, no editable source.
- **External references.** Bishop *PRML* Chs. 3-4 and 9; Murphy *PML* Chs. 8-11; Dempster, Laird, Rubin (1977).

---

## Section 1.3 — Evaluation, training, and generalization (L8-L10)

### Topic
Evaluating fixed classifiers, training new ones, and characterizing when they generalize.

### Summary
Three-lecture arc that teaches the supervised-learning loop. L8 evaluates a *fixed* classifier (calibration, discrimination, AUROC, decision-curve analysis); L9 turns to *training* (loss + optimization + overfitting control); L10 closes with generalization, inductive bias, regularization, domain shift, explainability, and fairness.

### Goals
- Pick metrics that match the clinical decision and utility.
- Build a training pipeline (data splits, loss, optimizer, monitoring).
- Diagnose overfitting and explain why over-parameterized models can still generalize.

### Key takeaways
- Evaluation is task-conditional; AUROC alone is rarely enough.
- Overfitting is controlled by inductive bias, not just parameter count.
- Domain shift, explainability, and fairness are first-order concerns in health AI.

---

### Lecture 8 — Binary-classification evaluation (guest: Florent Pollet)

- **Date.** Thu Feb 12, 2026.
- **Topic.** Evaluating a fixed binary classifier.
- **Summary.** Hard vs. soft classification; confusion matrix; clinical utility under thresholds; Bayes-optimal decision rules; calibration vs. discrimination; AUROC limitations; decision-curve analysis. Paradox: Simpson's, connected to AUC.
- **Goals.** Distinguish discrimination from calibration; choose thresholds via utility; recognize when AUROC is misleading (rare outcomes, miscalibration).
- **Key takeaways.** Score → decision is the missing step in many published reports. Discrimination and calibration are different failure modes.
- **Subsections.**
  - Hard classification, confusion matrix.
  - Utility and decision thresholds; soft scores; probabilities.
  - Bayes-optimal classifiers.
  - Decision-curve analysis.
  - Discrimination vs. calibration.
  - AUROC and its limits.
- **Materials.** `lecture-08-binary-classification-evaluation/Lecture 8 - Florent Pollet (guest).pdf` (canonical), `Lecture 8 - binary_classification_evaluation.pptx` (earlier draft).
- **External references.** Pepe, *The Statistical Evaluation of Medical Tests*; Steyerberg, *Clinical Prediction Models* Chs. 15-17; Vickers & Elkin (2006); Van Calster et al. (2019).

---

### Lecture 9 — Binary-classification training

- **Date.** Tue Feb 17, 2026.
- **Topic.** Training a classifier: loss, optimization, overfitting control.
- **Summary.** Opens with influenza vaccine effectiveness as a confounding/observational warning, then walks the ML pipeline: data splits → loss → optimization → overfitting → kNN as a procedural baseline. Paradox: Healthy Vaccinee Effect.
- **Goals.** Set up data splits; pick a loss; recognize overfitting; reason about kNN consistency.
- **Key takeaways.** The problem dictates the pipeline. Loss is a proxy; optimization solves the proxy, not the decision.
- **Subsections.**
  - Influenza vaccine effectiveness as a confounding case study.
  - The ML pipeline (loss, optimization, overfitting control).
  - Data splits; capacity; misspecification.
  - kNN and consistency.
  - Empirical loss as imperfect objective.
- **Materials.** `lecture-09-binary-classification-training/Lecture 9.pdf`, `Lecture 9.pptx`, `Lecture_9.ipynb`, `dataset (*).jpg`.
- **External references.** ESL Chs. 2 and 13; Murphy *PML* Chs. 4 and 16; Domingos, "A Few Useful Things to Know About Machine Learning," *CACM* 55(10), 2012.

---

### Lecture 10 — Generalization, domain shift, fairness recap

- **Date.** Thu Feb 19, 2026.
- **Topic.** Closing the foundations block: generalization, overfitting, regularization, inductive bias, negative controls, domain shift, explainability, fairness.
- **Summary.** Reframes overfitting through memorization, capacity, and inductive bias; introduces negative controls and the modern-DL puzzle (over-parameterized models that still generalize); closes with the failure modes — domain shift, explainability, fairness — that the second half of the course will revisit.
- **Goals.** Explain modern-DL generalization without invoking parameter count; design negative controls; identify when ML is the wrong tool.
- **Key takeaways.** Memorization-capable models can still generalize; what matters is what the optimization makes easy. Negative controls are basic ML hygiene.
- **Subsections.**
  - Overfitting and memorization.
  - Capacity, regularization, bias-variance.
  - Modern-DL generalization puzzle.
  - kNN/interpolation paradox.
  - Inductive bias.
  - Negative controls.
  - Domain shift, explainability, fairness as gating concerns.
- **Materials.** `lecture-10-generalization-domain-shift/Lecture 10.pdf`, `Lecture 10.pptx`.
- **External references.** Zhang et al. (*ICLR* 2017); Belkin et al. (*PNAS* 2019); D'Amour et al. (*JMLR* 2022); Finlayson et al. (*NEJM* 2021).

---

# Part 2 — Modern AI methods and lab work  (Lectures 11-16)

## Topic
Three lectures introducing modern AI (neural networks, LLMs, foundation models), interleaved with three in-class lab/Q&A days during which students worked through the released lab notebooks.

## Summary
Calendar-wise: lab → lab → NN → LLMs → FMs → lab, then spring break. The three lecture lectures generalize the optimization arc of Part 1 to expressive parametric function classes (NNs), instantiate next-token prediction at scale (LLMs), and abstract the task-conditioning view (FMs). The three lab days gave students supervised time to work through 17 lab notebooks released in three chunks: ML model types (labs 0-5), ML loss types (6-11), and data types (12-16).

## Goals
- Understand neural networks, transformers, and the foundation-model concept conceptually.
- Recognize architecture as inductive bias.
- Critique foundation-model claims by asking *what task distribution* a model covers.

## Key takeaways
- A neural network is the optimization arc of Part 1, scaled up via differentiable programming.
- LLMs train on next-token prediction but exhibit broad task behavior through scale and prompting.
- "Foundation model" is ambiguous; always ask what domain and task distribution it covers.

## Materials
`lecture-11-lab-day-1/`, `lecture-12-lab-day-2/`, `lecture-13-neural-networks/`, `lecture-14-large-language-models/`, `lecture-15-foundation-models/`, `lecture-16-lab-day-3/`. Master lab copies in `Labs/Labs_export.zip`.

## External references — Part 2
- Goodfellow, Bengio, Courville, *Deep Learning*, Chs. 6-12.
- Vaswani et al., "Attention Is All You Need," *NeurIPS* 2017.
- Jurafsky & Martin, *Speech and Language Processing*, 3rd ed. drafts.
- Bommasani et al., "On the Opportunities and Risks of Foundation Models," arXiv:2108.07258.
- "The Illustrated Transformer," Jay Alammar (blog).
- Karpathy, "A Recipe for Training Neural Networks" (blog).

---

### Lecture 11 — Lab Day #1

- **Date.** Tue Feb 24, 2026.
- **Topic.** In-class Q&A and lab work on the first lab chunk.
- **Summary.** No new lecture material. Students worked through labs 0-5 (released Sun Feb 22) covering preprocessing, logistic regression, decision trees, kNN, ensemble methods, and neural networks as ML *model types*.
- **Goals.** Hands-on practice with the model-type spectrum; instructor-supervised debugging.
- **Key takeaways.** The model-type spectrum (linear → tree → ensemble → neural) corresponds to different inductive biases.
- **Materials.** `lecture-11-lab-day-1/labs/lab[0-5]_*.ipynb`, `solutions/`.
- **External references.** scikit-learn user guide; Hands-On Machine Learning, Géron (3rd ed.) — Chs. on linear models, trees, ensembles.

---

### Lecture 12 — Lab Day #2

- **Date.** Thu Feb 26, 2026.
- **Topic.** Continued lab work on chunk #1.
- **Summary.** Second of two consecutive lab/Q&A days. Lab chunk #2 (ML losses) was released Mon Mar 2, just after this class.
- **Goals.** Finish the model-type chunk before moving to losses.
- **Key takeaways.** (Same as L11.)
- **Materials.** `lecture-12-lab-day-2/labs/lab[0-5]_*.ipynb`, `solutions/`.
- **External references.** Same as L11.

---

### Lecture 13 — Neural networks: from motivation to practice

- **Date.** Tue Mar 3, 2026.
- **Topic.** Neural networks as expressive, parametric, differentiable function classes.
- **Summary.** Anatomy (layers, activations, depth, parameters); architecture as inductive bias; practical optimization (init, normalization, residuals, optimizers, LR schedules, batch size, gradient clipping, accumulation, monitoring, regularization). Companion notebook runs MNIST experiments.
- **Goals.** Read a neural network as a parametric function class; pick architecture per inductive-bias intent; debug training with a checklist.
- **Key takeaways.** Architecture and optimization details *are* the model. Expressive models fail silently — monitoring is mandatory.
- **Subsections.**
  - Motivation; comparison to linear, kernel, and tree models.
  - Layers, activations, depth.
  - Architecture as inductive bias.
  - Loss matching task type.
  - Initialization, normalization, residuals.
  - Optimizers, LR, batch-size scaling.
  - Gradient clipping/accumulation.
  - Monitoring and regularization.
  - MNIST companion experiments.
- **Materials.** `lecture-13-neural-networks/nn_lecture.pdf`, `latex/nn_lecture.tex` + `figures/`, `nn_fundamentals_lab.ipynb`. *Source compiles to 95p / 1494 text-lines, exact match.*
- **External references.** Goodfellow et al. Chs. 6-8; He et al. (*ICCV* 2015) Kaiming init; Ioffe & Szegedy (*ICML* 2015) BatchNorm; He et al. (*CVPR* 2016) ResNet; Smith arXiv:1803.09820; Karpathy "Recipe for Training Neural Networks."

---

### Lecture 14 — Large language models: from n-grams to attention

- **Date.** Thu Mar 5, 2026.
- **Topic.** Language modeling, transformers, attention, the LLM ecosystem.
- **Summary.** Opens with the Chinese Room paradox; n-gram models and their failure under sparsity / combinatorial explosion; transformer/attention; next-token prediction as a flexible interface; LLM ecosystem and limitations. Notebook demos n-gram models, attention, sampling temperature.
- **Goals.** State the language-modeling objective; explain why attention beats n-grams; critique fluent-but-ungrounded LLM output.
- **Key takeaways.** A simple objective + scale + prompting yields broad task behavior, but fluency ≠ understanding.
- **Subsections.**
  - Chinese Room thought experiment.
  - Language-modeling objective.
  - N-grams; sparsity; combinatorics.
  - Transformer architecture and attention.
  - LLM ecosystem and modes.
  - Open challenges and epistemic hazards.
  - Notebook: n-grams, attention, temperature.
- **Materials.** `lecture-14-large-language-models/llms_lecture.pdf`, `latex/llm_lecture.tex` + `figures/`, `llm_lecture_notebook.ipynb`. *Source compiles to 145p / 2142 text-lines, exact match.*
- **External references.** Vaswani et al. (*NeurIPS* 2017); Bender, Gebru et al. "Stochastic Parrots" (*FAccT* 2021); Brown et al. GPT-3 (*NeurIPS* 2020); Hoffmann et al. Chinchilla (arXiv:2203.15556); Jurafsky & Martin 3rd ed.; Alammar, "The Illustrated Transformer."

---

### Lecture 15 — Foundation models

- **Date.** Tue Mar 10, 2026.
- **Topic.** What "foundation model" means, especially in health.
- **Summary.** Spectrum from single-task → multi-task → few-shot/transfer → zero-shot/task-conditioned models. Formalizes task-conditioning as taking input `x` *and* task `α`. Argues that "foundation model" is ambiguous and that the meaningful axes are task distribution, labeled-vs.-total data efficiency, and adaptation accessibility.
- **Goals.** Critique a foundation-model claim by asking what task distribution it covers; reason about prior-fitted networks and EHR autoregressive models as universal-task setups.
- **Key takeaways.** "Foundation model over what?" is the load-bearing question. Total data efficiency and labeled-data efficiency are different things.
- **Subsections.**
  - Motivation: clinical Q&A from L14.
  - Bommasani et al. definition.
  - The single-task → zero-shot spectrum.
  - Task-conditioning formalism (`x`, `α`).
  - Task distributions and inductive bias.
  - Labeled-data vs. total-data efficiency.
  - Evaluation over task distributions.
  - EHR autoregressive models; prior-fitted networks (TabPFN-style).
- **Materials.** `lecture-15-foundation-models/FMs Lecture.pdf`, `FMs Lecture.pptx` (PPTX-only source).
- **External references.** Bommasani et al. (arXiv:2108.07258); Moor et al. (*Nature* 2023); Steinberg et al. (*JBI* 2021) on EHR autoregressive models; Hollmann et al. TabPFN (*ICLR* 2023).

---

### Lecture 16 — Lab Day #3 (last class before spring break)

- **Date.** Thu Mar 12, 2026.
- **Topic.** Lab work on the second and third chunks.
- **Summary.** Last in-class lab day. Lab chunk #2 (ML losses, labs 6-11; released Mar 2) and chunk #3 (data types, labs 12-16; released Fri Mar 6) are both in scope.
- **Goals.** Hands-on practice with multiclass, regression, survival, probabilistic regression, clustering, dim-reduction, graphs, sequences, images, time series, and event streams.
- **Key takeaways.** Loss type and data type are independent ML axes; both matter.
- **Materials.** `lecture-16-lab-day-3/labs/lab[6-9]_*.ipynb`, `lab1[0-6]_*.ipynb`, `solutions/`.
- **External references.** scikit-learn user guide; Géron *Hands-On ML* — chs on regression and unsupervised learning; *Time Series Analysis*, Hamilton; *MEDS* schema docs (for `lab16_event_streams_MEDS`).

---

# Part 3 — Clinical AI  (Lectures 17-22)

## Topic
Three two-lecture pairs (data → modeling) through EHR/claims, clinical text, and medical imaging — the data types that arise as a byproduct of clinical care.

## Summary
For each of three major data types produced by the practice of care — EHR/claims (L17-L18), clinical & biomedical text (L19-L20), medical imaging (L21-L22) — students learn the data-generating process and care-specific pathologies first, then the modeling consequences. The recurring move is: enumerate how the data are produced (care delivery, billing, documentation, scanners, labs); identify what is informative beyond labels (timing, missingness, metadata); pick a representation; pick a model.

## Goals
- Read an EHR / claims dataset, clinical-note corpus, or imaging dataset and name what is generated, what is missing, and what is selection.
- Pick representations (tabularized, chunked, event stream; tokens, embeddings, RAG; 2D vs. 3D vs. WSI) with explicit assumption costs.
- Apply transfer learning, domain adaptation, U-Nets, MIL, etc., where appropriate.

## Key takeaways
- Health data are byproducts of measurement systems; their pathologies are informative *and* hazardous.
- Representation is a modeling decision, not preprocessing trivia.
- Modality-specific pretraining and architectures encode inductive bias that generic ML lacks.

## Materials
L17-L22 folders.

## External references — Part 3
- *The Book of OHDSI* (free online) for OMOP CDM.
- *MEDS schema specification* (the modality-agnostic event-stream format).
- Litjens et al., "A survey on deep learning in medical image analysis," *Med Image Anal* 42, 2017.
- Wu et al., "A survey on clinical NLP in the UK 2007-2022," *NPJ Digit Med* 5, 2022.
- Coursera *AI for Medical Diagnosis* (deeplearning.ai).

---

## Section 3.1 — EHR & claims (L17-L18)

### Lecture 17 — EHR and claims data: the modality

- **Date.** Tue Mar 24, 2026.
- **Topic.** EHR and claims data as a modality.
- **Summary.** Berkson's-paradox warm-up; what an EHR is; what claims data are; coding systems (ICD, CPT, RxNorm, SNOMED-CT); informative observation; selection (who appears in the data?); cohort definition; standards (OMOP, MEDS, FHIR). Paradox: Coastline / # of features.
- **Goals.** Read an EHR / claims schema; reason about who is selected; map a clinical question to an OMOP/MEDS query.
- **Key takeaways.** EHR/claims are not designed measurements; they are byproducts of care and billing. Code presence/absence is itself informative.
- **Subsections.**
  - Statistical-trap motivation (Berkson).
  - What an EHR is; what claims data are; comparison.
  - Diagnosis coding systems and hierarchy.
  - Who's in the data?
  - Health event streams.
  - Cohort selection as a task.
  - Standards (OMOP CDM, MEDS, FHIR).
- **Materials.** `lecture-17-ehr-claims-data/Health_Data_Modalities_EHR_Claims_Data.pdf`, `latex/Lecture17_EHR_Claims.tex` + `figures/`, `nb17_ehr_claims.ipynb`. *Source compiles to 107p / 1656 text-lines, exact match (after picking the correct .tex from `Health_Data_Modalities_I_EHR_Claims_Data__1_.zip`).*
- **External references.** Hripcsak & Albers (*JAMIA* 2013); Wells et al. (*EGEMS* 2013); *Book of OHDSI*; MEDS schema docs; Beam & Kohane (*JAMA* 2018).

---

### Lecture 18 — EHR and claims data: modeling

- **Date.** Thu Mar 26, 2026.
- **Topic.** What EHR/claims pathology does to modeling.
- **Summary.** Even keeping the prediction objective to binary classification, modeling EHR data forces task-definition decisions: prediction time, observation/prediction/label/action windows, censoring, competing risks. Three representation families — tabularized, chunked, event stream — encode different assumptions. Paradox: Birthday.
- **Goals.** Define a workflow-aligned health prediction task; pick a representation per assumption cost; recognize leakage and target misalignment.
- **Key takeaways.** Binary classification doesn't make EHR modeling simple. Survival analysis is often the principled generalization.
- **Subsections.**
  - Recap of EHR pathologies.
  - Task definition: actionability, censoring, competing risks.
  - Three representation families.
  - Implications for losses, evaluation, validation.
  - Common leakage modes.
- **Materials.** `lecture-18-ehr-claims-modeling/lecture18_modeling_ehr_claims.pdf`, `latex/lecture18_modeling_ehr_claims.tex` + 2 figures (no companion notebook). *Source compiles to 114p / 1854 text-lines, exact match.*
- **External references.** Tang et al. FIDDLE (*JAMIA* 2020); Choi et al. Doctor AI (*MLHC* 2016); Rajkomar et al. (*npj Digit Med* 2018); McDermott et al. *Event Stream GPT*; Lipton et al. (*MLHC* 2016).

---

## Section 3.2 — Clinical & biomedical text (L19-L20)

### Lecture 19 — Clinical and biomedical text: the modality

- **Date.** Tue Mar 31, 2026.
- **Topic.** Health text — clinical notes, reports, biomedical literature — as data.
- **Summary.** Three text domains; anatomy of a clinical note; templates and copy-paste / note bloat; abbreviation ambiguity; negation; radiology and pathology reports as semi-structured text; PubMed; de-identification (HIPAA Safe Harbor); MIMIC-III.
- **Goals.** Read a clinical note as workflow output; identify negation/abbreviation/copy-paste pitfalls; understand de-identification and access constraints.
- **Key takeaways.** Clinical text is not natural language; it's documentation produced under workflow and billing pressure.
- **Subsections.**
  - Three text domains.
  - Anatomy of a clinical note; real-note example.
  - Templates and copy-paste / note bloat.
  - Abbreviations and negation.
  - Radiology and pathology reports.
  - PubMed and biomedical literature.
  - De-identification and data access.
- **Materials.** `lecture-19-clinical-text-data/L19.pdf`, `latex/main.tex` + `figures/`, `nb19_clinical_text_data.ipynb`. *Source compiles to 100p / 1410 text-lines, exact match.*
- **External references.** Wang et al. (*BMC Med Inform Decis Mak* 2019); Wu et al. (*NPJ Digit Med* 2022); Steinkamp et al. (*JAMIA Open* 2021); Johnson et al. MIMIC-III (*Sci Data* 2016).

---

### Lecture 20 — Clinical and biomedical NLP: modeling

- **Date.** Thu Apr 2, 2026.
- **Topic.** Domain-adapted vs. general-language NLP; clinical NER; negation/assertion; relation extraction; LLMs vs. domain-adapted models; annotation bottlenecks; RAG.
- **Summary.** Domain mismatch motivates clinical pretraining (BioBERT, ClinicalBERT, PubMedBERT); NER as a core task; NegEx for negation; relation extraction for clinical IE; LLMs as a complement, not replacement; inter-annotator agreement.
- **Goals.** Pick between clinical-pretrained models and LLMs; design an annotation pipeline; recognize when relation extraction is needed beyond NER.
- **Key takeaways.** Clinical NLP is constrained by domain mismatch, privacy, annotation cost, and ambiguity. NER alone is rarely enough.
- **Subsections.**
  - Domain mismatch.
  - Clinical-NLP model lineage.
  - Why domain adaptation works.
  - NER and its difficulties.
  - Assertion / negation; NegEx.
  - Relation extraction and clinical IE.
  - LLMs vs. domain-adapted models.
  - Annotation bottleneck and inter-annotator agreement.
  - RAG pipelines.
- **Materials.** `lecture-20-clinical-nlp-modeling/L20.pdf`, `latex/main.tex` + `figures/`, `nb20_clinical_nlp.ipynb`. *Source compiles to 37p / 484 text-lines, exact match.*
- **External references.** Chapman et al. NegEx (*JBI* 2001); Alsentzer et al. ClinicalBERT (*ClinicalNLP@NAACL* 2019); Lee et al. BioBERT (*Bioinformatics* 2020); Singhal et al. Med-PaLM (*Nature* 2023); Zack et al. (*Lancet Digital Health* 2024).

---

## Section 3.3 — Medical imaging (L21-L22)

### Lecture 21 — Medical imaging: the modality

- **Date.** Tue Apr 7, 2026.
- **Topic.** X-ray, CT, MRI, histopathology, DICOM metadata — and how medical images differ from natural images.
- **Summary.** Acquisition physics and dataset properties for radiographs, CT (volumetric), MRI (volumetric, multi-sequence), histopathology (gigapixel, multi-instance), retinal/dermatoscopic/ultrasound. DICOM as both standard and shortcut source. Data-quality issues; shortcut learning. Paradox: Garden of forking paths.
- **Goals.** Read a DICOM header; pick 2D vs. volumetric vs. MIL representation; identify shortcut signals.
- **Key takeaways.** Medical images are not natural images. DICOM metadata is essential and a shortcut hazard. Histopathology is a gigapixel/MIL problem.
- **Subsections.**
  - X-ray production.
  - Medical vs. natural images.
  - CXR datasets.
  - CT volumetric imaging.
  - MRI volumetric imaging.
  - ML mapping for volumes.
  - Histopathology, gigapixel problem, multi-scale.
  - Multi-instance learning formulation.
  - Other modalities.
  - DICOM.
  - Shortcut learning; data quality.
- **Materials.** `lecture-21-medical-imaging-data/L21.pdf`, `latex/main.tex` + `figures/`, `nb21_medical_imaging_data.ipynb`. *Source compiles to 78p / 1120 text-lines, exact match.*
- **External references.** Mårtensson et al. (*Med Image Anal* 2020); DeGrave et al. (*Nat Mach Intell* 2021); Zech et al. (*PLOS Med* 2018); Litjens et al. (*Med Image Anal* 2017); DICOM Standard.

---

### Lecture 22 — Medical imaging: modeling

- **Date.** Thu Apr 9, 2026.
- **Topic.** Transfer learning, domain-specific and self-supervised pretraining, U-Net segmentation, MIL for pathology, augmentation, multi-site generalization.
- **Summary.** CXR classification (DenseNet-121); segmentation (U-Net, skip connections, Dice loss); attention-MIL for pathology; modality-specific augmentation; class imbalance; multi-site generalization; the "garden of forking paths" in evaluation.
- **Goals.** Pick a pretraining strategy; design a U-Net for segmentation; build an MIL pipeline; defend an augmentation strategy.
- **Key takeaways.** Architecture induces bias (CNN, U-Net, MIL). Multi-site generalization is the real benchmark.
- **Subsections.**
  - Recap of imaging data.
  - Transfer learning.
  - Domain-specific and self-supervised pretraining.
  - CXR classification; DenseNet-121.
  - Segmentation; U-Net; skip connections.
  - Segmentation losses and metrics.
  - MIL and attention-MIL.
  - Modality-specific augmentation.
  - Class imbalance.
  - Multi-site generalization.
  - Garden of forking paths.
- **Materials.** `lecture-22-medical-imaging-modeling/L22.pdf`, `latex/lec22_imaging_modeling.tex` + `figures/`, `nb22_medical_imaging_modeling.ipynb`. *Source compiles to 62p / 915 text-lines, exact match.*
- **External references.** Rajpurkar et al. CheXNet (arXiv:1711.05225); Ronneberger et al. U-Net (*MICCAI* 2015); Ilse et al. Attention-MIL (*ICML* 2018); Raghu et al. Transfusion (*NeurIPS* 2019); Azizi et al. (*ICCV* 2021); Glocker et al. (*Radiology AI* 2023).

---

# Part 4 — Population, causality, fairness  (Lectures 23-24)

## Topic
Lifting the lens beyond a single hospital's EHR/imaging system: registries, surveys, biobanks, trials; survival analysis; causal DAGs; fairness.

## Summary
L23 broadens the data lens from EHR/claims to designed data sources (NHANES, SEER, UK Biobank, RCTs) and introduces survival analysis (censoring, competing risks, Kaplan-Meier, Cox, modern survival models). L24 separates prediction from intervention via causal DAGs and the do-operator, then formalizes fairness (sufficiency, separation, the impossibility result), with the Obermeyer et al. study as a canonical mechanism-of-bias case.

## Goals
- Pick a data source per question (registry, survey, trial, biobank, EHR).
- Read a Kaplan-Meier curve; interpret a Cox forest plot.
- Read a DAG; distinguish prediction from intervention.
- Critique a fairness claim mechanistically.

## Key takeaways
- Population-scale questions often require non-EHR data.
- Censoring and competing risks are first-class problems, not annoyances.
- Fairness metrics are mutually incompatible under unequal base rates and imperfect prediction.

## Materials
L23-L24 folders.

## External references — Part 4
- Hernán & Robins, *Causal Inference: What If* (free PDF).
- Pearl, *Causality*; Pearl, Glymour, Jewell, *Causal Inference in Statistics: A Primer*.
- Kaplan & Meier (*JASA* 1958); Cox (*JRSS B* 1972).
- Obermeyer et al. (*Science* 2019).
- Coursera *A Crash Course in Causality*, Roy.

---

### Lecture 23 — Population health data and survival analysis

- **Date.** Tue Apr 14, 2026.
- **Topic.** Beyond EHR: registries, surveys, biobanks, RCTs; survival analysis.
- **Summary.** NHANES / SEER / UK Biobank / clinical-trial structure; healthy-volunteer effect; Simpson's paradox in real health data. Then survival analysis: censoring, competing risks, Kaplan-Meier, Cox, modern models (DeepSurv, DeepHit). Closes with a propensity-score preview for L24.
- **Goals.** Map a question to a data source; interpret KM curves and Cox hazard ratios; recognize when binary classification hides survival structure.
- **Key takeaways.** No data source is universally best. Survival analysis is necessary when time-to-event matters.
- **Subsections.**
  - Why EHR is not enough.
  - Registry data; Simpson's paradox.
  - RCTs and trial heterogeneity.
  - The data spectrum.
  - NHANES, SEER, biobanks; healthy-volunteer effect.
  - Survival concepts: censoring, competing risks.
  - Kaplan-Meier and subgroups.
  - Cox proportional hazards.
  - Modern survival models.
  - Propensity-score preview for L24.
- **Materials.** `lecture-23-population-health-survival/lecture23.pdf`, `latex/lecture23.tex` + `figures/`, `nb23_pophealth.ipynb`. *Source compiles to 68p / 990 text-lines, exact match.*
- **External references.** Kaplan & Meier (1958); Cox (1972); Katzman et al. DeepSurv (*BMC Med Res Methodol* 2018); Lee et al. DeepHit (*AAAI* 2018); Bycroft et al. UK Biobank (*Nature* 2018).

---

### Lecture 24 — Causality and fairness

- **Date.** Thu Apr 16, 2026.
- **Topic.** Causal DAGs, do-operator, propensity scores, fairness definitions, impossibility, mitigation.
- **Summary.** Three DAG patterns (chain, fork, collider); the do-operator; propensity-score adjustment; fairness definitions (sufficiency vs. separation); Chouldechova-style impossibility; Obermeyer et al. case study; mitigation across data, model, and threshold.
- **Goals.** Draw a DAG for a clinical question; pick a fairness metric per stakeholder claim; explain why two metrics are incompatible.
- **Key takeaways.** Prediction ≠ intervention. Observed labels can encode biased systems of care.
- **Subsections.**
  - Causal DAGs.
  - The do-operator.
  - Three DAG patterns.
  - Bias gallery.
  - Propensity scores.
  - Fairness definitions.
  - Sufficiency vs. separation.
  - Chouldechova impossibility.
  - Obermeyer case study.
  - Subgroup evaluation.
  - Threshold adjustment and mitigation.
- **Materials.** `lecture-24-causality-fairness/lec24_causality_fairness.pdf`, `latex/lec24_causality_fairness.tex`, `nb24_causality_fairness.ipynb`. *Source compiles to 55p in draft mode (figures 1-6 are notebook-generated and not bundled as static files); to recompile with embedded figures, run the notebook first.*
- **External references.** Pearl, Glymour, Jewell *Causal Inference: A Primer*; Hernán & Robins *What If*; Obermeyer et al. (*Science* 2019); Chouldechova (*Big Data* 2017); Kleinberg, Mullainathan, Raghavan (*ITCS* 2017); Rajkomar et al. (*Ann Intern Med* 2018).

---

# Part 5 — Biomedical molecules and modern biological AI  (Lectures 25-27)

## Topic
DNA → proteins/molecules → modern biological AI. The molecular tier of the course.

## Summary
L25 introduces DNA, the central dogma, GWAS, and gene regulation; L26 introduces protein biology, sequence alignment, MSAs, PSSMs, and small-molecule representations / docking / QSAR; L27 introduces modern biological AI — protein language models (ESM-2), AlphaFold-style structure prediction, DNA foundation models (Enformer / Evo), equivariant neural networks, and generative protein design (ProteinMPNN, RFdiffusion).

## Goals
- Read a Manhattan plot; reason about LD and population stratification.
- Build a SMILES → fingerprint → QSAR pipeline.
- Critique an ESM-2 / AlphaFold / Evo claim by asking what task and what evaluation.

## Key takeaways
- Genetic data are high-D, structured, and population-dependent.
- Classical baselines (MSA, PSSM, homology, QSAR, docking) are strong and not replaced by FMs.
- Generative biological design *requires external validation*.

## Materials
L25-L27 folders.

## External references — Part 5
- Visscher et al., "10 Years of GWAS Discovery," *AJHG* 101, 2017.
- Jumper et al., AlphaFold (*Nature* 2021).
- Lin et al., ESM-2 / ESMFold (*Science* 2023).
- Watson et al., RFdiffusion (*Nature* 2023).

---

### Lecture 25 — DNA, genetics, and gene regulation

- **Date.** Tue Apr 21, 2026.
- **Topic.** Genome basics → variants → GWAS → polygenic risk → gene expression / eQTLs.
- **Summary.** DNA, central dogma, variant types, sequencing/SNP arrays; population structure; LD; GWAS approach, effect sizes, multiple testing, QQ plots; PRS and transferability; gene expression, regulation, eQTLs; key databases.
- **Goals.** Read a Manhattan / QQ plot; explain why PRS underperforms cross-population; reason about expression vs. genotype.
- **Key takeaways.** Population stratification is central to genetic ML. PRS transferability is limited and equity-relevant.
- **Subsections.**
  - Central dogma and DNA basics.
  - Genetic variants.
  - Measurement (NovaSeq, SNP arrays).
  - Population structure.
  - Linkage disequilibrium.
  - GWAS approach and effect sizes.
  - Multiple testing across millions of hypotheses.
  - QQ plots and genomic inflation.
  - Stratification correction.
  - PRS and transferability.
  - Gene regulation, expression, eQTLs.
  - Databases (dbSNP, GTEx, ENCODE, UK Biobank).
- **Materials.** `lecture-25-dna-genetics/lec25_dna_genetics.pdf`, `latex/lec25_dna_genetics.tex` + `figures/`, `nb25_dna_genetics.ipynb`. *Source compiles to 62p / 937 text-lines, exact match.*
- **External references.** Visscher et al. (*AJHG* 2017); Martin et al. PRS transferability (*Nat Genet* 2019); Price et al. PCA-stratification (*Nat Genet* 2006); GTEx (*Science* 2020); ENCODE (*Nature* 2020).

---

### Lecture 26 — Proteins, molecules, and structural biology

- **Date.** Thu Apr 23, 2026.
- **Topic.** Protein biology; sequence alignment / MSA / PSSM; classical variant-effect prediction; small-molecule representation; QSAR; docking; drug discovery.
- **Summary.** Primary → quaternary protein structure; experimental structure determination and the protein-data gap; evolution and conservation; alignment, MSA, PSSMs, coevolution; SIFT / PolyPhen; homology modeling. Then small molecules: SMILES, fingerprints (ECFP), QSAR, AutoDock-style docking; the drug-discovery pipeline; scaffold splits.
- **Goals.** Read a SMILES string; build an ECFP-fingerprint pipeline; explain why scaffold splits matter; sketch a protein homology-modeling pipeline.
- **Key takeaways.** Classical baselines (MSA, PSSM, homology, QSAR) are strong and competitive with modern methods on many tasks.
- **Subsections.**
  - Protein biology and structure levels.
  - Experimental structure determination; protein data gap.
  - Evolution; sequence alignment; MSA.
  - PSSMs; coevolution.
  - Variant-effect prediction (SIFT, PolyPhen).
  - Homology modeling.
  - Small molecules.
  - SMILES; ECFP fingerprints.
  - QSAR.
  - Docking.
  - Drug-discovery pipeline.
  - Classical-baseline challenge.
- **Materials.** `lecture-26-proteins-molecules/lec26_proteins_molecules.pdf`, `latex/lec26_proteins_molecules.tex` + `figures/`, `nb26_proteins_molecules.ipynb`. *Source compiles to 56p / 842 text-lines, exact match.*
- **External references.** Berman et al. PDB (*NAR* 2000); Altschul et al. BLAST (*JMB* 1990); Adzhubei et al. PolyPhen-2 (*Nat Methods* 2010); Ng & Henikoff SIFT; Rogers & Hahn ECFP (*JCIM* 2010); Trott & Olson AutoDock Vina (*JCC* 2010); Wu et al. MoleculeNet (*Chem Sci* 2018).

---

### Lecture 27 — Modern biological AI

- **Date.** Tue Apr 28, 2026.
- **Topic.** Protein LMs, AlphaFold, DNA FMs, equivariant 3D models, generative protein design.
- **Summary.** ESM-2 masked LM; attention as a coevolution proxy; protein embeddings; zero-shot variant effect; AlphaFold 2 architecture; pLDDT; ESMFold; AlphaFold DB. Then DNA FMs (Enformer, Evo) and the ongoing controversy about whether they learn biology. Then 3D molecular models with equivariance (E(3)-equivariant NNs); ProteinMPNN inverse folding; RFdiffusion generative design; the validation gap.
- **Goals.** Critique a protein-LM claim per task; explain pLDDT and AlphaFold's failure modes; sketch an inverse-folding + experimental-validation pipeline.
- **Key takeaways.** Modern bio AI reuses FM ideas, but domain constraints — confidence calibration, dynamics, complex prediction, generative validation — dominate. Genomic FMs are promising but contested.
- **Subsections.**
  - Running question framing.
  - ESM-2 masked LM.
  - Attention and coevolution.
  - Protein embeddings.
  - Zero-shot variant effect.
  - What protein LMs miss.
  - AlphaFold 2 architecture.
  - pLDDT and confidence.
  - AlphaFold DB; ESMFold.
  - DNA foundation models.
  - Enformer / Evo and long-context genomic models.
  - The genomic-FM controversy.
  - 3D molecular geometry; equivariance.
  - ProteinMPNN inverse folding.
  - RFdiffusion generative design.
  - Validation requirements for designed biology.
- **Materials.** `lecture-27-modern-biological-ai/lec27_modern_bio_ai.pdf`, `latex/lec27_modern_bio_ai.tex` + `figures/`, `nb27_modern_bio_models.ipynb`. *Source compiles to 57p / 811 text-lines, exact match.*
- **External references.** Lin et al. ESM-2 / ESMFold (*Science* 2023); Jumper et al. AlphaFold (*Nature* 2021); Avsec et al. Enformer (*Nat Methods* 2021); Nguyen et al. Evo (*Science* 2024); Dauparas et al. ProteinMPNN (*Science* 2022); Watson et al. RFdiffusion (*Nature* 2023); Tang & Koo (*Genome Biol* 2025).

---

# Part 6 — Course recap (Lecture 28)

### Lecture 28 — Course recap

- **Date.** Thu Apr 30, 2026.
- **Topic.** Synthesis of everything covered during the semester.
- **Summary.** No new content; the originally-planned deployment lecture is *not* taught this cycle. The slot is used to walk back through the course arc — foundations → modern AI → clinical AI → population/causality/fairness → biological AI — and to surface the cross-cutting through-lines (see [`concept_map.md`](concept_map.md)) so students can see the course as a whole.
- **Goals.** Re-state the course-level learning objectives, identify which lectures contributed to each one, and give students a synthesis frame for the final exam.
- **Key takeaways.** Same as Level 0 — the six course-wide takeaways (see top of this file).
- **Subsections.**
  - Re-walk through Parts 1-5.
  - Cross-cutting through-lines (TL1-TL6).
  - Open questions / what was *not* covered (deployment, post-deployment monitoring, regulation — flagged for self-study).
  - Q&A.
- **Materials.** No new lecture deliverable for this slot. Students should re-read this syllabus and [`concept_map.md`](concept_map.md).
- **External references.** For the dropped deployment material, students wanting to self-study should read Finlayson et al. (*NEJM* 2021) and the FDA *AI/ML SaMD Action Plan* (2021); see [`concept_map.md`](concept_map.md) for the broader external-reference cluster.

> **Note on what was dropped.** A standalone deployment lecture (drift, feedback loops, alert fatigue, regulation, FDA SaMD) was originally planned for this slot but is not taught this cycle. Deployment-adjacent ideas still appear in L8 (calibration), L10 (domain shift), L17-L18 (label/action windows), and L24 (mechanism-level fairness mitigation).

---

> **Mind-map and through-lines.** The cross-cutting through-lines (TL1-TL6) and the suggested hierarchical mind-map structure live in [`concept_map.md`](concept_map.md) at the project root, alongside the external-reference clusters that the mind map links to.
