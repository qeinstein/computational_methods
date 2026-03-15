import numpy as np
import matplotlib.pyplot as plt

def linear_spline(x_data, y_data, x_interp):
    """
    Performs linear spline interpolation.
    
    Args:
        x_data: Known x coordinates (must be sorted).
        y_data: Known y coordinates.
        x_interp: X coordinates to interpolate at.
        
    Returns:
        Interpolated y values.
    """
    return np.interp(x_interp, x_data, y_data)

if __name__ == "__main__":
    # Define some data points
    x = np.array([0, 1, 2, 5, 6])
    y = np.array([0, 0.8, 0.9, 0.1, 0.2])
    
    # Points to interpolate
    x_new = np.linspace(0, 6, 100)
    y_new = linear_spline(x, y, x_new)
    
    print("Data Points:")
    for xi, yi in zip(x, y):
        print(f"({xi}, {yi})")
        
    print(f"\nInterpolated value at x=1.5: {linear_spline(x, y, 1.5):.4f}")
    
    # Visualization
    # plt.plot(x, y, 'ro', label='Data points')
    # plt.plot(x_new, y_new, 'b-', label='Linear Spline')
    # plt.legend()
    # plt.show()
