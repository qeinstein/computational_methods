# 04 - Numerical Differentiation

This module covers techniques for numerically approximating derivatives of functions. These methods are essential when analytical derivatives are unavailable or difficult to compute.

## Topics Covered

### 1. Forward Difference Method
- Finite difference approximation concept
- Derivation from Taylor series
- Local and global error analysis
- Accuracy and step size selection
- Practical applications and limitations

### 2. Backward Difference Method
- Mirror of forward difference
- Taylor series approach
- Error bounds
- When to use backward differences
- Asymmetric boundary conditions

### 3. Central Difference Method
- Higher-order accuracy
- Symmetry advantages
- Error analysis and convergence
- Optimal step size selection
- Comparison with forward/backward differences

## Files in This Module

- **01_forward_difference.md**: Forward difference theory and derivation
- **01_forward_difference.py**: Implementation and examples
- **02_backward_difference.md**: Backward difference theory
- **02_backward_difference.py**: Implementation with comparisons
- **03_center_difference.md**: Central difference method (most accurate)
- **03_center_difference.py**: Implementation and accuracy demonstrations

## How to Use

1. Start with **01_forward_difference.md** to understand finite differences
2. Review **02_backward_difference.md** for symmetry perspective
3. Learn **03_center_difference.md** for improved accuracy
4. Run implementations and visualize errors
5. Experiment with different step sizes and functions

## Key Learning Outcomes

By the end of this module, you should be able to:
- Approximate first derivatives numerically
- Understand trade-offs between accuracy and computational cost
- Select appropriate step sizes
- Analyze truncation and rounding errors
- Apply differentiation methods to practical problems
- Recognize when numerical differentiation is necessary

## Prerequisites

- Python fundamentals (Module 01)
- Error analysis (Module 02)
- Calculus and Taylor series (Module 03 concepts)

## Related Topics

- **Root Finding (Module 03)**: Uses derivatives in Newton-Raphson method
- **Numerical Integration (Module 05)**: Complementary operation

## Next Steps

Proceed to **05 - Numerical Integration**, the companion topic that numerically approximates integrals.
