"""
Modulo Operator

The modulo operator % tells you what's left over after dividing one number by another.

result = dividend % divisor
dividend: The number being divided.
divisor: The number that divides the dividend.
result: The remainder of the division.
For example

result = 10 % 3
Here, 10 is divided by 3. 3 goes into 10 three times, with a remainder of 1. So, result will be 1.

Usually modulo is used for checking if a number is even or odd:

If a number is even, dividing it by 2 will leave a remainder of 0.
If a number is odd, dividing it by 2 will leave a remainder of 1.

Challenge

Write a code that initializes three variables, a, b and c with the values 9, 2, and 11 (respectively).

After that, initialize the following variables:

d that will hold the result of a modulo 2
e that will hold the result of b modulo 3
f that will hold the result of c modulo 10
Check out the result and see how different dividends and divisors affect the result."""

# Type your code below
a = 9
b = 2
c = 11

d = a % 2
e = b % 3
f = c % 10

# Don't change the line below
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")
print(f"e = {e}")
print(f"f = {f}")
