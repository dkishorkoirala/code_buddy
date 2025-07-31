"""
Add Contact


Challenge

Now, create the add_contact function that takes one argument: contact_book (a dictionary). The function should:

Get input for the contact's name, phone, email, and address.
Check if the name already exists in the dictionary. If it does, print: "Contact already exists!".
If not, save the contact in the following format:

contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
}
Then print: "Contact added successfully!".
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
