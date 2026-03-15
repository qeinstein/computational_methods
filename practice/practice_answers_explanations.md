# Computational Methods Practice - Answers & Explanations

---

## 1. Python Basics - ANSWERS

### A1.1: Function Scope and Mutability (Theoretical)
In Python, default arguments are evaluated only once at the time of function definition. If a mutable object like a list is used as a default argument (e.g., `box=[]`), that same list object is shared across all calls to the function that do not provide an explicit value for that argument.
**Danger:** Appending items to `box` in one call will affect subsequent calls, leading to unexpected "persistence" of data. The standard fix is to use `def add_item(item, box=None):` and initialize `box = []` inside the function if it is `None`.

### A1.2: Bitwise Logic Trace (Manual)
**Initial:** `n = 13` (`1101` binary), `res = 0`.
1. **Iteration 1:** `n & 1 = 1`. `res = (0 << 1) | 1 = 1`. `n >>= 1` (n becomes 6, `110`).
2. **Iteration 2:** `n & 1 = 0`. `res = (1 << 1) | 0 = 2` (`10` binary). `n >>= 1` (n becomes 3, `11`).
3. **Iteration 3:** `n & 1 = 1`. `res = (2 << 1) | 1 = 5` (`101` binary). `n >>= 1` (n becomes 1, `1`).
4. **Iteration 4:** `n & 1 = 1`. `res = (5 << 1) | 1 = 11` (`1011` binary). `n >>= 1` (n becomes 0).
**Final Result:** `res = 11`. (This logic reverses the bits of the integer).

### A1.3: Algorithm Implementation (Code)
```python
def first_unique(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in s:
        if counts[char] == 1:
            return char
    return None
```

---

## 2. Object-Oriented Programming - ANSWERS

### A2.1: Diamond Inheritance and super() (Theoretical)
MRO (Method Resolution Order) is the order in which Python looks for a method in a hierarchy, determined by the C3 Linearization algorithm.
In a diamond (D -> B, C -> A), the MRO is `[D, B, C, A, object]`.
`super()` does not simply call the parent class; it calls the *next* class in the MRO. When `B.method()` calls `super()`, it goes to `C`, not `A`. This ensures every class in the graph is visited exactly once in a predictable order, preventing the "double-call" problem of $A$ from both $B$ and $C$.

### A2.2: Class vs Instance Variables (Manual)
1. `t1 = Tracker("A")`: `Tracker.count` becomes 1.
2. `t2 = Tracker("B")`: `Tracker.count` becomes 2.
3. `t1.count = 10`: This creates a new **instance variable** named `count` on `t1` that shadows the class variable.
4. `t2.count`: `t2` has no instance variable `count`, so it accesses the class variable (2).
5. `Tracker.count`: The class variable remains 2.
**Output:** `10 2 2`.

### A2.3: Operator Overloading (Code)
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

---

## 3. Data Visualization - ANSWERS

### A3.1: Axis Object Management (Theoretical)
The state-machine approach (`plt.plot`) is convenient for quick, single-plot scripts but relies on an implicit "current" figure/axes, which can become confusing in complex tasks.
The object-oriented approach (`fig, ax = plt.subplots()`) provides explicit handles to figures and axes. It is superior for:
1. Creating multiple subplots in a grid.
2. Passing specific axes to functions for drawing.
3. Managing dual-axis plots (`twinx`).
4. Fine-grained control over specific plot elements without ambiguity.

### A3.2: Histogram Binning Logic (Manual)
- Range: $33 - 5 = 28$.
- Bins: 3. Bin width: $28 / 3 \approx 9.33$.
- **Bin 1:** $[5, 14.33)$. Counts: $5, 7, 12$ (**3 points**).
- **Bin 2:** $[14.33, 23.66)$. Counts: $18, 21$ (**2 points**).
- **Bin 3:** $[23.66, 33]$. Counts: $28, 33$ (**2 points**).

### A3.3: Dual-Axis Implementation (Code)
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
fig, ax1 = plt.subplots()
ax1.plot(x, x**2, 'g-', label="Quadratic")
ax1.set_ylabel("y = x^2", color='g')

