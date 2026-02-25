# Data Visualization with Matplotlib

Matplotlib is the conventional plotting library for Python(That's what i use at least). This module introduces basic plotting techniques i matplotlib.

## Getting Started

Import `matplotlib.pyplot` (conventionally as `plt`) and create figures:

```python
import matplotlib.pyplot as plt

plt.plot([1,2,3],[4,5,6])
plt.show()
```

## Plot Types

- **Line plots:** `plt.plot(x,y)`
- **Scatter plots:** `plt.scatter(x,y)`
- **Bar charts:** `plt.bar(categories, values)`
- **Histograms:** `plt.hist(data, bins=10)`

## Customization

Add titles, labels, legends, gridlines:

```python
plt.title("Title")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["data"])
plt.grid(True) # 
```

### Subplots

Use `plt.subplot` or `plt.subplots` to create multiple plots in one figure.

```python
fig, axs = plt.subplots(2,1)
axs[0].plot(x, y)
axs[1].hist(data)
```

### Saving Figures

```python
plt.savefig("output.png")
```

`03_visualization.py` contains examples that generate and save plots so you can see.
