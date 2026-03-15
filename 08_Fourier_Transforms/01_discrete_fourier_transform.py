import numpy as np

def dft(x):
    """
    Computes the Discrete Fourier Transform of a 1D array x.
    Complexity: O(N^2)
    """
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x)

if __name__ == "__main__":
    # Create a simple signal: sum of two sine waves
    # f(t) = sin(2*pi*5*t) + 0.5*sin(2*pi*10*t)
    fs = 100 # Sampling frequency
    t = np.linspace(0, 1, fs, endpoint=False)
    x = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)
    
    # Compute DFT
    X = dft(x)
    
    # Frequency axis
    freqs = np.fft.fftfreq(fs, 1/fs)
    
    # Find dominant frequencies (magnitudes)
    magnitudes = np.abs(X)
    print("Top 5 dominant frequencies (indices):")
    print(np.argsort(magnitudes)[-5:])
    
    # Compare with NumPy's optimized FFT
    X_numpy = np.fft.fft(x)
    print(f"\nAll close to NumPy result: {np.allclose(X, X_numpy)}")
