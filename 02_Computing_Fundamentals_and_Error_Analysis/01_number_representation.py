# conversions

def show_bases(n): # show the number in different bases
    print(f"Decimal: {n}")
    print(f"Binary: {bin(n)}")
    print(f"Hex: {hex(n)}")


def float_identity(x): # show the internal representation of a float
    print(f"x = {x}
x in hex = {x.hex()}\n")


def machine_epsilon():
    eps = 1.0
    while 1.0 + eps/2.0 != 1.0:
        eps /= 2.0
    return eps


if __name__ == "__main__":
    print("Base conversions for 42:")
    show_bases(42)
    print()
    print("Floating-point inspection of 0.1 and 0.2:")
    float_identity(0.1)
    float_identity(0.2)
    print("0.1 + 0.2 == 0.3?", 0.1 + 0.2 == 0.3)
    print("actual sum:", 0.1 + 0.2)
    print()
    print("Machine epsilon for float:", machine_epsilon())
    # show effect of adding small value to large
    big = 1e16
    small = 1.0
    print("big + small == big?", big + small == big)
    print("big + (small*2):", big + (small*2))
    print("difference big+(small*2)-big:", (big+(small*2))-big)
