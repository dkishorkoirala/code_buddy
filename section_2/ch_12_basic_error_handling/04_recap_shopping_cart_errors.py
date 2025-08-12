"""
Recap - Shopping Cart Errors


Challenge

Create a program that simulates a shopping cart with error handling. Your task is to:

Create a function called handle_shopping_cart that processes customer orders

The function should accept a list of order strings in the format "item:quantity"
Process each order by:
    Splitting the input string to get the item and quantity

    Converting the quantity to an integer

    Adding the item to a shopping cart dictionary with the quantity as value

    If an item already exists in the cart, update its quantity
Handle these specific errors:
    If the input format is incorrect (missing colon), print "Invalid format: {order}"
    If the quantity is not a valid number, print "Invalid quantity: {order}"
    If the quantity is negative, print "Negative quantity not allowed: {order}"
Return the completed shopping cart dictionary"""


def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart = {}

    # Process each order in the list
    for order in orders:
        try:
            # Check for proper format
            if ":" not in order:
                print(f"Invalid format: {order}")
                continue

            # Split the order into item and quantity
            item = order.split(":")[0]
            quantity_str = order.split(":")[1]

            # Convert quantity to integer
            quantity = int(quantity_str)

            # Check for negative quantity
            if quantity < 0:
                print(f"Negative quantity not allowed: {order}")
                continue

            # Add to cart or update quantity if item exists
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity

        except ValueError:
            print(f"Invalid quantity: {order}")

        except Exception as e:
            print(f"Unexpected error: {e}")

    # Return the completed cart
    return cart
