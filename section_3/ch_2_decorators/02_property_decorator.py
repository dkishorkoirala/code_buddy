"""
Property Decorator


The @property decorator allows you to access methods like attributes, providing a clean way to get and set values.

Here is an example of a class using @property:

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
Create a circle and access properties:

my_circle = Circle(5)
Access properties like regular attributes:

print(my_circle.radius)
print(my_circle.area)
Output:

5
78.53975
Notice you don't use parentheses () when accessing properties - they look like attributes but run method code.

Add a setter to allow changing values:

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            print("Radius must be positive!")
Now you can set the radius like an attribute:

my_circle = Circle(5)
my_circle.radius = 10  # Uses the setter
print(my_circle.radius)  # Uses the getter
Output:

10
Key Point: @property makes methods look like attributes, while @property_name.setter allows you to control how values are assigned.
"""
