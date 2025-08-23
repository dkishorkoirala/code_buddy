"""The **kwarg


The **kwargs parameter allows a method to accept any number of keyword arguments. The double asterisk collects all extra keyword arguments into a dictionary.

Here is an example of a method using **kwargs:

class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        self.details = kwargs

    def show_info(self):
        print(f"Name: {self.name}")
        for key, value in self.details.items():
            print(f"{key}: {value}")
Call the method with different keyword arguments:

person1 = Person("Alice", age=25, city="New York", job="Engineer")
person2 = Person("Bob", age=30, country="Canada")

person1.show_info()
print()
person2.show_info()
The **kwargs collects all keyword arguments into a dictionary:

class Config:
    def __init__(self, **kwargs):
        self.settings = kwargs

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

    def show_all_settings(self):
        for key, value in self.settings.items():
            print(f"{key} = {value}")

config = Config(debug=True, max_users=100, timeout=30)
config.show_all_settings()
Combine regular parameters, *args, and **kwargs:

class Logger:
    def log(self, level, *messages, **options):
        # Regular parameter: level
        # *args: messages
        # **kwargs: options

        timestamp = options.get('timestamp', False)
        color = options.get('color', 'default')

        if timestamp:
            print("[2024-01-01 12:00:00]", end=" ")

        print(f"[{level}]", end=" ")

        for message in messages:
            print(message, end=" ")

        if color != 'default':
            print(f"(color: {color})")
        else:
            print()

logger = Logger()
logger.log("INFO", "User", "logged", "in", timestamp=True, color="green")
logger.log("ERROR", "Connection", "failed", timestamp=False)
Use **kwargs for flexible object initialization:

class Product:
    def __init__(self, name, price, **features):
        self.name = name
        self.price = price
        self.features = features

    def describe(self):
        print(f"{self.name} - ${self.price}")
        if self.features:
            print("Features:")
            for feature, value in self.features.items():
                print(f"  {feature}: {value}")

laptop = Product("Gaming Laptop", 1299,
                brand="TechCorp",
                ram="16GB",
                storage="1TB SSD",
                graphics="RTX 4060")
laptop.describe()
Output:

Name: Alice
age: 25
city: New York
job: Engineer

Name: Bob
age: 30
country: Canada
debug = True
max_users = 100
timeout = 30
[2024-01-01 12:00:00] [INFO] User logged in (color: green)
[ERROR] Connection failed
Gaming Laptop - $1299
Features:
  brand: TechCorp
  ram: 16GB
  storage: 1TB SSD
  graphics: RTX 4060
You can also unpack dictionaries when calling methods:

settings = {"debug": True, "verbose": False, "log_level": "INFO"}
config2 = Config(**settings)  # Unpacks the dictionary
config2.show_all_settings()
Output:

debug = True
verbose = False
log_level = INFO
Key Point: **kwargs collects any number of keyword arguments into a dictionary. Use it when you want flexible method signatures that can accept various named parameters. The name kwargs is conventional - you could use any name after the double asterisk, but kwargs is the standard.

Challenge

In this challenge, you'll implement a person creation system with comprehensive test coverage.

You need to edit only the person_creator.py file, following the TODO comments that guide your implementation. The file contains a class structure for creating and managing person objects with various properties.
"""
