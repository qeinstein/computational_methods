import numpy as np
from typing import Callable

def simpson_13_rule(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Approximates the definite integral of f from a to b using the composite Simpson's 1/3 rule.

    Args:
        f: The function to integrate.
        a: The lower limit of integration.
        b: The upper limit of integration.
        n: The number of sub-intervals (must be even).

    Returns:
        The approximated integral value.
    """
    if n % 2 != 0:
        raise ValueError("Number of sub-intervals n must be even for Simpson's 1/3 rule.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # Formula: (h/3) * [f(x0) + 4*sum(f(x_odd)) + 2*sum(f(x_even_internal)) + f(xn)]
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    
    return integral

def simpson_38_rule(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Approximates the definite integral of f from a to b using the composite Simpson's 3/8 rule.

    Args:
        f: The function to integrate.
        a: The lower limit of integration.
        b: The upper limit of integration.
        n: The number of sub-intervals (must be a multiple of 3).

    Returns:
        The approximated integral value.
    """
    if n % 3 != 0:
        raise ValueError("Number of sub-intervals n must be a multiple of 3 for Simpson's 3/8 rule.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # Formula: (3h/8) * [f(x0) + 3*f(x1) + 3*f(x2) + 2*f(x3) + ... + f(xn)]
    # Sum the endpoints
    total = y[0] + y[-1]
    
    # Sum the internal points
    for i in range(1, n):
        if i % 3 == 0:
            total += 2 * y[i]
        else:
            total += 3 * y[i]
            
    return (3 * h / 8) * total

if __name__ == "__main__":
    # Example: Integrate f(x) = exp(x) from 0 to 1
    # Analytical solution: e^1 - e^0 = e - 1 ≈ 1.718281828
    f = np.exp
    a, b = 0, 1
    exact = np.exp(1) - 1
    
    print(f"Integrating f(x) = exp(x) from {a} to {b}")
    print(f"{'n':>5} | {'1/3 Rule':>15} | {'3/8 Rule':>15} | {'Exact':>15}")
    print("-" * 60)
    
    # We choose n that are multiples of both 2 and 3 for direct comparison
    for n in [6, 12, 60]:
        s13 = simpson_13_rule(f, a, b, n)
        s38 = simpson_38_rule(f, a, b, n)
        print(f"{n:5d} | {s13:15.10f} | {s38:15.10f} | {exact:15.10f}")

    # Comparison of Errors
    print("\nComparison of Errors (Absolute):")
    n = 60
    err13 = abs(simpson_13_rule(f, a, b, n) - exact)
    err38 = abs(simpson_38_rule(f, a, b, n) - exact)
    
    print(f"Simpson's 1/3 (n={n}) Error: {err13:.15e}")
    print(f"Simpson's 3/8 (n={n}) Error: {err38:.15e}")
