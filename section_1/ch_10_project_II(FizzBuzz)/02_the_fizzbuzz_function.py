"""
The FizzBuzz Function


Challenge

Add a function named fizzbuzz that gets one number (int) as an argument, and:

If the number is divisible by 3, return "Fizz".
If the number is divisible by 7, return "Buzz".
If the number is divisible by both 3 and 7, return "FizzBuzz".
If none of the above conditions are met, return the number itself in a string format.
After the function:

Get input and cast it to int
Call the function fizzbuzz with the input number
Print the output of the function
"""

print("Welcome to FizzBuzz!")


def fizzbuzz(n):
    if (n % 3 == 0) and (n % 7 == 0):
        return "FizzBuzz"

    else:
        if n % 3 == 0:
            return "Fizz"

        elif n % 7 == 0:
            return "Buzz"

        else:
            return f"{n}"


num = int(input())
print(fizzbuzz(num))
