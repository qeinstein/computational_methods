# Gaussian Elimination

Gaussian elimination is an algorithm used to solve systems of linear equations of the form $Ax = b$. It is also used to find the rank of a matrix, the determinant, and the inverse of an invertible square matrix.

## The Process

The method consists of two main stages:

### 1. Forward Elimination
The goal is to transform the augmented matrix $[A | b]$ into an **upper triangular form** (Row Echelon Form).
- We use elementary row operations to create zeros below the diagonal elements (pivots).
- **Partial Pivoting:** To improve numerical stability and avoid division by zero, we often swap rows to ensure the pivot element is the largest possible value in its column.

### 2. Back Substitution
Once the matrix is in upper triangular form, we solve for the variables starting from the last row (which contains only one unknown) and working upwards.

## Complexity

The computational complexity of Gaussian elimination is **$O(n^3)$**. This means if you double the size of the matrix, the number of operations increases by roughly 8 times.

## Example Usage

Implementation details, including the augmentation and back-substitution logic, are in `02_gaussian_elimination.py`.
