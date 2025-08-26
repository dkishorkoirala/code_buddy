"""Decorator Pattern


The Decorator Pattern adds new functionality to objects dynamically without changing their structure. It wraps objects to extend their behavior.

Here is a simple coffee example:

class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"
Create decorators that add features to coffee:

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2

    def description(self):
        return self.coffee.description() + " + Milk"

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 1

    def description(self):
        return self.coffee.description() + " + Sugar"
Each decorator wraps another object and adds its own functionality.

Use decorators to build customized coffee:

# Start with basic coffee
my_coffee = Coffee()
print(f"{my_coffee.description()}: ${my_coffee.cost()}")

# Add milk
my_coffee = MilkDecorator(my_coffee)
print(f"{my_coffee.description()}: ${my_coffee.cost()}")

# Add sugar
my_coffee = SugarDecorator(my_coffee)
print(f"{my_coffee.description()}: ${my_coffee.cost()}")
Create another example with text formatting:

class Text:
    def __init__(self, content):
        self.content = content

    def render(self):
        return self.content

class BoldDecorator:
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"<b>{self.text.render()}</b>"

class ItalicDecorator:
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"<i>{self.text.render()}</i>"

# Build formatted text step by step
message = Text("Hello World")
message = BoldDecorator(message)
message = ItalicDecorator(message)

print(message.render())
Output:

Simple coffee: $5
Simple coffee + Milk: $7
Simple coffee + Milk + Sugar: $8
<i><b>Hello World</b></i>
Key Point: The Decorator Pattern wraps objects to add new behavior without changing the original object. Each decorator maintains a reference to the wrapped object and adds its own functionality. This allows you to combine multiple decorators for flexible feature combinations without creating many subclasses.


Challenge

In this challenge, you will implement the Decorator design pattern to create a flexible coffee ordering system for a coffee shop. The Decorator pattern allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects from the same class.

You're building a system for a coffee shop that needs to:

Offer various types of beverages (Espresso, Dark Roast, House Blend, Decaf)
Allow customers to add condiments (Milk, Mocha, Soy, Whipped Cream) to their beverages
Calculate the cost of beverages with added condiments
Manage orders and calculate total costs
Complete the abstract Beverage class and its concrete implementations
Implement the CondimentDecorator abstract class and concrete decorators
Create a CoffeeShop class to manage orders
Implement test scenarios to verify your implementation

"""
