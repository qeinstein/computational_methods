# Central (Centered) Difference Method

Central differences approximate derivatives using symmetric points around the evaluation point. They are usually more accurate (higher-order) than forward/backward formulas with the same stencil width.

## Second-order central difference (first derivative)

Using Taylor expansions of $f(x+h)$ and $f(x-h)$ and subtracting, we obtain the centered difference:

$$
f'(x) \approx \frac{f(x+h)-f(x-h)}{2h} + O(h^2).
$$

This is second-order accurate: truncation error scales like $h^2$.

## Second derivative (central)

The common second derivative centered formula is:

$$
f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2} + O(h^2).
$$

## Advantages and limitations

- Central differences give higher accuracy for interior points with the same number of function evaluations.
- They require values on both sides of the evaluation point; not usable at boundaries without one-sided schemes.

## Practical guidance

- Use central differences whenever you can (interior points) for better accuracy.
- Compare error vs step size to choose $h$; watch for round-off when $h$ is very small.

## Example usage

See `03_center_difference.py` for implementations and experiments comparing errors.
