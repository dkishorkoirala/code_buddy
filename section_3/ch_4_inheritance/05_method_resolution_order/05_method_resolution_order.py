"""
Method Resolution Order


Method Resolution Order (MRO) is the sequence Python uses to look for methods when multiple classes have the same method name.

Here is an example with multiple classes having the same method:

class A:
    def method(self):
        return "Method from A"

class B:
    def method(self):
        return "Method from B"

class C(A, B):
    pass
Check the MRO using __mro__:

print(C.__mro__)
Output:

(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
This shows Python will check C first, then A, then B, then the built-in object class.

Create an object and call the method:

c = C()
print(c.method())
Output:

Method from A
Python found the method in class A first, so it used that one.

Change the inheritance order to see the difference:

class D(B, A):  # B comes before A now
    pass

print(D.__mro__)
d = D()
print(d.method())
Output:

(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
Method from B
Now Python finds B's method first because B comes before A in the inheritance list.

You can also use the mro() method:

print(C.mro())
This gives the same result as __mro__ but as a list.

Key Point: Python searches for methods in MRO order - the class itself first, then parent classes from left to right as listed in the class definition. The first method found gets used.

Challenge

In this challenge, you'll implement a class hierarchy.

You'll need to edit these files:

device.py: Implement the base Device class
screen.py: Implement Screen class that inherits from Device
computer.py: Implement Computer class that inherits from Device
laptop.py: Implement Laptop class with multiple inheritance
driver.py - Implement test cases that will verify your implementation works correctly
Each file contains detailed TODO comments that will guide you step-by-step through the implementation.
"""
