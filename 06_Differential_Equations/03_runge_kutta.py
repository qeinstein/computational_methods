import numpy as np
from typing import Callable

def rk4_method(f: Callable[[float, float], float], t0: float, y0: float, tn: float, h: float):
    """
    Solves the ODE dy/dt = f(t, y) using the Fourth-Order Runge-Kutta (RK4) method.

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
        t = t_values[i]
        y = y_values[i]
        
        # Calculate 4 slopes (stages)
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        # Weighted average of slopes
        y_values[i+1] = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        t_values[i+1] = t + h
        
    return t_values, y_values

if __name__ == "__main__":
    # Example: Solve dy/dt = y - t^2 + 1 with y(0) = 0.5
    # Analytical solution: y(t) = (t+1)^2 - 0.5*exp(t)
    f = lambda t, y: y - t**2 + 1
    t0, y0, tn = 0, 0.5, 2
    exact_sol = lambda t: (t + 1)**2 - 0.5 * np.exp(t)
    
    print(f"Solving ODE, y({t0}) = {y0} up to t = {tn}")
    print(f"{'h':>5} | {'RK4 Approx':>15} | {'Exact':>15} | {'Error':>15}")
    print("-" * 60)
    
    exact_val = exact_sol(tn)
    
    for h in [0.5, 0.1, 0.01]:
        t, y = rk4_method(f, t0, y0, tn, h)
        approx = y[-1]
        error = abs(approx - exact_val)
        print(f"{h:5.3f} | {approx:15.10f} | {exact_val:15.10f} | {error:15.10e}")
