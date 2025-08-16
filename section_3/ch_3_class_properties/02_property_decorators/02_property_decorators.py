"""
Property Decorators


Property decorators let you control how attributes are accessed and modified, while keeping the simple attribute syntax.

Here is an example of a class with a property getter:

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age
Use the property like a regular attribute:

person = Person("Alice", 30)
print(person.age)
Output:

30
Notice you access age without parentheses, even though it's actually calling a method.

Add a setter to validate data when setting values:

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
Now you can set the age with automatic validation:

person = Person("Alice", 30)
person.age = 31     # Uses the setter with validation
print(person.age)   # Uses the getter

# This would raise an error:
# person.age = -5   # ValueError: Age cannot be negative
Output:

31
Create computed properties that calculate values:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(rect.area)  # Calculates 5 * 3 = 15
Output:

15
Key Point: Property decorators make methods look like attributes. Use @property for getters and @attribute_name.setter for setters. This allows data validation and computed values while keeping simple attribute access syntax.


Challenge

Complete the Temperature class in temperature.py that converts between Celsius and Fahrenheit. Then use this class in driver.py to test temperature conversions. Follow the TODO comments in both files for step-by-step instructions.
"""