ax2 = ax1.twinx()
ax2.plot(x, np.exp(x), 'b-', label="Exponential")
ax2.set_ylabel("y = e^x", color='b')
plt.show()
```

---

## 4. Floating Point Representation - ANSWERS

### A4.1: Precision Loss in Summation (Theoretical)
In 64-bit double precision, the mantissa has 53 bits, providing roughly 15-17 decimal digits of precision.
1. When computing `(10**16 + 1)`, the number $1$ is too small relative to $10^{16}$ (which requires all precision bits). The $+1$ is "rounded off" because it falls outside the representable window. Subtracting $10^{16}$ then leaves `0.0`.
2. In `1 + (10**16 - 10**16)`, the parentheses are evaluated first. $10^{16} - 10^{16}$ is exactly $0$. Then $1 + 0 = 1.0$.

### A4.2: IEEE 754 Single Precision Conversion (Manual)
Number: $-12.625$.
1. **Sign:** $1$ (negative).
2. **Binary:** $12 = 1100_2$. $0.625 = 0.101_2$. Total: $1100.101_2$.
3. **Normalize:** $1.100101 \times 2^3$.
4. **Exponent:** $3 + 127 = 130$ (`10000010` binary).
5. **Mantissa:** `10010100000000000000000` (23 bits).
**Result:** `1 10000010 10010100000000000000000`.

### A4.3: Finding Machine Epsilon (Code)
```python
eps = 1.0
while (1.0 + eps) != 1.0:
    last_eps = eps
    eps /= 2.0
print(f"Machine Epsilon: {last_eps}")
```

---

## 5. Error Analysis - ANSWERS

### A5.1: Condition Number and Stability (Theoretical)
The condition number $\kappa(x) = |x \cdot f'(x) / f(x)|$ measures how much a relative change in the input $x$ is amplified in the output $f(x)$.
- **Ill-conditioned:** A high $\kappa$ (e.g., $>10^3$) means small input errors (like round-off) cause massive output errors.
- **Reliability:** Even a "perfect" algorithm cannot produce a reliable result for an ill-conditioned problem because the sensitivity is inherent to the mathematical function itself.

### A5.2: Error Propagation in Addition (Manual)
- $S = X + Y = 100 + 50 = 150$.
- **Absolute Error:** $\Delta S = \Delta X + \Delta Y = 0.5 + 0.2 = 0.7$.
- **Relative Error:** $\Delta S / S = 0.7 / 150 \approx 0.00467$ (or $0.467\%$).

### A5.3: Catastrophic Cancellation (Code)
```python
import math
x = 1e14
# Unstable form
f1 = math.sqrt(x + 1) - math.sqrt(x)
# Stable form (rationalized)
f2 = 1 / (math.sqrt(x + 1) + math.sqrt(x))
print(f"Unstable: {f1}\nStable: {f2}")
```

---

## 6. Bisection Method - ANSWERS

### A6.1: Continuity Requirement (Theoretical)
If $f(x) = 1/(x-0.5)$ on the interval $[0, 1]$.
$f(0) = -2$ and $f(1) = 2$. The sign change suggests a root, but there isn't one; there is a singularity at $x=0.5$. The Bisection method would keep narrowing down on $x=0.5$ without ever finding a value where $f(x)=0$.

### A6.2: Manual Iteration (Manual)
$f(x) = x^3 - 5$ on $[1, 2]$.
1. **Iter 1:** $m = 1.5, f(1.5) = -1.625$. Sign change on $[1.5, 2]$.
2. **Iter 2:** $m = 1.75, f(1.75) \approx 0.359$. Sign change on $[1.5, 1.75]$.
3. **Iter 3:** $m = 1.625, f(1.625) \approx -0.709$. Sign change on $[1.625, 1.75]$.
**Result:** Root is approximately $1.6875 \pm 0.0625$.

### A6.3: Bisection Implementation (Code)
```python
def bisection(f, a, b, tol):
    if f(a) * f(b) >= 0:
        raise ValueError("Interval does not bracket a root")
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(m) == 0: return m
        if f(a) * f(m) < 0: b = m
        else: a = m
    return (a + b) / 2
