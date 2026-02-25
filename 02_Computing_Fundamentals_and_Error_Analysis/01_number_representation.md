# Number Representation

Computers store numbers using binary (base‑2) internally. Key concepts:

- **Binary, decimal, hexadecimal** systems and conversions.
- **Floating-point representation** follows IEEE 754 standard with sign bit, exponent, and mantissa (also called significand).
- A real number is stored roughly as \( (-1)^{sign} \times 1.mantissa \times 2^{exponent-bias}\).
- **Machine epsilon**: the smallest difference between 1 and the next representable float.
- **Precision limitations** cause round-off and truncation errors.

### Details

Floating-point numbers have a finite number of bits for exponent and mantissa (e.g., 64-bit `double` has 52 mantissa bits, 11 exponent bits).

Subnormal numbers, infinities (`inf`), and `NaN` (not a number) are also part of IEEE 754.

Arithmetic operations can introduce tiny errors; for example, `0.1 + 0.2 != 0.3` in binary floating point because 0.1 and 0.2 cannot be represented exactly.

### Common operations

- Convert between bases using built-in functions like `bin()`, `hex()`.
- Use `float.hex()` to inspect the underlying representation.


