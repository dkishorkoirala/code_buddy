# TODO: Import math module for pi calculation
from math import pi

# TODO: Import Shape class from shape.py
from shape import Shape
# Use format: from shape import Shape


class Circle(Shape):
    def __init__(self, color, radius):
        # TODO: Call parent constructor with color using super()
        # TODO: Store radius as instance attribute (self.radius)
        super().__init__(color)
        self.radius = radius

    def area(self):
        # TODO: Return circle area using math.pi * radius ** 2
        # TODO: Formula: math.pi * self.radius ** 2
        return pi * self.radius**2

    def describe(self):
        # TODO: Print a description of the circle
        # TODO: Format should be exactly: "This is a {self.color} circle with radius {self.radius}."
        print(f"This is a {self.color} circle with radius {self.radius}.")
