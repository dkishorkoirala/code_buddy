"""
Accessing Values

In a dictionary, each key is associated with a value. To access a value, you use its key. This is similar to how you would look up a word in a physical dictionary to find its definition.

Here's how you can access values in a Python dictionary:

# Dictionary of country capitals
country_capitals = {
 "USA": "Washington, D.C.",
 "France": "Paris",
 "Japan": "Tokyo"
}

# Accessing values using keys
print(country_capitals["USA"])
print(country_capitals["France"])

# Accessing a value that does not exist
# print(country_capitals["Germany"])  # This will cause an error
In this example, we access the capital of the USA by using the key "USA". If you try to access a key that does not exist in the dictionary, Python will raise a KeyError.

Challenge

Create a function named get_capital that takes two parameters: country_capitals (a dictionary) and country_name (a string). The function should return the capital city of the given country name using the country_capitals dictionary.
"""


def get_capital(country_capitals, country_name):
    # Write code here
    print(country_capitals[country_name])
