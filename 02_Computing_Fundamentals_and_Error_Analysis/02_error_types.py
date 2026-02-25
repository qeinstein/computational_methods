
import math

# simple error calculations

def abs_error(true_val, approx_val):
    return abs(true_val - approx_val)


def rel_error(true_val, approx_val):
    if true_val == 0:
        return float('inf')
    return abs_error(true_val, approx_val) / abs(true_val)


# propagate error for sum and product

def propagate_add(e1, e2):
    # worst-case absolute error
    return abs(e1) + abs(e2)


def propagate_mul(x, y, ex, ey):
    # approximate relative error propagation: |f|*(|ex/x|+|ey/y|)
    return abs(x * y) * (abs(ex / x) + abs(ey / y))


if __name__ == "__main__":
    pi_true = math.pi
    approximations = [3.14, 22/7, 3.14159]
    for a in approximations:
        print(f"approx {a}: abs error {abs_error(pi_true,a):.6g}, rel {rel_error(pi_true,a):.6g}")

    # demonstrate propagation
    e1, e2 = 1e-5, 2e-5
    print("add propagation (abs):", propagate_add(e1, e2))
    print("mul propagation (approx):", propagate_mul(100.0, 0.01, e1, e2))

    # cancellation example
    a = 1e8 + 1.0
    b = 1e8
    print("a - b =", a - b)
    # relative error when true result is 1
    print("relative error of subtraction:", rel_error(1.0, a-b))
