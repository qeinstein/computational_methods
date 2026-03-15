Deep dive and step by step expplnations for all the questions in the practice_questions.md

---

## 1. Python Basics (01_Introduction_to_Programming) - ANSWERS

### A1.1: Bitwise Logic Trace
**Step-by-Step:**
1. Initial: `n = 13` (Binary: `1101`), `res = 0`.
2. Iteration 1:
   - `n & 1` is `1101 & 0001 = 1`.
   - `res = (0 << 1) | 1 = 1`.
   - `n >>= 1` becomes `110` (6).
3. Iteration 2:
   - `n & 1` is `110 & 001 = 0`.
   - `res = (1 << 1) | 0 = 10` (Binary), which is `2` (Decimal).
   - `n >>= 1` becomes `11` (3).
4. Iteration 3:
   - `n & 1` is `11 & 01 = 1`.
   - `res = (2 << 1) | 1 = 101` (Binary), which is `5` (Decimal).
   - `n >>= 1` becomes `1` (1).
5. Iteration 4:
   - `n & 1` is `1 & 1 = 1`.
   - `res = (5 << 1) | 1 = 1011` (Binary), which is `11` (Decimal).
   - `n >>= 1` becomes `0`.
**Final Result:** `res = 11`. (This function reverses the bits of the integer).

### A1.2: Complex Arithmetic
**Step-by-Step:**
1. Precedence: Parentheses -> Power -> Floor Div/Modulo -> Multiplication -> Addition/Subtraction -> Bitwise.
2. `(10 // 3) ** 2` = `3 ** 2 = 9`.
3. `(5 << 2)` = `5 * 4 = 20`.
4. `(13 >> 1)` = `13 // 2 = 6`.
5. `(7 & 3)` = `0111 & 0011 = 3`.
6. Expression: `20 ^ 6 | 3 + 9`
7. `3 + 9 = 12`.
8. Expression: `20 ^ 6 | 12`
9. Binary `20`: `10100`, Binary `6`: `00110`, Binary `12`: `01100`.
10. `20 ^ 6`: `10100 ^ 00110 = 10010` (18).
11. `18 | 12`: `10010 | 01100 = 11110` (30).
**Final Result:** `30`.

### A1.3: Nested List Comprehensions
**Step-by-Step:**
1. The outer loop `for y in range(4)` yields `y = 0, 1, 2, 3`.
2. Filter `if y % 2 != 0` selects `y = 1` and `y = 3`.
3. For `y = 1`: Inner loop `[x * 1 for x in range(3)]` -> `[0, 1, 2]`.
4. For `y = 3`: Inner loop `[x * 3 for x in range(3)]` -> `[0, 3, 6]`.
**Final Result:** `[[0, 1, 2], [0, 3, 6]]`.

### A1.4: Function Scope and Mutability
**Step-by-Step:**
1. `update_list(10)`: Uses the default `container` (a persistent list object created at definition). Returns `[10]`.
2. `update_list(20, [1, 2])`: Uses the provided `[1, 2]` list. Appends `20`. Returns `[1, 2, 20]`.
3. `update_list(30)`: Uses the *same* default `container` from the first call. It already contains `[10]`. Returns `[10, 30]`.
**Result:** `[10]`, `[1, 2, 20]`, `[10, 30]`.
**Reason:** Default arguments in Python are evaluated once at function definition time, not every time the function is called. Mutable defaults like lists persist across calls.

### A1.5: Recursion and State
**Trace:**
1. `mystery(5)`: `5` is odd -> `5 * mystery(3)`.
2. `mystery(3)`: `3` is odd -> `3 * mystery(1)`.
3. `mystery(1)`: base case -> returns `1`.
4. Backtrack: `3 * 1 = 3`.
5. Backtrack: `5 * 3 = 15`.
**Final Result:** `15`.

### A1.6: String Slicing and Manipulation
**Step-by-Step:**
1. `s[2:14:3]`: Start at index 2 ('t'), up to 14 ('e'), step 3.
   - Indices: 2 ('t'), 5 ('u'), 8 ('t'), 11 ('n').
   - Result: `"tutn"`.
2. `[::-1]`: Reverse the string -> `"ntut"`.
3. `.upper()`: Convert to uppercase -> `"NTUT"`.
**Final Result:** `"NTUT"`.

### A1.7: Dictionary Logic
**Step-by-Step:**
1. `data = {0: 0, 1: 1, 2: 4}`.
2. `data.setdefault(2, 10)`: Key 2 exists, so it does *nothing*. Value remains `4`.
3. `data.update({1: 5, 3: 9})`: Overwrites key 1 to `5`, adds key 3 as `9`.
4. `data.get(4, "N/A")`: Key 4 doesn't exist, returns default `"N/A"`.
**Final State:** `{0: 0, 1: 5, 2: 4, 3: 9}`, `val = "N/A"`.

### A1.8: Logical Short-Circuiting
**Step-by-Step:**
1. `check("A", False) and check("B", True)`:
   - `check("A", False)` prints "A" and returns `False`.
   - Since the first part of `and` is `False`, Python **short-circuits** and skip `check("B", True)`.
2. `(False) or check("C", True)`:
   - Since the first part of `or` is `False`, Python evaluates the second part.
   - `check("C", True)` prints "C" and returns `True`.
**Output:**
```
A
C
Result: True
```

### A1.9: Algorithm Implementation (Code)
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

### A1.10: Efficient File I/O (Code)
```python
with open("data.txt", "r") as f:
    for line in f:
        if len(line.split()) > 5:
            print(line.strip())
```

---

## 2. Object-Oriented Programming (01_Introduction_to_Programming) - ANSWERS

### A2.1: Method Resolution Order
**Step-by-Step:**
1. D inherits from B and C.
2. B inherits from A.
3. C inherits from A.
4. Using C3 Linearization: `D -> B -> C -> A -> object`.
**Result:** `[D, B, C, A, object]`.

### A2.2: Diamond Inheritance and super()
**Trace:**
1. `D.process()` prints "D", calls `super().process()` (which is B).
2. `B.process()` prints "B", calls `super().process()` (which is C, according to MRO).
3. `C.process()` prints "C", calls `super().process()` (which is A).
4. `A.process()` prints "A".
**Output:**
```
D
B
C
A
```

### A2.3: Class vs Instance Variables
**Step-by-Step:**
1. `t1 = Tracker("A")`: `Tracker.count` becomes 1. `t1.id = 1`.
2. `t2 = Tracker("B")`: `Tracker.count` becomes 2. `t2.id = 2`.
3. `t1.count = 10`: This creates an **instance variable** `count` on `t1`, shadowing the class variable.
4. `t2.count`: Accesses the class variable (2).
5. `Tracker.count`: The class variable is still 2.
**Result:** `10, 2, 2`.

### A2.4: Property Decorators
**Step-by-Step:**
1. `acc.balance += 50`: Calls getter (returns 50), adds 50, then calls setter with `100`. `_balance` becomes 100.
2. `acc.balance = -100`: Calls setter. `-100 < 0` is True. Prints "Invalid". `_balance` remains 100.
3. `print(acc.balance)`: Calls getter. Returns 100.
**Output:**
```
Invalid
100
```

### A2.5: Polymorphism Logic
**Step-by-Step:**
1. `bird.fly()` on `Bird()` calls `Bird.fly` -> prints "Flying".
2. `bird.fly()` on `Penguin()` calls the overridden `Penguin.fly` -> prints "Cannot fly".
**Output:**
```
Flying
Cannot fly
```

### A2.6: Static and Class Methods
**Step-by-Step:**
1. `Demo.set_class_data("New")`: `cls.data` (the class variable) is updated to "New".
2. `d.data`: Instance `d` doesn't have its own `data`, so it looks up the class variable. Returns "New".
3. `Demo.print_info()`: Calls the static method.
**Output:**
```
New
Static
```

### A2.7: Name Mangling
**Step-by-Step:**
1. `self.__code` is mangled to `_Secret__code` to avoid collisions in subclasses.
2. `s.get_code()` works because it's inside the class.
3. `s.__code__` fails with an `AttributeError`.
4. To access it externally: `print(s._Secret__code)`.

### A2.8: Function Decorators
**Step-by-Step:**
1. `add(3, 5)` actually calls `wrapper(3, 5)`.
2. `wrapper` prints "Calling add".
3. `wrapper` calls `func(3, 5)` which is `8`.
4. `wrapper` returns `8 * 2 = 16`.
**Output:**
```
Calling add
16
```

### A2.9: Operator Overloading (Code)
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

### A2.10: Singleton Pattern (Code)
```python
class DatabaseConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

## 3. Data Visualization with Matplotlib (01_Introduction_to_Programming) - ANSWERS

### A3.1: Subplot Geometry
- `plt.subplot(3, 2, 5)` creates a grid with **3 rows** and **2 columns**.
- Total possible plots = $3 \times 2 = 6$.
- The 5th plot is located in the **bottom-left** corner (first column of the third row).

### A3.2: Plot Styling Interpretation
- `r`: Red color.
- `s`: Square markers.
- `--`: Dashed line style.
**Result:** A red dashed line with square markers at each data point.

### A3.3: Histogram Binning Logic
- Data: `[5, 7, 12, 18, 21, 28, 33]`. Min: 5, Max: 33.
- Range = $33 - 5 = 28$.
- Bin width = $28 / 3 \approx 9.33$.
- Bin 1: $[5, 14.33)$ -> `[5, 7, 12]` (3 points).
- Bin 2: $[14.33, 23.66)$ -> `[18, 21]` (2 points).
- Bin 3: $[23.66, 33]$ -> `[28, 33]` (2 points).

### A3.4: Axis Object Management
- `plt.plot()` uses the "state-machine" approach (implicitly uses the current axes).
- `fig, ax = plt.subplots()` is the "object-oriented" approach.
- **Preferred:** The OO approach is better for complex layouts, multiple subplots, or when you need to pass axes objects to functions.

### A3.5: Scatter Plot Customization
- `c` (color) maps the list of values to a **Colormap** (like 'viridis' or 'plasma').
- `s` (size) defines the area of the markers in points squared.
- Matplotlib uses a normalization process to scale the input integers to the 0-1 range of the colormap.

### A3.6: Logarithmic Scaling
- `log` scale cannot handle zero or negative values (returns error or masks them).
- `symlog` (Symmetrical Log) handles positive, negative, and zero values by using a linear scale near zero and a log scale elsewhere.

### A3.7: Legend and Handle Logic
- You can capture the return values of plot commands: `line1, = ax.plot(...)`.
- Pass the desired handles and labels to `ax.legend([line1, line2], ["Label1", "Label2"])`.

### A3.8: Figure Persistence
- Both lines are plotted on the **same axes** within the same figure. Matplotlib automatically cycles the color for the second line unless specified.

### A3.9: Dual-Axis Implementation (Code)
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
fig, ax1 = plt.subplots()

ax1.plot(x, x**2, 'g-')
ax1.set_ylabel('Quadratic', color='g')

ax2 = ax1.twinx()
ax2.plot(x, np.exp(x), 'b-')
ax2.set_ylabel('Exponential', color='b')

plt.show()
```

