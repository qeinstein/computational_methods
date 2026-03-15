# Euler Method

The Euler method is the most basic numerical procedure for solving ordinary differential equations (ODEs) with a given initial value. It is a first-order numerical procedure for solving initial value problems (IVPs).

## The Initial Value Problem (IVP)

Consider an ODE of the form:
$$\frac{dy}{dt} = f(t, y)$$
with the initial condition:
$$y(t_0) = y_0$$

We want to find the value of $y$ at a later time $t_n$.

## Derivation

The Euler method is derived from the Taylor expansion of $y(t+h)$ around $t$:
$$y(t+h) = y(t) + h y'(t) + \frac{h^2}{2} y''(\xi)$$
Substituting $y'(t) = f(t, y(t))$ and ignoring the higher-order terms ($O(h^2)$), we get the iterative formula:

$$y_{i+1} = y_i + h \cdot f(t_i, y_i)$$

where:
- $h$ is the step size.
- $t_{i+1} = t_i + h$.
- $y_i$ is the numerical approximation of $y(t_i)$.

![Euler Method Flowchart](https://kroki.io/graphviz/svg/eNpljssKwjAQRfd-xdCVj_oFNbpR3IgbdSEikjKjDcYkJCMYxH83rVVBl3M5c-5FdfLSVTCHO3hpzqi8WE8LMBYJdqGSjkRpbzkEjpqEt1eDhPsCViw9vwnSWrlAKd44lJw-tSxJiyyCgAgDqKAPxy7nEHsdThnXWZb4hbXuQysYgTkEJhcmWaps3KjkxZq6cmbwv_C1YzhuTK0vXT87thSy77o_ujG36NLW5OMJlj9bnA==)

## Geometric Interpretation

At each step, we use the slope of the function at the current point $(t_i, y_i)$ to predict the value of $y$ at the next point $t_{i+1}$. It's like following a straight line tangent to the curve at the current point.

## Error and Stability

- **Truncation Error:** The local truncation error is $O(h^2)$, while the global truncation error is $O(h)$. This makes it a **first-order** method.
- **Accuracy:** Because it only uses the slope at the *beginning* of the interval, it can deviate significantly from the true solution if the curve has high curvature or if the step size $h$ is too large.
- **Stability:** The Euler method can be unstable for certain types of "stiff" equations unless $h$ is extremely small.

## Example Usage

Implementation details and performance demonstrations can be found in `01_euler_method.py`.
