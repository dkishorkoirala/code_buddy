"""
Method Overriding


Method overriding allows a child class to provide its own implementation of a method that already exists in the parent class.

Here is an example of a parent class with methods:

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic animal sound")

    def info(self):
        print(f"I am {self.name}")
Create a child class that overrides one method:

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")  # Override the parent method
The make_sound method in Dog replaces the one from Animal, but info is still inherited unchanged.

Create instances and test the methods:

animal = Animal("Generic Animal")
dog = Dog("Buddy")
Call the overridden method:

animal.make_sound()
dog.make_sound()
Call the non-overridden method:

animal.info()
dog.info()
Output:

Some generic animal sound
Woof! Woof!
I am Generic Animal
I am Buddy
You can override any inherited method:

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

    def info(self):
        print(f"I am {self.name}, a sneaky cat")

cat = Cat("Whiskers")
cat.make_sound()
cat.info()
Output:

Meow!
I am Whiskers, a sneaky cat
Key Point: Method overriding lets child classes customize inherited behavior. Simply define a method with the same name in the child class. The child's version will be used instead of the parent's version.

Challenge

In this challenge, you'll implement a shape hierarchy.

shape.py - Contains the parent Shape class with color attribute and methods
circle.py - Contains the Circle class that inherits from Shape
square.py - Contains the Square class that inherits from Shape
Each file contains detailed TODO comments that will guide you step-by-step through the implementation.
"""
