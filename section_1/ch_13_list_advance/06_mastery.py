"""
Sequence Operators


Challenge

Create a program that receives a list of numbers as input and prints a new list that:

Contains the original list followed by its reverse
Has the first element of the original list inserted at the beginning and the last element inserted at the end
Repeats this entire sequence twice
For example:

1 2 3 → [1, 1, 2, 3, 3, 2, 1, 3, 1, 1, 2, 3, 3, 2, 1, 3]

"""

numbers = input().split()
# Write your code below

rev = numbers[::-1]
start = numbers[0:1]
end = numbers[-1::]
new_list = start + numbers + rev + end
print(new_list * 2)
# print(rev)
# print(start)
# print(end)
