"""Context Managers


Context managers allow you to allocate and release resources precisely when needed. They ensure proper cleanup even if errors occur.

Here is the most common example using the with statement:

with open('example.txt', 'w') as file:
    file.write('Hello, world!')
# File is automatically closed here
The file is automatically closed after the block, even if an exception occurs.

Create your own context manager by implementing __enter__ and __exit__ methods:

class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        return False  # Don't suppress exceptions
Use your custom context manager:

with MyContext() as ctx:
    print("Inside the context")
Output:

Entering the context
Inside the context
Exiting the context
Create a more practical context manager for database connections:

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        self.connection = None

with DatabaseConnection("users_db") as conn:
    print(f"Using {conn}")
    print("Performing database operations...")
Handle exceptions in context managers:

class SafeContext:
    def __enter__(self):
        print("Setting up resources")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleaning up resources")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return False  # Don't suppress the exception

with SafeContext():
    print("Working with resources")
    # raise ValueError("Something went wrong")  # Uncomment to test
Output:

Connecting to users_db
Using Connection to users_db
Performing database operations...
Closing connection to users_db
Setting up resources
Working with resources
Cleaning up resources
The __exit__ method receives three parameters:

exc_type: Exception type (or None)
exc_val: Exception value (or None)
exc_tb: Exception traceback (or None)
Key Point: Context managers use __enter__ and __exit__ methods to manage resources. The with statement automatically calls these methods, ensuring proper setup and cleanup. This is especially useful for files, database connections, and other resources that need guaranteed cleanup.

Challenge
In this challenge, you'll implement a context manager class that measures elapsed time between entering and exiting a context block.

timer.py - Contains the Timer class implementation (this is the file you'll edit)
driver.py - Contains comprehensive test cases (do not modify)
Implement the Timer context manager in timer.py following the TODO comments. The class should:

Record start time when entering a context
Record end time when exiting
Calculate and display the elapsed time
"""
