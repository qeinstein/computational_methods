# Computational Methods Practice Questions

This file contains 3 questions for each of the 22 topics covered in this repository. Each topic includes one Theoretical, one Manual Calculation, and one Code-based question.

---

## 1. Python Basics

### Q1.1: Function Scope and Mutability (Theoretical)
Explain the behavior of default arguments in Python when using mutable objects like lists. What is the danger of defining a function as `def add_item(item, box=[])`?

### Q1.2: Bitwise Logic Trace (Manual)
Trace the following code and determine the final value of `res`. Show the step-by-step binary transitions for each iteration of the loop.
```python
n = 13
res = 0
while n > 0:
    res = (res << 1) | (n & 1)
    n >>= 1
```

### Q1.3: Algorithm Implementation (Code)
Write a Python function `first_unique(s)` that returns the first non-repeating character in a string. If all characters repeat, return `None`. Use a dictionary to ensure the solution is efficient ($O(N)$).

---

## 2. Object-Oriented Programming

### Q2.1: Diamond Inheritance and super() (Theoretical)
Explain the Method Resolution Order (MRO) in Python. In a "Diamond" inheritance structure (A -> B, C; B, C -> D), how does `super()` ensure that each ancestor's method is called exactly once?

### Q2.2: Class vs Instance Variables (Manual)
Predict the output of the following code. Explain why `t1.count`, `t2.count`, and `Tracker.count` result in these specific values.
```python
class Tracker:
    count = 0
    def __init__(self, name):
        self.name = name
        Tracker.count += 1

t1 = Tracker("A")
t2 = Tracker("B")
t1.count = 10
print(t1.count, t2.count, Tracker.count)
```

### Q2.3: Operator Overloading (Code)
Implement a `Vector` class that supports 2D coordinates $(x, y)$. Overload the `__add__` and `__mul__` methods to support vector addition and scalar multiplication.

---

## 3. Data Visualization

### Q3.1: Axis Object Management (Theoretical)
Contrast the "state-machine" approach (`plt.plot()`) with the "object-oriented" approach (`fig, ax = plt.subplots()`). In what scenarios is the object-oriented approach significantly more advantageous?

### Q3.2: Histogram Binning Logic (Manual)
Given a dataset $D = [5, 7, 12, 18, 21, 28, 33]$, calculate the width of each bin and the count of data points per bin if you use exactly 3 bins (`plt.hist(D, bins=3)`).

### Q3.3: Dual-Axis Implementation (Code)
Write a Python script using Matplotlib to plot $y = x^2$ and $y = e^x$ on the same figure. Use `ax.twinx()` so that the two functions share the X-axis but have independent Y-axes with different scales.

---

## 4. Floating Point Representation

### Q4.1: Precision Loss in Summation (Theoretical)
Explain why the expression `(10**16 + 1) - 10**16` results in `0.0` in standard 64-bit floating-point arithmetic, while `1 + (10**16 - 10**16)` results in `1.0`. Reference the concept of relative precision.

### Q4.2: IEEE 754 Single Precision Conversion (Manual)
Convert the decimal number $-12.625$ into its IEEE 754 single-precision (32-bit) binary representation. Show the sign bit, the biased exponent, and the normalized mantissa.

### Q4.3: Finding Machine Epsilon (Code)
Write a Python script that calculates the machine epsilon ($\epsilon_{mach}$) of your system using a `while` loop. The script should determine the smallest positive value `eps` such that `1.0 + eps != 1.0`.

---

## 5. Error Analysis

### Q5.1: Condition Number and Stability (Theoretical)
Define the condition number of a function $\kappa(x)$. Explain what it means for a problem to be "ill-conditioned" and how a high condition number affects the reliability of numerical results.

### Q5.2: Error Propagation in Addition (Manual)
If two experimental measurements are given as $X = 100 \pm 0.5$ and $Y = 50 \pm 0.2$, calculate the absolute error and the relative error of their sum $S = X + Y$.

### Q5.3: Catastrophic Cancellation (Code)
Write a Python script that evaluates $f(x) = \sqrt{x+1} - \sqrt{x}$ for $x = 10^{14}$. Compare this result with the value obtained using the mathematically equivalent expression $1 / (\sqrt{x+1} + \sqrt{x})$ to demonstrate precision loss.

---

## 6. Bisection Method