```

---

## 7. Newton-Raphson Method - ANSWERS

### A7.1: Multiple Root Convergence (Theoretical)
For a root of multiplicity $p > 1$, the derivative $f'(x)$ also approaches zero at the root. In the Newton update $x_{n+1} = x_n - f(x_n)/f'(x_n)$, the ratio of errors $e_{n+1}/e_n$ approaches $(p-1)/p$.
For $f(x) = (x-1)^2$, $p=2$, so the ratio is $0.5$. This makes the convergence **linear** (slow) rather than the usual quadratic.

### A7.2: Manual Newton Step (Manual)
$f(x) = x^2 - 3, f'(x) = 2x, x_0 = 2$.
1. **Iter 1:** $x_1 = 2 - (2^2 - 3) / (2 \cdot 2) = 2 - 1/4 = 1.75$.
2. **Iter 2:** $x_2 = 1.75 - (1.75^2 - 3) / (2 \cdot 1.75) = 1.75 - 0.0625 / 3.5 \approx 1.7321$.

### A7.3: Newton with Lambda (Code)
```python
import math
def newton(f, df, x0, tol):
    x = x0
    while abs(f(x)) > tol:
        x = x - f(x) / df(x)
    return x

f = lambda x: x * math.exp(x) - 1
df = lambda x: math.exp(x) * (x + 1)
print(newton(f, df, 0.5, 1e-7))
```

---

## 8. Secant Method - ANSWERS

### A8.1: Secant vs Newton (Theoretical)
**Advantage:** The Secant method does not require the analytical derivative $f'(x)$, which may be unknown or expensive to calculate.
**Trade-off:** It is slightly slower than Newton's method (order $\approx 1.618$ vs $2.0$). It also requires two initial guesses and is slightly more prone to divergence if the function is not smooth.

### A8.2: Manual Secant Trace (Manual)
$f(x) = x^2 - 5, x_0 = 2 (f_0 = -1), x_1 = 3 (f_1 = 4)$.
1. **Iter 1:** $x_2 = 3 - 4 \cdot (3 - 2) / (4 - (-1)) = 3 - 4/5 = 2.2$.
2. **Iter 2:** $f(2.2) = 4.84 - 5 = -0.16$.
   $x_3 = 2.2 - (-0.16) \cdot (2.2 - 3) / (-0.16 - 4) = 2.2 - 0.128 / -4.16 \approx 2.2308$.

### A8.3: Secant Implementation (Code)
```python
def secant_method(f, x0, x1, tol):
    for _ in range(100):
        denom = f(x1) - f(x0)
        if abs(denom) < 1e-12: break
        x_new = x1 - f(x1) * (x1 - x0) / denom
        if abs(x_new - x1) < tol: return x_new
        x0, x1 = x1, x_new
    return x1
```

---

## 9. Forward & Backward Difference - ANSWERS

### A9.1: Error Scaling and Big-O (Theoretical)
The Taylor expansion is $f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(\xi)$.
Rearranging: $f'(x) = \frac{f(x+h) - f(x)}{h} - \frac{h}{2}f''(\xi)$.
The truncation error is $E \approx | \frac{h}{2}f''(\xi) |$, which is $O(h)$.
If $h$ is reduced by 10, the error is reduced by 10 (linear scaling).

### A9.2: Forward Difference Table (Manual)
$f(x) = x^3 \implies f'(x) = 3x^2, f'(1) = 3$.
- **$h=0.1$:** $(1.1^3 - 1^3) / 0.1 = (1.331 - 1) / 0.1 = 3.31$. (Error: 0.31).
- **$h=0.01$:** $(1.01^3 - 1^3) / 0.01 = (1.030301 - 1) / 0.01 = 3.0301$. (Error: 0.0301).

### A9.3: Forward Difference Implementation (Code)
```python
import math
def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

x = 1
for i in range(1, 7):
    h = 10**-i
    approx = forward_diff(math.sin, x, h)
    print(f"h={h:.0e}, Error: {abs(approx - math.cos(x)):.2e}")
