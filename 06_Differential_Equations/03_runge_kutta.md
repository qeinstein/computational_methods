# Runge-Kutta Methods

Runge-Kutta (RK) methods are a family of iterative methods used for the numerical solution of ordinary differential equations (ODEs). The most famous and widely used among them is the **Fourth-Order Runge-Kutta (RK4)** method.

## Fourth-Order Runge-Kutta (RK4)

The RK4 method is significantly more accurate than the Euler and Heun methods. It works by calculating the slope at four different points within the interval $[t_i, t_{i+1}]$ and taking a weighted average of these slopes.

### The Formula

For an IVP $\frac{dy}{dt} = f(t, y), y(t_0) = y_0$, the iteration is:

$$y_{i+1} = y_i + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

where:
- $k_1 = h \cdot f(t_i, y_i)$ (slope at the beginning of the interval)
- $k_2 = h \cdot f(t_i + \frac{h}{2}, y_i + \frac{k_1}{2})$ (slope at the midpoint, using $k_1$)
- $k_3 = h \cdot f(t_i + \frac{h}{2}, y_i + \frac{k_2}{2})$ (slope at the midpoint, using $k_2$)
- $k_4 = h \cdot f(t_i + h, y_i + k_3)$ (slope at the end of the interval, using $k_3$)

### Why is it $1/6$?
The coefficients $1/6, 2/6, 2/6, 1/6$ are derived to match the Taylor series expansion of the solution up to the fourth order ($O(h^4)$).

## Accuracy and Stability

- **Truncation Error:** The global truncation error is $O(h^4)$. This means if you halve the step size $h$, the error decreases by a factor of 16 ($2^4$).
- **Efficiency:** RK4 is the "workhorse" of ODE solvers. It provides a perfect balance between computational cost (4 function evaluations per step) and high accuracy.
- **Stability:** It is generally much more stable than lower-order methods for a given step size.

## Summary of Methods

| Method | Order | Slope Evaluations per Step |
| :--- | :--- | :--- |
| Euler | $O(h)$ | 1 |
| Heun's | $O(h^2)$ | 2 |
| RK4 | $O(h^4)$ | 4 |

## Example Usage

Implementation details and performance demonstrations can be found in `03_runge_kutta.py`.
