# Defining a base class and derived classes to demonstrate inheritance and polymorphism
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "<silence>"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"

# static and class methods
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return f"{cls.__name__} provides math utilities"

# simple factory pattern
def animal_factory(animal_type, name):
    if animal_type == "dog":
        return Dog(name)
    elif animal_type == "cat":
        return Cat(name)
    else:
        return Animal(name)

if __name__ == "__main__":
    pets = [Dog("Fido"), Cat("Whiskers")]
    for p in pets:
        print(p.name, "says", p.speak())

    print(MathHelper.add(2,3))
    print(MathHelper.description())

    a = animal_factory("dog", "Rex")
    print(a, a.speak())
# run the code to see the output 