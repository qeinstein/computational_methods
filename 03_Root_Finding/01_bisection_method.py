# Program a function my_bisection(f,a,b,tol) that approximates a root r of f, bounded
# by a and b, to within a tolerance tol. The function should return the approximation r.

import numpy as np

def my_bisection(f, a, b, tol):
    # approximates a root, R, of f bounded
    # by a and b, to within a tolerance tol
    # | f(m) | < tol with m being the midpoint of a and b
    # btw a an b, Recursive function

    # first check if a and b bound a root
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("f(a) and f(b) must have opposite signs")

    # getting our midpoint
    mid = (a + b) / 2

    # check if the midpoint is a root or if we are within the tolerance
    if np.abs(f(mid)) < tol:
        return mid
    elif np.sign(f(a)) == np.sign(f(mid)):
        # if f(a) and f(mid) have the same sign, the root is in the right half
        return my_bisection(f, mid, b, tol)
    else:
        # if f(b) and f(mid) have the same sign, the root is in the left half
        return my_bisection(f, a, mid, tol)


# Example usage
f = lambda x: x**2 - 2  # f(x) = x^2 - 2, root is sqrt(2)

r1 = my_bisection(f, 0, 2, 0.1) # using a and b of same sign will raise an exception, since it does not bound a root
print(f"Approximate root with tol=0.1: {r1}")

r01 = my_bisection(f, 0, 2, 0.01)
print(f"Approximate root with tol=0.01: {r01}")

print("f(r1) =", f(r1))
print("f(r01) =", f(r01)) # should be close to 0, within the specified tolerances