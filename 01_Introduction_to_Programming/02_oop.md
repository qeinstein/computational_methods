# Object-Oriented Programming (OOP)

Object-oriented programming is a paradigm that organizes software design around **objects** rather than functions and logic. An object is an instance of a **class**, which can contain data (attributes) and behavior (methods).

## Classes and Objects

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}"
```

Here `Person` is a class; `p = Person("Alice")` creates an object (instance), basically creating a new person.

## Inheritance and Polymorphism

Subclasses can inherit attributes and methods from parent classes, and override them:

```python
class Animal:
    def speak(self):
        return "<silence>"

class Dog(Animal):  # Dog is a subclass of animal because 
    def speak(self):
        return "Woof!"
```

Polymorphism allows code to use these objects interchangeably.

## Encapsulation and Abstraction

Attributes can be made private (by convention with `_` or `__` prefixes); properties provide controlled access.

```python
class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    """Getter : retrieves balance"""
    def balance(self): 
        return self._balance
```

## Static and Instance Methods

Instance methods operate on `self`; static methods are utility functions(They are bundled with the class but they're independenet of instances), and class methods receive the class.

```python
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return f"{cls.__name__} has math tools"
```

## Practical Design Patterns

- **Factory:** function that returns different class instances.
- **Singleton:** ensure only one instance exists (not shown).
- **Adapter, Decorator, etc.**

The `02_oop.py` file contains working examples.