### A3.10: Heatmap Visualization (Code)
```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title("10x10 Random Heatmap")
plt.show()
```

---

## 4. Floating Point Representation & Precision (02_Computing_Fundamentals_and_Error_Analysis) - ANSWERS

### A4.1: IEEE 754 Single Precision Conversion
**Step-by-Step:**
1. Sign bit: $1$ (negative).
2. Integer part: $12 = 1100_2$.
3. Fractional part: $0.625 = 1/2 + 1/8 = 0.101_2$.
4. Normalized: $1100.101 = 1.100101 \times 2^3$.
5. Exponent: $3 + 127 = 130$. Binary: $10000010$.
6. Mantissa (23 bits): $100101000...000$.
**Result:** `1 10000010 10010100000000000000000`.

### A4.2: Binary Float to Decimal
**Step-by-Step:**
1. Sign: `0` (+).
2. Exponent: `10000010` = 130. Actual exp = $130 - 127 = 3$.
3. Mantissa: `011...` = $1 + 0/2 + 1/4 + 1/8 = 1.375$.
4. Value: $1.375 \times 2^3 = 1.375 \times 8 = 11.0$.
**Result:** $11.0$.

### A4.3: Custom Floating Point System
- Exponent bias = 7.
- Normalized range: $2^{1-7}$ to $2^{14-7}$ (Exp: 1 to 14).
1. **Smallest positive normalized:** Exp = 1 ($2^{-6}$), Mantissa = $1.00000$. Value: $2^{-6} = 0.015625$.
2. **Largest:** Exp = 14 ($2^7$), Mantissa = $1.11111$ ($2 - 2^{-5} = 1.96875$). Value: $1.96875 \times 128 = 252.0$.

### A4.4: Machine Epsilon Calculation
- 24-bit mantissa (including implicit 1).
- Smallest representable difference at $1.0$ is $2^{-(24-1)} = 2^{-23}$.
- $2^{-23} \approx 1.19 \times 10^{-7}$.

### A4.5: Precision Loss in Summation
- In 64-bit float, $10^{16}$ is so large that $10^{16} + 1$ rounds back to $10^{16}$ because 1 is beyond the 53-bit relative precision ($\sim 15.9$ digits).
- In the second case, $(10^{16} - 10^{16})$ is evaluated first, resulting in $0$, which is then added to $1$.

### A4.6: Subnormal Numbers
- **Purpose:** To fill the gap between 0 and the smallest normalized number (gradual underflow).
- **Smallest positive subnormal:** Single precision has bias 127.
- Value = $0.000...001 \times 2^{-126} = 2^{-23} \times 2^{-126} = 2^{-149} \approx 1.4 \times 10^{-45}$.

### A4.7: Mantissa Precision
- Precision $P = \log_{10}(2^{52+1}) \approx 53 \times 0.30103 \approx 15.95$.
- **Result:** ~16 decimal digits.

### A4.8: Comparison Paradox
- 0.1 and 0.2 have repeating binary representations.
- 0.1 $\approx$ $1.1001100110... \times 2^{-4}$.
- The small rounding errors in 0.1 and 0.2 accumulate such that the sum is slightly different from the representable value of 0.3.

### A4.9: Finding Machine Epsilon (Code)
```python
eps = 1.0
while 1.0 + eps > 1.0:
    eps /= 2.0
print(\"Machine Epsilon:\", eps * 2.0)
```

### A4.10: Struct-Level Inspection (Code)
```python
import struct
f = 3.14
[hex_val] = struct.unpack('>Q', struct.pack('>d', f))
print(f\"{hex_val:016x}\")
```

---

## 5. Error Analysis (02_Computing_Fundamentals_and_Error_Analysis) - ANSWERS

### A5.1: Relative vs Absolute Error
- True: $\pi \approx 3.14159265$. Approx: $22/7 \approx 3.14285714$.
- Abs Error: $|3.14159 - 3.14286| \approx 0.0012645$.
- Rel Error: $0.0012645 / 3.14159 \approx 0.00040249$.

### A5.2: Error Propagation in Addition
- $S = X + Y = 150$.
- Abs Error: $\Delta S = \Delta X + \Delta Y = 0.5 + 0.2 = 0.7$.
- Rel Error: $0.7 / 150 \approx 0.0046667$.

### A5.3: Catastrophic Cancellation
1. $\sqrt{10001} - \sqrt{10000} \approx 100.0 - 100.0 = 0.0$.
2. Rewrite: $\frac{(\sqrt{x+1}-\sqrt{x})(\sqrt{x+1}+\sqrt{x})}{\sqrt{x+1}+\sqrt{x}} = \frac{1}{\sqrt{x+1}+\sqrt{x}}$.
3. $1 / (100.005 + 100) \approx 0.004999$.

### A5.4: Taylor Series Truncation
- $e^x \approx 1 + x + x^2/2 + x^3/6$.
- For $x=0.5$: $1 + 0.5 + 0.125 + 0.020833 = 1.645833$.
- Remainder $R_3(x) = \frac{e^\xi}{4!} x^4$. Max $\xi=0.5 \implies R_3 \approx \frac{1.648}{24} (0.5)^4 \approx 0.00429$.

