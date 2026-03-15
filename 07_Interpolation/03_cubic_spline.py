import numpy as np
from scipy.interpolate import CubicSpline

def cubic_spline_interp(x, y, x_new):
    """
    Computes Natural Cubic Spline interpolation.
    
    Args:
        x: Array of x-coordinates (must be strictly increasing).
        y: Array of y-coordinates.
        x_new: Point(s) to interpolate at.
        
    Returns:
        Interpolated y value(s).
    """
    # bc_type='natural' ensures second derivatives are zero at endpoints
    cs = CubicSpline(x, y, bc_type='natural')
    return cs(x_new)

if __name__ == "__main__":
    # Example data: Temperature readings over time
    time = np.array([0, 2, 4, 6, 8, 10])
    temp = np.array([15, 18, 22, 20, 17, 16])
    
    # Interpolate at a mid-point
    t_query = 5.0
    temp_query = cubic_spline_interp(time, temp, t_query)
    
    print(f"Data points (time, temp): {list(zip(time, temp))}")
    print(f"Interpolated temperature at t={t_query}: {temp_query:.2f}")
    
    # Verify that it passes through original points
    print(f"Verification at t=4: {cubic_spline_interp(time, temp, 4.0):.1f}")
