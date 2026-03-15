# Newton's Divided Difference Interpolation

Newton's interpolation is a method of finding the unique polynomial of degree $n-1$ that passes through $n$ data points. It uses "divided differences" to build the polynomial incrementally.

## The Newton Form

The interpolating polynomial is written as:
$$P_n(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + \dots + a_n(x-x_0)\dots(x-x_{n-1})$$

The coefficients $a_i$ are the divided differences.

## Divided Differences Table

The divided differences are defined recursively:
- Zeroth divided difference: $f[x_i] = y_i$
- First divided difference: $f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i}$
- Higher orders: $f[x_0, \dots, x_k] = \frac{f[x_1, \dots, x_k] - f[x_0, \dots, x_{k-1}]}{x_k - x_0}$

## Advantages

- **Incremental:** If you add a new data point, you only need to calculate one more coefficient ($a_{n+1}$). In contrast, Lagrange interpolation requires recalculating everything.
- **Efficiency:** The nested form (Horner's method) allows for fast evaluation of the polynomial.

## Example Usage

Implementation and the divided difference table logic are in `02_newton_interpolation.py`.
