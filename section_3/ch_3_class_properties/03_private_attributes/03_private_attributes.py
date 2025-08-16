"""
Private Attributes


Private attributes use underscores to indicate that certain data should not be accessed directly from outside the class.

Here is an example using single underscore (convention for "internal use"):

class Person:
    def __init__(self, name, age):
        self._name = name    # "protected" - internal use
        self._age = age      # "protected" - internal use
Single underscore attributes can still be accessed, but it's a signal not to:

person = Person("Alice", 30)
print(person._name)  # Works, but not recommended
Use double underscores for stronger privacy (name mangling):

class Person:
    def __init__(self, name, age):
        self.__name = name   # "private" - gets name mangled
        self.__age = age     # "private" - gets name mangled

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age must be positive!")
Use the accessor methods to interact with private attributes:

person = Person("Bob", 25)
print(person.get_name())  # Bob

person.set_age(30)
person.set_age(-5)        # Age must be positive!
Double underscore attributes get "name mangled" but can still be accessed:

person = Person("Charlie", 35)
# This doesn't work:
# print(person.__name)  # AttributeError

# But this works (discouraged):
print(person._Person__name)  # Charlie
Output:

Alice
Bob
Age must be positive!
Charlie
Key Point: Single underscore _attribute means "internal use only" by convention. Double underscore __attribute triggers name mangling for stronger privacy. Use accessor methods to properly interact with private data and add validation.

Challenge

Complete the User class in user.py with private password functionality, then use it in driver.py. Follow the TODO comments to implement password checking and changing methods.
"""
