# Error Types and Analysis

In numerical computation, errors arise from many sources. Understanding them helps design stable algorithms.

- **Absolute error**: \( |x_{true} - x_{approx}| \)
- **Relative error**: \( \frac{|x_{true} - x_{approx}|}{|x_{true}|} \) when \(x_{true}\neq0\).
- **Round-off error**: due to representing numbers with finite precision (floating-point rounding).
- **Truncation error**: from approximating an infinite process by a finite one (e.g., Taylor series, numerical derivatives).
- **Propagation of error**: errors can amplify when performing arithmetic; e.g.
  - adding numbers of vastly different magnitude can lose significance (`loss of precision`).
  - subtraction of nearly equal numbers causes catastrophic cancellation.
- **Condition number**: measures sensitivity of a function to perturbations in input. A high condition number means the problem is ill-conditioned.
- **Stability**: an algorithm is stable if it does not grow errors excessively as it executes.

### Estimation Techniques

- Use forward/backward error analysis
- Use finite differences to estimate derivative errors

### Exercises

1. Compute absolute and relative errors for approximations of \(\pi\).
2. Write function to propagate error through simple formula like \(f(x,y)=x+y\).

