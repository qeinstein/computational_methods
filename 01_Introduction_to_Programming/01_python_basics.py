# Vars and data types
x = 10
y = 3.14
name = "FLuxx" # string 
flag = True # boolean

# basic operations
print("Add:", x + y) # 13.14: int and float can be added
print("Multiply:", x * y) # 31.4: int and float can be multiplied
print("Comparison:", x > y) # true: x is greater than y

# Control flow
for i in range(3):
    print("Loop", i)
    """
    Output:
    Loop 0
    Loop 1
    Loop 2
    """

if x % 2 == 0:
    print("x is even")
    # would print "x is even" since 10 is divisible by 2
else:
    print("x is odd")



# Functions and modules
def square(z):
    return z * z


import math

print("sqrt(16):", math.sqrt(16))
print("square(5):", square(5))


# List comprehension
squares = [i**2 for i in range(10)]
print("squares:", squares) # squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# String operations
msg = "hello"
print(msg.capitalize(), msg[::-1]) # Hello olleh: capitalize() makes the first letter uppercase(NOTE: It doesn't make the whole work uppercase), [::-1] reverses the string

# File I/O
with open("sample.txt", "w") as f:
    f.write("first line\nsecond line\n")

with open("sample.txt", "r") as f:
    print("Contents of sample.txt:")
    print(f.read())
