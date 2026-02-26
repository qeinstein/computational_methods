import math
from typing import Callable


def central_first(f: Callable[[float], float], x: float, h: float) -> float:
	"""Second-order accurate central difference for first derivative."""
	return (f(x + h) - f(x - h)) / (2 * h)


def central_second(f: Callable[[float], float], x: float, h: float) -> float:
	"""Second-order accurate central difference for second derivative."""
	return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


if __name__ == "__main__":
	f = math.sin
	df = math.cos
	d2f = lambda x: -math.sin(x)
	x = 1.0
	print("True derivatives at x=1.0:", df(x), d2f(x))

	for h in [1e-1, 1e-2, 1e-3, 1e-4, 1e-6, 1e-8]:
		d1 = central_first(f, x, h)
		d2 = central_second(f, x, h)
		err1 = abs(d1 - df(x))
		err2 = abs(d2 - d2f(x))
		print(f"h={h:.0e}  central_first={d1:.12g} err={err1:.3g}  central_second={d2:.12g} err={err2:.3g}")
