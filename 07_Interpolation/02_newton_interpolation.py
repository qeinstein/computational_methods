import numpy as np

def divided_differences(x, y):
    """Calculates the Newton divided differences table."""
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
            
    return coef[0, :] # The top row contains the coefficients a_i

def newton_poly(coef, x_data, x):
    """Evaluates the Newton polynomial at x."""
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n-k] + (x - x_data[n-k]) * p
    return p

if __name__ == "__main__":
    # Data points
    x = np.array([-5, -1, 0, 2])
    y = np.array([-2, 6, 1, 3])
    
    # Get coefficients
    a = divided_differences(x, y)
    print(f"Divided Difference Coefficients: {a}")
    
    # Interpolate at a specific point
    test_x = 1.0
    result = newton_poly(a, x, test_x)
    print(f"Interpolated value at x={test_x}: {result:.4f}")
