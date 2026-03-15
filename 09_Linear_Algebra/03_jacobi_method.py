import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iter=100):
    """
    Solves Ax = b using the Jacobi iterative method.
    """
    n = len(b)
    x = x0.copy().astype(float)
    D = np.diag(A)
    R = A - np.diag(D)
    
    for k in range(max_iter):
        x_new = (b - np.dot(R, x)) / D
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Converged in {k+1} iterations.")
            return x_new
        
        x = x_new
        
    print("Warning: Did not converge within max iterations.")
    return x

if __name__ == "__main__":
    # Diagonally dominant matrix
    A = np.array([[10, -1, 2],
                  [-1, 11, -1],
                  [2, -1, 10]])
    b = np.array([6, 25, -11])
    x0 = np.zeros(len(b))
    
    solution = jacobi(A, b, x0)
    print(f"Jacobi solution: {solution}")
    print(f"Check Ax: {A @ solution} (Should be {b})")