```

---

## 10. Central Difference & Higher Order - ANSWERS

### A10.1: Central Difference Accuracy (Theoretical)
1. $f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + O(h^4)$
2. $f(x-h) = f(x) - hf'(x) + \frac{h^2}{2}f''(x) - \frac{h^3}{6}f'''(x) + O(h^4)$
Subtracting (2) from (1): $f(x+h) - f(x-h) = 2hf'(x) + \frac{2h^3}{6}f'''(x) + O(h^5)$.
Dividing by $2h$: $f'(x) \approx \frac{f(x+h)-f(x-h)}{2h} - O(h^2)$.

### A10.2: Second Derivative Central (Manual)
Adding the two Taylor expansions from A10.1:
$f(x+h) + f(x-h) = 2f(x) + h^2f''(x) + O(h^4)$.
Rearranging: $f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$.
For $f(x) = e^x, x=0, h=0.1$:
$f''(0) \approx (e^{0.1} - 2(1) + e^{-0.1}) / 0.01 \approx (1.10517 - 2 + 0.90484) / 0.01 = 1.0008$. (Exact: 1.0).

### A10.3: Higher-Order Derivative Implementation (Code)
```python
def second_deriv_central(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)

f = lambda x: x**4
print(second_deriv_central(f, 2, 0.01)) # ~48.001
```

---

## 11. Trapezoidal Rule - ANSWERS

### A11.1: Geometric Interpretation (Theoretical)
The Trapezoidal rule approximates the area under a curve using a straight line between $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$.
- If $f''(x) > 0$ (concave up), the line segment lies **above** the curve, so the trapezoid area is an over-estimate.
- If $f''(x) < 0$ (concave down), the line segment lies **below** the curve, so it is an under-estimate.

### A11.2: Single vs Composite (Manual)
$\int_0^1 x^2 dx$ (Exact = $1/3 \approx 0.3333$).
- **$n=1$:** $I = \frac{1}{2}(0^2 + 1^2) = 0.5$. (Error: 0.1667).
- **$n=2, h=0.5$:** $I = \frac{0.5}{2}(0^2 + 2(0.5^2) + 1^2) = 0.25(0 + 0.5 + 1) = 0.375$. (Error: 0.0417).

### A11.3: Composite Trapezoidal Implementation (Code)
```python
import math
def trapezoidal_composite(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

print(trapezoidal_composite(math.sin, 0, math.pi, 100)) # ~2.0
```

---

## 12. Simpson's Rules - ANSWERS

### A12.1: Composite 1/3 Parity (Theoretical)
Simpson's 1/3 rule fits a quadratic polynomial over **two** intervals at a time. To apply it across the entire range, the intervals must be grouped in pairs, requiring $n$ to be even.
Interestingly, it integrates **cubic** polynomials ($x^3$) exactly due to error cancellation, even though it is derived from a quadratic fit.

### A12.2: Comparison with Trapezoidal (Manual)
$\int_0^\pi \sin(x) dx, n=2, h=\pi/2$. (Exact = 2.0).
- **Trapezoidal:** $\frac{\pi/2}{2}(\sin 0 + 2\sin(\pi/2) + \sin \pi) = \frac{\pi}{4}(0 + 2 + 0) \approx 1.57$.
- **Simpson's 1/3:** $\frac{\pi/2}{3}(\sin 0 + 4\sin(\pi/2) + \sin \pi) = \frac{\pi}{6}(0 + 4 + 0) \approx 2.09$.
Simpson's rule is significantly closer to the true value of 2.0.

### A12.3: Simpson's 1/3 Implementation (Code)
```python
def simpson13_composite(f, a, b, n):
    if n % 2 != 0: raise ValueError("n must be even")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        weight = 4 if i % 2 != 0 else 2
        s += weight * f(a + i * h)
    return s * h / 3
```

---

## 13. Euler's Method - ANSWERS

### A13.1: Local vs Global Error (Theoretical)
- **LTE:** The error of one single step ($O(h^2)$ for Euler).
- **GTE:** The total accumulated error after all steps ($O(h^1)$ for Euler).
Because we take $N \propto 1/h$ steps, the total error is $N \times LTE \approx (1/h) \times h^2 = h$. Thus, Euler is a first-order method.

### A13.2: Single Step Trace (Manual)
$y' = y + t, y(0) = 1, h=0.1$.
1. **Step 1:** $y(0.1) \approx 1 + 0.1(1 + 0) = 1.1$.
2. **Step 2:** $y(0.2) \approx 1.1 + 0.1(1.1 + 0.1) = 1.1 + 0.12 = 1.22$.
**Result:** $y(0.2) \approx 1.22$.

### A13.3: Basic Euler Implementation (Code)
```python
import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, t0, y0, h, steps):
    t = [t0]; y = [y0]
    for _ in range(steps):
        y.append(y[-1] + h * f(t[-1], y[-1]))
        t.append(t[-1] + h)
    return np.array(t), np.array(y)

