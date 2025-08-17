"""The super() Function


The super() function allows a child class to call methods from its parent class. This lets you extend parent functionality rather than completely replace it.

Here is an example of using super() in the constructor:

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent's __init__
        self.breed = breed
        print(f"Dog breed set: {breed}")
Create a dog object:

buddy = Dog("Buddy", "Golden Retriever")
print(f"Name: {buddy.name}, Breed: {buddy.breed}")
Output:

Animal created: Buddy
Dog breed set: Golden Retriever
Name: Buddy, Breed: Golden Retriever
Use super() to extend parent methods:

class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # Call parent's method first
        print("Woof!")        # Add dog-specific behavior
Call the extended method:

buddy = Dog("Buddy", "Golden Retriever")
buddy.make_sound()
Output:

Generic animal sound
Woof!
Without super(), you would lose the parent's functionality:

class Cat(Animal):
    def make_sound(self):
        print("Meow!")  # Only cat sound, parent method ignored

cat = Cat("Whiskers")
cat.make_sound()
Output:

Meow!
Key Point: Use super() to call parent class methods from child classes. This allows you to extend functionality rather than completely replace it. Common uses include calling parent __init__ methods and extending parent behavior.

Challenge

In this challenge, you'll implement a Person and Employee class hierarchy using inheritance.

person.py: Contains the Person class with name and age attributes
employee.py: Contains the Employee class that inherits from Person
driver.py: Main file to test your implementation
Each file contains detailed TODO comments to guide you through the implementation.
"""
