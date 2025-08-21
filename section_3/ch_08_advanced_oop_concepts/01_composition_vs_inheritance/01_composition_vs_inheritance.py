'''Composition vs Inheritance


Object-oriented programming offers two main approaches for code reuse: inheritance ("is-a" relationship) and composition ("has-a" relationship).

Here is an example of inheritance creating an "is-a" relationship:

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):  # Dog "is an" Animal
    def bark(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.eat())   # Inherited method
print(dog.bark())  # Own method
Here is an example of composition creating a "has-a" relationship:

class Engine:
    def start(self):
        return "Engine started"
    
    def stop(self):
        return "Engine stopped"

class Car:  # Car "has an" Engine
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Uses composed engine
Compare both approaches with a more complex example:

# Inheritance approach
class Bird:
    def move(self):
        return "Flying"

class Duck(Bird):
    def quack(self):
        return "Quack!"

# Composition approach
class FlyBehavior:
    def move(self):
        return "Flying"

class SwimBehavior:
    def move(self):
        return "Swimming"

class Duck:
    def __init__(self):
        self.fly_behavior = FlyBehavior()
        self.swim_behavior = SwimBehavior()
    
    def fly(self):
        return self.fly_behavior.move()
    
    def swim(self):
        return self.swim_behavior.move()
    
    def quack(self):
        return "Quack!"
Test both approaches:

# Inheritance
duck1 = Duck()
print(duck1.move())  # Flying
print(duck1.quack()) # Quack!

# Composition  
duck2 = Duck()
print(duck2.fly())   # Flying
print(duck2.swim())  # Swimming
print(duck2.quack()) # Quack!
Output:

Buddy is eating
Woof!
Engine started
Flying
Quack!
Flying
Swimming
Quack!
Key differences:

Inheritance:

Tight coupling between parent and child
"Is-a" relationship
Changes to parent affect all children
Best for true hierarchical relationships
Composition:

Loose coupling between objects
"Has-a" relationship
More flexible - can change behavior at runtime
Easier to test and modify
Key Point: Use inheritance when you have a true "is-a" relationship. Use composition when you need flexibility and loose coupling. The principle "composition over inheritance" suggests favoring composition for most cases due to its flexibility and maintainability.

Challenge

In this challenge, you'll implement a media library system using both inheritance and composition patterns.

You need to edit the following files, following the TODO comments within each:

media.py, book.py, movie.py, musicalbum.py - For the inheritance implementation
mediaitem.py, bookcomposition.py, moviecomposition.py, musicalbumcomposition.py - For the composition implementation
Each media type should have:

Title, creator (author/director/artist), and year attributes
Appropriate display_info() method
'''