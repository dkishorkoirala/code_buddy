"""Factory Pattern


The Factory Pattern creates objects without specifying their exact class. Instead of calling constructors directly, you use a factory method that decides which class to instantiate.

Here are simple product classes:

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.type = "Car"

    def info(self):
        return f"{self.type}: {self.brand}"

class Bike:
    def __init__(self, brand):
        self.brand = brand
        self.type = "Bike"

    def info(self):
        return f"{self.type}: {self.brand}"
Create a factory class to produce these objects:

class VehicleFactory:
    def create_vehicle(self, vehicle_type, brand):
        if vehicle_type == "car":
            return Car(brand)
        elif vehicle_type == "bike":
            return Bike(brand)
        else:
            raise ValueError(f"Unknown type: {vehicle_type}")
Use the factory instead of calling constructors directly:

factory = VehicleFactory()
my_car = factory.create_vehicle("car", "Toyota")
my_bike = factory.create_vehicle("bike", "Honda")

print(my_car.info())   # Car: Toyota
print(my_bike.info())  # Bike: Honda
Make the factory more flexible using *args:

class FlexibleFactory:
    def create_vehicle(self, vehicle_type, *args):
        if vehicle_type == "car":
            return Car(args[0])  # Just brand
        elif vehicle_type == "truck":
            return Truck(args[0], args[1])  # Brand and capacity
        else:
            raise ValueError(f"Unknown type: {vehicle_type}")

class Truck:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity
        self.type = "Truck"

    def info(self):
        return f"{self.type}: {self.brand} ({self.capacity}t)"
Use the flexible factory:

flexible = FlexibleFactory()
car = flexible.create_vehicle("car", "Ford")
truck = flexible.create_vehicle("truck", "Volvo", "20")

print(car.info())    # Car: Ford
print(truck.info())  # Truck: Volvo (20t)
Output:

Car: Toyota
Bike: Honda
Car: Ford
Truck: Volvo (20t)
Key Point: The Factory Pattern lets you create objects without knowing their exact class. The factory method decides which class to instantiate based on parameters. Use *args to handle products with different constructor parameters. This makes your code more flexible and easier to extend with new product types.

Challenge

In this challenge, you'll implement a shape factory system using proper object-oriented design with inheritance and polymorphism.

Complete the implementation in the following files:

shape.py - Base Shape class
circle.py - Circle implementation
rectangle.py - Rectangle implementation
triangle.py - Triangle implementation
shapefactory.py - Factory class to create shapes
Each file contains detailed TODO comments to guide your implementation. Follow these comments carefully to ensure your code meets all requirements.
"""
