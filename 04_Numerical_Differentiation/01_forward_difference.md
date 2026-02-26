# Forward Difference Method

The forward difference is the simplest finite-difference approximation to the derivative. It approximates the derivative at a point using the function value at that point and a point a small step $h$ ahead.

## First-order forward difference (first derivative)

Given a sufficiently smooth function $f$, the first-order forward difference formula for the first derivative is derived from the Taylor expansion of $f(x+h)$ around $x$:

$$
f(x+h) = f(x) + h f'(x) + \frac{h^2}{2} f''(\xi),
$$
for some $\xi\in(x,x+h)$. Rearranging gives the forward difference approximation:

$$
f'(x) \approx \frac{f(x+h)-f(x)}{h} + O(h).
$$

This approximation has truncation error proportional to $h$ (first order).

## Higher-order forward formula (three-point)

Using more points, you can get higher-order accuracy. A common second-order forward approximation is:

$$
f'(x) \approx \frac{-3f(x) + 4f(x+h) - f(x+2h)}{2h} + O(h^2).
$$

## Error and step-size selection

- Truncation error scales like a power of $h$ (e.g., $O(h)$ or $O(h^2)$ depending on formula). Decreasing $h$ reduces truncation error but increases rounding error due to floating-point arithmetic.
- Choose $h$ by balancing truncation and rounding errors. A practical rule-of-thumb for double precision is $h \sim \sqrt{\varepsilon} \approx 10^{-8}$ for first-order differences on smooth functions, but use experiments for your problem.

## Practical notes

- Forward differences are useful at domain boundaries when central differences are not available (e.g., near the left endpoint).
- When possible, prefer central differences (higher accuracy for the same stencil width).

## Example usage

See `01_forward_difference.py` for an implementation and demonstrations comparing errors for different $h$.

