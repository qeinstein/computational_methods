# Quadratic and Cubic Splines

Higher-order splines use piecewise polynomials of degree 2 (quadratic) or 3 (cubic) to connect data points. This ensures not just continuity, but also smoothness.

## Quadratic Splines

A quadratic spline uses a parabola $f_i(x) = a_i x^2 + b_i x + c_i$ for each interval.
- **Continuity ($C^0$):** The splines meet at the data points.
- **Smoothness ($C^1$):** The first derivative (slope) is continuous at the points.

## Cubic Splines

A cubic spline uses a cubic polynomial $f_i(x) = a_i x^3 + b_i x^2 + c_i x + d_i$.
- **Continuity ($C^0$):** The splines meet at the data points.
- **Smoothness ($C^2$):** Both the first derivative and the second derivative (curvature) are continuous.

Cubic splines are the most common choice for interpolation because they provide a very "natural" and smooth-looking curve that minimizes "wiggles" (the minimum curvature property).

## Natural Cubic Spline

A cubic spline is "natural" if the second derivatives at the very first and very last endpoints are zero:
$$f''(x_0) = 0, \quad f''(x_n) = 0$$

## Implementation

Detailed implementations are provided in:
- `02_quadratic_spline.py`
- `03_cubic_spline.py`
