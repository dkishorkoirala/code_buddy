"""
Creating a Dictionary


Challenge

Create a function named create_book_dict that takes three parameters: title, author, and year. The function should return a dictionary where the keys are "title", "author", and "year", and the values are the corresponding values passed to the function.

For example, calling create_book_dict("To Kill a Mockingbird", "Harper Lee", 1960) should return a dictionary with the following key-value pairs:

Key: "title", Value: "To Kill a Mockingbird"
Key: "author", Value: "Harper Lee"
Key: "year", Value: 1960
"""


def create_book_dict(title, author, year):
    # Write code here
    k = {}
    k.update({"title": title, "author": author, "year": year})
    return k
