# Lecture 2 — Linear algebra: the language of representations

> ⚠️ **AI-synthesized content; not fully reviewed by course staff.** Treat as a study aid, not a primary source — the released slides, notebooks, and lecture recordings are authoritative. [Full caveat →](../intro.md)

**Thu Jan 22, 2026 · Part 1 — Foundations · §1.1 Mathematical preliminaries**

## What this lecture is about

Almost every model you'll meet in the rest of the course — from logistic regression to a transformer to a protein language model — boils down to operations on vectors and matrices. The point of this lecture is not to teach linear algebra from scratch (you've seen most of it); the point is to make a small but slippery distinction that ML papers never bother to spell out: **the difference between a vector and its coordinate representation, and the difference between a linear operator and the matrix that represents it.**

We walk through vectors and vector spaces, linearity and linear combinations, linear operators and matrices, bases and coordinatization, and matrix multiplication as composition of linear maps. Eigenvalues, SVD, matrix calculus, and matrix exponentials are flagged as topics you should review on your own — the course will use them as tools, not derive them.

## Why it matters

The reason this distinction is the load-bearing idea of the lecture: every time you "represent" something for ML — words as embeddings, EHR codes as one-hot vectors, an image as a tensor, a protein as a sequence of numerical features — you are picking a basis. Different basis choices give different matrices for the *same* underlying transformation. When a model "fails to generalize across hospitals," very often what's actually happening is that the basis is hospital-specific, and the abstract transformation we'd hoped to learn is not.

So this lecture sets up a vocabulary you'll reuse:

- "the model is a linear map from some input space to some output space"
- "the basis we chose is encoding more than we realized"
- "the architecture is performing a sequence of linear maps interleaved with nonlinearities"

You will see this language in L11 (NN architectures as inductive bias), L18 (tabularized vs. event-stream EHR representations), L20 (tokenization and embeddings), L21-L22 (image tensors), L25 (PCA on genotypes), L26 (SMILES and fingerprints).

## Things you should walk away believing

- A matrix is not a table of numbers; it's the coordinate form of a linear operator under a chosen basis. Different bases → different matrices for the same operator.
- "Choosing a representation" = "choosing a basis." This is a modeling decision, not preprocessing trivia.
- Matrix multiplication composes operators. If you can read a deep network as a stack of linear maps separated by nonlinearities, you've got the structural intuition the rest of the course needs.
- Eigenanalysis, SVD, and matrix calculus are the tools you'll most often need to review independently — they're standard but show up everywhere downstream.

## How this connects to the rest of the course

- L3-L4 build probability on top of these vector spaces (random variables → expectations are inner products in function space).
- L5-L6 do calculus on functions over these spaces (gradients are linear maps).
- L11+L13 (neural networks) read as sequences of linear maps + nonlinearities.
- L25 (population structure / PCA) is a literal eigenanalysis of a centered covariance matrix.
- L27 (equivariant 3D molecular models) is what happens when "the basis matters" becomes a hard architectural constraint.

## Source files in this folder

- `Lecture 2.pdf` — the slides as released to students.
- `Lecture 2 - linear_algebra.pptx` — editable PowerPoint source.

## To go deeper

- **3Blue1Brown, _Essence of Linear Algebra_ video series.** The single best companion if the basis-vs.-coordinates distinction is fuzzy. Episodes 1-9 cover everything in this lecture.
- **Strang, _Introduction to Linear Algebra_ (any recent edition), Chs. 1-3 and 7.** The standard textbook, with an emphasis on how the four fundamental subspaces relate.
- **Goodfellow, Bengio, Courville, _Deep Learning_, Ch. 2.** The exact subset of linear algebra you need for the rest of the course.
- **Murphy, _Probabilistic Machine Learning: An Introduction_ (vol 1, 2022), Ch. 7.** Linear algebra as ML uses it — eigenanalysis, SVD, matrix calculus.

## Study tools

- [Study guide for L02](../study_guides/lecture-02.md) — key terms, self-check questions, curated external resources.
- [Concept map](../concept_map.md) — see how this lecture connects to the rest of the course.
