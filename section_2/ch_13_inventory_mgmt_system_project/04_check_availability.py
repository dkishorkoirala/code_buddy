"""
Check Availability


Challenge

Create a function named check_availability that takes one argument: item (string). The function should:

Check if the item exists in the inventory dictionary.
If it does not exist, return "Item not found".
If the item exists, return the current stock of the item.
Add (replace) the following block of code at the bottom of your code:

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"
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


add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"
