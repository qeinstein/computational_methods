import math
from typing import Callable


def forward_first(f: Callable[[float], float], x: float, h: float) -> float:
	"""First-order forward difference approximation of f'(x)."""
	return (f(x + h) - f(x)) / h


def forward_three_point(f: Callable[[float], float], x: float, h: float) -> float:
	"""Second-order accurate forward derivative using f(x), f(x+h), f(x+2h)."""
	return (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h)


if __name__ == "__main__":
	# Demonstration: derivative of sin(x) at x=1.0
	f = math.sin
	df = math.cos
	x = 1.0
	print("True derivative cos(1.0):", df(x))

	for h in [1e-1, 1e-2, 1e-3, 1e-4, 1e-6, 1e-8]:
		d1 = forward_first(f, x, h)
		d2 = forward_three_point(f, x, h)
		err1 = abs(d1 - df(x))
		err2 = abs(d2 - df(x))
		print(f"h={h:.0e}  forward_first={d1:.12g} err={err1:.3g}  three_point={d2:.12g} err={err2:.3g}")
