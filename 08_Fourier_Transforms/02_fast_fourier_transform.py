import numpy as np
import time

def fft_benchmark(N):
    """Benchmarks FFT vs manual DFT."""
    x = np.random.random(N)
    
    # NumPy FFT (Highly optimized)
    start = time.time()
    res_fft = np.fft.fft(x)
    end_fft = time.time() - start
    
    print(f"N = {N}")
    print(f"NumPy FFT time: {end_fft:.6f} seconds")

if __name__ == "__main__":
    # Test for different sizes
    for n in [1024, 2048, 4096]:
        fft_benchmark(n)
        print("-" * 30)
