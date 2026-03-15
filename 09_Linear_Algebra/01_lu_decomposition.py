import numpy as np
from scipy.linalg import lu

def manual_lu(A):
    """
    Performs manual LU decomposition of a square matrix A.
    Returns L and U.
    """
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy().astype(float)
    
    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, :] -= factor * U[i, :]
            
    return L, U

if __name__ == "__main__":
    A = np.array([[2, -1, -2],
                  [-4, 6, 3],
                  [-4, -2, 8]])
    
    L, U = manual_lu(A)
    
    print("Matrix A:")
    print(A)
    print("\nL (Lower Triangular):")
    print(L)
    print("\nU (Upper Triangular):")
    print(U)
    
    # Verification
    print("\nL * U matches A:")
    print(np.allclose(L @ U, A))
