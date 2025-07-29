"""
Default Values

Sometimes when we create a function, we want to have some arguments that are optional, with predetermined default values.

Example:

def greet(name, greeting="Hello"):
    print(name, greeting)
Using the function with only required argument:

greet("John")
# Output: John Hello
Using the function with both arguments:

greet("john", "welcome")
# Output: John Welcome
You can have multiple default arguments:

def describe_person(name, age=25, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}")
describe_person("Alice")
# Uses both defaults

describe_person("Bob", 30)
# Uses default city

describe_person("Charlie", 35, "New York")
# Uses no defaults
Important Rule: Default arguments must come after non-default arguments in the function definition.

# Correct:
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
# Incorrect:
def greet(greeting="Hello", name):
    print(f"{greeting}, {name}!")
"""
