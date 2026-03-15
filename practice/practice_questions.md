10 questions each for all topics in this repository (medium + Hard difficulty) (80 percent manual solving and 20% code implementation)
22topics * 10 == 220 questions
for dft and fft make it harder than the rest little med + more hard, gimme dft for like > 12 iterations
and it's manual solving, code snippets where necessary 

---

## 1. Python Basics (01_Introduction_to_Programming)

### Q1.1: Bitwise Logic Trace (Manual)
Trace the following code and determine the final value of `res`. Show your work in binary.
```python
n = 13
res = 0
while n > 0:
    res = (res << 1) | (n & 1)
    n >>= 1
```

### Q1.2: Complex Arithmetic (Manual)
Evaluate the following expression following Python's operator precedence:
`result = (5 << 2) ^ (13 >> 1) | (7 & 3) + (10 // 3) ** 2`

### Q1.3: Nested List Comprehensions (Manual)
What is the output of the following code? Trace each step.
```python
matrix = [[x * y for x in range(3)] for y in range(4) if y % 2 != 0]
print(matrix)
```

### Q1.4: Function Scope and Mutability (Manual)
Predict the output of the following script. Explain why the results differ.
```python
def update_list(val, container=[]):
    container.append(val)
    return container

print(update_list(10))
print(update_list(20, [1, 2]))
print(update_list(30))
```

### Q1.5: Recursion and State (Manual)
Trace the execution of `mystery(5)`. What is the final return value?
```python
def mystery(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return n + mystery(n - 1)
    else:
        return n * mystery(n - 2)
```

### Q1.6: String Slicing and Manipulation (Manual)
Given `s = "ComputationalMethods"`, determine the output of:
`print(s[2:14:3][::-1].upper())`

### Q1.7: Dictionary Logic (Manual)
What is the state of the dictionary `data` after these operations?
```python
data = {x: x**2 for x in range(3)}
data.setdefault(2, 10)
data.update({1: 5, 3: 9})
val = data.get(4, "N/A")
print(data, val)
```

### Q1.8: Logical Short-Circuiting (Manual)
Determine the output and explain which parts of the expression are evaluated:
```python
def check(msg, ret):
    print(msg)
    return ret

res = check("A", False) and check("B", True) or check("C", True)
print("Result:", res)
```

### Q1.9: Algorithm Implementation (Code)
Write a Python function `first_unique(s)` that returns the first non-repeating character in a string. If all characters repeat, return `None`. Use a dictionary for efficiency.

### Q1.10: Efficient File I/O (Code)
Write a code snippet that reads a large text file `data.txt` line by line and prints only the lines that contain more than 5 words, without loading the entire file into memory.

---

## 2. Object-Oriented Programming (01_Introduction_to_Programming)

### Q2.1: Method Resolution Order (Manual)
Given the following inheritance hierarchy, determine the MRO for class `D`.
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
```

### Q2.2: Diamond Inheritance and super() (Manual)
Trace the output of `D().process()`.
```python
class A:
    def process(self): print("A")
class B(A):
    def process(self):
        print("B")
        super().process()
class C(A):
    def process(self):
        print("C")
        super().process()
class D(B, C):
    def process(self):
        print("D")
        super().process()
```

### Q2.3: Class vs Instance Variables (Manual)
Predict the output:
```python
class Tracker:
    count = 0
    def __init__(self, name):
        self.name = name
        Tracker.count += 1
        self.id = Tracker.count

t1 = Tracker("A")
t2 = Tracker("B")
t1.count = 10
print(t1.count, t2.count, Tracker.count)
```

### Q2.4: Property Decorators (Manual)
Trace the execution of the following code. What happens when `acc.balance = -100` is executed?
```python
class Account:
    def __init__(self, val):
        self._balance = val
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, val):
        if val < 0:
            print("Invalid")
        else:
            self._balance = val

acc = Account(50)
acc.balance += 50
acc.balance = -100
print(acc.balance)
```

### Q2.5: Polymorphism Logic (Manual)
What is the output of the following?
```python
class Bird:
    def fly(self): print("Flying")
class Penguin(Bird):
    def fly(self): print("Cannot fly")

def lift_off(birds):
    for bird in birds:
        bird.fly()

lift_off([Bird(), Penguin()])
```

### Q2.6: Static and Class Methods (Manual)
Explain the output:
```python
class Demo:
    data = "Class"
    @classmethod
    def set_class_data(cls, val):
        cls.data = val
    @staticmethod
    def print_info():
        print("Static")

Demo.set_class_data("New")
d = Demo()
print(d.data)
Demo.print_info()
```

### Q2.7: Name Mangling (Manual)
Trace the following and explain why the second print statement might fail or what it produces.
```python
class Secret:
    def __init__(self):
        self.__code = 1234
    def get_code(self):
        return self.__code

s = Secret()
print(s.get_code())
# print(s.__code__) # How would you access this externally?
```

### Q2.8: Function Decorators (Manual)
Trace the output of `add(3, 5)`.
```python
def logger(func):
    def wrapper(*args):
        print(f"Calling {func.__name__}")
        return func(*args) * 2
    return wrapper

@logger
def add(x, y):
    return x + y
