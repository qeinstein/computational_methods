# 03_visualization.py

import matplotlib.pyplot as plt
import numpy as np

def example_line():
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    plt.figure()
    plt.plot(x, y, label="sin(x)")
    plt.title("Sine Function")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("line_plot.png")
    plt.close()

def example_scatter():
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = 100 * np.random.rand(50)
    plt.figure()
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
    plt.title("Random Scatter")
    plt.savefig("scatter_plot.png")
    plt.close()

def example_histogram():
    data = np.random.randn(1000)
    plt.figure()
    plt.hist(data, bins=30, color="blue", alpha=0.7)
    plt.title("Histogram of Gaussian Noise")
    plt.savefig("histogram.png")
    plt.close()

if __name__ == "__main__":
    example_line()
    example_scatter()
    example_histogram()
    print("Plots saved as PNG files.")
