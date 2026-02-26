"""
02_newton_interpolation.py

Newton forward and backward interpolation for equally spaced data.

Provides:
- `difference_table(y)` - builds forward difference table from y-values
- `newton_forward(x_nodes, y_nodes, x)` - evaluate Newton forward polynomial at x
- `newton_backward(x_nodes, y_nodes, x)` - evaluate Newton backward polynomial at x

Examples are included in the `__main__` block.
"""

from typing import List, Tuple
import math


def difference_table(y: List[float]) -> List[List[float]]:
    """Build forward difference table.

    Returns a list of rows: table[0] = y, table[1] = Delta y, etc.
    table[k][i] = Delta^k y_i
    """
    n = len(y)
    table = [y[:]]
    for k in range(1, n):
        prev = table[-1]
        row = [prev[i+1] - prev[i] for i in range(len(prev)-1)]
        table.append(row)
    return table


def falling_factorial(s: float, k: int) -> float:
    """Compute s^(k) = s(s-1)...(s-k+1). Return 1 for k=0."""
    res = 1.0
    for i in range(k):
        res *= (s - i)
    return res


def newton_forward(x_nodes: List[float], y_nodes: List[float], x: float) -> float:
    """Evaluate Newton forward interpolation at x for equally spaced x_nodes.

    x_nodes must be equally spaced. Uses forward differences built from y_nodes.
    """
    n = len(x_nodes)
    if n != len(y_nodes):
        raise ValueError("x_nodes and y_nodes must have same length")
    h = x_nodes[1] - x_nodes[0]
    x0 = x_nodes[0]
    s = (x - x0) / h
    table = difference_table(y_nodes)
    result = 0.0
    for k in range(n):
        coeff = table[k][0]
        term = coeff * falling_factorial(s, k) / math.factorial(k)
        result += term
    return result


def newton_backward(x_nodes: List[float], y_nodes: List[float], x: float) -> float:
    """Evaluate Newton backward interpolation at x for equally spaced x_nodes.

    Uses the backward differences taken from the end of the table.
    """
    n = len(x_nodes)
    if n != len(y_nodes):
        raise ValueError("x_nodes and y_nodes must have same length")
    h = x_nodes[1] - x_nodes[0]
    xn = x_nodes[-1]
    s = (x - xn) / h
    table = difference_table(y_nodes)
    result = 0.0
    # backward differences: table[k][n-k-1] corresponds to nabla^k y_n
    for k in range(n):
        coeff = table[k][n-k-1]
        # rising factorial for backward: s(s+1)(s+2)... of length k
        # we can use (-1)^k * falling_factorial(-s, k) equivalently
        # but implement directly as product
        prod = 1.0
        for j in range(k):
            prod *= (s + j)
        term = coeff * prod / math.factorial(k)
        result += term
    return result


if __name__ == "__main__":
    # Demonstration: interpolate f(x)=x^2 at x=0.5 using nodes [0,0.25,0.5,0.75,1.0]
    x_nodes = [0.0, 0.25, 0.5, 0.75, 1.0]
    y_nodes = [xi**2 for xi in x_nodes]
    x_query = 0.5
    print("Nodes:", x_nodes)
    print("y:", y_nodes)
    print("Query x:", x_query)
    print("Forward interp at x=0.5:", newton_forward(x_nodes, y_nodes, x_query))
    print("Backward interp at x=0.5:", newton_backward(x_nodes, y_nodes, x_query))

    # Compare to exact
    print("Exact:", x_query**2)

    # Example: use a function not polynomial and see approximate value
    import math
    x_nodes2 = [0.0, 0.5, 1.0, 1.5]
    y_nodes2 = [math.sin(xi) for xi in x_nodes2]
    xq = 0.75
    print()
    print("sin nodes:", x_nodes2)
    print("sec forward interp sin(0.75):", newton_forward(x_nodes2, y_nodes2, xq))
    print("actual sin(0.75):", math.sin(xq))
