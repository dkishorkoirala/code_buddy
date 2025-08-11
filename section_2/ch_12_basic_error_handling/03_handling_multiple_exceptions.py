"""
Handling Multiple Exceptions

In Python, we can handle different types of exceptions in separate except blocks. This allows us to respond differently based on the specific error that occurs.

Start with a basic try-except structure:

try:
    # Code that might raise exceptions
    pass
except Exception as e:
    # Handle any exception
    pass
To handle multiple exceptions, add specific except blocks:

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
You can also catch multiple exception types in a single except block:

try:
    # Some code
    pass
except (ValueError, TypeError):
    print("Invalid input type!")
The order of except blocks matters - always place more specific exceptions before more general ones.


Challenge

Create a function called process_data that:

Takes a string input representing potential data
Tries to convert it to an integer, then calculates 100 divided by that integer
Returns the result
Handles at least 3 possible exceptions:
ValueError if the input cannot be converted to an integer (print "Input must be a number!")
ZeroDivisionError if the input is 0 (print "Cannot divide by zero!")
Any other exception with a generic handler (print "An unexpected error occurred!")
"""


def process_data(input_string):
    try:
        # Try to convert the input string to an integer
        data = int(input_string)
        # Calculate 100 divided by the input value
        result = 100 / data
        # Return the result
        return result
    except ValueError:
        # Handle the case where input cannot be converted to an integer
        return "Input must be a number!"
    except ZeroDivisionError:
        # Handle the case where input is zero
        return "Cannot divide by zero!"
    except:
        # Handle any other unexpected exceptions
        return "An unexpected error occurred!"
