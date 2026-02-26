# USing f_solve to find the root of a function
import numpy as np
from scipy import optimize # or from scipy.optimize import fsolve

f = lambda x: np.cos(x) - x
r = optimize.fsolve(f, -2)  # r is the root of f, i.e. f(r) = 0
print(f"Root of f: {r}")

# verification
result = f(r)
print(f"result = {result}")