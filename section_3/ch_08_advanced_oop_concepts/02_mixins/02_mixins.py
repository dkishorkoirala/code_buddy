"""Mixins


Mixins are a special kind of multiple inheritance used to "mix in" additional functionality to classes. They provide specific methods without being complete classes themselves.

Here is an example of a simple mixin:

class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(JSONSerializableMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email
The mixin adds JSON functionality to any class that inherits from it:

user = User("Alice", "alice@example.com")
print(user.to_json())
Output:

{"name": "Alice", "email": "alice@example.com"}
Create multiple mixins for different functionality:

class PrintableMixin:
    def pretty_print(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

class ComparableMixin:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
Combine multiple mixins in one class:

class Product(JSONSerializableMixin, PrintableMixin, ComparableMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = Product("Laptop", 999)
product2 = Product("Laptop", 999)
Use all mixin functionalities:

print(product1.to_json())         # From JSONSerializableMixin
product1.pretty_print()          # From PrintableMixin
print(product1 == product2)      # From ComparableMixin
Output:

{"name": "Laptop", "price": 999}
name: Laptop
price: 999
True
Key characteristics of mixins:

Not meant to be instantiated on their own
Provide specific, reusable functionality
Don't usually have __init__ methods
Names often end with "Mixin" or "able"
Can be combined with multiple inheritance
Key Point: Mixins provide a way to share functionality across different class hierarchies without creating complex inheritance trees. They allow you to "mix in" specific capabilities like serialization, comparison, or printing to any class that needs them. This promotes code reuse and keeps classes focused on their primary responsibilities.

Challenge

In this challenge, you'll implement a simple e-commerce system using mixins and inheritance.

Implement the required classes in these files (follow the TODO comments in each file):

printablemixin.py - Create the PrintableMixin with formatted output functionality
discountmixin.py - Implement the DiscountMixin for price reduction calculations
shippablemixin.py - Build the ShippableMixin for weight and shipping cost features
product.py - Develop the base Product class with appropriate mixin inheritance
physicalproduct.py - Create the PhysicalProduct class extending Product
digitalproduct.py - Implement the DigitalProduct class with special discount behavior
"""
