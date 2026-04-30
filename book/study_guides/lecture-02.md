# L2 Study Guide — Linear Algebra

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

## Key Terms

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

## Why Linear Algebra Matters in ML

- Data is represented as vectors / matrices (feature matrices, weight matrices in neural nets).
- Model training involves matrix multiplications and decompositions.
- PCA, SVD, and eigendecomposition underlie dimensionality reduction and many algorithms.
- Understanding the geometry of vector spaces builds intuition for what models are actually doing.

```{admonition} Conceptual takeaway
:class: tip
A matrix is **not** a table of numbers; it is the coordinate form of a linear operator under a chosen basis. Different bases → different matrices for the *same* operator. "Choosing a representation" = "choosing a basis."
```

## Self-Check Questions

1. Prove that matrix multiplication is associative but not generally commutative.
2. What does it mean geometrically for a matrix to be singular (non-invertible)?
3. If A has eigenvalue 0, what does that imply about the transformation A represents?
4. Write out what ∂/∂**x** of **x**ᵀA**x** equals (matrix-vector derivative identity).
5. What is the difference between a basis and an orthonormal basis? Why does orthonormality simplify computations?

## Additional Resources

- [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — best visual introduction to the geometry of linear algebra.
- [Gilbert Strang — Linear Algebra (MIT OCW 18.06)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — full course with lectures, problem sets, and exams.
- [The Matrix Cookbook (PDF)](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf) — reference for matrix derivatives and identities.
- [Immersive Linear Algebra (interactive online textbook)](http://immersivemath.com/ila/index.html) — visual treatment of key concepts.
- Goodfellow, Bengio, Courville, *Deep Learning*, Ch. 2 — the exact subset of LA needed for the rest of the course.

> See also: [L2 lecture page](../lectures/lecture-02.md).
