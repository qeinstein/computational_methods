import numpy as np
from scipy.interpolate import interp1d

# Quadratic spline implementation using scipy for robustness
def quadratic_spline(x, y, x_new):
    f = interp1d(x, y, kind='quadratic')
    return f(x_new)

if __name__ == "__main__":
    x = np.linspace(0, 10, 5)
    y = np.sin(x)
    
    x_interp = 5.5
    y_interp = quadratic_spline(x, y, x_interp)
    print(f"Quadratic Spline at x={x_interp}: {y_interp:.4f}")
    print(f"Actual sin({x_interp}): {np.sin(x_interp):.4f}")
