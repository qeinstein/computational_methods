# Gaussian Elimination and LU Decomposition

These are fundamental methods for solving systems of linear equations $Ax = b$.

## Gaussian Elimination

Gaussian Elimination transforms a matrix $A$ into an upper triangular matrix ($U$) using row operations.
1. **Forward Elimination:** Eliminate variables to create zeros below the diagonal.
2. **Back Substitution:** Solve for the variables starting from the bottom.

![Gaussian Elimination Flowchart](https://kroki.io/graphviz/svg/eNptj0EKwjAQRa8yZK0nKBG6chM3QlbFxdSMNliTMIlYKb27SYXgotv3_mf-GHtnDAMcYQZG9zCWpTo34Lwh6OKAgWTvpx3E9BlJsn85Q-bSQAvdiD2NUpwwsZ2gFZmqSpV_E4MqUFeoQ8hQi7W_P_zFb3hNnqvQG0IVkc_-lhiMwzpEb-O5fCMjPik3c2qB5Qu-bkvv)

## LU Decomposition

LU Decomposition factors a square matrix $A$ into the product of two matrices:
- **$L$ (Lower Triangular):** Has 1s on the diagonal and the multipliers used during elimination below.
- **$U$ (Upper Triangular):** The result of Gaussian elimination.

![LU Decomposition Concept](https://kroki.io/graphviz/svg/eNptj0EKwjAQRa8yZK0nKBG6chM3QlbFxdSMNliTMIlYKb27SYXgotv3_mf-GHtnDAMcYQZG9zCWpTo34Lwh6OKAgWTvpx3E9BlJsn85Q-bSQAvdiD2NUpwwsZ2gFZmqSpV_E4MqUFeoQ8hQi7W_P_zFb3hNnqvQG0IVkc_-lhiMwzpEb-O5fCMjPik3c2qB5Qu-bkvv)

### Why use LU?
If you need to solve $Ax = b$ for many different $b$ vectors, you only decompose $A$ once. Then you solve two simpler triangular systems:
1. $Ly = b$ (Forward substitution)
2. $Ux = y$ (Backward substitution)

## Implementations

- `01_lu_decomposition.py`: Step-by-step factorization.
- `02_gaussian_elimination.py`: Solving systems directly.
