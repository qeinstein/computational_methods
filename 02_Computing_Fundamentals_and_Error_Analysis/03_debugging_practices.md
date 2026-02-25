# Debugging Practices for Numerical Code

Good debugging saves time and prevents subtle errors in computational methods.

## Common Numerics Pitfalls

- Floating-point rounding/overflow/underflow
- Indexing mistakes in loops or arrays
- Off-by-one errors in discretizations
- Ignoring edge cases (zero, negative, large values)

## Testing and Validation

- Write **unit tests** for small functions; compare against known values or analytic solutions.
- Use **assertions** to catch invalid states early: `assert n>0, "n must be positive"`.
- **Regression tests** to ensure bug fixes persist.

## Debugging Techniques

- `print()` or `logging` statements to inspect intermediate values.
- Use a debugger (`pdb`, IDE breakpoints) for step-by-step execution.
- Check variable shapes/types when using numpy arrays.

## Performance Profiling

- Use `timeit` or `%time` in notebooks to measure speed.
- `cProfile` to identify slow subroutines.

## Documentation and Code Hygiene

- Comment tricky math and choices.
- Keep functions small and focused.
- Use consistent naming and style.

