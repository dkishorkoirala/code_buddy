"""
Declare a Function

A function is a sequence of code that has a name. The purpose of a function is to reuse a piece of code multiple times.

For example, take a look at this code:

print("Welcome to Coddy")
print("New session...")
print("Welcome to Coddy")
print("Another session...")
print("Welcome to Coddy")
We use the same code print("Welcome to Coddy") over and over again. Another issue with this code is that if we wanted to change the message: Welcome to Coddy to something different, like "Welcome aboard" it would have to change 3 different lines of code. To solve this issue, we will use functions.

To declare a function, we use the following syntax:

def function_name():
    code
For our example, we will create a function named greet and it will look like this:

def greet():
    print("Welcome to Coddy")
To use/call/execute the function, we write greet():

greet()
print("New session...")
greet()
print("Another session...")
greet()
This will result in the same output as above.

Important! The function code must come before it's call


Challenge

Write a program that gets one input, a number. The input number indicates how many times to execute the below function.

Create a function that calculates the sum of all of the numbers between 1 and 10000 (including) and prints it, name the function however you like.

Note! In your code, write the function before it's call statements.
"""


def sum_numbers():
    result = 0
    for i in range(1, 10001):
        result += i
    print(result)


n = int(input())
for i in range(n):
    sum_numbers()
