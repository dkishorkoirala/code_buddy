'''
Access Modifiers


Access modifiers control the visibility of class attributes and methods. Python uses naming conventions rather than keywords for access control.

Here is an example of public access (no prefix):

class Person:
    def __init__(self):
        self.name = "Coddy"      # Public attribute
        
    def greet(self):             # Public method
        return f"Hello, I'm {self.name}"
Access public members from anywhere:

person = Person()
print(person.name)           # Coddy
print(person.greet())        # Hello, I'm Coddy
Here is an example of protected access (single underscore):

class Employee:
    def __init__(self):
        self._salary = 50000     # Protected attribute
    
    def _calculate_bonus(self):  # Protected method
        return self._salary * 0.1

    def show_bonus(self):
        return self._calculate_bonus()  # OK to use within class
Access protected members (works but not recommended):

employee = Employee()
print(employee._salary)      # 50000 - works but discouraged
print(employee.show_bonus()) # 5000.0 - proper way
Here is an example of private access (double underscore):

class User:
    def __init__(self):
        self.__password = "secure123"   # Private attribute
        
    def __encrypt(self, data):          # Private method
        return f"Encrypted: {data}"
        
    def verify(self, input_password):
        # Private members accessible inside the class
        return input_password == self.__password
Use private members correctly:

user = User()
print(user.verify("secure123"))  # True - using public method
# print(user.__password)         # AttributeError - cannot access directly
Output:

Coddy
Hello, I'm Coddy
50000
5000.0
True
Key Point: Python access modifiers are naming conventions: no prefix = public (accessible anywhere), single underscore = protected (internal use), double underscore = private (class only). These help establish clear boundaries and prevent accidental misuse of class internals.

Challenge

In this challenge, you'll implement a FileManager class that demonstrates Python's access modifiers (public, protected, and private) while experiencing the benefits of comprehensive testing.

Edit filemanager.py to implement the FileManager class following the TODO comments. The file contains detailed instructions for implementing:

Public methods for file operations
Protected methods (with single underscore prefix)
Private methods (with double underscore prefix)
Method interactions demonstrating encapsulation

'''