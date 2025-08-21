'''
Magic Methods Introduction


Magic methods (also called dunder methods) are special methods with double underscores at the beginning and end. Python calls them automatically in response to certain operations.

Here is an example of a class with magic methods:

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
The __init__ method is called automatically when you create an object:

my_book = Book("Python Programming", "John Smith", 350)
The __str__ method is called automatically when you convert the object to a string:

print(my_book)        # Calls __str__ automatically
print(str(my_book))   # Also calls __str__
Output:

Python Programming by John Smith
Python Programming by John Smith
Without __str__, printing would show the object's memory location:

class SimpleBook:
    def __init__(self, title):
        self.title = title

simple = SimpleBook("Test Book")
print(simple)  # <__main__.SimpleBook object at 0x...>
Add another magic method for length:

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages

my_book = Book("Python Programming", "John Smith", 350)
print(len(my_book))   # Calls __len__ automatically
Output:

350
Key Point: Magic methods start and end with double underscores (__method__) and are called automatically by Python. They allow your objects to work with built-in functions like str(), len(), and operators, making your classes more Pythonic and intuitive to use.

Challenge

In this challenge, you'll implement a Counter class with magic methods.

counter.py - This is the file you need to edit, containing TODO comments to guide your implementation
driver.py - Contains extensive test cases
Implement the Counter class in counter.py and test cases in driver.py following the TODO comments. The class should support initialization with optional values, string representation, and addition operations.

'''