f = lambda t, y: -2 * y
t, y = euler_method(f, 0, 1, 0.1, 20)
plt.plot(t, y); plt.show()
```

---

## 14. Heun's Method - ANSWERS

### A14.1: Predictor-Corrector Logic (Theoretical)
Heun's method uses an Euler step to **predict** the next value ($\tilde{y}_{n+1}$), then uses the average of the slopes at the current and predicted points to **correct** the estimate. This averaging of slopes is mathematically identical to using the Trapezoidal rule for integration, making it second-order accurate.

### A14.2: Manual Heun Step (Manual)
$y' = y - t^2 + 1, y(0) = 0.5, h=0.2$.
1. **Predict:** $f(0, 0.5) = 1.5$. $\tilde{y}_{0.2} = 0.5 + 0.2(1.5) = 0.8$.
2. **Correct:** $f(0.2, 0.8) = 0.8 - 0.04 + 1 = 1.76$.
   $y_{0.2} = 0.5 + \frac{0.2}{2}(1.5 + 1.76) = 0.5 + 0.326 = 0.826$.
**Result:** $y(0.2) \approx 0.826$.

### A14.3: Heun Implementation (Code)
```python
def heun_method(f, t0, y0, h, steps):
    t, y = [t0], [y0]
    for _ in range(steps):
        ti, yi = t[-1], y[-1]
        k1 = f(ti, yi)
        y_pred = yi + h * k1
        k2 = f(ti + h, y_pred)
        y.append(yi + (h / 2) * (k1 + k2))
        t.append(ti + h)
    return t, y
```

---

## 15. Runge-Kutta 4th Order - ANSWERS

### A15.1: Symmetry of Slopes (Theoretical)
RK4 effectively samples the derivative at the start ($k_1$), twice at the midpoint ($k_2, k_3$), and once at the end ($k_4$). The weighted average follows Simpson's 1/3 rule. Sampling the midpoint twice (once using $k_1$ to get there, once using $k_2$) provides the $O(h^4)$ accuracy that makes it the industry standard.

### A15.2: Manual RK4 Step (Manual)
$y' = t + y, y(0) = 1, h=0.1$.
1. $k_1 = 0.1 \cdot f(0, 1) = 0.1(1) = 0.1$.
2. $k_2 = 0.1 \cdot f(0.05, 1.05) = 0.1(1.1) = 0.11$.
3. $k_3 = 0.1 \cdot f(0.05, 1.055) = 0.1(1.105) = 0.1105$.
4. $k_4 = 0.1 \cdot f(0.1, 1.1105) = 0.1(1.2105) = 0.12105$.
$y(0.1) \approx 1 + \frac{1}{6}(0.1 + 2(0.11) + 2(0.1105) + 0.12105) \approx 1.11034$.

### A15.3: RK4 Implementation (Code)
```python
def rk4_step(f, t, y, h):
    k1 = h * f(t, y)
    k2 = h * f(t + h/2, y + k1/2)
    k3 = h * f(t + h/2, y + k2/2)
    k4 = h * f(t + h, y + k3)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6
