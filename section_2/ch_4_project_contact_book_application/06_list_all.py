"""
List All


Challenge

The next step is to create the list_all_contacts function. This function will allow users to view all the contacts stored in the Contact Book along with their details.

Your Task:
Create a function named list_all_contacts that takes one argument: contact_book (a dictionary).
Check if the contact_book is empty:
If it is empty, print: "No contacts available.".
If it is not empty:
Loop through each contact in the dictionary and print their name, phone, email, and address in a readable format.
Expected Behavior:
For a contact_book containing:

{
    "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
    "Bob": {"phone": "234-567-8901", "email": "bob@example.com", "address": "456 Oak Ave"}
}
The output should be:

Name: Alice
Phone: 123-456-7890
Email: alice@example.com
Address: 123 Main St

Name: Bob
Phone: 234-567-8901
Email: bob@example.com
Address: 456 Oak Ave
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


def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")

    else:
        for key, value in contact_book.items():
            print(f"Name: {key}")
            print(f"Phone: {value['phone']}")
            print(f"Email: {value['email']}")
            print(f"Address: {value['address']}")
            print()