### Q6.1: Continuity Requirement (Theoretical)
The Bisection Method relies on the Intermediate Value Theorem. Provide an example of a function $f(x)$ that is discontinuous on $[a, b]$ where the method would fail to find a root even if $f(a)f(b) < 0$.

### Q6.2: Manual Iteration (Manual)
Find the root of $f(x) = x^3 - 5$ on the interval $[1, 2]$ using the Bisection Method. Perform exactly 3 iterations and record the interval $[a, b]$, midpoint $m$, and $f(m)$ at each step.

### Q6.3: Bisection Implementation (Code)
Implement a robust Python function `bisection(f, a, b, tol)` that returns the root of function `f`. Include a check to ensure that the initial interval $[a, b]$ actually brackets a root.

---

## 7. Newton-Raphson Method

### Q7.1: Multiple Root Convergence (Theoretical)
Explain why Newton's method converges linearly instead of quadratically for a function with a multiple root (e.g., $f(x) = (x-1)^2$ at $x=1$). How does the ratio $e_{n+1}/e_n$ behave in this case?

### Q7.2: Manual Newton Step (Manual)
Apply two iterations of the Newton-Raphson method to find the square root of 3 (solve $x^2 - 3 = 0$), starting with an initial guess $x_0 = 2$. Round your results to 4 decimal places.

### Q7.3: Newton with Lambda (Code)
Write a Python function `newton(f, df, x0, tol)` that takes a function `f`, its derivative `df`, and an initial guess `x0`. Test it by finding the root of $x e^x - 1 = 0$.

---

## 8. Secant Method

### Q8.1: Secant vs Newton (Theoretical)
What is the primary computational advantage of the Secant method over the Newton-Raphson method? Discuss the trade-off in terms of the order of convergence ($\phi \approx 1.618$ vs $2.0$).

### Q8.2: Manual Secant Trace (Manual)
Perform 2 iterations of the Secant method to solve $f(x) = x^2 - 5 = 0$ using the initial guesses $x_0 = 2$ and $x_1 = 3$. Show the calculation for $x_2$ and $x_3$.

### Q8.3: Secant Implementation (Code)
Implement the `secant_method(f, x0, x1, tol)` function. Add a safeguard to prevent division by zero if $f(x_1) - f(x_0)$ becomes too small.

---

## 9. Forward & Backward Difference

### Q9.1: Error Scaling and Big-O (Theoretical)
Prove that the first-order forward difference formula has a truncation error of $O(h)$. What happens to the error if the step size $h$ is reduced by a factor of 10?

### Q9.2: Forward Difference Table (Manual)
Given $f(x) = x^3$, approximate $f'(1)$ using the forward difference formula with $h=0.1$ and $h=0.01$. Compare your results with the exact derivative $f'(1) = 3$.

### Q9.3: Forward Difference Implementation (Code)
Write a Python function `forward_diff(f, x, h)` that returns the derivative approximation. Create a loop that prints the error for $h = 10^{-1}, 10^{-2}, \dots, 10^{-6}$ for the function $f(x) = \sin(x)$ at $x=1$.

---

## 10. Central Difference & Higher Order

### Q10.1: Central Difference Accuracy (Theoretical)
Using Taylor series expansions, prove that the central difference formula $f'(x) \approx [f(x+h) - f(x-h)] / 2h$ is second-order accurate ($O(h^2)$).

### Q10.2: Second Derivative Central (Manual)
Derive the central difference formula for the second derivative $f''(x)$. Use this formula to approximate $f''(0)$ for $f(x) = e^x$ with $h=0.1$.

### Q10.3: Higher-Order Derivative Implementation (Code)
Write a Python function `second_deriv_central(f, x, h)` that computes the second derivative. Test it on $f(x) = x^4$ at $x=2$ and compare with the exact value 48.

---

## 11. Trapezoidal Rule

### Q11.1: Geometric Interpretation (Theoretical)
Explain why the Trapezoidal rule tends to over-estimate the integral of a "concave up" function ($f''(x) > 0$) and under-estimate a "concave down" function ($f''(x) < 0$).

### Q11.2: Single vs Composite (Manual)
Approximate $\int_0^1 x^2 dx$ using: (a) the single Trapezoidal rule ($n=1$), and (b) the composite Trapezoidal rule with $n=2$ ($h=0.5$). Calculate the absolute error for both.

### Q11.3: Composite Trapezoidal Implementation (Code)
Write a Python function `trapezoidal_composite(f, a, b, n)` that integrates a function `f` from `a` to `b` using $n$ intervals. Test it by integrating $\sin(x)$ from 0 to $\pi$.

