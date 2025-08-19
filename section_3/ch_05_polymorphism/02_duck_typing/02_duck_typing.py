'''Duck Typing


Duck typing focuses on what an object can do, not what it is. If an object has the methods you need, you can use it - regardless of its class type.

Here are two unrelated classes with the same methods:

class Duck:
    def swim(self):
        return "Duck swimming"
    
    def quack(self):
        return "Quack!"

class Person:
    def swim(self):
        return "Person swimming"
    
    def quack(self):
        return "Person imitating a duck: Quack!"
Notice that Duck and Person don't inherit from the same parent class, but they both have swim() and quack() methods.

Create a function that works with any "duck-like" object:

def make_it_swim_and_quack(duck_like_object):
    print(duck_like_object.swim())
    print(duck_like_object.quack())
This function doesn't care about the object's type - it only cares that the object has the required methods.

Use the function with both classes:

make_it_swim_and_quack(Duck())
make_it_swim_and_quack(Person())
Output:

Duck swimming
Quack!
Person swimming
Person imitating a duck: Quack!
Add another "duck-like" class:

class Robot:
    def swim(self):
        return "Robot swimming with propellers"
    
    def quack(self):
        return "Robot sound: BEEP BEEP!"

make_it_swim_and_quack(Robot())
Output:

Robot swimming with propellers
Robot sound: BEEP BEEP!
Key Point: Duck typing allows polymorphism without inheritance. If an object has the methods you need, you can use it. This makes Python code flexible and follows the principle "it's easier to ask forgiveness than permission."

Challenge

In this challenge, you'll implement a system demonstrating duck typing with different file-like objects:

textfile.py: Implement the TextFile class with read() and write(data) methods
database.py: Implement the Database class with matching method signatures
networkresource.py: Implement the NetworkResource class with matching method signatures
driver.py - Implement test cases that will verify your implementation works correctly
Each file contains detailed TODO comments guiding your implementation.
'''