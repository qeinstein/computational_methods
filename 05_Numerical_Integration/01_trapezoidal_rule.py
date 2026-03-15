import numpy as np
from typing import Callable

def trapezoidal_rule(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Approximates the definite integral of f from a to b using the composite trapezoidal rule.

    Args:
        f: The function to integrate.
        a: The lower limit of integration.
        b: The upper limit of integration.
        n: The number of sub-intervals (strips).

    Returns:
        The approximated integral value.
    """
    if n <= 0:
        raise ValueError("Number of sub-intervals n must be a positive integer.")
    
    # Calculate step size
    h = (b - a) / n
    
    # Generate points
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # Apply the composite trapezoidal formula: (h/2) * [f(x0) + 2*sum(f(xi)) + f(xn)]
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    
    return integral

if __name__ == "__main__":
    # Example 1: Integrate f(x) = x^2 from 0 to 1
    # Analytical solution: [x^3 / 3] from 0 to 1 = 1/3 ≈ 0.333333
    f1 = lambda x: x**2
    a, b = 0, 1
    exact_solution = 1/3
    
    print(f"Integrating f(x) = x^2 from {a} to {b}")
    print(f"{'n':>5} | {'Approximation':>15} | {'Error':>15}")
    print("-" * 40)
    
    for n in [1, 10, 100, 1000]:
        approx = trapezoidal_rule(f1, a, b, n)
        error = abs(approx - exact_solution)
        print(f"{n:5d} | {approx:15.10f} | {error:15.10e}")

    # Example 2: Integrate f(x) = sin(x) from 0 to pi
    # Analytical solution: [-cos(x)] from 0 to pi = -(-1) - (-1) = 2
    f2 = np.sin
    a2, b2 = 0, np.pi
    exact_solution2 = 2.0
    
    print(f"\nIntegrating f(x) = sin(x) from {a2} to {b2:.4f}")
    approx_sin = trapezoidal_rule(f2, a2, b2, 100)
    print(f"Approximation (n=100): {approx_sin:.10f}")
    print(f"True Error: {abs(approx_sin - exact_solution2):.10e}")
