# Fast Fourier Transform (FFT)

The Fast Fourier Transform (FFT) is an efficient algorithm for calculating the Discrete Fourier Transform (DFT). It is one of the most important algorithms in modern computing.

## The Cooley-Tukey Algorithm

The most common FFT algorithm is the Cooley-Tukey algorithm, which uses a "divide and conquer" approach. It recursively breaks down a DFT of size $N$ into two smaller DFTs of size $N/2$.

### The Principle

$$X_k = \sum_{n=0}^{N-1} x_n e^{-i \frac{2\pi}{N} kn}$$
This can be split into even-indexed and odd-indexed terms:
$$X_k = \text{Even}_k + e^{-i \frac{2\pi}{N} k} \cdot \text{Odd}_k$$

## Computational Cost

The FFT reduces the complexity from $O(N^2)$ to **$O(N \log N)$**.
For $N = 1024$:
- $N^2 \approx 1,000,000$ operations.
- $N \log_2 N \approx 10,000$ operations.
The FFT is roughly **100 times faster** for this small example!

## Example Usage

NumPy provides a highly optimized implementation in `np.fft.fft()`. See `02_fast_fourier_transform.py` for demonstrations.
