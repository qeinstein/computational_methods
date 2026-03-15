# Quadratic Splines

Quadratic spline interpolation uses a second-degree polynomial (a parabola) for each interval between data points.

## The Concept

For each interval $[x_i, x_{i+1}]$, we define a polynomial:
$$f_i(x) = a_i x^2 + b_i x + c_i$$

To find the coefficients ($a_i, b_i, c_i$), we apply the following conditions:
1.  **Continuity:** The splines must pass through all data points.
2.  **Smoothness:** The first derivatives (slopes) must be equal at the internal nodes.
3.  **Boundary Condition:** Since we have more unknowns than equations, we usually assume the second derivative at the first point is zero ($a_1 = 0$), effectively making the first segment linear.

## Advantages over Linear Splines

- The resulting curve is smoother because there are no sharp "corners" at the data points.
- It provides a better approximation for functions that have a constant or slowly changing second derivative.

## Example Usage

See `02_quadratic_spline.py` for the implementation.
