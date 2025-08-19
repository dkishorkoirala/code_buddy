'''
Method Overriding Revisited


Polymorphism means "many forms" and allows objects of different classes to respond differently to the same method call. Method overriding makes this possible.

Here is a parent class with a method:

class Animal:
    def speak(self):
        return "Animal makes a sound"
Create child classes that override the same method:

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"
Each child class provides its own implementation of speak().

Create a list of different animals:

animals = [Dog(), Cat(), Cow(), Animal()]
Call the same method on all objects:

for animal in animals:
    print(animal.speak())
Output:

Woof!
Meow!
Moo!
Animal makes a sound
This is polymorphism in action - the same method call behaves differently based on the object's actual type.

You can also use polymorphism with functions:

def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Woof!
make_animal_speak(cat)  # Meow!
The function doesn't need to know what type of animal it receives - it just calls speak() and gets the right behavior.

Key Point: Polymorphism lets you treat different objects the same way through a common interface. Method overriding provides different implementations, while polymorphism lets you call them uniformly. This makes code more flexible and easier to extend.

In this challenge, you'll implement a vehicle inheritance system.

You'll need to edit these files:

vehicle.py: Implement the base Vehicle class with make/model attributes and methods
car.py: Create the Car class that inherits from Vehicle
motorcycle.py: Create the Motorcycle class that inherits from Vehicle
truck.py: Create the Truck class that inherits from Vehicle
Each file contains detailed TODO comments to guide your implementation step-by-step. Pay attention to the import statements needed between files and follow the inheritance relationships. The driver.py file contains test cases that will verify your implementation works correctly across all vehicle types.
'''