```

---

## 16. Linear & Quadratic Splines - ANSWERS

### A16.1: Degree of Freedom Analysis (Theoretical)
With $n$ intervals, there are $3n$ coefficients.
- **Continuity ($C^0$):** $2n$ equations.
- **Smoothness ($C^1$):** $n-1$ equations (internal nodes).
Total equations: $3n - 1$. We have one degree of freedom left, hence the need for a boundary condition like $a_1 = 0$.

### A16.2: Linear Spline Construction (Manual)
Points: $(1, 2), (3, 6), (5, 4)$.
1. **Interval [1, 3]:** $m = (6-2)/(3-1) = 2$. $s_1(x) = 2 + 2(x-1)$.
2. **Interval [3, 5]:** $m = (4-6)/(5-3) = -1$. $s_2(x) = 6 - (x-3) = 9 - x$.
**At $x=4$:** $s_2(4) = 9 - 4 = 5$.

### A16.3: Quadratic Spline Solver (Code)
(The code sets up a $5 \times 5$ matrix for the 2 intervals and solves for $b_1, c_1, a_2, b_2, c_2$ with $a_1=0$).

---

## 17. Newton Interpolation - ANSWERS

### A17.1: Uniqueness of Interpolants (Theoretical)
For $n+1$ distinct points, there exists exactly one unique polynomial of degree $\leq n$ that passes through all of them. Newton and Lagrange are simply different ways of writing the **same** polynomial (different bases). The Newton form is preferred for adding new data points incrementally.

### A17.2: Divided Difference Table (Manual)
Points: $(-1, 3), (0, 1), (1, 3), (2, 9)$.
1. **1st DD:** -2, 2, 6.
2. **2nd DD:** 2, 2.
3. **3rd DD:** 0.
$P_3(x) = 3 - 2(x+1) + 2(x+1)(x-0) + 0 = 2x^2 + 1$.

### A17.3: Newton Polynomial Evaluator (Code)
```python
def evaluate_newton(x_data, coefs, x):
    n = len(coefs) - 1
    p = coefs[n]
    for k in range(1, n + 1):
        p = coefs[n-k] + (x - x_data[n-k]) * p
    return p
```

---

## 18. Cubic Spline Interpolation - ANSWERS

### A18.1: Natural Boundary Conditions (Theoretical)
The "Natural" condition sets $f''(x) = 0$ at both ends. Physically, this corresponds to a flexible beam that is pinned at the ends but allowed to extend straight beyond them (zero curvature). It is the most common boundary condition when the endpoint slopes are unknown.

### A18.2: Manual Cubic Spline (Manual)
Points: $(0, 0), (1, 1), (2, 0), h=1$. $M_0 = 0, M_2 = 0$.
The tridiagonal equation for $M_1$: $hM_0 + 2(h+h)M_1 + hM_2 = 6[(y_2-y_1)/h - (y_1-y_0)/h]$.
$0 + 4M_1 + 0 = 6[(0-1)/1 - (1-0)/1] = -12$.
**Result:** $M_1 = -3$.

### A18.3: SciPy Spline Usage (Code)
```python
from scipy.interpolate import CubicSpline
cs = CubicSpline(x_data, y_data, bc_type='natural')
y_interp = cs(x_new)
```

---

## 19. Discrete Fourier Transform - ANSWERS

### A19.1: The Leakage Phenomenon (Theoretical)
The DFT treats the input sequence as one period of an infinite periodic signal. If the wave does not complete an integer number of cycles within $N$ samples, there is a sharp "jump" or discontinuity where the end of the window meets the start. This discontinuity in the time domain spreads energy across the entire frequency spectrum.

### A19.2: Manual DFT Summation (N=11) (Manual)
$x_n = 5, N=11$.
$X_1 = \sum_{n=0}^{10} 5 e^{-i \frac{2\pi n}{11}} = 5 \sum_{n=0}^{10} (e^{-i \frac{2\pi}{11}})^n$.
Let $r = e^{-i \frac{2\pi}{11}}$. The sum is $5 \cdot \frac{1 - r^{11}}{1 - r}$.
Since $r^{11} = e^{-i 2\pi} = 1$, the numerator is $1 - 1 = 0$.
**Result:** $X_1 = 0$. (This confirms that a DC signal has no energy in non-zero frequency bins).

### A19.3: Naive DFT Complexity (Code)
```python
import numpy as np
def manual_dft(x):
    N = len(x)
    n = np.arange(N); k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x)
