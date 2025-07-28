"""
Continue

The continue statement stops the current iteration and continues to the next iteration. For example:

for i in range(3, 9):
    if i == 5:
        continue
    print(i)
The loop will iterate through the numbers from 3 to 8, and when it reaches i=5 it will skip that iteration and continue to the next one. The output is:

3
4
6
7
8
Notice, number 5 is not in the output.

Challenge

You are given a code which prints the numbers from 1 to 20 (including).

Your task is to add if and continue statements so that only the even numbers will be printed (2, 4, 6, ...).
"""

for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)
