"""Basic Inheritance


Inheritance allows a class to inherit attributes and methods from another class, creating a parent-child relationship.

Here is an example of a parent class:

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"I am {self.name}, an animal")
Create a child class that inherits from the parent:

class Dog(Animal):
    pass  # Inherits everything from Animal
The syntax class Dog(Animal): means Dog inherits from Animal. Put the parent class name in parentheses.

Create objects from both classes:

generic_animal = Animal("Creature")
buddy = Dog("Buddy")
Use the inherited methods:

generic_animal.info()
buddy.info()
Output:

I am Creature, an animal
I am Buddy, an animal
Even though Dog doesn't define __init__ or info, it automatically gets them from Animal.

You can add new methods to the child class:

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

buddy = Dog("Buddy")
buddy.info()  # Inherited method
buddy.bark()  # New method
Output:

I am Buddy, an animal
Buddy says Woof!
Key Point: Child classes inherit all attributes and methods from their parent class. Use class Child(Parent): syntax to create inheritance. This helps you reuse code and create logical class hierarchies.

Challenge

vehicle.py: Contains the parent Vehicle class
car.py: Contains the Car class that inherits from Vehicle
driver.py: Main file to test your implementation
Each file contains detailed TODO comments to guide you through the implementation. You'll need to:

Complete the Vehicle class with make and model attributes
Implement proper class inheritance in the Car class
Set up the correct import statements between files
Create and test objects in the driver file
Follow the TODO comments carefully as they provide step-by-step guidance to the solution.

"""
