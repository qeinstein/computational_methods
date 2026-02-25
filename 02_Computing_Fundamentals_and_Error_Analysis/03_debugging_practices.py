import logging
import math

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s') # set up logging for debugging


def faulty_function(x):
    # intentionally wrong: divides by zero for x==0
    assert x != 0, "x must not be zero"
    return 1 / x


def profile_example(n):
    # simple loop to profile
    total = 0
    for i in range(n):
        total += math.sqrt(i)
    return total


if __name__ == "__main__":
    # demonstration of assertion and logging
    try:
        print(faulty_function(0))
    except AssertionError as e:
        logging.error("Caught assertion: %s", e)

    print("faulty_function(5):", faulty_function(5))

    # profiling using timeit in script
    import timeit
    t = timeit.timeit('profile_example(10000)', globals=globals(), number=10)
    print(f"Time for profile_example: {t:.6f} seconds (10 runs)")

    # example debugging with print
    x = [1,2,3]
    print("Before modify", x)
    x.append(4)
    print("After modify", x)
