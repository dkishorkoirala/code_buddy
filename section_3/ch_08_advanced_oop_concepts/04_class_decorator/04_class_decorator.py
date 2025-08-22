"""Class Decorators


Class decorators allow you to modify or enhance classes by wrapping them with another function. They work like function decorators but are applied to entire classes.

Here is a simple class without decoration:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"
Create a class decorator that adds a new method:

def add_farewell(cls):
    def farewell(self):
        return f"Goodbye from {self.name}"

    cls.farewell = farewell  # Add the method to the class
    return cls
Apply the decorator to a class using @:

@add_farewell
class EnhancedPerson:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"
Now the class has both original and added methods:

person = EnhancedPerson("Alice")
print(person.greet())     # Hello, my name is Alice
print(person.farewell())  # Goodbye from Alice
Key Point: Class decorators take a class as input, modify or enhance it, and return the modified class. They can add methods, modify attributes, or wrap existing functionality. Use @decorator_name above the class definition to apply them. This provides a clean way to extend class functionality without inheritance.

Challenge

In this challenge, you'll implement a class decorator that adds method call tracking functionality.

decorator.py - Implement the add_counter class decorator
calculator.py - Contains the classes that will use your decorator
The driver.py file contains extensive test scenarios that will validate your implementation against various use cases, inheritance patterns, and edge cases. You don't need to modify this file, but examining it will help you understand the expected behavior.
"""
