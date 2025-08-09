"""
Returning Multiple Values


Challenge

Create a function named get_product_info that takes no arguments. The function should return a tuple containing the following information about a product:

Name: "Laptop"
Price: 999.99
Rating: 4.5
After defining the function, call it and unpack the returned values into three variables: product_name, product_price, and product_rating. Then, print the values of these variables.
"""


# Write code here
def get_product_info():
    name = "Laptop"
    price = 999.99
    rating = 4.5
    return name, price, rating


product_name, product_price, product_rating = get_product_info()
print(product_name)
print(product_price)
print(product_rating)
