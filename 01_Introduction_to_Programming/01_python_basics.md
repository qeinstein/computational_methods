# Python Basics(CSC205)

### Python Variables 
They are essentially the building blocks for creating and managing python scripts or applications

Assignment Operator "=" is used to assign a value to a variable.

Restrictions to Python variable naming.
- Vars can only contain alphanumeric Characters as well as underscores
- First character of a var must always be a letter or an underscore.
- Spaces are not permitted within a variable name.
- variable names are case sensitive "X" is not the same as "x"



### Python Data-Types:
Basically int, float, string
There are others but those are the most important for now



### Python Operators
They're essentially the symbols that perform operations on values and variables. They're grouped into:
- Arithmetic operators: for math:
+, -, *, /, % (modulo), ** (power), // (floor division)

- Comparison operators – compare values and return True/False:
==, !=, <, >, <=, >=

- Assignment operators – assign or update variables:
=, +=, -=, *=, /=, etc.

- Logical operators – combine boolean expressions:
and, or, not

- Bitwise operators – work on binary digits:
&, |, ^, ~, <<, >>

- Membership operators – test membership in sequences:
in, not in

- Identity operators – check object identity:
is, is not


---

### Control Flow
Control flow statements like `if`, `elif`, and `else` let you us decisions. Loops (`for` and `while`) repeat actions.

```python
x = 10
if x > 5:
    print("large")
else:
    print("small")

for i in range(3):
    print(i)

while x > 0:
    x -= 2
```

### Functions and Modules
Functions are basically reusable pieces of code. Use `def` to define and `import` to bring in modules or to use a function in another dir.

```python
def greet(name):
    return f"Hello, {name}!"

import math
print(math.sqrt(16))
```

Modules are files containing Python definitions; use `import filename` (without `.py`) to access them.

### List Comprehensions and String Operations
List comprehensions provide a concise way to build lists.

```python
squares = [i**2 for i in range(5)] # This says, squares contains the squared value of every i in the range of one to 5.
even = [x for x in range(10) if x % 2 == 0] # This is the same as above, but a diff condition
```

Strings are immutable sequences; common operations include slicing, formatting, and methods like `.upper()`.

```python
text = "python"
print(text.capitalize())
print(text[::-1])  # reverse, python slicing
print(reversed(text)) # reverse also.
```

### File I/O Operations
Reading from and writing to files uses `open()` context managers.

```python
with open("example.txt", "w") as f:
    f.write("Hello\n")

with open("example.txt", "r") as f:
    print(f.read())
```

