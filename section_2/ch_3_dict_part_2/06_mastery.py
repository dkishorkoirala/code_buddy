"""
Looping Through Dictionaries


Challenge

Create a function named print_product_details that takes a dictionary product_data as an argument. The function should loop through the dictionary and print each key-value pair in the format 'Key: Value', with the key capitalized. If the dictionary is empty, the function should print 'No product information available'.
"""


def print_product_details(product_data):
    # Write code here
    if not product_data:
        print("No product information available")
    else:
        for k, v in product_data.items():
            print(f"{k.capitalize()}: {v}")
