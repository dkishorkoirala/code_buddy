'''
Operator Overloading


Operator overloading allows your classes to work with Python's built-in operators (+, -, *, etc.) by implementing special magic methods.

Here is an example of a class with operator overloading:

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
The __add__ method defines what happens when you use the + operator:

v1 = Vector(2, 3)
v2 = Vector(5, 7)
result = v1 + v2  # Calls v1.__add__(v2)
print(result)
The __mul__ method defines what happens when you use the * operator:

v1 = Vector(2, 3)
scaled = v1 * 3   # Calls v1.__mul__(3)
print(scaled)
Output:

Vector(7, 10)
Vector(6, 9)
Add comparison operators:

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(2, 3)
v3 = Vector(1, 1)

print(v1 == v2)  # True - calls v1.__eq__(v2)
print(v1 == v3)  # False
Key Point: Operator overloading uses magic methods like __add__ (+), __sub__ (-), __mul__ (*), __eq__ (==) to define how operators work with your objects. This makes your classes behave naturally with Python's built-in operators.

Challenge

In this challenge, you'll implement a Money class that represents monetary amounts with robust operator overloading. Your implementation will be thoroughly tested against a comprehensive test suite.

money.py - This is the only file you need to edit. It contains the class definition with TODO comments guiding your implementation.
driver.py - Contains extensive test scenarios that validate your implementation (do not modify).
Implement the Money class with the following features:

Constructor that takes amount (float) and currency (string)
Addition (+) of Money objects with the same currency
Multiplication (*) by a number to scale the amount
Equality comparison (==) between Money objects
String representation in the format “X.XX CUR”
'''