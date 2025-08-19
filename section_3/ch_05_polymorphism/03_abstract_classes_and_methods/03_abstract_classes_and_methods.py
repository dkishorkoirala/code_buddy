'''
Abstract Classes and Methods


Abstract classes are classes that cannot be instantiated directly and contain abstract methods that must be implemented by subclasses.

Import the abc module to create abstract classes:

from abc import ABC, abstractmethod
Create an abstract class with abstract methods:

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return "This is a shape"  # Concrete method (has implementation)
The @abstractmethod decorator marks methods that must be implemented by subclasses. Regular methods like describe() can have implementations.

Try to create an instance of the abstract class:

# This will cause an error:
# shape = Shape()  # TypeError: Can't instantiate abstract class
Create a concrete subclass that implements all abstract methods:

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
Now you can create instances of the concrete class:

circle = Circle(5)
print(circle.area())
print(circle.perimeter())
print(circle.describe())  # Inherited concrete method
Create another concrete subclass:

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(4, 6)
print(rectangle.area())
print(rectangle.perimeter())
Output:

78.5
31.400000000000002
This is a shape
24
20
Key Point: Abstract classes define a template that subclasses must follow. Use ABC and @abstractmethod to create abstract classes. Subclasses must implement all abstract methods or they'll also be abstract.

Challenge

In this challenge, you'll implement a payment processing system.

You need to complete the implementation in these files:

paymentmethod.py - Abstract base class with validation logic
creditcard.py - Credit card payment implementation
paypal.py - PayPal payment implementation
Follow the TODO comments in each file to implement the required functionality. The comments will guide you step-by-step through creating abstract methods, implementing concrete subclasses, and establishing proper import relationships between files.

The driver.py file contains test cases that will verify your implementation works correctly, processing different payment scenarios and displaying appropriate details for each payment method.

'''