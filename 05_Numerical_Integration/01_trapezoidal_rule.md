# Trapezoidal Rule

The trapezoidal rule is a numerical integration method used to approximate the definite integral of a function $f(x)$ over an interval $[a, b]$. It is based on approximating the region under the graph of the function as a trapezoid and calculating its area.

## The Single Trapezoidal Rule

For a single interval $[a, b]$, the area under the curve is approximated by a straight line connecting $(a, f(a))$ and $(b, f(b))$. The area of the resulting trapezoid is:

$$I = \int_a^b f(x) \, dx \approx (b - a) \frac{f(a) + f(b)}{2}$$

## The Composite Trapezoidal Rule

To improve accuracy, the interval $[a, b]$ is divided into $n$ sub-intervals of equal width $h = \frac{b - a}{n}$. The total integral is the sum of the areas of the trapezoids in each sub-interval:

$$I \approx \frac{h}{2} \left[ f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$

where $x_i = a + i \cdot h$ for $i = 0, 1, \dots, n$.

## Error Analysis

The truncation error for the composite trapezoidal rule is given by:

$$E_t = -\frac{(b - a)h^2}{12} f''(\xi)$$

where $\xi$ is some value in the interval $(a, b)$. This indicates that the trapezoidal rule is:
1.  **Exact** for linear functions (where $f''(x) = 0$).
2.  **Second-order accurate** with respect to the step size $h$ (error decreases by a factor of 4 when $h$ is halved).

## Practical Considerations

- **Simplicity:** It is one of the easiest numerical integration methods to implement.
- **Robustness:** It works well for functions that are relatively smooth.
- **Limitations:** For functions with high curvature, Simpson's rules or higher-order quadrature methods are generally preferred for better efficiency.

## Example Usage

Implementation details and performance demonstrations can be found in `01_trapezoidal_rule.py`.
