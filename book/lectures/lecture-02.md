# Lecture 2 — Linear algebra: the language of representations

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

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

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Key Terms

| Term | Definition |
|---|---|
| **Vector** | An ordered list of numbers representing a point or direction in space; formally, an element of a vector space. |
| **Vector Space** | A set V closed under addition and scalar multiplication, satisfying eight axioms (commutativity, associativity, identity, inverse, distributivity). |
| **Linear Operator** | A function T : V → W that preserves addition and scalar multiplication: T(u+v) = T(u)+T(v) and T(αv) = αT(v). |
| **Matrix** | A rectangular array of numbers representing a linear operator when acting by multiplication on column vectors. |
| **Basis** | A linearly independent spanning set for a vector space. Every vector has a unique representation as a linear combination of basis vectors. |
| **Coordinatization** | The process of representing abstract vectors as tuples of numbers relative to a chosen basis. |
| **Eigenvalue / Eigenvector** | For matrix A, λ and v satisfy Av = λv. The eigenvector's direction is unchanged by A; λ is the scaling factor. |
| **Singular Values (SVD)** | A = UΣVᵀ. Singular values σᵢ are the square roots of eigenvalues of AᵀA, measuring how much A stretches space in each direction. |
| **Matrix Transpose** | Aᵀ has rows and columns swapped. Key identity: (AB)ᵀ = BᵀAᵀ. |
| **Trace** | Sum of diagonal elements of a square matrix. Tr(A) = Σ Aᵢᵢ = sum of eigenvalues. |

### Why Linear Algebra Matters in ML

- Data is represented as vectors / matrices (feature matrices, weight matrices in neural nets).
- Model training involves matrix multiplications and decompositions.
- PCA, SVD, and eigendecomposition underlie dimensionality reduction and many algorithms.
- Understanding the geometry of vector spaces builds intuition for what models are actually doing.

```{admonition} Conceptual takeaway
:class: tip
A matrix is **not** a table of numbers; it is the coordinate form of a linear operator under a chosen basis. Different bases → different matrices for the *same* operator. "Choosing a representation" = "choosing a basis."
```

### Self-Check Questions

1. Prove that matrix multiplication is associative but not generally commutative.
2. What does it mean geometrically for a matrix to be singular (non-invertible)?
3. If A has eigenvalue 0, what does that imply about the transformation A represents?
4. Write out what ∂/∂**x** of **x**ᵀA**x** equals (matrix-vector derivative identity).
5. What is the difference between a basis and an orthonormal basis? Why does orthonormality simplify computations?

### Additional Resources

- [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — best visual introduction to the geometry of linear algebra.
- [Gilbert Strang — Linear Algebra (MIT OCW 18.06)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — full course with lectures, problem sets, and exams.
- [The Matrix Cookbook (PDF)](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf) — reference for matrix derivatives and identities.
- [Immersive Linear Algebra (interactive online textbook)](http://immersivemath.com/ila/index.html) — visual treatment of key concepts.
- Goodfellow, Bengio, Courville, *Deep Learning*, Ch. 2 — the exact subset of LA needed for the rest of the course.
