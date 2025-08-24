"""Intro to design pattern


Design patterns are reusable solutions to common problems in software design. They're like blueprints that you can customize to solve recurring design problems in your code.

Think of design patterns as proven templates that experienced developers use to solve similar problems. When you say "I used the Singleton pattern," other developers immediately understand your code's structure.

Here is a simple example of why patterns matter:

# Without pattern - messy approach
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected to database"

# Problem: Multiple connections created
db1 = DatabaseConnection()
db2 = DatabaseConnection()  # Wasteful - creates another connection
With a design pattern, you get a better solution:

# With Singleton pattern - controlled approach
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to database"
        return cls._instance

# Now only one connection exists
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True - same instance
Why use design patterns:

Reusability: Solutions you can apply to similar problems
Communication: Common vocabulary among developers
Best Practices: Time-tested solutions
Maintainability: Well-structured, organized code
What you'll learn in this series:

Creational Patterns (how objects are created):

Singleton Pattern - One instance only
Factory Pattern - Create objects without specifying exact class
Structural Patterns (how objects are composed):

Adapter Pattern - Make incompatible interfaces work together
Decorator Pattern - Add functionality without changing structure
Behavioral Patterns (how objects interact):

Observer Pattern - Notify multiple objects of changes
Strategy Pattern - Switch algorithms dynamically
Command Pattern - Encapsulate requests as objects
Each pattern lesson will cover:

What problem it solves
How to implement it in Python
When to use it
Real-world examples
Key Point: Design patterns are proven solutions to common programming problems. They provide a shared vocabulary and best practices that make your code more maintainable, flexible, and easier to understand. You'll learn 7 essential patterns that every Python developer should know.
"""