```

### Q2.9: Operator Overloading (Code)
Implement a `Vector` class that supports addition (`+`) and scalar multiplication (`*`) by overloading `__add__` and `__mul__`.

### Q2.10: Singleton Pattern (Code)
Implement a `DatabaseConnection` class using the Singleton pattern (ensure only one instance of the class can ever exist using `__new__`).

---

## 3. Data Visualization with Matplotlib (01_Introduction_to_Programming)

### Q3.1: Subplot Geometry (Manual)
Explain the layout created by `plt.subplot(3, 2, 5)`. How many total plots are possible in this grid, and where is the 5th one located?

### Q3.2: Plot Styling Interpretation (Manual)
Given the command `plt.plot(x, y, 'rs--')`, describe exactly what the resulting line will look like (color, marker, line style).

### Q3.3: Histogram Binning Logic (Manual)
If you have a dataset `D = [5, 7, 12, 18, 21, 28, 33]` and you call `plt.hist(D, bins=3)`, calculate the width of each bin and which data points fall into each bin.

### Q3.4: Axis Object Management (Manual)
Explain the difference between `fig, ax = plt.subplots()` and using `plt.plot()`. When is the former preferred?

### Q3.5: Scatter Plot Customization (Manual)
Trace the logic of the `c` and `s` parameters in `plt.scatter(x, y, c=colors, s=sizes)`. If `colors` is a list of integers, how does Matplotlib determine the actual colors?

### Q3.6: Logarithmic Scaling (Manual)
Compare `plt.yscale('log')` and `plt.yscale('symlog')`. In what specific mathematical scenario would `symlog` be required over `log`?

### Q3.7: Legend and Handle Logic (Manual)
How do you create a legend for only two out of five lines plotted on the same axes? Describe the manual handle/label passing process.

### Q3.8: Figure Persistence (Manual)
If you call `plt.plot(x1, y1)` and then `plt.plot(x2, y2)` without calling `plt.show()` or creating a new figure, what is the result?

### Q3.9: Dual-Axis Implementation (Code)
Write a snippet to plot two different functions with vastly different scales (e.g., $y=x^2$ and $y=e^x$) on the same plot using a shared X-axis but independent Y-axes (`twinx()`).

### Q3.10: Heatmap Visualization (Code)
Generate a 10x10 matrix of random values and visualize it as a heatmap using `plt.imshow()`. Include a colorbar and title.

---

## 4. Floating Point Representation & Precision (02_Computing_Fundamentals_and_Error_Analysis)

### Q4.1: IEEE 754 Single Precision Conversion (Manual)
Convert the decimal number $-12.625$ into its IEEE 754 single-precision (32-bit) binary representation. Show the sign bit, exponent (with bias), and mantissa.

### Q4.2: Binary Float to Decimal (Manual)
Given the IEEE 754 single-precision representation `0 10000010 01100000000000000000000`, determine the equivalent decimal value.

### Q4.3: Custom Floating Point System (Manual)
Suppose a computer uses a 10-bit floating-point format: 1 sign bit, 4 exponent bits (bias = 7), and 5 mantissa bits. 
1. What is the smallest positive normalized number?
2. What is the largest representable number (before infinity)?

### Q4.4: Machine Epsilon Calculation (Manual)
Calculate the machine epsilon ($\epsilon_{mach}$) for a system with a 24-bit mantissa (including the implicit leading 1). Express your answer as a power of 2 and in scientific notation.

### Q4.5: Precision Loss in Summation (Manual)
Explain why `(10**16 + 1) - 10**16` results in `0.0` in standard 64-bit floating-point arithmetic (double precision), while `1 + (10**16 - 10**16)` results in `1.0`.

### Q4.6: Subnormal Numbers (Manual)
In the IEEE 754 format, what is the purpose of subnormal (denormal) numbers? Calculate the decimal value of the smallest positive subnormal number in single precision (Exponent bits all 0, Mantissa = `000...001`).

### Q4.7: Mantissa Precision (Manual)
How many decimal digits of precision does a 64-bit double-precision float provide? Show the calculation based on the 52-bit mantissa.

### Q4.8: Comparison Paradox (Manual)
Trace why the expression `0.1 + 0.2 == 0.3` returns `False` in Python. Show the binary representation of `0.1` and `0.2` (first 10 bits of mantissa).

### Q4.9: Finding Machine Epsilon (Code)
Write a Python script that calculates the machine epsilon of your current environment using a `while` loop, without using `sys.float_info.epsilon`.

### Q4.10: Struct-Level Inspection (Code)
Write a code snippet using the `struct` module to convert a float (e.g., `3.14`) into its hexadecimal representation and extract the raw binary bits of the sign, exponent, and mantissa.

---

## 5. Error Analysis (02_Computing_Fundamentals_and_Error_Analysis)

### Q5.1: Relative vs Absolute Error (Manual)
A measurement of $\pi$ is approximated as $22/7$. Calculate the absolute error and the relative error. Round your final answers to 5 significant digits.

### Q5.2: Error Propagation in Addition (Manual)
If $X = 100 \pm 0.5$ and $Y = 50 \pm 0.2$, calculate the absolute and relative error of the sum $S = X + Y$.

### Q5.3: Catastrophic Cancellation (Manual)
Consider the function $f(x) = \sqrt{x+1} - \sqrt{x}$. 
1. Calculate $f(10000)$ using 4-digit rounding at each step.
2. Rewrite the formula to avoid catastrophic cancellation and re-calculate.

### Q5.4: Taylor Series Truncation (Manual)
Use the Taylor series for $e^x$ centered at 0 to approximate $e^{0.5}$ using the first 4 terms. Estimate the truncation error using the remainder term formula.

### Q5.5: Condition Number (Manual)
Calculate the condition number $\kappa(x)$ for the function $f(x) = \frac{1}{1-x}$ near $x = 0.99$. Is the problem well-conditioned or ill-conditioned?

### Q5.6: Stability of Iterative Schemes (Manual)
Consider the recurrence $x_{n+1} = 2.1x_n - 1.1x_{n-1}$. If $x_0 = 1$ and $x_1 = 1$, the exact solution is $x_n = 1$ for all $n$. Explain what happens if a small rounding error $\epsilon$ is introduced in $x_1$.

### Q5.7: Round-off in Large Sums (Manual)
You are summing $10^7$ numbers, each approximately $0.1$, in single-precision float. Estimate the total potential round-off error if the machine epsilon is $10^{-7}$.

### Q5.8: Derivative Approximation Error (Manual)
The forward difference approximation for a derivative is $f'(x) \approx \frac{f(x+h)-f(x)}{h}$. Show that the truncation error is $O(h)$.

### Q5.9: Error Calculator (Code)
Write a Python function `analyze_error(true_val, approx_val)` that returns a dictionary containing the absolute error, relative error, and a boolean indicating if the approximation is within a 1% relative tolerance.

### Q5.10: Cancellation Demonstration (Code)
Write a script that computes $1 - \cos(x)$ for very small $x$ (e.g., $10^{-8}$) and compares it to the more stable Taylor expansion $x^2/2$. Print the difference to show the loss of precision.

---

## 6. Bisection Method (03_Root_Finding)

### Q6.1: Manual Iteration (Manual)
Find the root of $f(x) = x^3 - 5$ on the interval $[1, 2]$ using the Bisection Method. Perform 3 iterations and record the interval $[a, b]$, midpoint $m$, and $f(m)$ at each step.

### Q6.2: Iteration Count Estimation (Manual)
How many iterations of the Bisection Method are required to find a root on the interval $[0, 1]$ with an absolute tolerance of $10^{-6}$?

### Q6.3: Convergence Logic (Manual)
Does the Bisection Method converge for $f(x) = \frac{1}{x-0.5}$ on the interval $[0, 1]$? Justify your answer using the requirements of the method.

### Q6.4: Bisection on Quadratic (Manual)
Use Bisection to find the positive root of $x^2 - 2 = 0$ on $[1, 2]$. After 2 iterations, what is the maximum possible error in your estimate?

### Q6.5: Bracketing Failure (Manual)
Provide an example of a continuous function $f(x)$ and an interval $[a, b]$ where $f(a)f(b) > 0$ but a root exists in the interval. Why does Bisection fail here?

### Q6.6: Stopping Criteria Comparison (Manual)
Explain the difference between stopping when $|f(m)| < \epsilon$ and $(b-a)/2 < \epsilon$. In what scenario would the former be satisfied while the latter is not?

### Q6.7: Multiple Roots (Manual)
If $f(x) = (x-1)(x-2)(x-3)$, and you start Bisection on $[0, 4]$, which root will the method converge to? Trace the first two midpoints.

### Q6.8: Efficiency vs Robustness (Manual)
Compare Bisection to Newton's method in terms of "guaranteed convergence" and "speed of convergence". Under what conditions is Bisection preferred?

### Q6.9: Bisection Implementation (Code)
Write a robust Python function `bisection(f, a, b, tol)` that includes a check for the Intermediate Value Theorem and returns the root.

### Q6.10: Iteration Table Generator (Code)
Write a script that uses your `bisection` function to solve $x = \cos(x)$ on $[0, 1]$ and prints a formatted Markdown table of each iteration's values ($k, a, b, m, f(m)$).

---

## 7. Newton-Raphson Method (03_Root_Finding)

### Q7.1: Manual Newton Step (Manual)
Apply two iterations of the Newton-Raphson method to find the root of $f(x) = x^2 - 3$, starting with $x_0 = 2$.

### Q7.2: Derivation from Taylor Series (Manual)
Show how the Newton-Raphson update formula $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ is derived using a first-order Taylor expansion.

### Q7.3: Quadratic Convergence Trace (Manual)
Newton's method typically doubles the number of correct decimal digits each iteration. If $|x_1 - r| = 10^{-2}$, what is the approximate error $|x_3 - r|$?

### Q7.4: Failure at Stationary Point (Manual)
Attempt to find the root of $f(x) = x^3 - 3x + 2$ using Newton's method with $x_0 = 1$. What happens and why?

### Q7.5: Multiple Root Convergence (Manual)
For $f(x) = (x-1)^2$, show that Newton's method converges linearly instead of quadratically. Calculate the ratio $\frac{e_{n+1}}{e_n}$ where $e_n = |x_n - 1|$.

### Q7.6: Newton for Division (Manual)
Newton's method can be used to compute $1/a$ without using division. Derive the update formula for $f(x) = \frac{1}{x} - a$.

### Q7.7: Geometric Divergence (Manual)
Draw or describe a function $f(x)$ and a starting point $x_0$ where Newton's method enters an infinite cycle between two values (e.g., $x_0 \to x_1 \to x_0$).

### Q7.8: Complex Roots (Manual)
What happens if you apply Newton's method to $f(x) = x^2 + 1$ starting from a real initial guess $x_0 = 1$?

### Q7.9: Newton with Lambda (Code)
Write a Python function `newton(f, df, x0, tol)` that takes the function `f` and its derivative `df` as arguments and returns the root.

### Q7.10: Root Finding with `scipy` (Code)
Write a snippet using `scipy.optimize.newton` to find the root of $x e^x - 1 = 0$. Compare the result with a manual implementation for 5 iterations.

---

## 8. Secant Method (03_Root_Finding)

### Q8.1: Manual Secant Trace (Manual)
Perform 2 iterations of the Secant method for $f(x) = x^2 - 5$ with initial guesses $x_0 = 2$ and $x_1 = 3$.

### Q8.2: Secant vs Newton (Manual)
Explain the primary advantage of the Secant method over Newton-Raphson. What is the "cost" of this advantage in terms of convergence rate?

### Q8.3: Derivative Approximation (Manual)
Show that the Secant method update formula is equivalent to Newton's method where the derivative is replaced by a finite difference approximation.

### Q8.4: Superlinear Convergence (Manual)
The convergence rate of the Secant method is $\phi \approx 1.618$. If the error at iteration $n$ is $10^{-2}$, estimate the error at iteration $n+2$.

### Q8.5: Stability and Slopes (Manual)
What happens to the Secant method if $f(x_n) \approx f(x_{n-1})$? Describe the geometric consequence and the impact on the numerical calculation.

### Q8.6: Secant vs Bisection (Manual)
Which method is more likely to diverge if the initial guesses are far from the root: Bisection or Secant? Why?

### Q8.7: Iteration History (Manual)
For the Secant method, does $x_{n+1}$ always stay between $x_n$ and $x_{n-1}$? Contrast this with the Bisection method.

### Q8.8: Regula Falsi Comparison (Manual)
Briefly describe the "False Position" (Regula Falsi) method. How does it differ from the Secant method in terms of bracketing?

### Q8.9: Secant Implementation (Code)
Implement the `secant_method(f, x0, x1, tol)` function in Python. Ensure it handles the case where the denominator becomes zero.

### Q8.10: Performance Benchmarking (Code)
Write a script that solves $x^3 - x - 1 = 0$ using Bisection, Newton, and Secant methods. Count and print the number of function evaluations required by each to reach a tolerance of $10^{-8}$.

---

## 9. Forward & Backward Difference (04_Numerical_Differentiation)

### Q9.1: Forward Difference Table (Manual)
Given $f(x) = x^3$, compute the forward difference approximation for $f'(1)$ with $h=0.1$ and $h=0.01$. Calculate the true error for both cases.

### Q9.2: Backward Difference Derivation (Manual)
Derive the first-order backward difference formula using the Taylor series expansion of $f(x-h)$ about $x$.

### Q9.3: Error Scaling (Manual)
If the step size $h$ is halved for a first-order forward difference, by what factor do you expect the truncation error to change? Prove this using the big-O notation.

### Q9.4: Boundary Problem (Manual)
Why is the forward difference preferred over the backward difference at the left boundary of a domain $[a, b]$?

### Q9.5: Second-Order Forward Formula (Manual)
Derive the second-order forward difference formula for the first derivative: $f'(x) \approx \frac{-3f(x) + 4f(x+h) - f(x+2h)}{2h}$.

### Q9.6: Stencil Identification (Manual)
Which derivative approximation does the stencil $[-1, 1]$ with step $h$ represent? What is its order of accuracy?

### Q9.7: Truncation vs Round-off (Manual)
As $h \to 0$, truncation error decreases but round-off error increases. Sketch a graph of Total Error vs $h$ and mark the optimal $h$.

### Q9.8: Non-Uniform Grid (Manual)
Write the formula for the forward difference if the grid points are not equally spaced, i.e., $x_{i+1} = x_i + h_i$.

### Q9.9: Forward Difference Implementation (Code)
Write a Python function `forward_diff(f, x, h)` that returns the first derivative approximation.

### Q9.10: Error Analysis Script (Code)
Write a script that calculates $f'(1)$ for $f(x) = \sin(x)$ using forward difference for $h = 10^{-1}, 10^{-2}, \dots, 10^{-10}$ and prints the error at each step.

---

## 10. Central Difference & Higher Order Derivatives (04_Numerical_Differentiation)

### Q10.1: Central Difference Accuracy (Manual)
Prove that the central difference formula $f'(x) \approx \frac{f(x+h)-f(x-h)}{2h}$ is second-order accurate $O(h^2)$.

### Q10.2: Second Derivative Central (Manual)
Derive the central difference formula for the second derivative $f''(x)$ using Taylor expansions of $f(x+h)$ and $f(x-h)$.

### Q10.3: Comparison (Manual)
For $f(x) = e^x$ at $x=0$ with $h=0.1$, which is more accurate: forward, backward, or central difference? Show your calculations.

### Q10.4: Stencil for f''(x) (Manual)
Identify the stencil $[1, -2, 1]$. What derivative does it approximate and what is the step size denominator?

### Q10.5: Richardson Extrapolation (Manual)
Briefly explain how Richardson Extrapolation can be used to improve a $O(h^2)$ central difference to $O(h^4)$.

### Q10.6: Fourth-Order Central (Manual)
The fourth-order central difference for $f'(x)$ is $\frac{-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)}{12h}$. How many function evaluations are required?

### Q10.7: Mixed Partial Derivatives (Manual)
How would you approximate $\frac{\partial^2 f}{\partial x \partial y}$ using central differences on a 2D grid?

### Q10.8: Stability in f''(x) (Manual)
Why does the second derivative central difference formula often suffer more from round-off error than the first derivative formula?

### Q10.9: Central Difference Implementation (Code)
Write a Python function `central_diff(f, x, h)` for the first derivative.

### Q10.10: Higher-Order Derivative Implementation (Code)
Write a Python function `second_deriv_central(f, x, h)` that computes $f''(x)$.

---

## 11. Trapezoidal Rule (Composite) (05_Numerical_Integration)

### Q11.1: Single vs Composite (Manual)
Approximate $\int_0^1 x^2 dx$ using: (a) Single Trapezoidal rule, (b) Composite Trapezoidal rule with $n=2$. Compare with the exact value.

### Q11.2: Geometric Interpretation (Manual)
The Trapezoidal rule approximates the area under a curve using a linear spline. For a concave down function ($f''(x) < 0$), will the Trapezoidal rule over-estimate or under-estimate the integral?

### Q11.3: Error Formula (Manual)
The error for composite trapezoidal is $E = -\frac{(b-a)h^2}{12} f''(\xi)$. If you want to guarantee an error less than $10^{-4}$ for $\int_0^2 e^x dx$, how many intervals $n$ are needed?

### Q11.4: Linear Exactness (Manual)
Show that the Trapezoidal rule is exact for any linear function $f(x) = mx + c$.

### Q11.5: Table-Based Integration (Manual)
Given data points $(0, 1), (0.5, 0.8), (1, 0.5)$, compute the integral using the Trapezoidal rule.

### Q11.6: Recursive Trapezoidal (Manual)
If $I(h)$ is the trapezoidal estimate with step $h$, what is the relationship between $I(h)$ and $I(h/2)$?

### Q11.7: Periodic Functions (Manual)
Why is the Trapezoidal rule exceptionally accurate for periodic functions integrated over a full period?

### Q11.8: Unequal Intervals (Manual)
Write the formula for the Trapezoidal rule if the intervals $h_i$ are not equal.

### Q11.9: Composite Trapezoidal Implementation (Code)
Write a Python function `trapezoidal_composite(f, a, b, n)` that implements the rule.

### Q11.10: Integration Convergence (Code)
Write a script to integrate $f(x) = \frac{1}{1+x^2}$ from 0 to 1 for $n=2, 4, 8, 16, 32$ and show that the error decreases by a factor of 4 each time $n$ doubles.

---

## 12. Simpson's 1/3 and 3/8 Rules (05_Numerical_Integration)

### Q12.1: Simpson's 1/3 for Parabola (Manual)
Show that Simpson's 1/3 rule is exact for $f(x) = x^3$, even though it's derived from a quadratic fit.

### Q12.2: Composite 1/3 Parity (Manual)
Explain why the composite Simpson's 1/3 rule requires an even number of intervals ($n$).

### Q12.3: Simpson's 3/8 Logic (Manual)
When is Simpson's 3/8 rule preferred over Simpson's 1/3 rule? (Hint: Think about $n$).

### Q12.4: Comparison Table (Manual)
Approximate $\int_0^{\pi} \sin(x) dx$ using (a) Trapezoidal, (b) Simpson's 1/3 with $n=2$. Which is closer to the true value?

### Q12.5: Error Comparison (Manual)
The error of Simpson's 1/3 is $O(h^4)$. If $h$ is halved, by what factor does the error decrease?

### Q12.6: Weight Coefficients (Manual)
Identify the pattern of weights for Composite Simpson's 1/3 rule for $n=6$.

### Q12.7: Cubic Exactness (Manual)
Verify if Simpson's 3/8 rule is exact for $f(x) = x^3$.

### Q12.8: Mixing Rules (Manual)
If you have $n=5$ intervals, how would you combine Simpson's rules to integrate the entire domain?

### Q12.9: Simpson's 1/3 Implementation (Code)
Write a Python function `simpson13_composite(f, a, b, n)`. Include a check for $n$ parity.

### Q12.10: Simpson's 3/8 Implementation (Code)
Write a Python function `simpson38_composite(f, a, b, n)`. Include a check if $n$ is a multiple of 3.

---

## 13. Euler's Method (06_Differential_Equations)

### Q13.1: Single Step Trace (Manual)
Given $\frac{dy}{dt} = y + t$, $y(0) = 1$. Use Euler's method with $h=0.1$ to find $y(0.2)$.

### Q13.2: Geometric Interpretation (Manual)
Explain why Euler's method is often called the "tangent line method".

### Q13.3: Error and Step Size (Manual)
If you reduce the step size $h$ by a factor of 10, how do you expect the global truncation error of Euler's method to change?

### Q13.4: Stability Region (Manual)
For the test equation $y' = \lambda y$, what is the condition on $h$ for Euler's method to be stable if $\lambda = -10$?

### Q13.5: Local vs Global Error (Manual)
Distinguish between local truncation error and global truncation error for Euler's method. Give their big-O orders.

### Q13.6: Backward Euler (Manual)
Write the formula for the Implicit (Backward) Euler method. Why is it used despite being harder to solve?

### Q13.7: System of ODEs (Manual)
How would you apply Euler's method to a second-order ODE $y'' + y = 0$?

### Q13.8: Vectorized Euler (Manual)
Express the Euler update step in vector form for a system $\mathbf{y}' = \mathbf{f}(t, \mathbf{y})$.

### Q13.9: Basic Euler Implementation (Code)
Write a Python function `euler_method(f, t0, y0, h, steps)` that returns arrays of $t$ and $y$ values.

### Q13.10: ODE Solution Plotting (Code)
Write a script to solve $y' = -2y$, $y(0)=1$ using Euler's method up to $t=2$ with $h=0.1$, and plot the result against the exact solution $y = e^{-2t}$.

---

## 14. Heun's Method (Improved Euler) (06_Differential_Equations)

### Q14.1: Manual Heun Step (Manual)
Given the IVP $\frac{dy}{dt} = y - t^2 + 1, y(0) = 0.5$. Use Heun's method with $h = 0.2$ to calculate $y(0.2)$. Show both the predictor and corrector steps.

### Q14.2: Comparison with Euler (Manual)
For the ODE $\frac{dy}{dt} = -2ty, y(0) = 1$, perform one step of both Euler's method and Heun's method with $h = 0.1$. Calculate the absolute error for both using the exact solution $y(t) = e^{-t^2}$.

### Q14.3: Stability Limit (Manual)
For the test equation $y' = \lambda y$, show that the stability region for Heun's method is defined by $|1 + h\lambda + \frac{(h\lambda)^2}{2}| \leq 1$. If $\lambda = -5$, what is the maximum stable step size $h$?

### Q14.4: Local Truncation Error (Manual)
Derive the local truncation error of Heun's method using Taylor series expansions. Show that it is $O(h^3)$ for a single step.

### Q14.5: Multiple Iterations (Manual)
Solve $y' = 1 + y^2, y(0) = 0$ using Heun's method for 2 steps with $h = 0.1$. Provide a table showing $t_i, y_i^{predictor}, f(t_i, y_i), f(t_{i+1}, y_{i+1}^{predictor})$, and the final $y_{i+1}$.

### Q14.6: Systems of ODEs with Heun (Manual)
Express the Heun update steps for a system of two first-order ODEs:
$u' = v$
$v' = -u$
with $u(0)=1, v(0)=0$. Calculate one step with $h=0.1$.

### Q14.7: Geometric Interpretation (Manual)
Explain how Heun's method relates to the Trapezoidal Rule for integration. If $f(t, y)$ is independent of $y$, show that Heun's method reduces exactly to the Trapezoidal Rule.

### Q14.8: Error Scaling Analysis (Manual)
If the step size $h$ is reduced from $0.1$ to $0.05$ in Heun's method, by what factor do you expect the global truncation error to decrease? Justify your answer with the order of the method.

### Q14.9: Heun Implementation (Code)
Write a Python function `heun_method(f, t0, y0, h, steps)` that returns arrays of $t$ and $y$. Include a docstring explaining the predictor-corrector logic.

### Q14.10: Predictor-Corrector Comparison (Code)
Write a script that solves $y' = y \cos(t), y(0)=1$ using both Euler and Heun. Plot the error $|y_{approx} - y_{exact}|$ on a log scale for both methods as a function of $t$.

---

## 15. Runge-Kutta 4th Order (RK4) (06_Differential_Equations)

### Q15.1: Manual RK4 Step (Manual)
Given $y' = t + y, y(0) = 1$, calculate $y(0.1)$ using a single step of RK4 ($h=0.1$). Show the values of $k_1, k_2, k_3, k_4$ clearly.

### Q15.2: RK4 vs Heun (Manual)
Compare the number of function evaluations required by RK4 and Heun's method to solve an ODE from $t=0$ to $t=1$ with a step size $h=0.1$. Which method is expected to be more accurate, and why?

### Q15.3: Symmetry of Slopes (Manual)
In the RK4 formula, why are $k_2$ and $k_3$ weighted by $2/6$ while $k_1$ and $k_4$ are weighted by $1/6$? Relate this to Simpson's 1/3 rule.

### Q15.4: RK4 for Autonomous Systems (Manual)
For the autonomous ODE $y' = y(1-y), y(0)=0.5$, calculate the first RK4 step with $h=0.2$.

### Q15.5: Order of Accuracy Verification (Manual)
If an RK4 implementation yields an error of $10^{-4}$ for $h=0.1$, estimate the error for $h=0.05$. Show the calculation using $O(h^4)$.

### Q15.6: Second-Order ODE with RK4 (Manual)
Convert $y'' + 4y = 0, y(0)=1, y'(0)=0$ into a system of first-order ODEs and write the RK4 vector update step for $\mathbf{k}_1$.

### Q15.7: Stability Region of RK4 (Manual)
The stability condition for RK4 on $y' = \lambda y$ is $|1 + z + \frac{z^2}{2} + \frac{z^3}{6} + \frac{z^4}{24}| \leq 1$, where $z = h\lambda$. For $\lambda = -10$, is $h=0.2$ stable?

### Q15.8: Butcher Tableau (Manual)
Briefly explain what a Butcher Tableau is and provide the tableau for the standard RK4 method.

### Q15.9: RK4 Implementation (Code)
Implement the `rk4_step(f, t, y, h)` function in Python. Then use it in a loop to solve $y' = -y + \sin(t), y(0)=1$ for 10 steps with $h=0.1$.

### Q15.10: Adaptive Step Size Concept (Code)
Write a pseudo-code or Python logic for \"RK45\" (Runge-Kutta-Fehlberg). How does it use two different orders to estimate the local error and adjust $h$?

---

## 16. Linear & Quadratic Splines (07_Interpolation)

### Q16.1: Linear Spline Construction (Manual)
Given data points $(1, 2), (3, 6), (5, 4)$, write the equations for the linear splines $s_1(x)$ and $s_2(x)$. Calculate the interpolated value at $x=4$.

### Q16.2: Quadratic Spline Equations (Manual)
For the points $(0, 0), (1, 1), (2, 5)$, set up the system of equations required to find the quadratic spline coefficients $a_i, b_i, c_i$ for each interval. Assume $a_1 = 0$.

### Q16.3: Derivative Continuity (Manual)
Prove that for a quadratic spline $f_i(x) = a_ix^2 + b_ix + c_i$, the condition for $C^1$ continuity at internal node $x_i$ is $2a_{i-1}x_i + b_{i-1} = 2a_ix_i + b_i$.

### Q16.4: Solving Quadratic Splines (Manual)
Solve the system from Q16.2 to find the exact polynomials for the intervals $[0, 1]$ and $[1, 2]$.

### Q16.5: Degree of Freedom Analysis (Manual)
If you have $n+1$ data points, how many unknown coefficients are there for quadratic splines? How many equations are provided by continuity and smoothness? Explain why one boundary condition is necessary.

### Q16.6: Linear vs Quadratic Smoothness (Manual)
Sketch or describe the first derivative $f'(x)$ for both a linear spline and a quadratic spline passing through the same 3 non-collinear points. Which one is continuous?

### Q16.7: Spline Error Bound (Manual)
The error for linear spline interpolation is bounded by $|f(x) - s(x)| \leq \frac{h^2}{8} \max |f''(x)|$. If $f(x) = \sin(x)$ and $h=0.1$, calculate the maximum possible error.

### Q16.8: Natural Boundary for Quadratic? (Manual)
Why is the condition $a_1=0$ commonly used for quadratic splines? What happens to the first segment of the spline under this condition?

### Q16.9: Linear Spline Implementation (Code)
Write a Python function `linear_spline(x_data, y_data, x_val)` that performs interpolation for any `x_val` within the range of `x_data`.

### Q16.10: Quadratic Spline Solver (Code)
Write a script that uses `numpy.linalg.solve` to find the coefficients of a quadratic spline for a given set of 4 points.

---

## 17. Newton Interpolation (Divided Differences) (07_Interpolation)

### Q17.1: Divided Difference Table (Manual)
Given points $(-1, 3), (0, 1), (1, 3), (2, 9)$, construct the complete divided difference table.

### Q17.2: Polynomial Construction (Manual)
Using the table from Q17.1, write the Newton form of the interpolating polynomial $P_3(x)$. Simplify it to standard form $ax^3 + bx^2 + cx + d$.

### Q17.3: Incremental Property (Manual)
If a new point $(3, 19)$ is added to the dataset in Q17.1, calculate only the additional divided difference needed to update the polynomial. Write the new term.

### Q17.4: Horner's Method Evaluation (Manual)
Evaluate $P(2.5)$ for the polynomial $P(x) = 1 + 2(x-0) + 0.5(x-0)(x-1)$ using the nested (Horner-like) form. Show the steps.

### Q17.5: Uniqueness of Interpolants (Manual)
Is the Newton interpolating polynomial different from the Lagrange interpolating polynomial for the same set of points? Justify your answer.

### Q17.6: Error Formula for Newton (Manual)
The error in Newton interpolation is $R_n(x) = f[x_0, \dots, x_n, x] \prod_{i=0}^n (x-x_i)$. If $f(x)$ is a polynomial of degree $n$, what is the error of $P_n(x)$?

### Q17.7: Divided Differences and Derivatives (Manual)
Show that $f[x_0, x_1]$ approaches $f'(x_0)$ as $x_1 \to x_0$.

### Q17.8: High-Order Oscillation (Manual)
Describe Runge's Phenomenon. Why does increasing the degree of the Newton polynomial not always improve the fit for certain functions?

### Q17.9: Divided Difference Generator (Code)
Write a Python function `divided_diff(x, y)` that returns the 2D table (matrix) of divided differences.

### Q17.10: Newton Polynomial Evaluator (Code)
Write a function `evaluate_newton(x_data, coefs, x)` that uses the coefficients from the divided difference table to calculate $P(x)$ efficiently.

---

## 18. Cubic Spline Interpolation (07_Interpolation)

### Q18.1: Cubic Spline Continuity Conditions (Manual)
List all the conditions (equations) required to define a cubic spline across $n$ intervals. How many total unknowns and equations are there?

### Q18.2: Natural Cubic Spline (Manual)
Define the \"Natural\" boundary condition for cubic splines. Why is it called \"natural\"? What does it imply about the curvature at the endpoints?

### Q18.3: Tridiagonal System Derivation (Manual)
The second derivatives $M_i = f''(x_i)$ of a cubic spline satisfy a tridiagonal system. Write the general equation for $M_i$ in terms of $M_{i-1}, M_i, M_{i+1}$ and the data values $y_i$.

### Q18.4: Manual Cubic Spline for 3 Points (Manual)
For points $(0, 0), (1, 1), (2, 0)$, set up the system to find the second derivatives $M_0, M_1, M_2$ for a natural cubic spline. Solve for $M_1$.

### Q18.5: Piecewise Polynomial Form (Manual)
Using $M_1$ from Q18.4, write the cubic polynomial $s_1(x)$ for the first interval $[0, 1]$.

### Q18.6: Clamped Boundary Condition (Manual)
How does a \"Clamped\" cubic spline differ from a \"Natural\" one? Write the boundary equations if the slopes at the ends are $f'(x_0) = S_0$ and $f'(x_n) = S_n$.

### Q18.7: Minimum Curvature Property (Manual)
Explain the statement: \"Cubic splines are the smoothest interpolants.\" What integral property do they minimize?

### Q18.8: Comparison with Newton Polynomial (Manual)
Compare a cubic spline and a 10th-degree Newton polynomial for interpolating 11 points. Discuss stability and \"wiggles.\"

### Q18.9: Cubic Spline Matrix Builder (Code)
Write a Python snippet to construct the tridiagonal matrix $A$ for the natural cubic spline system $AM = Y$ given $n$ intervals.

### Q18.10: SciPy Spline Usage (Code)
Write a script using `scipy.interpolate.CubicSpline` to interpolate $f(x) = \frac{1}{1+25x^2}$ on $[-1, 1]$ with 11 points. Plot the result.


---

## 19. Discrete Fourier Transform (DFT) (08_Fourier_Transforms)

### Q19.1: Manual N=4 DFT (Manual)
Given the sequence $x = [1, 2, 3, 4]$, calculate the full DFT $X_k$ for $k=0, 1, 2, 3$ using the formula $X_k = \sum_{n=0}^{N-1} x_n e^{-i rac{2\pi}{N} kn}$. Show all steps including the evaluation of the twiddle factors $W_N^{kn} = e^{-i rac{2\pi}{N} kn}$.

### Q19.2: High-Resolution Manual DFT Trace (N=12) (Manual)
Consider a sequence $x_n$ of length $N=12$, where $x_n = \cos(rac{\pi n}{6})$. Calculate the first three components ($X_0, X_1, X_2$) of the DFT. Provide the step-by-step expansion of the summation for $X_1$ to demonstrate the interaction between the signal and the complex roots of unity.

### Q19.3: Linearity and Shifting Theorems (Manual)
If the DFT of $x[n]$ is $X[k]$, prove the Time Shifting property: $DFT\{x[n-m]\} = X[k] e^{-i rac{2\pi}{N} km}$. Apply this to find the DFT of $y = [4, 1, 2, 3]$ given your result from Q19.1.

### Q19.4: Parseval's Theorem Verification (Manual)
Verify Parseval's Theorem ($\sum |x_n|^2 = rac{1}{N} \sum |X_k|^2$) for the sequence $x = [1, -1, 1, -1]$. Show the energy calculation in both time and frequency domains.

### Q19.5: Zero Padding and Spectral Resolution (Manual)
Suppose you have a 4-point sequence $x = [1, 1, 1, 1]$. 
1. Calculate its DFT $X_k$.
2. Zero-pad the sequence to $N=8$ and calculate the new DFT $Y_k$. 
3. Explain the difference between "increased spectral resolution" and "increased sampling in the frequency domain".

### Q19.6: The Leakage Phenomenon (Manual)
Explain why the DFT of $x_n = \sin(rac{2\pi \cdot 1.5 n}{N})$ will show "leakage" across all frequency bins, whereas $x_n = \sin(rac{2\pi \cdot 2 n}{N})$ will be concentrated in a single bin. Use the concept of periodic extension to justify your answer.

### Q19.7: Inverse DFT Matrix Form (Manual)
The DFT can be expressed as a matrix-vector multiplication $X = Wx$. 
1. Construct the $4 	imes 4$ DFT matrix $W_4$.
2. Derive the Inverse DFT matrix $W_4^{-1}$ and explain the significance of the $rac{1}{N}$ scaling factor.

### Q19.8: DFT of a Rectangular Pulse (Manual)
Calculate the DFT of a sequence $x_n = 1$ for $0 \leq n < M$ and $x_n = 0$ for $M \leq n < N$. Show that the magnitude $|X_k|$ follows a Dirichlet kernel (sinc-like) shape.

### Q19.9: Complexity Analysis of Naive DFT (Code)
Write a Python function `manual_dft(x)` that implements the $O(N^2)$ summation. Use it to compute the DFT of a random sequence of $N=1000$ and time the execution. Estimate how long it would take for $N=1,000,000$ based on this timing.

### Q19.10: Magnitude and Phase Spectrum Visualization (Code)
Write a script that generates a signal containing two frequencies (50Hz and 120Hz) sampled at 1000Hz. Compute the DFT using your `manual_dft`, then plot the Magnitude Spectrum and Phase Spectrum. Label the axes correctly with frequency in Hz.

---

## 20. Fast Fourier Transform (FFT) (08_Fourier_Transforms)

### Q20.1: Bit-Reversal Permutation (Manual)
To perform an in-place Radix-2 FFT, the input array must be reordered. 
1. List the indices 0 to 7 in binary.
2. Reverse the bits for each.
3. Determine the final bit-reversed order for an 8-point FFT.

### Q20.2: Cooley-Tukey Butterfly Diagram (Manual)
Draw the butterfly diagram for a 4-point Radix-2 Decimation-in-Time (DIT) FFT. Label all nodes ($x_n$), twiddle factors ($W_N^k$), and the final output $X_k$. Show the specific calculations for $X_1$ and $X_3$.

### Q20.3: Twiddle Factor Periodicities (Manual)
In a Radix-2 FFT of size $N=16$, identify which twiddle factors $W_{16}^k$ are used in the first, second, and third stages. How many unique complex multiplications are saved compared to the naive DFT?

### Q20.4: Radix-2 FFT Operation Count (Manual)
Derive the total number of complex multiplications and complex additions for a Radix-2 FFT of length $N = 2^m$. Show that the complexity is indeed $O(N \log_2 N)$.

### Q20.5: Decimation-in-Frequency (DIF) vs DIT (Manual)
Explain the structural difference between Decimation-in-Time (DIT) and Decimation-in-Frequency (DIF). Specifically, where do the twiddle factor multiplications occur in each?

### Q20.6: Symmetry in FFT of Real Signals (Manual)
If the input $x_n$ is purely real, prove that $X_k = X_{N-k}^*$ (Hermitian symmetry). How can this property be used to calculate two $N$-point real FFTs using a single $N$-point complex FFT?

### Q20.7: Butterfly Trace (Manual)
Given two complex numbers $A = 2+3i$ and $B = 1-i$, and a twiddle factor $W = e^{-i \pi/4}$, perform a single butterfly operation:
$X = A + WB$
$Y = A - WB$
Show the result in rectangular form.

### Q20.8: FFT of a Sine Wave (Manual)
Trace the FFT of $x = [0, 1, 0, -1]$ ($N=4$). Use the butterfly diagram logic to show why the magnitude is non-zero only at $k=1$ and $k=3$.

### Q20.9: Recursive FFT Implementation (Code)
Write a recursive Python function `fft_recursive(x)` based on the Cooley-Tukey DIT algorithm. Ensure it handles the base case $N=1$. Test it against `numpy.fft.fft`.

### Q20.10: Performance Comparison (Code)
Write a script to compare the execution time of your `manual_dft` (from Q19.9) and `fft_recursive` for $N = 2^4, 2^5, \dots, 2^{10}$. Plot the results on a log-log scale.

---

## 21. Gaussian Elimination & LU Decomposition (09_Linear_Algebra)

### Q21.1: Partial Pivoting Trace (Manual)
Solve the following system using Gaussian Elimination with Partial Pivoting:
$$
egin{bmatrix} 1 & 1 & 1 \ 2 & 4 & 2 \ 4 & 10 & 2 nd{bmatrix} egin{bmatrix} x_1 \ x_2 \ x_3 nd{bmatrix} = egin{bmatrix} 3 \ 8 \ 16 nd{bmatrix}
$$
Show the augmented matrix at each step and identify which rows were swapped.

### Q21.2: LU Decomposition (Doolittle Method) (Manual)
Find the $L$ and $U$ matrices for:
$$
A = egin{bmatrix} 2 & 3 & 1 \ 4 & 7 & 5 \ 0 & -2 & 2 nd{bmatrix}
$$
Assume $L$ has 1s on the diagonal ($l_{ii} = 1$). Show the inner-product calculations for each element.

### Q21.3: Operation Count for GE (Manual)
Calculate the exact number of floating-point operations (additions/subtractions and multiplications/divisions) required to reduce an $n 	imes n$ matrix to upper triangular form. Sum the series to show the $O(n^3/3)$ complexity.

### Q21.4: Forward and Backward Substitution (Manual)
Given $L = egin{bmatrix} 1 & 0 \ 3 & 1 nd{bmatrix}$, $U = egin{bmatrix} 2 & 5 \ 0 & -1 nd{bmatrix}$, and $b = egin{bmatrix} 7 \ 18 nd{bmatrix}$:
1. Solve $Ly = b$ for $y$.
2. Solve $Ux = y$ for $x$.

### Q21.5: Pivoting Necessity (Manual)
Consider the system $egin{bmatrix} psilon & 1 \ 1 & 1 nd{bmatrix} egin{bmatrix} x_1 \ x_2 nd{bmatrix} = egin{bmatrix} 1 \ 2 nd{bmatrix}$ where $psilon < psilon_{mach}$. 
1. Solve without pivoting.
2. Solve with partial pivoting.
3. Explain why the first result is numerically unstable.

### Q21.6: Condition Number and Stability (Manual)
Calculate the condition number $\kappa(A)_\infty$ for $A = egin{bmatrix} 1 & 100 \ 0 & 1 nd{bmatrix}$. If $b$ is perturbed by $\Delta b$, what is the maximum relative error in the solution $x$?

### Q21.7: LU for Tridiagonal Systems (Manual)
Show that the LU decomposition of a tridiagonal matrix results in $L$ and $U$ matrices that are also bidiagonal. How does this reduce the computational complexity from $O(n^3)$ to $O(n)$?

### Q21.8: Determinant from LU (Manual)
Explain how to calculate the determinant of a matrix $A$ using its LU decomposition. Find $|A|$ for the matrix in Q21.2.

### Q21.9: Gaussian Elimination with Pivoting (Code)
Write a Python function `gaussian_elimination(A, b)` that implements partial pivoting. Return the solution vector $x$. Test it with a $4 	imes 4$ Hilbert matrix (which is notoriously ill-conditioned).

### Q21.10: LU Decomposition Solver (Code)
Write a script that decomposes a matrix into $L$ and $U$, then solves $Ax=b$ for multiple $b$ vectors using forward and backward substitution. Explain why this is more efficient than running Gaussian Elimination multiple times.

---

## 22. Jacobi Iterative Method (09_Linear_Algebra)

### Q22.1: Strictly Diagonal Dominance (Manual)
Determine if the following matrices are strictly diagonally dominant. If not, can you rearrange the rows to make them so?
1. $A = egin{bmatrix} 1 & 2 \ 3 & 1 nd{bmatrix}$
2. $B = egin{bmatrix} 4 & 1 & 2 \ 1 & 5 & 1 \ 2 & 1 & 4 nd{bmatrix}$

### Q22.2: Manual Jacobi Step (Manual)
Perform two iterations of the Jacobi method for the system:
$$
egin{aligned}
10x_1 + x_2 + 2x_3 &= 3 \
x_1 + 10x_2 - x_3 &= 1.5 \
2x_1 + x_2 + 10x_3 &= -9
nd{aligned}
$$
Start with $x^{(0)} = [0, 0, 0]^T$.

### Q22.3: Iteration Matrix and Convergence (Manual)
Express the Jacobi iteration in the form $x^{(k+1)} = Mx^{(k)} + c$. Find $M$ and $c$ for the system in Q22.2. Calculate the spectral radius $ho(M)$ (max eigenvalue) to prove convergence.

### Q22.4: Jacobi vs Gauss-Seidel Logic (Manual)
Explain the difference in how $x_i^{(k+1)}$ is calculated in Jacobi vs Gauss-Seidel. Which one is generally faster? Which one is easier to parallelize?

### Q22.5: Matrix Splitting (Manual)
Show that the Jacobi iteration is derived from splitting $A = D + L + U$ where $D$ is diagonal, $L$ is strictly lower triangular, and $U$ is strictly upper triangular. Write the update rule in terms of these matrices.

### Q22.6: Stopping Criteria (Manual)
Define the relative residual $rac{\|b - Ax^{(k)}\|}{\|b\|}$ and the relative change $rac{\|x^{(k)} - x^{(k-1)}\|}{\|x^{(k)}\|}$. In what scenario might the relative change be small while the residual is still large?

### Q22.7: Convergence Speed (Manual)
If the spectral radius of the Jacobi iteration matrix is $ho(M) = 0.9$, estimate how many iterations are needed to reduce the initial error by a factor of $10^{-6}$.

### Q22.8: Sparse Matrix Advantage (Manual)
Explain why iterative methods like Jacobi are preferred over direct methods (like LU) for extremely large, sparse systems (e.g., $N=10^6$ with only 5 non-zeros per row). Discuss memory and operation counts.

### Q22.9: Jacobi Method Implementation (Code)
Write a Python function `jacobi(A, b, x0, tol, max_iter)` that returns the solution and the number of iterations taken. Include a check for diagonal dominance.

### Q22.10: Convergence Visualization (Code)
Using the system from Q22.2, write a script that plots the norm of the error $\|x^{(k)} - x_{true}\|$ versus the iteration number $k$ on a semi-log scale. Use `numpy.linalg.solve` to get $x_{true}$.
