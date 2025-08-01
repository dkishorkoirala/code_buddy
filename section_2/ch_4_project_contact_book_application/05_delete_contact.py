"""
Delete Contact


Challenge

The next step is to create the delete_contact function. This function will allow users to remove a specific contact from the Contact Book.

Your Task:
Create a function named delete_contact that takes one argument: contact_book (a dictionary).
Get input for the contact's name that the user wants to delete.
Check if the name exists in the contact_book:
If it exists, remove the contact from the dictionary.
Print: "Contact deleted successfully!".
If the contact does not exist, print: "Contact not found!".
"""

MENU = """1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit
"""


def display_menu():
    print("Contact Book Menu:")
    print(MENU)


def add_contact(contact_book):
    name = input()
    if name in contact_book:
        print("Contact already exists!")
        return

    phone = input()
    email = input()
    address = input()
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")


def view_contact(contact_book):
    name = input()
    if name not in contact_book:
        print("Contact not found!")

    else:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")


def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        current = contact_book[name]

        phone = input()
        email = input()
        address = input()

        if phone != "":
            current["phone"] = phone

        if email != "":
            current["email"] = email

        if address != "":
            current["address"] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")

    else:
        print("Contact not found!")
