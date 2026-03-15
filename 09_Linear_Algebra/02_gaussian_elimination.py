import numpy as np

def gaussian_elimination(A, b):
    """Solves Ax = b using Gaussian elimination with back substitution."""
    n = len(b)
    # Augment matrix A with b
    Ab = np.column_stack((A, b)).astype(float)
    
    # Forward elimination
    for i in range(n):
        # Pivot selection (simple)
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
            
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
        
    return x

if __name__ == "__main__":
    A = np.array([[3, 2, -1],
                  [2, -2, 4],
                  [-1, 0.5, -1]])
    b = np.array([1, -2, 0])
    
    x = gaussian_elimination(A, b)
    print(f"Solution x: {x}")
    
    # Verify Ax = b
    print(f"Check Ax: {A @ x} (Should be {b})")
