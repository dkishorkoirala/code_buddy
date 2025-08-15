'''
Introduction to OOP


Object-Oriented Programming (OOP) organizes code around objects that contain data (attributes) and functions (methods).

Create a file called car.py with a class

class Car:
    pass  # placeholder that does nothing
Create another file called driver.py to use the class

from car import Car
Create an object from the Car class

my_car = Car()
Check the type of your object

print(type(my_car))
Output:

<class 'car.Car'>
This confirms you've successfully created an object from your Car class. In OOP, a class is like a blueprint, and an object is what you build from that blueprint.

Challenge

In this challenge, you'll implement a Car class in car.py and use it in driver.py.

You need to update driver.py to import and use the Car class properly

Detailed TODO comments will guide you through each step of the implementation. The driver file contains test cases that will verify your implementation works correctly.
'''

