"""
Adding The Twist


Challenge

Add a small twist to the game:

Numbers that contain the digit "3" but aren't divisible by 3 or 7 will output Almost Fizz

To check if a string contains a char use in for instance, "a" in word, note that you must cast the number to string for it work use str(num)
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
            if "3" in str(n):
                return "Almost Fizz"
            else:
                return f"{n}"


num = int(input())

for i in range(1, num + 1):
    print(fizzbuzz(i))
