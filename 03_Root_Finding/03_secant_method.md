# Secant Method

The secant method is a root-finding algorithm that approximates the derivative using two recent function values instead of requiring an analytic derivative. It is often used when the derivative $f'$ is difficult or expensive to compute. The method produces a sequence of approximations $x_0, x_1, x_2, \\\dots$ that (under mild conditions) converge to a root of $f(x)=0$.

## Basic idea

Rather than computing $f'(x_n)$ explicitly (as in Newton's method), the secant method approximates the derivative by the finite difference between two most recent iterates:

$$
f'(x_n) \\approx \\frac{f(x_n)-f(x_{n-1})}{x_n-x_{n-1}}.
$$

Plugging this into the Newton update yields the secant update:

$$
x_{n+1} = x_n - f(x_n)\\frac{x_n - x_{n-1}}{f(x_n)-f(x_{n-1})}.
$$

This uses two starting guesses $x_0$ and $x_1$ and requires only evaluations of $f$, not $f'$.

## Algorithm (step-by-step)

1. Choose two initial guesses $x_0$ and $x_1$ (preferably close to the root).
2. For $n = 1,2,\\dots$ until convergence or maximum iterations:
	- Compute $f(x_{n-1})$ and $f(x_n)$.
	- If $f(x_n) - f(x_{n-1})$ is (near) zero, stop or use a fallback (division by near-zero will produce a large jump).
	- Compute $x_{n+1} = x_n - f(x_n) (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))$.
	- Check stopping criteria: absolute/relative change or residual.

## Convergence properties

- The secant method has **superlinear convergence** with rate approximately $\\phi \\approx 1.618$ (the golden ratio), which is slower than Newton's quadratic rate but faster than the linear rate of bisection.
- Requires only function evaluations (no derivatives), so each iteration is cheaper than Newton if derivative computation is costly.
- Not guaranteed to converge unless the initial guesses are chosen reasonably well; unlike bisection, it does not bracket the root.

## Stopping criteria and tolerances

- Absolute change: $|x_{n+1}-x_n| < \\text{tol}$.
- Residual: $|f(x_{n+1})| < \\text{ftol}$.
- Relative change: $|x_{n+1}-x_n|/(|x_{n+1}|+\\epsilon) < \\text{rtol}$.

Choose tolerances consistent with the application and machine precision. Typical defaults: `tol=1e-10`, `ftol=1e-12`.

## Practical tips and pitfalls

- If $f(x_n)$ and $f(x_{n-1})$ are very close, the denominator becomes tiny and the method can produce a very large $x_{n+1}$ (unstable). Detect this and fall back to another method (e.g., bisection) or perturb the iterates.
- The method does not require derivatives but can fail if the function is not smooth enough near the root.
- It is common to combine a bracketing method (bisection) with secant/Newton: use a bracket to ensure global convergence, switch to secant for faster local convergence.

## Example (intuition)

For $f(x)=x^2-2$ with guesses $x_0=1$ and $x_1=2$ the secant step computes an approximate slope between $(1,f(1))$ and $(2,f(2))$ and intersects the x-axis at the new estimate; repeating this converges toward $\\sqrt{2}\\approx 1.4142$.

## Code example

Check `03_secant_method.py` 

