"""
Constructor Method (__init__)


The __init__ method is a special method that automatically runs when you create a new object. It initializes the object's attributes.

Here is an example of a class with a constructor:

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
The __init__ method takes parameters and assigns them to instance attributes using self.

Create objects using the constructor:

rex = Dog("Rex", "German Shepherd")
buddy = Dog("Buddy", "Golden Retriever")
When you call Dog("Rex", "German Shepherd"), Python automatically calls __init__ and passes the arguments.

Access the attributes that were set by the constructor:

print(rex.name)
print(rex.breed)
print(buddy.name)
print(buddy.breed)
Output:

Rex
German Shepherd
Buddy
Golden Retriever
You can also have a constructor with default values:

class Cat:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

# Create cats
fluffy = Cat("Fluffy", 3)
whiskers = Cat("Whiskers")  # age defaults to 1

print(f"{fluffy.name} is {fluffy.age} years old")
print(f"{whiskers.name} is {whiskers.age} years old")
Output:

Fluffy is 3 years old
Whiskers is 1 years old
Key Point: The __init__ method ensures every object is properly set up with its initial data when created. It saves you from manually setting attributes after object creation.

You are given Python files (book.py and driver.py) to implement a book management system. In this challenge, you'll define a Book class in one file that will be imported and used in another.

Your task is to:

Complete the Book class in book.py with an __init__ method that initializes title, author, and pages attributes
The driver.py file will import and use your Book class to create a book object for "Harry Potter" by "J.K. Rowling" with 400 pages
Follow the detailed TODO comments in the book.py .
"""
