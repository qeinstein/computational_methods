# Backward Difference Method

The backward difference approximates derivatives using points behind the evaluation point and is particularly useful near right-hand boundaries.

## First-order backward difference (first derivative)

From the Taylor expansion of $f(x-h)$ about $x$:

$$
f(x-h) = f(x) - h f'(x) + \frac{h^2}{2} f''(\xi),
$$
which gives the backward approximation:

$$
f'(x) \approx \frac{f(x) - f(x-h)}{h} + O(h).
$$

## Higher-order backward formula (three-point)

A second-order backward approximation is:

$$
f'(x) \approx \frac{3f(x) - 4f(x-h) + f(x-2h)}{2h} + O(h^2).
$$

## Error and practical notes

- Backward differences mirror forward differences and are convenient at the domain right endpoint.
- Step selection and rounding/truncation trade-offs are similar to forward differences.

## Example usage

See `02_backward_difference.py` for implementations and numerical comparisons.
