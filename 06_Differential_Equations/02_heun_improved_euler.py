import numpy as np
from typing import Callable

def heun_method(f: Callable[[float, float], float], t0: float, y0: float, tn: float, h: float):
    """
    Solves the ODE dy/dt = f(t, y) using Heun's method (Improved Euler).

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
    n_steps = int((tn - t0) / h)
    t_values = np.zeros(n_steps + 1)
    y_values = np.zeros(n_steps + 1)
    
    t_values[0] = t0
    y_values[0] = y0
    
    for i in range(n_steps):
        t_curr = t_values[i]
        y_curr = y_values[i]
        t_next = t_curr + h
        
        # 1. Predictor step (Euler)
        k1 = f(t_curr, y_curr)
        y_predicted = y_curr + h * k1
        
        # 2. Corrector step
        k2 = f(t_next, y_predicted)
        y_values[i+1] = y_curr + (h / 2) * (k1 + k2)
        t_values[i+1] = t_next
        
    return t_values, y_values

if __name__ == "__main__":
    # Example: Solve dy/dt = t + y with y(0) = 1
    # Analytical solution: y(t) = 2*exp(t) - t - 1
    f = lambda t, y: t + y
    t0, y0, tn = 0, 1, 2
    exact_sol = lambda t: 2 * np.exp(t) - t - 1
    
    print(f"Solving dy/dt = t + y, y({t0}) = {y0} up to t = {tn}")
    print(f"{'h':>5} | {'Heun Approx':>15} | {'Exact':>15} | {'Error':>15}")
    print("-" * 60)
    
    exact_val = exact_sol(tn)
    
    for h in [0.5, 0.1, 0.01]:
        t, y = heun_method(f, t0, y0, tn, h)
        approx = y[-1]
        error = abs(approx - exact_val)
        print(f"{h:5.3f} | {approx:15.10f} | {exact_val:15.10f} | {error:15.10e}")
