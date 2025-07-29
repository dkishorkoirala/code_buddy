"""
Looping The Numbers

Everything is ready, let's play the game!


Challenge

Loop over the numbers from 1 to the number that the user entered, and each time use the function you created to calculate the FizzBuzz result and output it.

For example, for input of 7 output:

Welcome to FizzBuzz!
1
2
Fizz
4
5
Fizz
Buzz
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

for i in range(1, num + 1):
    print(fizzbuzz(i))
