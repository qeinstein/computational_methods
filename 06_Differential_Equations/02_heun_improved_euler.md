# Heun's Method (Improved Euler)

Heun's method, also known as the **Improved Euler method** or the **Predictor-Corrector method**, is a second-order numerical procedure for solving ordinary differential equations (ODEs).

## The Concept

The basic Euler method is inaccurate because it only uses the slope at the *beginning* of the interval. Heun's method improves this by:
1.  **Predicting:** Use the Euler method to estimate the value of $y$ at the next step ($y_{i+1}^*$).
2.  **Correcting:** Use the average of the slope at the current point and the slope at the predicted point to calculate the final $y_{i+1}$.

## The Formula

The iterative process for Heun's method is:

1.  **Predictor step (Euler):**
    $$\tilde{y}_{i+1} = y_i + h \cdot f(t_i, y_i)$$

2.  **Corrector step (Trapezoidal):**
    $$y_{i+1} = y_i + \frac{h}{2} [f(t_i, y_i) + f(t_{i+1}, \tilde{y}_{i+1})]$$

where:
- $h$ is the step size.
- $t_{i+1} = t_i + h$.

## Accuracy and Error

- **Truncation Error:** Heun's method has a global truncation error of $O(h^2)$, making it a **second-order** method.
- **Comparison:** It is significantly more accurate than the Euler method ($O(h)$) for the same step size $h$, as it accounts for the curvature of the solution.

## Geometric Interpretation

While Euler's method follows the tangent line at the start of the interval, Heun's method calculates two slopes (start and predicted end) and uses their average. This is equivalent to applying the **Trapezoidal Rule** to the integral form of the ODE.

## Example Usage

Implementation details and performance demonstrations can be found in `02_heun_improved_euler.py`.
