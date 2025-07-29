"""
Iterating Over Strings Part 2

String splitting allows you to break a string into a list, while joining lets you combine list items into a string.

The split() method divides a string into a list of substrings based on a delimiter.

Split by whitespace:

text = "apple banana cherry"
fruits = text.split()
print(fruits)
# ['apple', 'banana', 'cherry']
Split with specific delimiter:

data = "john,25,new york"
data = data.split(',')
print(data)
# ['john', '25', 'new york']
The join() method combines elements of an iterable into a single string.

Basic joining:

words = ['Hello', 'World', 'Python']
text = ' '.join(words)
print(text)
# "Hello World Python"
Join with different separator:

fruits = ['apple', 'banana', 'cherry']
line = ','.join(fruits)
print(line)
# "apple,banana,cherry"

Challenge

Write a program that takes two inputs: a text string and a delimiter character. The program should split the text by whitespace into words, then join these words using the specified delimited character and print the resulting string.
"""

text = input()
delimiter = input()
# Write your code below
a = text.split()
b = f"{delimiter}".join(a)
print(b)
