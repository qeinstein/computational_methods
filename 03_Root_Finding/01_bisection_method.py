# """Bisection method implementation and examples.
#
# Provides a robust iterative `my_bisection` function with input validation,
# stopping criteria, and a maximum iteration guard.
# """

import numpy as np


def my_bisection(f, a, b, tol=1e-8, max_iter=1000, return_iters=False):
    """Find a root of f in [a,b] using the bisection method.

    Parameters
    ----------
    f : callable
        Function of a single variable.
    a, b : float
        Interval endpoints. Requires f(a) and f(b) to have opposite signs.
    tol : float
        Tolerance for stopping. Stops when |f(m)| <= tol or interval half-width
        (b-a)/2 <= tol.
    max_iter : int
        Maximum number of iterations.
    return_iters : bool
        If True, return a tuple (root, iterations).

    Returns
    -------
    root : float
        Approximate root.
    (root, iterations) : tuple
        If return_iters is True.

    Raises
    ------
    ValueError if f(a) and f(b) do not have opposite signs, or RuntimeError
    if the method fails to converge within max_iter.
    """

    fa = f(a)
    fb = f(b)
    if fa == 0:
        return (a, 0) if return_iters else a
    if fb == 0:
        return (b, 0) if return_iters else b
    if np.sign(fa) == np.sign(fb):
        raise ValueError("f(a) and f(b) must have opposite signs (a bracket is required)")

    for k in range(1, max_iter + 1):
        m = (a + b) / 2.0
        fm = f(m)

        # stopping criteria: small residual or small interval
        if abs(fm) <= tol or (b - a) / 2.0 <= tol:
            return (m, k) if return_iters else m

        # decide which subinterval contains the root
        if np.sign(fa) == np.sign(fm):
            a = m
            fa = fm
        else:
            b = m
            fb = fm

    raise RuntimeError(f"Bisection did not converge after {max_iter} iterations")


if __name__ == "__main__":
    # Example: root of x^2 - 2 is sqrt(2) ~ 1.41421356
    f = lambda x: x ** 2 - 2

    root, iters = my_bisection(f, 0.0, 2.0, tol=1e-6, max_iter=100, return_iters=True)
    print(f"Approximate root (tol=1e-6): {root} after {iters} iterations")
    print("Residual f(root):", f(root))

    # demonstrate different tolerance
    r2 = my_bisection(f, 0.0, 2.0, tol=1e-2)
    print(f"Approximate root (tol=1e-2): {r2}")
    print("Residual f(r2):", f(r2))