```

---

## 20. Fast Fourier Transform - ANSWERS

### A20.1: Butterfly Structure (Theoretical)
The butterfly structure exploits the periodicity and symmetry of the twiddle factors ($W_N^{k+N/2} = -W_N^k$). It breaks an $N$-point DFT into two $N/2$-point DFTs recursively. This divide-and-conquer approach reduces the work from $N^2$ to $N \log_2 N$, making real-time signal processing possible.

### A20.2: Bit-Reversal Permutation (Manual)
1. 0(000) -> 0(000) = **0**
2. 1(001) -> 4(100) = **4**
3. 2(010) -> 2(010) = **2**
4. 3(011) -> 6(110) = **6**
5. 4(100) -> 1(001) = **1**
6. 5(101) -> 5(101) = **5**
7. 6(110) -> 3(011) = **3**
8. 7(111) -> 7(111) = **7**
Order: `[0, 4, 2, 6, 1, 5, 3, 7]`.

### A20.3: Recursive FFT Implementation (Code)
```python
def fft_recursive(x):
    N = len(x)
    if N <= 1: return x
    even = fft_recursive(x[0::2])
    odd = fft_recursive(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]
```

---

## 21. Gaussian Elimination & LU - ANSWERS

### A21.1: Operation Count (Theoretical)
The process involves $n$ stages. In stage $k$, we eliminate $n-k$ rows. Each row requires 1 division and roughly $n-k$ multiplications. Summing $(n-k)^2$ from 1 to $n$ gives $\sum i^2 \approx n^3/3$. Back substitution is $O(n^2)$, which is negligible compared to the elimination phase.

### A21.2: Partial Pivoting Trace (Manual)
Original: `[1 1 1; 2 4 2; 4 10 2]`.
1. **Swap R1, R3** (Max in col 1 is 4): `[4 10 2; 2 4 2; 1 1 1]`.
2. **Eliminate Col 1:**
   R2 = R2 - 0.5*R1 -> `[0 -1 1]`.
   R3 = R3 - 0.25*R1 -> `[0 -1.5 0.5]`.
   (System: `[4 10 2 | 16; 0 -1 1 | 0; 0 -1.5 0.5 | -1]`).

### A21.3: Gaussian Elimination with Pivoting (Code)
```python
import numpy as np
def gaussian_elimination(A, b):
    n = len(b)
    for i in range(n):
        pivot = np.argmax(np.abs(A[i:, i])) + i
        A[[i, pivot]] = A[[pivot, i]]
        b[[i, pivot]] = b[[pivot, i]]
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    # Back substitution...
```

---

## 22. Jacobi Iterative Method - ANSWERS

### A22.1: Convergence and Diagonal Dominance (Theoretical)
Strict diagonal dominance ($|a_{ii}| > \sum_{j \neq i} |a_{ij}|$) ensures that in each iteration, the "error" from the off-diagonal terms is reduced, as they are weighted by the large diagonal element. This guarantees that the spectral radius of the iteration matrix $\rho(M)$ is less than 1.

### A22.2: Manual Jacobi Step (Manual)
1. **Iter 1:** $x_1 = 3/10 = 0.3, x_2 = 1.5/10 = 0.15, x_3 = -9/10 = -0.9$.
2. **Iter 2:**
   $x_1 = (3 - 0.15 - 2(-0.9)) / 10 = 4.65 / 10 = 0.465$.
   $x_2 = (1.5 - 0.3 + (-0.9)) / 10 = 0.3 / 10 = 0.03$.
   $x_3 = (-9 - 2(0.3) - 0.15) / 10 = -9.75 / 10 = -0.975$.

### A22.3: Jacobi Method Implementation (Code)
```python
def jacobi(A, b, x0, tol, max_iter):
    D = np.diag(A)
    R = A - np.diagflat(D)
    for _ in range(max_iter):
        x = (b - np.dot(R, x0)) / D
        if np.linalg.norm(x - x0) < tol: return x
        x0 = x
    return x
```
