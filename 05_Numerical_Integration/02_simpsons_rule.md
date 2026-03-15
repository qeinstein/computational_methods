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

**Understanding the Indices:**
- **$i \in \text{odd}$:** These are the points with odd indices ($1, 3, 5, \dots, n-1$). These points get a multiplier of **4**.
- **$i \in \text{even}$:** These are the internal points with even indices ($2, 4, 6, \dots, n-2$). These points get a multiplier of **2**.
- **$x_0, x_n$:** The boundary points have a multiplier of **1**.

![Simpson's 1/3 Rule Flowchart](https://kroki.io/graphviz/svg/eNplkEFLw0AQhe_-iiGnpDWU1t7CKkJFAqJgvYh42DBTs7jdDbsbqIj_3dmkSWo9LW_eY-d7g-rDyaaGe_gGJ80nKideNgUYiwRvvpYNicoeLsGHL03C2dYg4XsB2yBdGBKktWo88bg0iqdaVqRFUoOAtMpltjAX23bPapfKDOb8VFnC6QdrmzGt2F9CsGDyZTRL_4R44ioPFvEmYZZuKSq5tyay3CKux2BcNBewnu3Sg-q2sL06t1eT_Uy-1RN0aQLxTTTTxOwM6sVVjN0Z_F-3v0J-3ffmt2sUdYQfOrD-g_hKfirYmxPgo02GSsf_jg1GNew4A99YQyd9OMDIBfz8AoPNlcE=)

## Simpson's 3/8 Rule

Simpson's 3/8 rule approximates the function with a cubic polynomial. It uses four points over three sub-intervals. It is generally used when the number of sub-intervals $n$ is a **multiple of 3**.

### The Single Simpson's 3/8 Rule
For an interval $[a, b]$, let $h = \frac{b-a}{3}$:

$$I \approx \frac{3h}{8} [f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]$$

### The Composite Simpson's 3/8 Rule
To apply this rule over $n$ sub-intervals (where $n$ is a **multiple of 3**):

$$I \approx \frac{3h}{8} \left[ f(x_0) + 3\sum_{i=1, i \nmid 3}^{n-1} f(x_i) + 2\sum_{i=3, 6, 9}^{n-3} f(x_i) + f(x_n) \right]$$

**Understanding the Indices:**
- **$i \nmid 3$:** This symbol means **"$i$ is not divisible by 3"**. These are indices like $1, 2, 4, 5, 7, 8, \dots$. These points get a multiplier of **3**.
- **$i=3, 6, 9, \dots$:** These are internal indices that are **multiples of 3**. They represent the shared boundaries between cubic segments and get a multiplier of **2**.
- **$x_0, x_n$:** The boundary points have a multiplier of **1**.

## Error Analysis

- **Simpson's 1/3 Rule:** The error is $O(h^4)$. Surprisingly, it is exact for cubic polynomials even though it's derived from quadratic ones.
- **Simpson's 3/8 Rule:** Also has an error of $O(h^4)$, but with a smaller constant coefficient for some functions, making it slightly more accurate than the 1/3 rule for functions that are closer to cubic.

## The Role of Step Size ($h$)

In Simpson's rules, the step size $h$ has a much more dramatic impact on accuracy than in the Trapezoidal rule.

### Error Convergence
Because Simpson's rules are $O(h^4)$ methods:
- **Halving the step size ($h/2$)** reduces the error by a factor of **16** ($2^4$).
- This means you can achieve very high precision with a much larger $h$ (smaller $n$) compared to the Trapezoidal rule.

### Rule of Thumb
- Use **Simpson's 1/3** if you can easily divide your interval into an even number of strips.
- Use **Simpson's 3/8** if your data points come in multiples of 3.
- If you have an odd number of intervals, a common trick is to use Simpson's 1/3 for most of the area and the Trapezoidal rule for the very last strip.

## Summary Table

| Method | Points | Order | Constraints |
| :--- | :--- | :--- | :--- |
| Trapezoidal | 2 | $O(h^2)$ | None |
| Simpson's 1/3 | 3 | $O(h^4)$ | $n$ must be even |
| Simpson's 3/8 | 4 | $O(h^4)$ | $n$ must be multiple of 3 |

## Example Usage

See `02_simpsons_rule.py` for Python implementations and accuracy comparisons.
