# Discrete Fourier Transform (DFT)

The Discrete Fourier Transform (DFT) is a mathematical technique used to transform a sequence of values from the time (or spatial) domain into the frequency domain.

## The Concept

The DFT decomposes a signal into a sum of sine and cosine waves of different frequencies. It is the discrete equivalent of the continuous Fourier Transform.

## The Formula

For a sequence of $N$ complex numbers $x_0, x_1, \dots, x_{N-1}$, the DFT is defined as:
$$X_k = \sum_{n=0}^{N-1} x_n \cdot e^{-i \frac{2\pi}{N} kn}$$
where:
- $X_k$ is the $k$-th frequency component.
- $i$ is the imaginary unit.
- $e^{-i \theta} = \cos(\theta) - i \sin(\theta)$ (Euler's formula).

![DFT Flowchart](https://kroki.io/graphviz/svg/eNplj81uwjAQhF9llFMJjfi5Ru4FCuICh_ZQKcrB1KtixVpbjpGCUN-9JmmCCLfRzLeaWaV_vHQnbHGFl1wp7cXnOgdbRSjqk3QkjrZ5RR0uhoS3Z1akyhwfQfrQE2SMdjVF-3AO5FEYeSQjko31qCAwR7DYZ4skEjvmEcEjYiXN9wB8FVWJqUBTcIkU1LiXbOl0qtMq5dl-cjt4Z_W8pBuYvf1PiqJrjqIt6I387j-OX1umZHgpxm3NKPz9Aw0jZnk=)

## Computational Cost


The basic DFT calculation involves a double loop (summation over $N$ terms for each of the $N$ frequency components). This results in a complexity of **$O(N^2)$**, which becomes very slow for large signals.

## Applications

- Signal processing (filtering, noise reduction).
- Image compression (JPEG).
- Analyzing the frequency content of any periodic data.

## Example Usage

See `01_discrete_fourier_transform.py` for a manual implementation.
