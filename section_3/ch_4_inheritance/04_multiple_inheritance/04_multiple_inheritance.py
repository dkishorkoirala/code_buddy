"""
Multiple Inheritance


Multiple inheritance allows a class to inherit from more than one parent class, combining functionality from different sources.

Here are two parent classes:

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

class Flyable:
    def fly(self):
        return f"{self.name} is flying"
Create a child class that inherits from both parents:

class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)  # Calls Animal's __init__
        self.species = species

    def sing(self):
        return f"{self.name} is singing"
The syntax class Bird(Animal, Flyable): means Bird inherits from both Animal and Flyable.

Create a bird object and use methods from both parents:

sparrow = Bird("Sparrow", "House sparrow")
Call methods from the first parent class:

print(sparrow.eat())
Call methods from the second parent class:

print(sparrow.fly())
Call the bird's own method:

print(sparrow.sing())
Output:

Sparrow is eating
Sparrow is flying
Sparrow is singing
You can check the inheritance order:

print(Bird.__mro__)  # Method Resolution Order
This shows which parent gets checked first when looking for methods.

Key Point: Multiple inheritance uses class Child(Parent1, Parent2): syntax. The child class gets all methods from all parent classes. Python checks parents from left to right when looking for methods.

Challenge

In this challenge, you'll implement a multi-file class system demonstrating multiple inheritance with smartphones. Each class is organized in its own file for better code organization.

You'll need to edit these files:

device.py - Implement the Device base class
internet.py - Implement the Internet base class
smartphone.py - Implement the Smartphone class that inherits from both base classes
driver.py - Implement test cases that will verify your implementation works correctly
Each file contains detailed TODO comments that will guide you step-by-step through the implementation.
"""
