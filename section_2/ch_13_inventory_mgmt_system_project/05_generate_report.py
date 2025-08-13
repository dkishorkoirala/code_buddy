"""
Generate Report


Challenge

The inventory system already has these components implemented:

A global inventory dictionary where:
Keys are item names (strings)
Values are dictionaries containing:
"price": The price of the item (float)
"stock": Current quantity in stock (integer)
An add_item(item, price, stock) function that adds new items to inventory
An update_stock(item, quantity) function that updates the stock level
A check_availability(item) function that returns the current stock level
Your task is to implement the sales_report(sales) function that:

Takes a sales dictionary where:
Keys are item names
Values are quantities sold
For each item in the sales dictionary:
Checks if the item exists in inventory
Checks if there's sufficient stock
Updates the inventory by reducing stock levels
Calculates revenue based on price and quantity sold
Returns a formatted string with the total revenue
Handle these specific errors:

If an item doesn't exist in inventory, print: "Error: Item '{item}' not found."
If there's insufficient stock, print: "Error: Insufficient stock for '{item}'."
The output should be a string formatted as: “Total revenue: ${total:.2f}”



Add (replace) the following block of code at the bottom of your code:

add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)
"""

inventory = {}


def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {"price": float(price), "stock": int(stock)}
        print(f"Item '{item}' added successfully.")


def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")

    else:
        new_stock = inventory[item]["stock"] + quantity
        if new_stock < 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] = new_stock
            print(f"Stock for '{item}' updated successfully.")


def check_availability(item):
    if item not in inventory:
        return "Item not found"
    else:
        return inventory[item]["stock"]


def sales_report(sales):
    total_revenue = 0

    for item, qty in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue

        if inventory[item]["stock"] < qty:
            print(f"Error: Insufficient stock for '{item}'.")
            continue

        inventory[item]["stock"] -= qty

        total_revenue += inventory[item]["price"] * qty

    return f"Total revenue: ${total_revenue:.2f}"


add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)
