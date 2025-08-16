"""Static Method Decorator


The @staticmethod decorator creates methods that don't need self or the class. They work like regular functions but belong to the class.

Here is an example of a class with static methods:

class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0
Call static methods using the class name:

result = MathHelper.add(5, 3)
print(result)

check = MathHelper.is_even(10)
print(check)
You can also call them from an object:

helper = MathHelper()
result2 = helper.add(2, 4)
print(result2)
Output:

8
True
6
Static methods don't access instance or class data:

class Calculator:
    brand = "Python Calc"

    def __init__(self, owner):
        self.owner = owner

    @staticmethod
    def multiply(x, y):
        # Cannot access self.owner or Calculator.brand
        return x * y
Key Point: Use @staticmethod when you need a function that's related to the class but doesn't need access to instance (self) or class data. No self parameter needed.
"""
