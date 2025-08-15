'''
The self Parameter


The self parameter refers to the instance of a class within methods. It allows you to access and modify attributes of the current object.

Here is an example of a class with methods using self:

class Car:
    def honk(self):
        print("Beep beep!")
    
    def describe(self):
        print(f"I am a {self.color} {self.model}")
The self parameter must always be the first parameter in method definitions. It tells the method which specific object is being used.

Create a car object and add attributes:

my_car = Car()
my_car.color = "Red"
my_car.model = "Sedan"
Now call the methods:

my_car.honk()
my_car.describe()
Output:

Beep beep!
I am a Red Sedan
Notice that when calling my_car.describe(), you don't pass anything for self - Python automatically passes my_car as the self parameter.

Here's what happens behind the scenes:

# When you write this:
my_car.describe()

# Python actually does this:
Car.describe(my_car)
The self parameter lets each object access its own data. Without self, methods wouldn't know which object's attributes to use.

Key Point: Always include self as the first parameter in method definitions, but never pass it when calling methods - Python handles this automatically.

Challenge: 

Complete the Car class in car.py by adding a method called display_info that uses the self parameter to print the car's year, make, and model in the format:

"This car is a [year] [make] [model]".

car.py: Contains the Car class definition where you'll add the display_info method
driver.py: Main execution file that imports and uses the Car class
The driver.py file will import your Car class and create instances to test your implementation. Make sure your method works correctly when called from the driver file.
'''