# Linear Spline Interpolation

Linear spline interpolation is the simplest form of interpolation. It involves connecting adjacent data points with straight-line segments.

## The Concept

Given a set of $n$ data points $(x_i, y_i)$, for any value $x$ in the interval $[x_i, x_{i+1}]$, the interpolated value $y$ is found using the equation of the line passing through $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$.

## The Formula

For $x \in [x_i, x_{i+1}]$:
$$f(x) = y_i + \frac{y_{i+1} - y_i}{x_{i+1} - x_i}(x - x_i)$$

This can be rewritten as:
$$f(x) = y_i (1 - t) + y_{i+1} t$$
where $t = \frac{x - x_i}{x_{i+1} - x_i}$ is the fractional distance between the points.

## Characteristics

- **Continuity:** The resulting function is continuous ($C^0$).
- **Smoothness:** The function is **not** smooth at the data points; the first derivative is discontinuous (the "slope" changes abruptly).
- **Simplicity:** Very easy to compute and guaranteed to never overshoot the data points.

## Example Usage

Implementation details can be found in `01_linear_spline.py`.