---

## 12. Simpson's Rules

### Q12.1: Composite 1/3 Parity (Theoretical)
Explain why the composite Simpson's 1/3 rule requires an even number of intervals ($n$). What polynomial degree does Simpson's 1/3 rule integrate exactly?

### Q12.2: Comparison with Trapezoidal (Manual)
Approximate $\int_0^\pi \sin(x) dx$ using Simpson's 1/3 rule with $n=2$. Compare this result and its error to the Trapezoidal rule result with the same number of intervals.

### Q12.3: Simpson's 1/3 Implementation (Code)
Write a Python function `simpson13_composite(f, a, b, n)` that includes a check to ensure $n$ is even. Use it to integrate $f(x) = 1/(1+x^2)$ from 0 to 1 with $n=4$.

---

## 13. Euler's Method

### Q13.1: Local vs Global Error (Theoretical)
Distinguish between Local Truncation Error (LTE) and Global Truncation Error (GTE) for Euler's Method. Why is Euler's method considered a "first-order" method despite the LTE being $O(h^2)$?

### Q13.2: Single Step Trace (Manual)
Given the Initial Value Problem $y' = y + t, y(0) = 1$, use Euler's method with a step size $h=0.1$ to find the approximate value of $y(0.2)$ (two steps).

### Q13.3: Basic Euler Implementation (Code)
Write a Python function `euler_method(f, t0, y0, h, steps)` that returns an array of $t$ values and an array of $y$ values. Plot the results for $y' = -2y, y(0)=1$ up to $t=2$.

---

## 14. Heun's Method

### Q14.1: Predictor-Corrector Logic (Theoretical)
Explain the "Predictor-Corrector" mechanism used in Heun's method. How does it relate to the Trapezoidal rule for integration?

### Q14.2: Manual Heun Step (Manual)
Given $y' = y - t^2 + 1, y(0) = 0.5$, use Heun's method with $h = 0.2$ to calculate $y(0.2)$. Show both the Euler predictor step and the trapezoidal corrector step.

### Q14.3: Heun Implementation (Code)
Write a Python function `heun_method(f, t0, y0, h, steps)`. Use it to solve $y' = y \cos(t), y(0)=1$ and compare the result at $t=1$ with the exact solution $y = e^{\sin(t)}$.

---

## 15. Runge-Kutta 4th Order

### Q15.1: Symmetry of Slopes (Theoretical)
In the RK4 formula, we calculate four slopes ($k_1, k_2, k_3, k_4$). Explain the significance of the weights $(1/6, 2/6, 2/6, 1/6)$ and why $k_2$ and $k_3$ are sampled at the midpoint of the interval.

### Q15.2: Manual RK4 Step (Manual)
Given $y' = t + y, y(0) = 1$, calculate $y(0.1)$ using a single step of RK4 with $h=0.1$. List the values of $k_1, k_2, k_3,$ and $k_4$ explicitly.

### Q15.3: RK4 Implementation (Code)
Implement the `rk4_step(f, t, y, h)` function. Use it in a loop to solve the system $y' = -y + \sin(t), y(0)=1$ for 5 steps with $h=0.2$.

---

## 16. Linear & Quadratic Splines

### Q16.1: Degree of Freedom Analysis (Theoretical)
For a quadratic spline interpolation of $n+1$ points ($n$ intervals), how many total unknown coefficients are there? Explain why we need exactly one additional boundary condition (e.g., $a_1 = 0$) to solve the system.

### Q16.2: Linear Spline Construction (Manual)
Given the data points $(1, 2), (3, 6), (5, 4)$, derive the linear spline equations for each of the two intervals. Use these equations to find the interpolated value at $x=4$.

### Q16.3: Quadratic Spline Solver (Code)
Write a script that sets up and solves the linear system $Ax=b$ to find the coefficients of a quadratic spline for the points $(0, 0), (1, 1), (2, 5)$, assuming $a_1=0$.

---

## 17. Newton Interpolation

### Q17.1: Uniqueness of Interpolants (Theoretical)
Explain why the Newton form and the Lagrange form of the interpolating polynomial result in the exact same mathematical function for a given set of points, despite looking different.

### Q17.2: Divided Difference Table (Manual)
Given the points $(-1, 3), (0, 1), (1, 3), (2, 9)$, construct the complete divided difference table and write out the resulting Newton polynomial $P_3(x)$.

