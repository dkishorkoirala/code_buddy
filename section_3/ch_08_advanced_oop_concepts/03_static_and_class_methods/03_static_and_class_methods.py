"""Static and Class Methods


Besides regular instance methods, classes can have static methods and class methods that serve different purposes.

Here is an example of a static method:

class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0
Static methods don't need self and work like regular functions. Call them directly from the class:

result = MathHelper.add(5, 3)
print(result)

check = MathHelper.is_even(10)
print(check)
Here is an example of a class method:

class Person:
    count = 0  # Class variable

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous")
Class methods receive the class itself (cls) as the first parameter:

person1 = Person("Alice")
person2 = Person("Bob")
print(Person.get_count())  # 2
Use class methods as alternative constructors:

anonymous = Person.create_anonymous()
print(anonymous.name)      # Anonymous
print(Person.get_count())  # 3
Compare all three method types in one class:

class Calculator:
    brand = "Python Calc"

    def __init__(self, owner):
        self.owner = owner

    # Instance method - needs self, accesses instance data
    def show_owner(self):
        return f"Owned by {self.owner}"

    # Class method - needs cls, accesses class data
    @classmethod
    def get_brand(cls):
        return cls.brand

    # Static method - needs neither, just a utility function
    @staticmethod
    def multiply(x, y):
        return x * y

calc = Calculator("Alice")
print(calc.show_owner())        # Owned by Alice
print(Calculator.get_brand())   # Python Calc
print(Calculator.multiply(4, 5)) # 20
Output:

8
True
2
Anonymous
3
Owned by Alice
Python Calc
20
You can call class and static methods from instances too:

calc = Calculator("Bob")
print(calc.get_brand())      # Python Calc
print(calc.multiply(2, 3))   # 6
Key Differences:

Instance methods: Need self, access instance data
Class methods: Need cls, access class data, good for alternative constructors
Static methods: Need neither, just utility functions related to the class
Key Point: Use @staticmethod for utility functions that belong logically to the class but don't need class or instance data. Use @classmethod when you need access to the class itself, like for alternative constructors or accessing class variables.

Challenge

In this challenge, you'll implement a Temperature class with specific functionality while leveraging a comprehensive testing framework.

You need to edit only the temperature.py file, following the TODO comments that guide your implementation. The class should include:

A class variable to track temperature readings
A static method for temperature conversion
Class methods for adding readings and calculating averages
"""