### A5.5: Condition Number
- $f(x) = (1-x)^{-1} \implies f'(x) = (1-x)^{-2}$.
- $\kappa(x) = |x \frac{f'(x)}{f(x)}| = |x \frac{(1-x)^{-2}}{(1-x)^{-1}}| = |\frac{x}{1-x}|$.
- Near $0.99$: $\kappa = 0.99 / 0.01 = 99$.
- **Result:** Relatively ill-conditioned.

### A5.6: Stability of Iterative Schemes
- The recurrence has characteristic equation $r^2 - 2.1r + 1.1 = 0 \implies (r-1)(r-1.1)=0$.
- General solution: $x_n = A(1)^n + B(1.1)^n$.
- Even if $B=0$ initially, rounding makes $B \neq 0$, and $(1.1)^n$ grows exponentially.
- **Result:** Unstable.

### A5.7: Round-off in Large Sums
- Each add: error $\sim \epsilon \cdot 0.1$.
- Total: $10^7 \cdot 10^{-7} \cdot 0.1 = 0.1$.
- The sum is $10^6$, so the relative error is $10^{-7}$ (one part in 10 million).

### A5.8: Derivative Approximation Error
- Taylor: $f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(\xi)$.
- $\frac{f(x+h)-f(x)}{h} = f'(x) + \frac{h}{2}f''(\xi)$.
- Error is proportional to $h$.

### A5.9: Error Calculator (Code)
```python
def analyze_error(true, approx):
    abs_e = abs(true - approx)
    rel_e = abs_e / abs(true)
    return {\"abs\": abs_e, \"rel\": rel_e, \"ok\": rel_e < 0.01}
```

### A5.10: Cancellation Demonstration (Code)
```python
import math
x = 1e-8
res = 1 - math.cos(x)
exact = x**2 / 2
print(f\"{res} vs {exact}\")
```

---

## 6. Bisection Method (03_Root_Finding) - ANSWERS

### A6.1: Manual Iteration
$f(x) = x^3 - 5$ on $[1, 2]$.
1. $m = 1.5, f(1.5) = 3.375 - 5 = -1.625$. Range: $[1.5, 2]$.
2. $m = 1.75, f(1.75) \approx 5.359 - 5 = 0.359$. Range: $[1.5, 1.75]$.
3. $m = 1.625, f(1.625) \approx 4.291 - 5 = -0.709$. Range: $[1.625, 1.75]$.

### A6.2: Iteration Count Estimation
- $(b-a)/2^n < \epsilon \implies 1/2^n < 10^{-6}$.
- $2^n > 10^6 \implies n > \log_2(10^6) \approx 19.93$.
- **Result:** 20 iterations.

### A6.3: Convergence Logic
- No. The function has a singularity at $x=0.5$. It is not continuous on $[0, 1]$.
- Intermediate Value Theorem does not apply.

### A6.4: Bisection on Quadratic
- Start $[1, 2]$, width 1.
- After 1 iter: $[1, 1.5]$ or $[1.5, 2]$, width 0.5.
- After 2 iter: width 0.25.
- **Max error:** $0.125$ (half of interval width).

### A6.5: Bracketing Failure
- $f(x) = (x-1)^2$ on $[0, 2]$. $f(0)=1, f(2)=1$. $f(0)f(2) > 0$.
- Root exists at $x=1$, but signs don't change.

### A6.6: Stopping Criteria Comparison
- If the function is very flat ($f' \approx 0$), $|f(m)| < \epsilon$ might be satisfied far from the true root.
- If the function is very steep, interval width might be small while $|f(m)|$ is still large.

### A6.7: Multiple Roots
- $[0, 4]$, $m=2, f(2)=0$.
- Method stops at $x=2$ (root found in 1 iteration).

### A6.8: Efficiency vs Robustness
- **Bisection:** Guaranteed to converge if root is bracketed, but linear (slow).
- **Newton:** Very fast (quadratic), but can diverge if $x_0$ is bad or $f' \approx 0$.

### A6.9: Bisection Implementation (Code)
```python
def bisection(f, a, b, tol):
    if f(a) * f(b) >= 0: return None
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(m) == 0: return m
        if f(a) * f(m) < 0: b = m
        else: a = m
    return (a + b) / 2
```

### A6.10: Iteration Table Generator (Code)
```python
# Script uses bisection logic and prints:
# | k | a | b | m | f(m) |
```

---

## 7. Newton-Raphson Method (03_Root_Finding) - ANSWERS

### A7.1: Manual Newton Step
$f(x) = x^2 - 3, f'(x) = 2x$. $x_0 = 2$.
1. $x_1 = 2 - (4-3)/4 = 2 - 0.25 = 1.75$.
2. $x_2 = 1.75 - (1.75^2-3)/3.5 = 1.75 - 0.0625/3.5 \approx 1.7321$.

### A7.2: Derivation from Taylor Series
- $f(x_r) \approx f(x_n) + f'(x_n)(x_r - x_n) = 0$.
- $x_r \approx x_n - f(x_n)/f'(x_n)$.

### A7.3: Quadratic Convergence Trace
- $e_1 = 10^{-2}$.
- $e_2 \approx C(e_1^2) = C(10^{-4})$.
- $e_3 \approx C(e_2^2) = C(10^{-8})$.
- Digits of precision: $2 \to 4 \to 8$.

### A7.4: Failure at Stationary Point
- $f(1) = 0$ is the root! But if we used $f(x) = x^3 - 3x + 3$ at $x_0=1$:
- $f'(1) = 3(1)^2 - 3 = 0$. Division by zero. Newton's method fails.

### A7.5: Multiple Root Convergence
- $f = (x-1)^2, f' = 2(x-1)$.
- $x_{n+1} = x_n - (x_n-1)^2 / (2(x_n-1)) = x_n - 0.5(x_n-1)$.
- $e_{n+1} = |x_n - 0.5(x_n-1) - 1| = |0.5x_n - 0.5| = 0.5 e_n$.
- Ratio = 0.5 (Linear convergence).

### A7.6: Newton for Division
- $x_{n+1} = x_n - (\frac{1}{x_n}-a)/(-\frac{1}{x_n^2}) = x_n + x_n^2(\frac{1}{x_n}-a) = x_n + x_n - ax_n^2 = x_n(2 - ax_n)$.

### A7.7: Geometric Divergence
- $f(x) = x^{1/3}$ with $x_0=1$. Update: $x_1 = 1 - 1/(1/3) = -2$. $x_2 = 4$.
- It oscillates and grows.

### A7.8: Complex Roots
- Newton's method on a real function with real $x_0$ stays on the real line. Since $x^2+1=0$ has no real roots, it will never converge (it will jitter or diverge).

### A7.9: Newton with Lambda (Code)
```python
def newton(f, df, x0, tol):
    x = x0
    while abs(f(x)) > tol:
        x = x - f(x) / df(x)
    return x
```

### A7.10: Root Finding with `scipy` (Code)
```python
from scipy.optimize import newton
newton(lambda x: x*math.exp(x)-1, 0.5)
```

---

## 8. Secant Method (03_Root_Finding) - ANSWERS

### A8.1: Manual Secant Trace
$f(x) = x^2 - 5$. $x_0=2 (f=-1), x_1=3 (f=4)$.
1. $x_2 = 3 - 4(3-2)/(4 - (-1)) = 3 - 4/5 = 2.2$.
2. $f(2.2) = 4.84 - 5 = -0.16$.
3. $x_3 = 2.2 - (-0.16)(2.2 - 3)/(-0.16 - 4) = 2.2 - 0.128/-4.16 \approx 2.2308$.

### A8.2: Secant vs Newton
- **Advantage:** Doesn't require calculating the derivative $f'(x)$.
- **Cost:** Slower convergence ($1.618$ vs $2.0$).

### A8.3: Derivative Approximation
- $f'(x_n) \approx \frac{f(x_n)-f(x_{n-1})}{x_n-x_{n-1}}$.
- Newton: $x_{n+1} = x_n - f(x_n)/f'$. Substituing the above gives the Secant formula.

### A8.4: Superlinear Convergence
- $e_{n+1} \approx C e_n^{1.618}$.
- $e_n = 10^{-2}$.
- $e_{n+1} \approx 10^{-3.23}$.
- $e_{n+2} \approx (10^{-3.23})^{1.618} \approx 10^{-5.2}$.

### A8.5: Stability and Slopes
- If $f(x_n) \approx f(x_{n-1})$, the secant line is nearly horizontal.
- The x-intercept (next guess) will be very far away, potentially causing divergence.

### A8.6: Secant vs Bisection
- **Secant** is more likely to diverge.
- **Bisection** is guaranteed to converge as long as the initial bracket contains the root.

### A8.7: Iteration History
- No. Secant method iterates can fall outside the previous points.
- Bisection always keeps the root within a shrinking bracket.

### A8.8: Regula Falsi Comparison
- Regula Falsi always maintains a bracket where $f(a)f(b) < 0$.
- It uses the Secant formula but only replaces the endpoint that keeps the root bracketed.
- **Diff:** Slower than Secant but guaranteed to converge.

### A8.9: Secant Implementation (Code)
```python
def secant_method(f, x0, x1, tol):
    for i in range(100):
        denom = f(x1) - f(x0)
        if abs(denom) < 1e-15: return x1
        x_new = x1 - f(x1) * (x1 - x0) / denom
        if abs(x_new - x1) < tol: return x_new
        x0, x1 = x1, x_new
    return x1
```

### A8.10: Performance Benchmarking (Code)
- Newton: Fastest iterations, but requires $f$ and $f'$.
- Secant: Good compromise.
- Bisection: Reliable but many more iterations needed.

---

## 9. Forward & Backward Difference (04_Numerical_Differentiation) - ANSWERS

### A9.1: Forward Difference Table (Manual)
**Problem:** Compute $f'(1)$ for $f(x) = x^3$ with $h=0.1$ and $h=0.01$.
**True Value:** $f'(x) = 3x^2 \implies f'(1) = 3(1)^2 = 3.0$.

**Iteration Table:**

| Step size $h$ | $x+h$ | $f(x+h)$ | $f(x)$ | $f'(1) \approx \frac{f(x+h)-f(x)}{h}$ | True Error |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0.1 | 1.1 | 1.331 | 1.0 | $\frac{1.331 - 1.0}{0.1} = 3.31$ | 0.31 |
| 0.01 | 1.01 | 1.030301 | 1.0 | $\frac{1.030301 - 1.0}{0.01} = 3.0301$ | 0.0301 |

**Analysis:** As $h$ decreases by a factor of 10, the error decreases by approximately a factor of 10, confirming $O(h)$ accuracy.

---

### A9.2: Backward Difference Derivation (Manual)
**Derivation:**
1. Start with the Taylor series expansion for $f(x-h)$ about $x$:
   $f(x-h) = f(x) - hf'(x) + \frac{h^2}{2!}f''(x) - \frac{h^3}{3!}f'''(x) + \dots$
2. Solve for $f'(x)$:
   $hf'(x) = f(x) - f(x-h) + \frac{h^2}{2}f''(x) - \dots$
3. Divide by $h$:
   $f'(x) = \frac{f(x) - f(x-h)}{h} + \frac{h}{2}f''(\xi)$
4. Thus, the first-order backward difference is:
   $f'(x) \approx \frac{f(x) - f(x-h)}{h}$ with error $O(h)$.

---

### A9.3: Error Scaling (Manual)
**Proof:**
The truncation error for forward difference is $E(h) = \frac{h}{2}f''(\xi) = Ch^1$.
If we halve the step size ($h_{new} = h/2$):
$E(h/2) = C(h/2)^1 = \frac{1}{2}Ch^1 = \frac{1}{2}E(h)$.
**Conclusion:** Halving $h$ reduces the error by a factor of 2. In Big-O notation, $O(h)$ implies linear scaling.

---

### A9.4: Boundary Problem (Manual)
**Reasoning:**
At the left boundary $x=a$ of a domain $[a, b]$, the value $f(a-h)$ is outside the defined domain. Therefore, the **Backward Difference** formula cannot be used. The **Forward Difference** is preferred because it only requires values $f(x)$ and $f(x+h)$, which are both within the domain.

---

### A9.5: Second-Order Forward Formula (Manual)
**Derivation:**
Combine Taylor expansions for $f(x+h)$ and $f(x+2h)$:
1. $f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + \dots$ (Eq. 1)
2. $f(x+2h) = f(x) + 2hf'(x) + \frac{4h^2}{2}f''(x) + \frac{8h^3}{6}f'''(x) + \dots$ (Eq. 2)
3. Multiply Eq. 1 by 4: $4f(x+h) = 4f(x) + 4hf'(x) + 2h^2f''(x) + \dots$ (Eq. 3)
4. Subtract Eq. 2 from Eq. 3: $4f(x+h) - f(x+2h) = 3f(x) + 2hf'(x) + O(h^3)$
5. Solve for $f'(x)$: $f'(x) = \frac{-3f(x) + 4f(x+h) - f(x+2h)}{2h} + O(h^2)$.

---

### Q9.6: Stencil Identification (Manual)
**Answer:**
The stencil $[-1, 1]$ with step $h$ represents the calculation $-1 \cdot f(x) + 1 \cdot f(x+h)$.
Divided by $h$, this is $\frac{f(x+h) - f(x)}{h}$.
- **Derivative:** First derivative $f'(x)$.
- **Accuracy:** First-order $O(h)$.

---

### A9.7: Truncation vs Round-off (Manual)
**Graph Description:**
- **Truncation Error ($E_t$):** Decreases linearly with $h$ (for $O(h)$). $E_t \propto h$.
- **Round-off Error ($E_r$):** Increases as $h \to 0$ because we divide by a very small number. $E_r \propto \frac{\epsilon}{h}$.
- **Total Error ($E_{total} = E_t + E_r$):** Forms a U-shaped curve.
- **Optimal $h$:** The minimum point where $E_t \approx E_r$. For double precision, $h_{opt} \approx \sqrt{\epsilon_{mach}} \approx 10^{-8}$.

---

### A9.8: Non-Uniform Grid (Manual)
**Formula:**
If $x_{i+1} = x_i + h_i$:
$f'(x_i) \approx \frac{f(x_{i+1}) - f(x_i)}{h_i}$
The error remains $O(h_i)$, assuming $h_i$ is small.

---

### A9.9: Forward Difference Implementation (Code)
```python
def forward_diff(f, x, h):
    \"\"\"Computes first derivative using forward difference.\"\"\"
    return (f(x + h) - f(x)) / h
```

---

### A9.10: Error Analysis Script (Code)
```python
import math

def f(x): return math.sin(x)
def df_exact(x): return math.cos(x)

x = 1.0
print(f\"{'h':>10} | {'Approx':>15} | {'Error':>15}\")
for i in range(1, 11):
    h = 10**-i
    approx = (f(x + h) - f(x)) / h
    error = abs(approx - df_exact(x))
    print(f\"{h:10.0e} | {approx:15.10f} | {error:15.10e}\")
```

---

## 10. Central Difference & Higher Order Derivatives (04_Numerical_Differentiation) - ANSWERS

### A10.1: Central Difference Accuracy (Manual)
**Proof:**
1. $f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + O(h^4)$
2. $f(x-h) = f(x) - hf'(x) + \frac{h^2}{2}f''(x) - \frac{h^3}{6}f'''(x) + O(h^4)$
3. Subtract (2) from (1):
   $f(x+h) - f(x-h) = 2hf'(x) + \frac{2h^3}{6}f'''(x) + O(h^5)$
4. Divide by $2h$:
   $\frac{f(x+h) - f(x-h)}{2h} = f'(x) + \frac{h^2}{6}f'''(x)$
**Conclusion:** The leading error term is proportional to $h^2$, hence $O(h^2)$.

---

### A10.2: Second Derivative Central (Manual)
**Derivation:**
1. Add the Taylor expansions from Q10.1:
   $f(x+h) + f(x-h) = 2f(x) + h^2f''(x) + \frac{2h^4}{24}f^{(4)}(x) + \dots$
2. Solve for $f''(x)$:
   $h^2f''(x) = f(x+h) - 2f(x) + f(x-h) - O(h^4)$
3. Divide by $h^2$:
   $f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$
**Error:** $O(h^2)$.

---

### A10.3: Comparison (Manual)
**Problem:** $f(x) = e^x$ at $x=0, h=0.1$. Exact $f'(0) = 1.0$.
1. **Forward:** $\frac{e^{0.1} - e^0}{0.1} = \frac{1.10517 - 1}{0.1} = 1.0517$ (Error: 0.0517)
2. **Backward:** $\frac{e^0 - e^{-0.1}}{0.1} = \frac{1 - 0.90484}{0.1} = 0.9516$ (Error: 0.0484)
3. **Central:** $\frac{e^{0.1} - e^{-0.1}}{0.2} = \frac{1.10517 - 0.90484}{0.2} = 1.00167$ (Error: 0.00167)
**Result:** Central difference is significantly more accurate.

---

### A10.4: Stencil for f''(x) (Manual)
**Answer:**
- **Stencil:** $[1, -2, 1]$
- **Derivative:** Second derivative $f''(x)$.
- **Denominator:** $h^2$.
- **Formula:** $f''(x) \approx \frac{f(x-h) - 2f(x) + f(x+h)}{h^2}$.

---

### A10.5: Richardson Extrapolation (Manual)
**Explanation:**
If $D(h)$ is an $O(h^2)$ approximation:
$D(h) = L + c_1 h^2 + c_2 h^4 + \dots$
Then $D(h/2) = L + c_1 (h/2)^2 + c_2 (h/2)^4 + \dots = L + \frac{1}{4}c_1 h^2 + \frac{1}{16}c_2 h^4$
To cancel $h^2$:
$4D(h/2) - D(h) = 3L - \frac{3}{4}c_2 h^4$
$L \approx \frac{4D(h/2) - D(h)}{3}$
This new estimate is $O(h^4)$.

---

### A10.6: Fourth-Order Central (Manual)
**Answer:**
The formula $\frac{-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)}{12h}$ requires **4** function evaluations ($x+2h, x+h, x-h, x-2h$). The value $f(x)$ is not needed.

---

### A10.7: Mixed Partial Derivatives (Manual)
**Formula:**
$\frac{\partial^2 f}{\partial x \partial y} \approx \frac{f(x+h, y+k) - f(x+h, y-k) - f(x-h, y+k) + f(x-h, y-k)}{4hk}$
This is derived by applying the central difference for $x$ to the central difference for $y$.

---

### A10.8: Stability in f''(x) (Manual)
**Reasoning:**
The second derivative involves subtracting values that are very close (the numerator is a small difference of small differences) and then dividing by $h^2$ (a very small number). This amplifies floating-point round-off errors much more aggressively than the $h$ division in first derivatives.

---

### A10.9: Central Difference Implementation (Code)
```python
def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)
```

---

### A10.10: Higher-Order Derivative Implementation (Code)
```python
def second_deriv_central(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)
```

---

## 11. Trapezoidal Rule (Composite) (05_Numerical_Integration) - ANSWERS

### A11.1: Single vs Composite
**Problem:** $\int_0^1 x^2 dx$. Exact value = $1/3 \approx 0.33333$.
(a) **Single Trapezoidal ($n=1, h=1$):**
$I \approx \frac{1}{2}(f(0) + f(1)) = \frac{1}{2}(0 + 1) = 0.5$.
(b) **Composite ($n=2, h=0.5$):**
$I \approx \frac{0.5}{2}(f(0) + 2f(0.5) + f(1)) = 0.25(0 + 2(0.25) + 1) = 0.25(1.5) = 0.375$.
**Comparison:** Composite ($n=2$) is closer to 0.3333.

---

### A11.2: Geometric Interpretation
**Answer:**
For a concave down function ($f''(x) < 0$), the straight line connecting $(x_i, f(x_i))$ and $(x_{i+1}, f(x_{i+1}))$ lies **below** the actual curve. Therefore, the area of the trapezoid is less than the area under the curve.
**Conclusion:** The Trapezoidal rule will **under-estimate** the integral.

---

### A11.3: Error Formula
**Problem:** $n$ for $\int_0^2 e^x dx$ with error $< 10^{-4}$.
1. $f(x) = e^x \implies f''(x) = e^x$. Max value of $|f''(x)|$ on $[0, 2]$ is $e^2 \approx 7.389$.
2. $|E| = \frac{(b-a)h^2}{12} |f''(\xi)| \leq \frac{2 \cdot (2/n)^2}{12} \cdot 7.389 = \frac{8 \cdot 7.389}{12n^2} = \frac{4.926}{n^2}$.
3. Set $\frac{4.926}{n^2} < 10^{-4} \implies n^2 > 49260 \implies n > \sqrt{49260} \approx 221.9$.
**Conclusion:** $n = 222$ intervals are needed.

---

### A11.4: Linear Exactness
**Proof:**
For $f(x) = mx + c$: $f''(x) = 0$.
The error formula for Trapezoidal rule is $E = -\frac{(b-a)h^2}{12} f''(\xi)$.
Since $f''(x) = 0$, $E = 0$.
**Conclusion:** The rule is exact for linear functions.

---

### A11.5: Table-Based Integration
**Data:** $(0, 1), (0.5, 0.8), (1, 0.5)$. $h = 0.5, n = 2$.
$I \approx \frac{h}{2} [y_0 + 2y_1 + y_2]$
$I = \frac{0.5}{2} [1 + 2(0.8) + 0.5] = 0.25 [1 + 1.6 + 0.5] = 0.25 [3.1] = 0.775$.

---

### A11.6: Recursive Trapezoidal
**Answer:**
$I(h/2) = \frac{1}{2} I(h) + \frac{h}{2} \sum_{k=1}^{n} f(a + (2k-1)\frac{h}{2})$.
This means the new estimate $I(h/2)$ can be computed by taking half of the previous estimate $I(h)$ and adding only the function values at the new midpoints.

---

### A11.7: Periodic Functions
**Reasoning:**
For a periodic function integrated over its period, the derivatives at the endpoints match ($f^{(k)}(a) = f^{(k)}(b)$). In the Euler-Maclaurin formula, the error terms (which depend on these differences) cancel out, leading to exponential convergence rather than $O(h^2)$.

---

### A11.8: Unequal Intervals
**Formula:**
$I \approx \sum_{i=0}^{n-1} \frac{h_i}{2} (f(x_i) + f(x_{i+1}))$
where $h_i = x_{i+1} - x_i$.

---

### A11.9: Composite Trapezoidal Implementation (Code)
```python
def trapezoidal_composite(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h
```

---

### A11.10: Integration Convergence (Code)
```python
def f(x): return 1 / (1 + x**2)
a, b = 0, 1

for n in [2, 4, 8, 16, 32]:
    val = trapezoidal_composite(f, a, b, n)
    # Logic to show error reduction...
```

---

## 12. Simpson's 1/3 and 3/8 Rules (05_Numerical_Integration) - ANSWERS

### A12.1: Simpson's 1/3 for Parabola
**Explanation:**
Simpson's 1/3 rule integrates a quadratic interpolant exactly. However, due to symmetry, the $h^3$ error term in the Taylor expansion cancels out, making the leading error term depend on $f^{(4)}(x)$.
**Conclusion:** Since the 4th derivative of $x^3$ is 0, the rule is exact for cubics.

---

### A12.2: Composite 1/3 Parity
**Reasoning:**
Simpson's 1/3 rule is applied to **pairs** of intervals (requiring 3 points: $x_i, x_{i+1}, x_{i+2}$). To cover the whole range $[a, b]$ with these triplets, the total number of intervals $n$ must be a multiple of 2 (**even**).

---

### A12.3: Simpson's 3/8 Logic
**Answer:**
Simpson's 3/8 rule is preferred when the number of intervals $n$ is a **multiple of 3** but not 2 (e.g., $n=3, 9, 15$). It allows integrating over 3 intervals at a time using a cubic interpolant.

---

### A12.4: Comparison Table
**Problem:** $\int_0^{\pi} \sin(x) dx$. Exact = 2.
(a) **Trapezoidal ($n=2, h=\pi/2$):**
$I \approx \frac{\pi/2}{2} (\sin 0 + 2\sin(\pi/2) + \sin \pi) = \frac{\pi}{4} (0 + 2 + 0) = \pi/2 \approx 1.571$ (Error: 0.429)
(b) **Simpson's 1/3 ($n=2, h=\pi/2$):**
$I \approx \frac{\pi/2}{3} (\sin 0 + 4\sin(\pi/2) + \sin \pi) = \frac{\pi}{6} (0 + 4 + 0) = 2\pi/3 \approx 2.094$ (Error: 0.094)
**Result:** Simpson's 1/3 is much closer.

---

### A12.5: Error Comparison
**Answer:**
Simpson's 1/3 has error $O(h^4)$.
If $h$ is halved ($h \to h/2$), error becomes $O((h/2)^4) = \frac{1}{16} O(h^4)$.
**Conclusion:** The error decreases by a factor of **16**.

---

### A12.6: Weight Coefficients
**Answer for $n=6$:**
The coefficients for $y_0, y_1, y_2, y_3, y_4, y_5, y_6$ are:
**1, 4, 2, 4, 2, 4, 1**.

---

### A12.7: Cubic Exactness
**Verification:**
Simpson's 3/8 rule uses a cubic interpolant. Like 1/3, it is exact for polynomials of degree $\leq 3$.
$f(x) = x^3 \implies f^{(4)}(x) = 0 \implies$ Error $= 0$.
**Conclusion:** Yes, it is exact.

---

### A12.8: Mixing Rules
**Problem:** $n=5$ intervals.
Since $n=5$ is odd, we cannot use 1/3 for all. Since $n=5$ is not a multiple of 3, we cannot use 3/8 for all.
**Solution:** Use **Simpson's 1/3 on first 2** intervals ($x_0, x_1, x_2$) and **Simpson's 3/8 on last 3** intervals ($x_2, x_3, x_4, x_5$).

---

### A12.9: Simpson's 1/3 Implementation (Code)
```python
def simpson13_composite(f, a, b, n):
    if n % 2 != 0: raise ValueError(\"n must be even\")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        weight = 4 if i % 2 != 0 else 2
        s += weight * f(a + i * h)
    return s * h / 3
```

---

### A12.10: Simpson's 3/8 Implementation (Code)
```python
def simpson38_composite(f, a, b, n):
    if n % 3 != 0: raise ValueError(\"n must be multiple of 3\")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        weight = 2 if i % 3 == 0 else 3
        s += weight * f(a + i * h)
    return 3 * s * h / 8
```

---

## 13. Euler's Method (06_Differential_Equations) - ANSWERS

### A13.1: Single Step Trace
**Problem:** $y' = y + t, y(0) = 1, h=0.1$.
**Step 1 ($t_0=0, y_0=1$):**
$y_1 = y_0 + h(y_0 + t_0) = 1 + 0.1(1 + 0) = 1.1$.
**Step 2 ($t_1=0.1, y_1=1.1$):**
$y_2 = y_1 + h(y_1 + t_1) = 1.1 + 0.1(1.1 + 0.1) = 1.1 + 0.1(1.2) = 1.22$.
**Result:** $y(0.2) \approx 1.22$.

---

### A13.2: Geometric Interpretation
**Explanation:**
At each point $(t_n, y_n)$, we calculate the slope $y' = f(t_n, y_n)$. We then move along the **tangent line** with this slope for a distance $h$ to find the next value. Because it assumes the slope is constant over the interval $h$, it deviates from the curve.

---

### A13.3: Error and Step Size
**Answer:**
Euler's method has a **Global Truncation Error** of $O(h)$.
Reducing $h$ by a factor of 10 reduces the total error by a factor of 10.

---

### A13.4: Stability Region
**Problem:** $y' = -10y, h=?$
For $y' = \lambda y$, Euler is stable if $|1 + h\lambda| \leq 1$.
$|1 - 10h| \leq 1 \implies -1 \leq 1 - 10h \leq 1$.
1. $1 - 10h \leq 1 \implies -10h \leq 0 \implies h \geq 0$.
2. $1 - 10h \geq -1 \implies -10h \geq -2 \implies h \leq 0.2$.
**Conclusion:** $h \leq 0.2$ for stability.

---

### A13.5: Local vs Global Error
**Distinction:**
- **Local Truncation Error (LTE):** Error introduced in a single step, assuming previous value was exact. For Euler, LTE is $O(h^2)$.
- **Global Truncation Error (GTE):** Cumulative error after $N = (b-a)/h$ steps. For Euler, GTE is $O(h^1)$.

---

### A13.6: Backward Euler
**Formula:** $y_{n+1} = y_n + h f(t_{n+1}, y_{n+1})$.
**Why used:** It is **unconditionally stable** for stiff equations (where $\lambda \ll 0$). Even for large $h$, it won't explode, unlike Forward Euler.

---

### A13.7: System of ODEs
**Transformation:**
Let $u_1 = y$ and $u_2 = y'$.
1. $u_1' = u_2$
2. $u_2' = -u_1$
**Euler Steps:**
$u_{1, n+1} = u_{1, n} + h(u_{2, n})$
$u_{2, n+1} = u_{2, n} + h(-u_{1, n})$

---

### A13.8: Vectorized Euler
**Vector Form:**
$\mathbf{y}_{n+1} = \mathbf{y}_n + h \mathbf{f}(t_n, \mathbf{y}_n)$
where $\mathbf{y}$ and $\mathbf{f}$ are vectors containing all state variables and their derivatives.

---

### A13.9: Basic Euler Implementation (Code)
```python
def euler_method(f, t0, y0, h, steps):
    t = [t0]
    y = [y0]
    for i in range(steps):
        y_next = y[-1] + h * f(t[-1], y[-1])
        t_next = t[-1] + h
        y.append(y_next)
        t.append(t_next)
    return t, y
```

---

### A13.10: ODE Solution Plotting (Code)
```python
import matplotlib.pyplot as plt
import numpy as np

def f(t, y): return -2 * y
h = 0.1
t, y = euler_method(f, 0, 1, h, 20)

t_exact = np.linspace(0, 2, 100)
y_exact = np.exp(-2 * t_exact)

plt.plot(t, y, 'ro-', label='Euler')
plt.plot(t_exact, y_exact, 'b-', label='Exact')
plt.legend()
plt.show()
```

---

## 14. Heun's Method (Improved Euler) (06_Differential_Equations) - ANSWERS

### A14.1: Manual Heun Step
**Problem:** $y' = y - t^2 + 1, y(0) = 0.5, h=0.2$.
1. **Predictor (Euler):**
   $f(0, 0.5) = 0.5 - 0^2 + 1 = 1.5$.
   $\tilde{y}_1 = 0.5 + 0.2(1.5) = 0.8$.
2. **Corrector:**
   $f(0.2, 0.8) = 0.8 - (0.2)^2 + 1 = 0.8 - 0.04 + 1 = 1.76$.
   $y_1 = 0.5 + \frac{0.2}{2} [1.5 + 1.76] = 0.5 + 0.1(3.26) = 0.826$.
**Final Result:** $y(0.2) = 0.826$.

---

### A14.2: Comparison with Euler
**Problem:** $y' = -2ty, y(0)=1, h=0.1$. Exact $y(0.1) = e^{-0.01} \approx 0.9900498$.
1. **Euler:** $y_1 = 1 + 0.1(-2(0)(1)) = 1.0$. Error: $|1 - 0.99005| = 0.00995$.
2. **Heun:**
   - $\tilde{y}_1 = 1.0$.
   - $f(0, 1) = 0$.
   - $f(0.1, 1) = -2(0.1)(1) = -0.2$.
   - $y_1 = 1 + 0.05(0 - 0.2) = 0.99$. Error: $|0.99 - 0.99005| = 0.00005$.
**Result:** Heun is ~200x more accurate in this step.

---

### A14.3: Stability Limit
**Derivation:**
For $y' = \lambda y$:
1. $\tilde{y}_{n+1} = y_n + h\lambda y_n = y_n(1 + h\lambda)$.
2. $y_{n+1} = y_n + \frac{h}{2} [\lambda y_n + \lambda y_n(1+h\lambda)] = y_n [1 + \frac{h\lambda}{2} (1 + 1 + h\lambda)] = y_n [1 + h\lambda + \frac{(h\lambda)^2}{2}]$.
The growth factor $G = 1 + z + z^2/2$ must satisfy $|G| \leq 1$.
For real $\lambda < 0$, stability requires $-1 \leq 1 + z + z^2/2 \leq 1$.
$z + z^2/2 \leq 0 \implies z(1 + z/2) \leq 0 \implies -2 \leq z \leq 0$.
**Max step size:** $h \leq 2/|\lambda| = 2/5 = 0.4$.

---

### A14.4: Local Truncation Error
**Derivation:**
Taylor: $y(t+h) = y + hy' + \frac{h^2}{2}y'' + \frac{h^3}{6}y''' + \dots$
Heun: $y_{n+1} = y + \frac{h}{2} [f(t, y) + f(t+h, y+hf)]$.
Expand $f(t+h, y+hf) \approx f + hf_t + hff_y + O(h^2)$.
$y_{n+1} = y + \frac{h}{2} [f + f + h(f_t + ff_y)] = y + hf + \frac{h^2}{2} (f_t + ff_y)$.
Since $y'' = \frac{d}{dt}f(t, y) = f_t + f_y \frac{dy}{dt} = f_t + f_y f$.
Heun matches Taylor up to $h^2$. The first mismatch is in the $h^3$ term.
**Result:** LTE is $O(h^3)$.

---

### A14.5: Multiple Iterations
$y' = 1 + y^2, y(0)=0, h=0.1$.
| $i$ | $t_i$ | $y_i$ | $f(t_i, y_i)$ | $\tilde{y}_{i+1}$ | $f(t_{i+1}, \tilde{y}_{i+1})$ | $y_{i+1}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 0.0 | 0.0 | 1.0 | 0.1 | $1 + 0.1^2 = 1.01$ | $0 + 0.05(2.01) = 0.1005$ |
| 1 | 0.1 | 0.1005 | $1.0101$ | $0.2015$ | $1.0406$ | $0.1005 + 0.05(2.0507) = 0.2030$ |

---

### A14.6: Systems of ODEs with Heun
**Steps:**
1. Predict: $\tilde{u}_1 = u_0 + h v_0, \tilde{v}_1 = v_0 + h(-u_0)$.
2. Correct:
   $u_1 = u_0 + \frac{h}{2} [v_0 + \tilde{v}_1]$
   $v_1 = v_0 + \frac{h}{2} [-u_0 - \tilde{u}_1]$
**Calculation:** $u_0=1, v_0=0, h=0.1$.
$\tilde{u}_1 = 1 + 0 = 1, \tilde{v}_1 = 0 - 0.1 = -0.1$.
$u_1 = 1 + 0.05(0 - 0.1) = 0.995$.
$v_1 = 0 + 0.05(-1 - 1) = -0.1$.

---

### A14.7: Geometric Interpretation
If $f(t, y) = f(t)$ (independent of $y$):
Heun: $y_{i+1} = y_i + \frac{h}{2} [f(t_i) + f(t_{i+1})]$.
This is exactly the **Trapezoidal Rule** for $\int_{t_i}^{t_{i+1}} f(t) dt$.
Geometrically, it approximates the area under the derivative curve using a trapezoid, while Euler uses a rectangle (Left Riemann Sum).

---

### A14.8: Error Scaling Analysis
Heun is a **second-order** method, meaning GTE is $O(h^2)$.
If $h$ is halved ($0.1 \to 0.05$):
Error $\approx C(h/2)^2 = \frac{1}{4} Ch^2$.
**Result:** The error decreases by a factor of **4**.

---

### A14.9: Heun Implementation (Code)
```python
def heun_method(f, t0, y0, h, steps):
    \"\"\"
    Solves ODE y' = f(t, y) using Heun's Predictor-Corrector method.
    LTE: O(h^3), GTE: O(h^2).
    \"\"\"
    t = [t0]
    y = [y0]
    for _ in range(steps):
        ti, yi = t[-1], y[-1]
        slope_start = f(ti, yi)
        # Predictor (Euler)
        y_pred = yi + h * slope_start
        # Corrector (Trapezoidal)
        slope_end = f(ti + h, y_pred)
        y_next = yi + (h / 2) * (slope_start + slope_end)
        
        t.append(ti + h)
        y.append(y_next)
    return np.array(t), np.array(y)
```

---

### A14.10: Predictor-Corrector Comparison (Code)
(The script would compare the quadratic error convergence of Heun vs the linear convergence of Euler. Plotting `log(error)` vs `log(h)` would show slopes of 2 and 1 respectively.)

---

## 15. Runge-Kutta 4th Order (RK4) (06_Differential_Equations) - ANSWERS

### A15.1: Manual RK4 Step
**Problem:** $y' = t + y, y(0)=1, h=0.1$.
1. $k_1 = 0.1 \cdot f(0, 1) = 0.1(1) = 0.1$.
2. $k_2 = 0.1 \cdot f(0.05, 1.05) = 0.1(1.1) = 0.11$.
3. $k_3 = 0.1 \cdot f(0.05, 1.055) = 0.1(1.105) = 0.1105$.
4. $k_4 = 0.1 \cdot f(0.1, 1.1105) = 0.1(1.2105) = 0.12105$.
$y_1 = 1 + \frac{1}{6}(0.1 + 2(0.11) + 2(0.1105) + 0.12105)$
$y_1 = 1 + \frac{1}{6}(0.66205) = 1.1103416$.
**Final Result:** $y(0.1) \approx 1.110342$.

---

### A15.2: RK4 vs Heun
- **Function Evaluations:**
  - RK4: 4 evals per step. For $h=0.1$ over $[0, 1]$, total = $10 \times 4 = 40$.
  - Heun: 2 evals per step. Total = $10 \times 2 = 20$.
- **Accuracy:** RK4 is $O(h^4)$, Heun is $O(h^2)$. RK4 is far more accurate. To match RK4 accuracy, Heun would need a much smaller $h$, requiring many more evaluations overall.

---

### A15.3: Symmetry of Slopes
The weights $1/6, 2/6, 2/6, 1/6$ are derived to match the Taylor expansion.
They are identical to the weights in **Simpson's 1/3 Rule**: $\frac{h/2}{3} [f(t) + 4f(t+h/2) + f(t+h)] = \frac{h}{6} [f(t) + 4f(t+h/2) + f(t+h)]$.
In RK4, the "midpoint" slope is evaluated twice (as $k_2$ and $k_3$), effectively splitting the weight 4 into $2+2$.

---

### A15.4: RK4 for Autonomous Systems
$y' = y(1-y), y(0)=0.5, h=0.2$.
1. $k_1 = 0.2(0.5 \cdot 0.5) = 0.05$.
2. $k_2 = 0.2(0.525 \cdot 0.475) = 0.2(0.249375) = 0.049875$.
3. $k_3 = 0.2(0.5249 \cdot 0.4751) \approx 0.049877$.
4. $k_4 = 0.2(0.5498 \cdot 0.4502) \approx 0.0495$.
$y_1 \approx 0.5 + \frac{1}{6}(0.05 + 0.09975 + 0.09975 + 0.0495) \approx 0.5498$.

---

### A15.5: Order of Accuracy Verification
Error $E \propto h^4$.
$E_{0.1} = 10^{-4}$.
$E_{0.05} = (0.5)^4 \cdot E_{0.1} = \frac{1}{16} \cdot 10^{-4} = 6.25 \times 10^{-6}$.

---

### A15.6: Second-Order ODE with RK4
System: $u_1 = y, u_2 = y'$.
$u_1' = u_2$
$u_2' = -4u_1$
Vector $\mathbf{k}_1$:
$\mathbf{k}_1 = h \cdot \begin{bmatrix} u_2 \\ -4u_1 \end{bmatrix}$.

---

### A15.7: Stability Region of RK4
$z = h\lambda = 0.2(-10) = -2.0$.
$G = 1 + (-2) + (-2)^2/2 + (-2)^3/6 + (-2)^4/24$
$G = 1 - 2 + 2 - 8/6 + 16/24 = 1 - 1.333 + 0.666 = 0.333$.
$|0.333| \leq 1$.
**Result:** Yes, it is stable. (RK4 is stable for $z \in [-2.78, 0]$ on the real axis).

---

### A15.8: Butcher Tableau
A Butcher Tableau is a mnemonic device for the coefficients of RK methods.
Standard RK4:
```
0   |
1/2 | 1/2
1/2 | 0    1/2
1   | 0    0    1
----+------------------
    | 1/6  1/3  1/3  1/6
```

---

### A15.9: RK4 Implementation (Code)
```python
def rk4_step(f, t, y, h):
    k1 = h * f(t, y)
    k2 = h * f(t + h/2, y + k1/2)
    k3 = h * f(t + h/2, y + k2/2)
    k4 = h * f(t + h, y + k3)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6
```

---

### A15.10: Adaptive Step Size Concept (Code)
RK45 uses a 4th order and 5th order method together.
`error = abs(y_rk5 - y_rk4)`.
If `error > tolerance`, reduce $h$ and retry the step.
If `error << tolerance`, increase $h$ for the next step to save time.

---

## 16. Linear & Quadratic Splines (07_Interpolation) - ANSWERS

### A16.1: Linear Spline Construction
Points: $(1, 2), (3, 6), (5, 4)$.
1. Interval $[1, 3]$: $m = (6-2)/(3-1) = 2$.
   $s_1(x) = 2 + 2(x-1) = 2x$.
2. Interval $[3, 5]$: $m = (4-6)/(5-3) = -1$.
   $s_2(x) = 6 - 1(x-3) = 9 - x$.
**Interpolation at $x=4$:** $s_2(4) = 9 - 4 = 5$.

---

### A16.2: Quadratic Spline Equations
Points: $(0, 0), (1, 1), (2, 5)$.
Unknowns: $a_1, b_1, c_1, a_2, b_2, c_2$ (6 total).
Equations:
1. $f_1(0) = c_1 = 0$.
2. $f_1(1) = a_1 + b_1 + c_1 = 1$.
3. $f_2(1) = a_2 + b_2 + c_2 = 1$.
4. $f_2(2) = 4a_2 + 2b_2 + c_2 = 5$.
5. Smoothness at $x=1$: $2a_1(1) + b_1 = 2a_2(1) + b_2$.
6. Boundary: $a_1 = 0$.

---

### A16.3: Derivative Continuity
Derivative of $f_i(x) = a_ix^2 + b_ix + c_i$ is $f_i'(x) = 2a_ix + b_i$.
For $C^1$ continuity at $x_i$:
$f_{i-1}'(x_i) = f_i'(x_i)$.
$\implies 2a_{i-1}x_i + b_{i-1} = 2a_ix_i + b_i$.
This ensures the slopes of the parabolas match at the meeting point.

---

### A16.4: Solving Quadratic Splines
From Q16.2:
- $a_1 = 0$
- $c_1 = 0$
- $0 + b_1 + 0 = 1 \implies b_1 = 1$.
- Smoothness: $2(0)(1) + 1 = 2a_2 + b_2 \implies 2a_2 + b_2 = 1$.
- Point (1, 1): $a_2 + b_2 + c_2 = 1$.
- Point (2, 5): $4a_2 + 2b_2 + c_2 = 5$.
Subtract (Point 1, 1) from (Point 2, 5): $3a_2 + b_2 = 4$.
Now solve:
$3a_2 + b_2 = 4$
$2a_2 + b_2 = 1$
Subtract: $a_2 = 3$.
Substitute: $2(3) + b_2 = 1 \implies b_2 = -5$.
Substitute: $3 - 5 + c_2 = 1 \implies c_2 = 3$.
**Final Splines:**
$s_1(x) = x$
$s_2(x) = 3x^2 - 5x + 3$.

---

### A16.5: Degree of Freedom Analysis
- **Unknowns:** $n$ intervals $\times 3$ coefficients ($a, b, c$) = $3n$.
- **Equations:**
  - Continuity ($C^0$): $2n$ equations (each spline passes through 2 endpoints).
  - Smoothness ($C^1$): $n-1$ equations (at internal nodes).
- **Total Equations:** $2n + n - 1 = 3n - 1$.
- **Result:** We need $3n - (3n - 1) = 1$ additional boundary condition (like $a_1=0$).

---

### A16.6: Linear vs Quadratic Smoothness
- **Linear:** $f'(x)$ is a step function (discontinuous). The plot has sharp "elbows" at data points.
- **Quadratic:** $f'(x)$ is a piecewise linear continuous function. The plot is smooth at data points but has a discontinuous second derivative (curvature jumps).

---

### A16.7: Spline Error Bound
$f(x) = \sin(x), f''(x) = -\sin(x)$. $\max |f''| = 1$.
$|E| \leq \frac{0.1^2}{8} \cdot 1 = \frac{0.01}{8} = 0.00125$.

---

### A16.8: Natural Boundary for Quadratic?
Setting $a_1=0$ makes the first segment a **straight line** ($b_1x + c_1$). This is often done to reduce the degree of freedom when no other information about the derivatives is known. It simplifies the starting point of the spline chain.

---

### A16.9: Linear Spline Implementation (Code)
```python
def linear_spline(x_data, y_data, x):
    idx = np.searchsorted(x_data, x) - 1
    idx = max(0, min(idx, len(x_data)-2))
    x0, x1 = x_data[idx], x_data[idx+1]
    y0, y1 = y_data[idx], y_data[idx+1]
    return y0 + (y1 - y0)/(x1 - x0) * (x - x0)
```

---

### A16.10: Quadratic Spline Solver (Code)
(The solver would construct a $(3n-1) \times (3n-1)$ matrix using the conditions from A16.5 and solve using `np.linalg.solve`).

---

## 17. Newton Interpolation (Divided Differences) (07_Interpolation) - ANSWERS

### A17.1: Divided Difference Table
Points: $(-1, 3), (0, 1), (1, 3), (2, 9)$.
| $x_i$ | $y_i$ | 1st DD | 2nd DD | 3rd DD |
| :--- | :--- | :--- | :--- | :--- |
| -1 | 3 | | | |
| 0 | 1 | (1-3)/(0 - -1) = -2 | | |
| 1 | 3 | (3-1)/(1-0) = 2 | (2 - -2)/(1 - -1) = 2 | |
| 2 | 9 | (9-3)/(2-1) = 6 | (6-2)/(2-0) = 2 | (2-2)/(2 - -1) = 0 |

---

### A17.2: Polynomial Construction
$P_3(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + a_3(x-x_0)(x-x_1)(x-x_2)$
$P_3(x) = 3 - 2(x+1) + 2(x+1)(x-0) + 0$
$P_3(x) = 3 - 2x - 2 + 2x^2 + 2x = 2x^2 + 1$.
**Standard Form:** $2x^2 + 1$. (Note: 3rd DD was 0, so it's a 2nd degree polynomial).

---

### A17.3: Incremental Property
New point $(3, 19)$.
New 1st DD: $(19-9)/(3-2) = 10$.
New 2nd DD: $(10-6)/(3-1) = 2$.
New 3rd DD: $(2-2)/(3-0) = 0$.
New 4th DD: $(0-0)/(3 - -1) = 0$.
**Additional Term:** $0(x+1)(x)(x-1)(x-2) = 0$.
The polynomial remains $2x^2 + 1$.

---

### A17.4: Horner's Method Evaluation
$P(x) = 1 + (x-0)[2 + (x-1)[0.5]]$.
For $x=2.5$:
1. Inner: $0.5 \cdot (2.5 - 1) = 0.5 \cdot 1.5 = 0.75$.
2. Middle: $2 + 0.75 = 2.75$.
3. Outer: $1 + (2.5 - 0) \cdot 2.75 = 1 + 6.875 = 7.875$.
**Value:** $7.875$.

---

### A17.5: Uniqueness of Interpolants
No. For a given set of $n+1$ points, there is exactly one unique polynomial of degree $\leq n$. Newton and Lagrange are just different **forms** (bases) for representing the same polynomial.

---

### A17.6: Error Formula for Newton
If $f(x)$ is a polynomial of degree $n$, its $(n+1)$-th derivative is zero.
$R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} \prod (x-x_i) = 0$.
**Conclusion:** The error is zero; the interpolation is perfect.

---

### A17.7: Divided Differences and Derivatives
$f[x_0, x_1] = \frac{f(x_1) - f(x_0)}{x_1 - x_0}$.
As $x_1 \to x_0$, this expression matches the definition of the derivative $f'(x_0)$.
In general, $f[x_0, \dots, x_n] = \frac{f^{(n)}(\xi)}{n!}$.

---

### A17.8: High-Order Oscillation
Runge's Phenomenon occurs when using high-degree polynomials with equidistant points. The polynomial oscillates wildly near the edges of the interval. Splines are preferred because they keep the degree low.

---

### A17.9: Divided Difference Generator (Code)
```python
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    for j in range(1, n):
        for i in range(n-j):
            coef[i,j] = (coef[i+1,j-1] - coef[i,j-1]) / (x[i+j] - x[i])
    return coef[0, :] # Diagonal contains a0, a1, ...
```

---

### A17.10: Newton Polynomial Evaluator (Code)
```python
def evaluate_newton(x_data, coefs, x):
    n = len(coefs) - 1
    p = coefs[n]
    for k in range(1, n + 1):
        p = coefs[n-k] + (x - x_data[n-k]) * p
    return p
```

---

## 18. Cubic Spline Interpolation (07_Interpolation) - ANSWERS

### A18.1: Cubic Spline Continuity Conditions
- $n$ intervals, each with 4 coefficients $\to 4n$ unknowns.
- **Equations:**
  - $C^0$ at internal nodes: $2(n-1)$.
  - $C^0$ at endpoints: $2$.
  - $C^1$ at internal nodes: $n-1$.
  - $C^2$ at internal nodes: $n-1$.
- **Total:** $4n - 2$. We need 2 more boundary conditions.

---

### A18.2: Natural Cubic Spline
Boundary condition: $f''(x_0) = 0$ and $f''(x_n) = 0$.
It is "natural" because it's the shape a thin flexible beam (a draftman's spline) would naturally take if pinned at the points without being clamped. It implies zero curvature (straight line) at the ends.

---

### A18.3: Tridiagonal System Derivation
$h_i M_{i-1} + 2(h_i + h_{i+1})M_i + h_{i+1} M_{i+1} = 6 [\frac{y_{i+1}-y_i}{h_{i+1}} - \frac{y_i-y_{i-1}}{h_i}]$.
This system relates the curvature ($M$) at adjacent nodes.

---

### A18.4: Manual Cubic Spline for 3 Points
Points: $(0, 0), (1, 1), (2, 0)$. $h_1 = 1, h_2 = 1$.
Natural: $M_0 = 0, M_2 = 0$.
$1 M_0 + 2(1+1)M_1 + 1 M_2 = 6 [\frac{0-1}{1} - \frac{1-0}{1}]$.
$4M_1 = 6 [-1 - 1] = -12$.
$M_1 = -3$.

---

### A18.5: Piecewise Polynomial Form
$s_1(x) = \frac{M_0(x_1-x)^3}{6h_1} + \frac{M_1(x-x_0)^3}{6h_1} + (y_0 - \frac{M_0h_1^2}{6})\frac{x_1-x}{h_1} + (y_1 - \frac{M_1h_1^2}{6})\frac{x-x_0}{h_1}$.
$s_1(x) = 0 + \frac{-3x^3}{6} + (0-0)(1-x) + (1 - \frac{-3}{6})x$.
$s_1(x) = -0.5x^3 + 1.5x$.

---

### A18.6: Clamped Boundary Condition
Clamped splines have specified first derivatives at the ends.
$s_1'(x_0) = f'(x_0)$ and $s_n'(x_n) = f'(x_n)$.
This provides the extra 2 equations instead of $M_0=M_n=0$.

---

### A18.7: Minimum Curvature Property
Cubic splines minimize the "strain energy" integral $\int_a^b [f''(x)]^2 dx$. Out of all functions that interpolate the points, the cubic spline has the minimum total curvature.

---

### A18.8: Comparison with Newton Polynomial
- **Newton (Degree 10):** High risk of oscillations (Runge's Phenomenon). Sensitive to single point changes.
- **Cubic Spline:** Very stable. Local changes only affect nearby segments. "Smooth" look with no wild wiggles.

---

### A18.9: Cubic Spline Matrix Builder (Code)
```python
# A is tridiagonal
A[i, i-1] = h[i]
A[i, i] = 2*(h[i] + h[i+1])
A[i, i+1] = h[i+1]
```

---

### A18.10: SciPy Spline Usage (Code)
```python
from scipy.interpolate import CubicSpline
cs = CubicSpline(x_data, y_data, bc_type='natural')
y_interp = cs(x_new)
```


---

## 19. Discrete Fourier Transform (DFT) (08_Fourier_Transforms) - ANSWERS

### A19.1: Manual N=4 DFT
**Step-by-Step:**
1. Sequence $x = [1, 2, 3, 4], N=4$. Twiddle factor $W_4 = e^{-i 2\pi/4} = e^{-i \pi/2} = -i$.
2. $X_k = \sum_{n=0}^3 x_n (W_4)^{kn}$.
3. $k=0: X_0 = 1(1) + 2(1) + 3(1) + 4(1) = 10$.
4. $k=1: X_1 = 1(1) + 2(-i) + 3(-1) + 4(i) = (1-3) + i(4-2) = -2 + 2i$.
5. $k=2: X_2 = 1(1) + 2(-1) + 3(1) + 4(-1) = (1+3) - (2+4) = -2$.
6. $k=3: X_3 = 1(1) + 2(i) + 3(-1) + 4(-i) = (1-3) + i(2-4) = -2 - 2i$.
**Final Result:** $X = [10, -2+2i, -2, -2-2i]$.

### A19.2: High-Resolution Manual DFT Trace (N=12)
**Step-by-Step for $X_1$:**
1. $x_n = \cos(\pi n / 6), N=12$.
2. $X_k = \sum_{n=0}^{11} x_n e^{-i rac{2\pi}{12} kn} = \sum_{n=0}^{11} \cos(rac{\pi n}{6}) [ \cos(rac{\pi kn}{6}) - i \sin(rac{\pi kn}{6}) ]$.
3. For $k=1$: $X_1 = \sum_{n=0}^{11} \cos(rac{\pi n}{6}) [ \cos(rac{\pi n}{6}) - i \sin(rac{\pi n}{6}) ]$.
4. Real part: $\sum \cos^2(rac{\pi n}{6}) = \sum rac{1 + \cos(\pi n / 3)}{2} = rac{12}{2} + 0 = 6$.
5. Imag part: $\sum \cos(rac{\pi n}{6})\sin(rac{\pi n}{6}) = \sum rac{1}{2}\sin(rac{\pi n}{3}) = 0$.
6. For $k=0$: $X_0 = \sum \cos(rac{\pi n}{6}) = 0$ (Sum of cosine over full period).
7. For $k=2$: $X_2 = \sum \cos(rac{\pi n}{6})e^{-i rac{\pi n}{3}} = 0$ (Orthogonality).
**Result:** $X_0=0, X_1=6, X_2=0$. $X_1$ captures the frequency of the cosine exactly.

### A19.3: Linearity and Shifting Theorems
**Proof:**
$DFT\{x[n-m]\} = \sum x[n-m] W_N^{kn}$. Let $l = n-m \implies n = l+m$.
$= \sum x[l] W_N^{k(l+m)} = W_N^{km} \sum x[l] W_N^{kl} = W_N^{km} X[k]$.
**Application:**
$y = [4, 1, 2, 3]$ is $x = [1, 2, 3, 4]$ shifted right by 1 ($m=1$).
$Y_k = X_k \cdot e^{-i rac{2\pi}{4} k \cdot 1} = X_k \cdot (-i)^k$.
$Y_0 = 10 \cdot 1 = 10$.
$Y_1 = (-2+2i)(-i) = 2i + 2 = 2+2i$.
$Y_2 = (-2)(-1) = 2$.
$Y_3 = (-2-2i)(i) = -2i + 2 = 2-2i$.

### A19.4: Parseval's Theorem Verification
**Time Energy:** $1^2 + (-1)^2 + 1^2 + (-1)^2 = 4$.
**Frequency DFT:** $X_0=0, X_1=0, X_2=4, X_3=0$.
**Freq Energy:** $rac{1}{4} (0^2 + 0^2 + 4^2 + 0^2) = rac{16}{4} = 4$.
**Result:** Both equal 4. Verified.

### A19.5: Zero Padding and Spectral Resolution
1. $x=[1,1,1,1] \implies X = [4, 0, 0, 0]$.
2. $y=[1,1,1,1,0,0,0,0] \implies Y = [4, 1-2.414i, 0, 1-0.414i, 0, \dots]$ (values of sinc function).
3. **Difference:** Zero padding does **not** increase resolution (the ability to distinguish two close frequencies). It only **interpolates** the spectrum, providing more samples of the same underlying DTFT.

### A19.6: The Leakage Phenomenon
- A DFT assumes the signal is periodic with period $N$.
- If $x_n$ has a frequency that isn't an integer multiple of $1/N$, the periodic extension has a **discontinuity** at the wrap-around point ($n=N-1$ to $n=0$).
- Discontinuities in time require infinite frequencies (high frequency components), which "leak" into all bins.

### A19.7: Inverse DFT Matrix Form
1. $W_4 = egin{bmatrix} 1 & 1 & 1 & 1 \ 1 & -i & -1 & i \ 1 & -1 & 1 & -1 \ 1 & i & -1 & -i nd{bmatrix}$.
2. $W_4^{-1} = rac{1}{4} W_4^*$ (Complex conjugate transpose).
3. The $1/N$ factor ensures that applying the transform then the inverse returns the original signal energy levels.

### A19.8: DFT of a Rectangular Pulse
$X_k = \sum_{n=0}^{M-1} 1 \cdot e^{-i rac{2\pi}{N} kn} = rac{1 - e^{-i rac{2\pi}{N} kM}}{1 - e^{-i rac{2\pi}{N} k}}$.
Using $1 - e^{i	heta} = e^{i	heta/2}(e^{-i	heta/2} - e^{i	heta/2}) = -2ie^{i	heta/2}\sin(	heta/2)$:
$|X_k| = |rac{\sin(\pi kM/N)}{\sin(\pi k/N)}|$. This is the Dirichlet kernel.

### A19.9: Complexity Analysis of Naive DFT (Code)
```python
import numpy as np
import time

def manual_dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x)

# N=1000 timing ~ 0.1s. 
# N=10^6 is 1000^2 times larger. 
# Time = 0.1 * 1,000,000 = 100,000 seconds (~27 hours).
```

### A19.10: Magnitude and Phase Spectrum Visualization (Code)
```python
import matplotlib.pyplot as plt
# Use manual_dft to get X.
# freq = np.fft.fftfreq(N, d=1/fs)
# plt.plot(freq, np.abs(X))
```

---

## 20. Fast Fourier Transform (FFT) (08_Fourier_Transforms) - ANSWERS

### A20.1: Bit-Reversal Permutation
1. 0(000) $	o$ 0(000) $	o$ 0
2. 1(001) $	o$ 4(100) $	o$ 4
3. 2(010) $	o$ 2(010) $	o$ 2
4. 3(011) $	o$ 6(110) $	o$ 6
5. 4(100) $	o$ 1(001) $	o$ 1
6. 5(101) $	o$ 5(101) $	o$ 5
7. 6(110) $	o$ 3(011) $	o$ 3
8. 7(111) $	o$ 7(111) $	o$ 7
**Order:** $[0, 4, 2, 6, 1, 5, 3, 7]$.

### A20.2: Cooley-Tukey Butterfly Diagram
**Calculations for $N=4$:**
- Stage 1: $s1_{0,1} = x_0 \pm x_2$, $s1_{2,3} = x_1 \pm x_3$.
- Stage 2 (Twiddles $W_4^0=1, W_4^1=-i$):
- $X_0 = s1_0 + 1 \cdot s1_2$
- $X_1 = s1_1 - i \cdot s1_3$
- $X_2 = s1_0 - 1 \cdot s1_2$
- $X_3 = s1_1 + i \cdot s1_3$

### A20.3: Twiddle Factor Periodicities
- For $N=16$:
- Stage 1: $W_2^0$
- Stage 2: $W_4^0, W_4^1$
- Stage 3: $W_8^0 \dots W_8^3$
- Stage 4: $W_{16}^0 \dots W_{16}^7$
- **Savings:** Naive DFT needs $N^2 = 256$ mults. FFT needs $(N/2)\log_2 N = 8 \cdot 4 = 32$ mults. Saving = 224 mults.

### A20.4: Radix-2 FFT Operation Count
- Each stage has $N/2$ butterflies.
- Each butterfly has 1 complex mult and 2 complex adds.
- Total stages: $\log_2 N$.
- **Mults:** $(N/2) \log_2 N$.
- **Adds:** $N \log_2 N$.

### A20.5: Decimation-in-Frequency (DIF) vs DIT
- **DIT:** Input is bit-reversed, output is normal. Twiddle mults happen **before** the butterfly addition/subtraction.
- **DIF:** Input is normal, output is bit-reversed. Twiddle mults happen **after** the butterfly addition/subtraction.

### A20.6: Symmetry in FFT of Real Signals
- $X_k = \sum x_n e^{-i 2\pi kn/N}$. If $x_n$ is real, $X_k^* = \sum x_n e^{i 2\pi kn/N} = X_{-k} = X_{N-k}$.
- **Trick:** Pack $x_n$ and $y_n$ into $z_n = x_n + i y_n$. Compute $Z_k = FFT(z)$. Then $X_k = rac{Z_k + Z_{N-k}^*}{2}$ and $Y_k = rac{Z_k - Z_{N-k}^*}{2i}$.

### A20.7: Butterfly Trace
- $W = e^{-i \pi/4} = rac{\sqrt{2}}{2} - i rac{\sqrt{2}}{2} pprox 0.707 - 0.707i$.
- $WB = (0.707 - 0.707i)(1 - i) = 0.707 - 0.707i - 0.707i - 0.707 = -1.414i$.
- $X = (2+3i) + (-1.414i) = 2 + 1.586i$.
- $Y = (2+3i) - (-1.414i) = 2 + 4.414i$.

### A20.8: FFT of a Sine Wave
$x = [0, 1, 0, -1]$. 
- $x_{even} = [0, 0] 	o E = [0, 0]$.
- $x_{odd} = [1, -1] 	o O = [0, 2]$.
- $X_k = E_k + W_4^k O_k$:
- $X_0 = 0 + 1(0) = 0$.
- $X_1 = 0 + (-i)(2) = -2i$.
- $X_2 = 0 + (-1)(0) = 0$.
- $X_3 = 0 + (i)(2) = 2i$.
Non-zero only at bins 1 and 3.

### A20.9: Recursive FFT Implementation (Code)
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

### A20.10: Performance Comparison (Code)
(The graph would show the $O(N^2)$ line curving up steeply while the $O(N \log N)$ line remains relatively flat.)

---

## 21. Gaussian Elimination & LU Decomposition (09_Linear_Algebra) - ANSWERS

### A21.1: Partial Pivoting Trace
1. Matrix: $egin{bmatrix} 1 & 1 & 1 & 3 \ 2 & 4 & 2 & 8 \ 4 & 10 & 2 & 16 nd{bmatrix}$.
2. Step 1: Max in col 1 is 4 (Row 3). Swap R1, R3.
   $egin{bmatrix} 4 & 10 & 2 & 16 \ 2 & 4 & 2 & 8 \ 1 & 1 & 1 & 3 nd{bmatrix}$.
3. Eliminate col 1:
   $R2 = R2 - 0.5R1 	o [0, -1, 1, 0]$.
   $R3 = R3 - 0.25R1 	o [0, -1.5, 0.5, -1]$.
4. Step 2: Max in col 2 is -1.5 (Row 3). Swap R2, R3.
   $egin{bmatrix} 4 & 10 & 2 & 16 \ 0 & -1.5 & 0.5 & -1 \ 0 & -1 & 1 & 0 nd{bmatrix}$.
5. Eliminate col 2: $R3 = R3 - (2/3)R2 	o [0, 0, 2/3, 2/3]$.
6. Solve: $x_3=1, x_2=1, x_1=1$.

### A21.2: LU Decomposition (Doolittle Method)
1. $u_{11}=2, u_{12}=3, u_{13}=1$.
2. $l_{21}=4/2=2, l_{31}=0/2=0$.
3. $u_{22}=7 - (2)(3) = 1$. $u_{23} = 5 - (2)(1) = 3$.
4. $l_{32}=(-2 - (0)(3))/1 = -2$.
5. $u_{33}=2 - (0)(1) - (-2)(3) = 8$.
**Result:** $L = egin{bmatrix} 1 & 0 & 0 \ 2 & 1 & 0 \ 0 & -2 & 1 nd{bmatrix}, U = egin{bmatrix} 2 & 3 & 1 \ 0 & 1 & 3 \ 0 & 0 & 8 nd{bmatrix}$.

### A21.3: Operation Count for GE
- Stage $k$: elimination of $n-k$ rows.
- Each row requires 1 div ($m_{ik}$), $n-k$ mults, and $n-k$ subs.
- Total Mults $pprox \sum_{k=1}^n (n-k)^2 pprox \int_0^n x^2 dx = n^3/3$.

### A21.4: Forward and Backward Substitution
1. $Ly=b: y_1=7, 3(7)+y_2=18 \implies y_2=-3$.
2. $Ux=y: -x_2=-3 \implies x_2=3$. $2x_1+5(3)=7 \implies 2x_1=-8 \implies x_1=-4$.
**Result:** $x = [-4, 3]$.

### A21.5: Pivoting Necessity
1. No pivot: $x_2 = (2 - 1/psilon)/(1 - 1/psilon) pprox 1$. $x_1 = (1 - x_2)/psilon pprox 0$.
2. Pivot: swap rows. $egin{bmatrix} 1 & 1 \ psilon & 1 nd{bmatrix} 	o egin{bmatrix} 1 & 1 \ 0 & 1-psilon nd{bmatrix}$. $x_2 = (2 - psilon)/(1-psilon) pprox 2$. $x_1 = 2-x_2 pprox 0$.
3. **Stability:** Small $psilon$ causes subtraction of very large numbers, losing precision.

### A21.6: Condition Number and Stability
- $\|A\|_\infty = 101, \|A^{-1}\|_\infty = 101$. $\kappa = 10201$.
- Relative error in $x$ can be up to $10201 	imes$ relative error in $b$.

### A21.7: LU for Tridiagonal Systems
- $l_{i, i-1} u_{i-1, i}$ are the only terms in the product sum. Complexity becomes $3n$ mults instead of $n^3/3$.

### A21.8: Determinant from LU
- $\det(A) = \det(L)\det(U)$. Since $l_{ii}=1, \det(L)=1$. $\det(A) = \prod u_{ii}$.
- For Q21.2: $\det(A) = 2 \cdot 1 \cdot 8 = 16$.

### A21.9: Gaussian Elimination with Pivoting (Code)
```python
def gaussian_elimination(A, b):
    n = len(b)
    for i in range(n):
        # Pivot
        p = np.argmax(np.abs(A[i:, i])) + i
        A[[i, p]] = A[[p, i]]
        b[[i, p]] = b[[p, i]]
        # Eliminate...
```

### A21.10: LU Decomposition Solver (Code)
- LU decomposition is $O(n^3/3)$.
- Substitution is $O(n^2)$.
- Multiple $b$ vectors: $O(n^3/3) + m \cdot O(n^2)$. GE would be $m \cdot O(n^3/3)$.

---

## 22. Jacobi Iterative Method (09_Linear_Algebra) - ANSWERS

### A22.1: Strictly Diagonal Dominance
1. $1 < 2$ (No). Rearrange: $3 > 1$ and $2 > 1$ (Yes, swap rows).
2. $4 > 1+2=3$ (Yes). $5 > 1+1=2$ (Yes). $4 > 2+1=3$ (Yes). (Strictly DD).

### A22.2: Manual Jacobi Step
1. $x_1^{(1)} = (3 - 0 - 0)/10 = 0.3$.
2. $x_2^{(1)} = (1.5 - 0 - 0)/10 = 0.15$.
3. $x_3^{(1)} = (-9 - 0 - 0)/10 = -0.9$.
4. Iter 2:
   $x_1^{(2)} = (3 - 0.15 - 2(-0.9))/10 = (3 - 0.15 + 1.8)/10 = 0.465$.
   $x_2^{(2)} = (1.5 - 0.3 + (-0.9))/10 = 0.03$.
   $x_3^{(2)} = (-9 - 2(0.3) - 0.15)/10 = -0.975$.

### A22.3: Iteration Matrix and Convergence
- $M = -D^{-1}(L+U)$. $D = 10 \cdot I$.
- $M = egin{bmatrix} 0 & -0.1 & -0.2 \ -0.1 & 0 & 0.1 \ -0.2 & -0.1 & 0 nd{bmatrix}$.
- Sum of absolute rows: $[0.3, 0.2, 0.3]$. All $< 1$. $ho(M) < 1$. Converges.

### A22.4: Jacobi vs Gauss-Seidel Logic
- Jacobi uses ONLY values from iteration $k$.
- Gauss-Seidel uses new values $x_1^{(k+1)}, x_2^{(k+1)}$ as soon as they are available for the rest of the same iteration.
- GS is faster (usually $2x$) and uses less memory but is harder to parallelize.

### A22.5: Matrix Splitting
$Ax = b \implies (D+L+U)x = b \implies Dx = b - (L+U)x$.
$x^{(k+1)} = D^{-1}b - D^{-1}(L+U)x^{(k)}$.

### A22.6: Stopping Criteria
- If $A$ is very ill-conditioned, small changes in $x$ don't necessarily mean $Ax pprox b$. The residual is the only true measure of how well the equations are satisfied.

### A22.7: Convergence Speed
- Error $e_k pprox ho^k e_0$.
- $0.9^k = 10^{-6} \implies k \log(0.9) = -6 \implies k pprox -6 / -0.045 pprox 133$.

### A22.8: Sparse Matrix Advantage
- Direct methods like LU cause "fill-in" (zeros become non-zeros), requiring $O(n^2)$ space.
- Jacobi only ever needs the original non-zeros and 2 vectors of size $n$. Memory stays $O(n)$.

### A22.9: Jacobi Method Implementation (Code)
```python
def jacobi(A, b, x0, tol, max_iter):
    D = np.diag(A)
    R = A - np.diagflat(D)
    for i in range(max_iter):
        x = (b - np.dot(R, x0)) / D
        if np.linalg.norm(x - x0) < tol: return x, i
        x0 = x
```

### A22.10: Convergence Visualization (Code)
(The plot would show a straight line on the log-linear scale, indicating exponential decay of the error.)
