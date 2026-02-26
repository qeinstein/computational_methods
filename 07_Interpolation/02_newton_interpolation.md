# Newton Forward and Backward Interpolation

This document describes Newton's forward and backward interpolation formulas for equally spaced data, how they are derived from forward differences, and how to use them in practice. The companion implementation is provided in `07_Interpolation/02_newton_interpolation.py`.

## Overview

- Forward/backward interpolation are polynomial interpolation techniques that are especially convenient when the data points are equally spaced with spacing $h$.
- They build the interpolating polynomial using forward differences $\Delta y_i = y_{i+1}-y_i$, $\Delta^2 y_i$, etc., rather than solving a Vandermonde system.

## Notation

- Data: $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$ with $x_i = x_0 + i h$ (uniform spacing $h$).
- Let $s = \dfrac{x - x_0}{h}$ (a normalized offset for forward interpolation) and for backward interpolation we often use $s = \dfrac{x - x_n}{h}$.

## Forward difference table


Construct the forward difference table starting from the original $y$ values. In display math form:

$$
\begin{array}{cccc}
y_0 & y_1 & y_2 & \dots \\
\Delta y_0 & \Delta y_1 & \dots & \\
\Delta^2 y_0 & \dots & & \\
\vdots & & &
\end{array}
$$

Compute differences column by column: $\Delta y_i = y_{i+1}-y_i$, $\Delta^2 y_i = \Delta(\Delta y_i)$, and so on. The coefficients for Newton forward polynomial are the top elements of each column: $y_0, \Delta y_0, \Delta^2 y_0, ...$.

## Newton forward interpolation formula

For $x$ near $x_0$ define $s = \dfrac{x-x_0}{h}$. The Newton forward interpolating polynomial is:

$$
P_f(x) = y_0 + s\Delta y_0 + \frac{s(s-1)}{2!}\Delta^2 y_0 + \frac{s(s-1)(s-2)}{3!}\Delta^3 y_0 + \cdots
$$

The general term uses falling factorials $s^{(k)} = s(s-1)\cdots(s-k+1)$ divided by $k!$.

## Newton backward interpolation formula

For $x$ near $x_n$ define $s = \dfrac{x-x_n}{h}$ (note $s$ may be negative). The Newton backward polynomial uses backward differences (or equivalently the forward differences taken from the end):

$$
P_b(x) = y_n + s\nabla y_n + \frac{s(s+1)}{2!}\nabla^2 y_n + \frac{s(s+1)(s+2)}{3!}\nabla^3 y_n + \cdots
$$

where $\nabla y_n = y_n - y_{n-1}$ and higher backward differences are defined similarly.

## When to use forward vs backward

- Use forward when $x$ is close to the beginning of the data ($x_0$).
- Use backward when $x$ is close to the end of the data ($x_n$).

## Practical steps to interpolate

1. Ensure nodes are equally spaced. If not, use other interpolation methods (Lagrange, Newton divided differences).
2. Build the forward difference table.
3. Choose forward or backward formula based on where $x$ is located relative to the data.
4. Evaluate the polynomial using the stored differences and the falling (or rising) factorial terms.

## Error and degree

- The interpolation polynomial of degree $m$ will exactly match the data for polynomials of degree $\le m$. The remainder term involves the $(m+1)$-th derivative of the true underlying function and the product $(x-x_0)(x-x_1)\cdots(x-x_m)$ scaled by $(m+1)!$.

## Example and implementation

See `07_Interpolation/02_newton_interpolation.py` for a detailed, well-commented implementation with examples and helper functions to build difference tables.

#### This is fully the courtesy of gpt, not me.