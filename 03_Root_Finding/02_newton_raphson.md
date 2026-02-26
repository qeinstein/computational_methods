# Newton–Raphson Method

The Newton–Raphson (or Newton) method is an iterative technique for finding roots of a nonlinear equation
$f(x)=0$. It uses the tangent line at the current approximation to produce a better approximation.

## Intuition and derivation

Starting from a current guess $x_n$, approximate the function by its first-order Taylor expansion around $x_n$:

$$
f(x) \approx f(x_n) + f'(x_n)(x - x_n).
$$

Set the right-hand side to zero and solve for \(x\) to obtain the Newton update:

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.
$$

Geometrically, this finds the x-intercept of the tangent line to $f$ at $x_n$.

## Algorithm (pseudocode)

1. Choose an initial guess $x_0$.
2. For $n = 0,1,2,\dots$ until convergence or maximum iterations:
	- If $f'(x_n) = 0$ (or close to zero) stop: the method cannot proceed.
	- Compute $x_{n+1} = x_n - f(x_n)/f'(x_n)$.
	- If $|x_{n+1} - x_n| < \text{tol}$ or $|f(x_{n+1})| < \text{ftol}$ then stop and return $x_{n+1}$.

## Convergence properties

- If the function is sufficiently smooth and the initial guess is close to a simple root, Newton's method has **quadratic convergence**: the number of correct digits roughly doubles each iteration.
- If the derivative near the root is zero (multiple root) or the initial guess is far from the root, the method may converge slowly or diverge.

## Stopping criteria and tolerances

- **Absolute change**: $|x_{n+1}-x_n| < \text{tol}$.
- **Residual**: $|f(x_{n+1})| < \text{ftol}$.
- **Relative change**: $|x_{n+1}-x_n| / (|x_{n+1}| + \epsilon) < \text{rtol}$.
- Use values compatible with machine precision (double precision machine epsilon ≈ 2.22e-16). Typical choices: `tol=1e-10`, `ftol=1e-12`, `rtol=1e-12`.

## Practical notes and pitfalls

- Always inspect or plot $f$ and $f'$ to avoid starting near stationary points (where $f'$ ≈ 0).
- If $f'$ is expensive or unavailable, consider the secant method as an alternative (no derivative required, but slower).
- Combine Newton with a bracketing method (e.g., bisection) to get global convergence: use bisection until you are close, then switch to Newton for fast convergence.

## Example usage

1. One Newton step for $f(x)=x^2-2$ from $x_0=1.4$:

```python
x0 = 1.4
f = lambda x: x**2 - 2
df = lambda x: 2*x
x1 = x0 - f(x0)/df(x0)  # single Newton step
```

