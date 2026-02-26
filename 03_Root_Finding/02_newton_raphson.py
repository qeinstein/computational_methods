import numpy as np

# Single iteration of Newton's method
f = lambda x: x**2 - 2  # f(x) = x^2 - 2, root is sqrt(2)
df = lambda x: 2 * x # derivative of f

newton_raphson = 1.4 - (f(1.4) / df(1.4)) # x1 = x0 - f(x0) / df(x0), with x0 = 1.4
print("newton_raphson =", newton_raphson)
print("sqrt(2) =", np.sqrt(2))


"""
Newton's method uses the tangent line at the current guess to jump closer to the root.
Each iteration typically doubles the number of correct digits (quadratic convergence).
"""


def my_newton_raphson(f, df, x0, tol):
    # output is an estimation of the root of f
    # using the newton raphson method, starting from x0 and iterating until |f(x)| <= tol
    # recursive implementation  

    if abs(f(x0)) <= tol: # check if we are within the tolerance
        return x0
    else:
        x1 = x0 - f(x0) / df(x0)  # Newton's update
        return my_newton_raphson(f, df, x1, tol)


# Example: root of x^2 - 2 is sqrt(2) ~ 1.41421356
root = my_newton_raphson(f, df, x0=1.4, tol=1e-10)
print(f"Approximate root (tol=1e-10): {root}")
print("Residual f(root):", f(root))

# Note: Newton's method can fail to converge if the derivative is zero or near zero, 
# or if the initial guess is not chosen wisely. Always check the behavior of f and df before applying Newton's method.

# How to check the behavior of f and df? Plotting them can help visualize where the roots and critical points are.