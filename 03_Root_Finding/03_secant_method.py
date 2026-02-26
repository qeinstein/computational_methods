"""
03_secant_method.py

Documented, robust implementation of the secant method with demonstration examples.

The secant method approximates the derivative using two previous iterates:
    x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))

This file provides:
- `secant_solve` : an iterative solver returning (root, converged, iterations, residual)
- `secant_step`  : perform a single secant update

"""

from typing import Callable, Tuple
import math


def secant_step(f: Callable[[float], float], x_prev: float, x_curr: float) -> float:  # Leetcode style parameter annotations
    """Perform one secant update using points x_prev and x_curr and return x_next.

    Raises ZeroDivisionError if denominator is zero (or extremely close).
    """
    f_prev = f(x_prev)
    f_curr = f(x_curr)
    denom = f_curr - f_prev
    if abs(denom) < 1e-16:
        raise ZeroDivisionError("Denominator for secant update too small; f(x_curr) ~= f(x_prev)")
    return x_curr - f_curr * (x_curr - x_prev) / denom


def secant_solve(f: Callable[[float], float], x0: float, x1: float,
                 tol: float = 1e-10, ftol: float = 1e-12, max_iter: int = 100,
                 rtol: float = None) -> Tuple[float, bool, int, float]:
    """Iterative secant solver.

    Returns (root, converged, iterations, residual)

    - `tol` checks absolute change in x
    - `ftol` checks function residual
    - `rtol` if provided checks relative change
    """
    x_prev = x0
    x_curr = x1
    for k in range(1, max_iter + 1):
        try:
            x_next = secant_step(f, x_prev, x_curr)
        except ZeroDivisionError:
            return x_curr, False, k - 1, f(x_curr)

        # stopping criteria
        if rtol is not None:
            change = abs(x_next - x_curr) / (abs(x_next) + 1e-30)
            if change < rtol or abs(f(x_next)) < ftol:
                return x_next, True, k, f(x_next)
        else:
            if abs(x_next - x_curr) < tol or abs(f(x_next)) < ftol:
                return x_next, True, k, f(x_next)

        # shift and continue
        x_prev, x_curr = x_curr, x_next

    return x_curr, False, max_iter, f(x_curr)


if __name__ == "__main__":
    # Demonstration

    # Example 1: f(x)=x^2-2 -> root sqrt(2)
    f = lambda x: x ** 2 - 2
    x0, x1 = 1.0, 2.0  # two initial guesses
    root, conv, iters, resid = secant_solve(f, x0, x1)
    print("Secant on x^2-2 from (1.0,2.0):")
    print("  root =", root)
    print("  converged =", conv, "iters =", iters)
    print("  residual f(root) =", resid)
    print()

    # Example 2: potential failure case (small denominator)
    g = lambda x: x ** 3 - 2 * x + 2
    # choose starting points where g(x1) ~ g(x0) to show safeguard
    a, b = -2.0, -1.999999999999
    try:
        r2, c2, it2, res2 = secant_solve(g, a, b, max_iter=20)
        print("Secant on problematic g starting near (a,b):")
        print("  root =", r2, "converged =", c2, "iters=", it2, "resid=", res2)
    except Exception as e:
        print("Secant failed on test case:", e)

    # single step demonstration
    h = lambda x: x ** 3 + 3 * x ** 2 - 2 * x - 5
    x0_h, x1_h = 0.0, 0.29
    try:
        x2 = secant_step(h, x0_h, x1_h)
        print() 
        print("Single secant step for h from (0.0,0.29) ->", x2)
        print("h(x0_h) =", h(x0_h), "h(x1_h) =", h(x1_h))
    except Exception as e:
        print("Single secant step error:", e)
