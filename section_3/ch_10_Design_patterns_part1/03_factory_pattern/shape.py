from abc import ABC, abstractmethod


class Shape:
    # TODO: Define the Shape base class with abstract methods

    @abstractmethod
    def area(self):
        # TODO: Define an abstract area method that will be implemented by subclasses
        # This method should calculate and return the area of the shape
        pass

    @abstractmethod
    def perimeter(self):
        # TODO: Define an abstract perimeter method that will be implemented by subclasses
        # This method should calculate and return the perimeter of the shape
        pass
