# Basic visualization examples using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

def example_line():
    x = np.linspace(0, 2*np.pi, 100) # generate 100 points from 0 to 2*pi
    y = np.sin(x) # compute the sine of x
    plt.figure() # create a new figure
    plt.plot(x, y, label="sin(x)") # plot a line graph of sin(x)
    plt.title("Sine Function") # add a title to the plot
    plt.xlabel("x")  # label the x-axis
    plt.ylabel("sin(x)") # label the y-axis
    plt.legend() # add a legend to the plot
    plt.grid(True) # add a grid for better visibility
    plt.savefig("line_plot.png") # save the figure as a PNG file
    plt.close() # `close` the figure to free up memory

def example_scatter():
    x = np.random.rand(50) # generate 50 random x values between 0 and 1
    y = np.random.rand(50) # generate 50 random y values between 0 and 1
    colors = np.random.rand(50) # generate 50 random colors
    sizes = 100 * np.random.rand(50) # generate 50 random sizes for the points
    plt.figure() # create a new figure
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5) # create a scatter plot with random colors and sizes
    plt.title("Random Scatter") # add a title to the plot
    plt.savefig("scatter_plot.png") # save the figure as a PNG file
    plt.close() # `close` the figure to free up memory

def example_histogram():
    data = np.random.randn(1000) # generate 1000 random numbers from a normal distribution
    plt.figure() # create a new figure
    plt.hist(data, bins=30, color="blue", alpha=0.7) # create a histogram with 30 bins
    plt.title("Histogram of Gaussian Noise") # add a title to the plot
    plt.savefig("histogram.png") # save the figure as a PNG file
    plt.close() # `close` the figure to free up memory

if __name__ == "__main__":
    example_line()
    example_scatter()
    example_histogram()
    print("Plots saved as PNG files.")
