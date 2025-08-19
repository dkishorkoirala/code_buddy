'''
Interface Design


An interface defines a contract that classes must follow. In Python, we create interfaces using abstract base classes where all methods are abstract.

Import the abc module:

from abc import ABC, abstractmethod
Create an interface with abstract methods only:

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def resize(self, width, height):
        pass
All methods in an interface should be abstract - they define what implementing classes must do, not how to do it.

Implement the interface in a concrete class:

class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius
    
    def draw(self):
        return "Drawing a circle"
    
    def resize(self, width, height):
        self.radius = min(width, height) / 2
        return f"Resized circle to radius {self.radius}"
Create another class that implements the same interface:

class Rectangle(Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self):
        return "Drawing a rectangle"
    
    def resize(self, width, height):
        self.width = width
        self.height = height
        return f"Resized rectangle to {width}x{height}"
Use the interface polymorphically:

shapes = [Circle(5), Rectangle(3, 4)]

for shape in shapes:
    print(shape.draw())
    print(shape.resize(10, 8))
Output:

Drawing a circle
Resized circle to radius 4.0
Drawing a rectangle
Resized rectangle to 10x8
You can also use interfaces as type hints:

def render_shape(drawable: Drawable):
    return drawable.draw()

circle = Circle(3)
print(render_shape(circle))
Output:

Drawing a circle
Key Point: Interfaces define what classes must do, not how they do it. Use abstract base classes with only abstract methods to create clear contracts that implementing classes must follow. This ensures consistent behavior across different implementations.

Challenge

In this challenge, you'll implement a media player system with interfaces.

You need to edit the following files:

playable.py - Implement the abstract base classes (interfaces)
song.py - Implement the Song class
video.py - Implement the Video class
mediaplayer.py - Implement the MediaPlayer class
Each file contains detailed TODO comments to guide your implementation. Follow these comments to create a complete media player system with proper inheritance and interface implementation.
'''