# Jacobi Method

The Jacobi method is an **iterative** algorithm for solving a diagonally dominant system of linear equations $Ax = b$.

## The Concept

Instead of direct elimination, the Jacobi method starts with an initial guess and refines it until it converges to the solution.

## The Iteration Formula

For each equation $i$:
$$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right)$$

![Jacobi Method Flowchart](https://kroki.io/graphviz/svg/eNpljskKwjAQhl9l6KmVig-gUUTFmxf1ICVIygwajUlJUq2I725arQueZuFfPpQ7K4o9zOEGVugjSstW0z5ogwSZ24uCWG6qFJy_KmLWlBoJeR-WXljfKkgpWTgK73WBwgenEjkpFlVbTZdMcmAQ5_XsgitP8TiT6YF3quzAkwR6UN-SR8E_MfpMdkf4jhC5i5uY4K0SGIA3ahQFoKYZpTgZXQPNNP7jPCm7w5YrbO-G77Lwb_yvzg25X5hPQitZmFpxfwBGZmsU)

## Convergence Condition

The Jacobi method is guaranteed to converge if the matrix $A$ is **strictly diagonally dominant**. This means for every row, the absolute value of the diagonal element is greater than the sum of the absolute values of the other elements in that row:
$$|a_{ii}| > \sum_{j \neq i} |a_{ij}|$$

## Advantages

- **Large Sparse Matrices:** Extremely efficient for matrices where most elements are zero.
- **Parallelization:** Unlike Gaussian elimination, all components of $x^{(k+1)}$ can be computed simultaneously.

## Example Usage

See `03_jacobi_method.py` for the iterative implementation.