### Q17.3: Newton Polynomial Evaluator (Code)
Write a Python function `evaluate_newton(x_data, coefs, x)` that evaluates the Newton polynomial at a point `x` using the nested (Horner-like) form for efficiency.

---

## 18. Cubic Spline Interpolation

### Q18.1: Natural Boundary Conditions (Theoretical)
Define the "Natural" boundary condition for cubic splines ($M_0 = 0, M_n = 0$). What does this condition imply about the shape of the spline at its endpoints?

### Q18.2: Manual Cubic Spline (Manual)
For the points $(0, 0), (1, 1), (2, 0)$, set up the tridiagonal system for the second derivatives $M_0, M_1, M_2$ assuming natural boundaries. Solve for $M_1$.

### Q18.3: SciPy Spline Usage (Code)
Write a Python script using `scipy.interpolate.CubicSpline` to interpolate the function $f(x) = 1/(1+25x^2)$ on the interval $[-1, 1]$ using 11 equidistant points. Plot the result.

---

## 19. Discrete Fourier Transform

### Q19.1: The Leakage Phenomenon (Theoretical)
Explain why the DFT of a pure sine wave $\sin(2\pi f t)$ might show non-zero values in multiple frequency bins (leakage) if the frequency $f$ is not an integer multiple of the fundamental frequency $1/T$.

### Q19.2: Manual DFT Summation (N=11) (Manual)
Given a constant sequence $x_n = 5$ for all $n \in \{0, 1, \dots, 10\}$ (where $N=11$), write out the full summation for the DFT component $X_1$. Prove that $X_1 = 0$ by applying the geometric series formula $\sum_{n=0}^{N-1} r^n = (1-r^N)/(1-r)$.

### Q19.3: Naive DFT Complexity (Code)
Write a Python function `manual_dft(x)` that implements the $O(N^2)$ summation. Use it to compute the DFT of a random sequence of $N=512$ and verify the result against `numpy.fft.fft`.

---

## 20. Fast Fourier Transform

### Q20.1: Butterfly Structure (Theoretical)
Describe the "Butterfly" operation in the Radix-2 Cooley-Tukey FFT algorithm. How does this structure allow the FFT to reduce the complexity from $O(N^2)$ to $O(N \log N)$?

### Q20.2: Bit-Reversal Permutation (Manual)
List the indices 0 to 7 in binary, reverse the bits, and determine the final "bit-reversed" order used as the input for an 8-point Decimation-in-Time FFT.

### Q20.3: Recursive FFT Implementation (Code)
Write a recursive Python function `fft_recursive(x)` based on the Cooley-Tukey algorithm. Ensure it handles the base case $N=1$ and works for any input of length $N = 2^k$.

---

## 21. Gaussian Elimination & LU

### Q21.1: Operation Count (Theoretical)
Provide a high-level derivation of the $O(n^3/3)$ complexity for Gaussian Elimination. Why does the number of operations grow cubically with the size of the matrix?

### Q21.2: Partial Pivoting Trace (Manual)
Solve the following system using Gaussian Elimination with Partial Pivoting:
$$
\begin{bmatrix} 1 & 1 & 1 \\ 2 & 4 & 2 \\ 4 & 10 & 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 3 \\ 8 \\ 16 \end{bmatrix}
$$
Show the matrix after the first row swap and the first column elimination.

### Q21.3: Gaussian Elimination with Pivoting (Code)
Write a Python function `gaussian_elimination(A, b)` that implements partial pivoting. Test it by solving a $3 \times 3$ system of your choice.

---

## 22. Jacobi Iterative Method

### Q22.1: Convergence and Diagonal Dominance (Theoretical)
Define "Strict Diagonal Dominance". Why is this condition sufficient (though not always necessary) to guarantee the convergence of the Jacobi method?

### Q22.2: Manual Jacobi Step (Manual)
Perform two iterations of the Jacobi method for the system below, starting with $x^{(0)} = [0, 0, 0]^T$:
$$
10x_1 + x_2 + 2x_3 = 3 \\
x_1 + 10x_2 - x_3 = 1.5 \\
2x_1 + x_2 + 10x_3 = -9
$$

### Q22.3: Jacobi Method Implementation (Code)
Write a Python function `jacobi(A, b, x0, tol, max_iter)` that returns the solution vector. Ensure it uses the previous iteration's values exclusively to update the current vector (the "Jacobi" rule).
