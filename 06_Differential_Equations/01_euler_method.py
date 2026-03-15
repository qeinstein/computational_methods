import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

def euler_method(f: Callable[[float, float], float], t0: float, y0: float, tn: float, h: float):
    """
    Solves the ODE dy/dt = f(t, y) using the Euler method.

    Args:
        f: The function f(t, y) representing the slope.
        t0: Initial time.
        y0: Initial value of y at t0.
        tn: Final time to solve for.
        h: Step size.

    Returns:
        t_values: Array of time points.
        y_values: Array of approximated y values.
    """
    # Calculate number of steps
    n_steps = int((tn - t0) / h)
    
    # Initialize arrays
    t_values = np.zeros(n_steps + 1)
    y_values = np.zeros(n_steps + 1)
    
    # Initial conditions
    t_values[0] = t0
    y_values[0] = y0
    
    # Iteration
    for i in range(n_steps):
        # Apply Euler formula: y_next = y_current + h * f(t_current, y_current)
        y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])
        t_values[i+1] = t_values[i] + h
        
    return t_values, y_values

if __name__ == "__main__":
    # Example: Solve dy/dt = y with y(0) = 1
    # Analytical solution: y(t) = exp(t)
    f = lambda t, y: y
    t0, y0, tn = 0, 1, 2
    
    print(f"Solving dy/dt = y, y({t0}) = {y0} up to t = {tn}")
    print(f"{'h':>5} | {'Approx y(2)':>15} | {'Exact y(2)':>15} | {'Error':>15}")
    print("-" * 60)
    
    exact_y_tn = np.exp(tn)
    
    for h in [0.5, 0.1, 0.01, 0.001]:
        t, y = euler_method(f, t0, y0, tn, h)
        approx_y_tn = y[-1]
        error = abs(approx_y_tn - exact_y_tn)
        print(f"{h:5.3f} | {approx_y_tn:15.10f} | {exact_y_tn:15.10f} | {error:15.10e}")

    # Visualization (Optional but helpful)
    # plt.plot(t, y, label='Euler Approximation')
    # t_exact = np.linspace(t0, tn, 100)
    # plt.plot(t_exact, np.exp(t_exact), 'r--', label='Exact Solution')
    # plt.legend()
    # plt.show()
