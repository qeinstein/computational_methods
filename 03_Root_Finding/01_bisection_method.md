# Bisection Method

The bisection method is a simple, robust root-finding algorithm that repeatedly
halves an interval known to contain a root. It relies on the Intermediate Value
Theorem: if a continuous function `f` takes opposite signs at `a` and `b` (i.e.
`f(a)` and `f(b)` have opposite signs), then there exists at least one root in
the open interval `(a, b)`.

## Algorithm (in words)

- Verify `f(a)` and `f(b)` have opposite signs. If not, bisection cannot be
  applied directly.
- Compute the midpoint `m = (a + b) / 2` and evaluate `f(m)`.
- If `|f(m)|` is below the tolerance (or the interval width is below the
  tolerance), accept `m` as the root.
- Otherwise, determine which half-interval contains a sign change and repeat on
  that half: if `f(a)` and `f(m)` have the same sign, the root lies in `(m,b)`;
  otherwise it lies in `(a,m)`.

Each iteration halves the search interval, so the method converges linearly
and is guaranteed to find a root for continuous functions when a bracketing
interval is provided.

## Pseudocode

```
function bisection(f, a, b, tol, max_iter):
    require f(a)*f(b) < 0
    for k in 1..max_iter:
        m = (a + b)/2
        if |f(m)| <= tol or (b-a)/2 <= tol:
            return m
        if sign(f(a)) == sign(f(m)):
            a = m
        else:
            b = m
    error "did not converge"
```

## Stopping criteria

- Absolute function tolerance: `|f(m)| < tol` — useful when you want the
  residual to be small.
- Interval width tolerance: `(b-a)/2 < tol` — useful when you want the root
  location to be accurate to a given distance.

Choose `tol` relative to the problem scale and machine epsilon (for double
precision floats, machine epsilon ≈ 2.22e-16). Do not set `tol` significantly
smaller than machine epsilon.

## Example (usage)

See `01_bisection_method.py` for a working `my_bisection` implementation and
examples showing how to call it and verify the residual `f(root)`.

## Notes

- Bisection requires only function evaluations (no derivatives).
- It is robust but not the fastest method; after bracketing a root, faster
  methods (e.g., Newton or secant) can be used if derivatives or better
  convergence are desired.
- If you still don't understand, study it again from the perspective of binary search(BS)
