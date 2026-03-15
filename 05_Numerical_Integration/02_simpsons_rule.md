# Simpson's Rules

Simpson's rules are more accurate numerical integration methods than the trapezoidal rule. They approximate the function using higher-order polynomials (parabolas or cubics) instead of straight lines.

## Simpson's 1/3 Rule

Simpson's 1/3 rule approximates the function with a quadratic polynomial (parabola). It uses three points $(x_0, x_1, x_2)$ over two sub-intervals.

### The Single Simpson's 1/3 Rule
For an interval $[a, b]$, let $h = \frac{b-a}{2}$ and $x_1 = a + h$:

$$I \approx \frac{h}{3} [f(a) + 4f(x_1) + f(b)]$$

### The Composite Simpson's 1/3 Rule
To apply this rule over a larger interval $[a, b]$, the interval must be divided into an **even** number of sub-intervals ($n$).

$$I \approx \frac{h}{3} \left[ f(x_0) + 4\sum_{i \in \text{odd}} f(x_i) + 2\sum_{i \in \text{even}} f(x_i) + f(x_n) \right]$$

## Simpson's 3/8 Rule

Simpson's 3/8 rule approximates the function with a cubic polynomial. It uses four points over three sub-intervals. It is generally used when the number of sub-intervals $n$ is a **multiple of 3**.

### The Single Simpson's 3/8 Rule
For an interval $[a, b]$, let $h = \frac{b-a}{3}$:

$$I \approx \frac{3h}{8} [f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]$$

## Error Analysis

- **Simpson's 1/3 Rule:** The error is $O(h^4)$. Surprisingly, it is exact for cubic polynomials even though it's derived from quadratic ones.
- **Simpson's 3/8 Rule:** Also has an error of $O(h^4)$, but with a smaller constant coefficient for some functions, making it slightly more accurate than the 1/3 rule for functions that are closer to cubic.

## Summary Table

| Method | Points | Order | Constraints |
| :--- | :--- | :--- | :--- |
| Trapezoidal | 2 | $O(h^2)$ | None |
| Simpson's 1/3 | 3 | $O(h^4)$ | $n$ must be even |
| Simpson's 3/8 | 4 | $O(h^4)$ | $n$ must be multiple of 3 |

## Example Usage

See `02_simpsons_rule.py` for Python implementations and accuracy comparisons.
