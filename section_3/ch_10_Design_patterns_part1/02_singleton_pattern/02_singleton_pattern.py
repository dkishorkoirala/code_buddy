"""
Singleton Pattern


The Singleton pattern ensures a class has only one instance and provides a global point of access to it. This is useful for resources like database connections or configuration settings.

Here is a basic Singleton implementation:

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
The __new__ method controls object creation. It checks if an instance already exists before creating a new one.

Create two instances of the Singleton class:

singleton1 = Singleton()
singleton2 = Singleton()
Check if both variables reference the same object:

print(singleton1 is singleton2)  # True
print(id(singleton1))            # Same memory address
print(id(singleton2))            # Same memory address
Here is a more practical example with a database connection:

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to MySQL database"
            print("Creating new database connection")
        return cls._instance

    def query(self, sql):
        return f"Executing: {sql}"

# First access creates the connection
db1 = DatabaseConnection()
print(db1.connection)

# Second access reuses the same connection
db2 = DatabaseConnection()
print(db2.connection)

print(db1.query("SELECT * FROM users"))
print(db1 is db2)
Create a configuration manager using Singleton:

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key)

config1 = Config()
config1.set_setting("debug", True)

config2 = Config()
print(config2.get_setting("debug"))  # True - same settings
Output:

True
140234567890123
140234567890123
Creating new database connection
Connected to MySQL database
Connected to MySQL database
Executing: SELECT * FROM users
True
True
Key Point: The Singleton pattern uses __new__ to control object creation, ensuring only one instance exists. Use it for resources that should have only one copy throughout your application, like database connections, loggers, or configuration managers. Remember that all variables pointing to a Singleton reference the same object in memory.

Challenge

In this challenge, you'll implement the Singleton design pattern for a database connection class.

Edit databaseconnection.py to implement the Singleton pattern following the TODO comments
The driver.py file contains extensive test scenarios and should not be modified
"""
