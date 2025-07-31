"""
Edit Contact


Challenge

The next step is to create the edit_contact function. This function will allow users to update the details of an existing contact in the Contact Book.

Your Task:
Create a function named edit_contact that takes one argument: contact_book (a dictionary).
Get input for the contact's name that the user wants to edit.
Check if the name exists in the contact_book:
If it exists, prompt the user to input new values for the contact's phone, email, and address (in that order!).
If the user provides no input (presses Enter), keep the current value for that field (in this case the input will be an empty string, '').
Update the contact's information in the dictionary.
Print: "Contact updated successfully!".
If the contact does not exist, print: "Contact not found!".
Expected Behavior:
For a contact_book containing:

{"Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"}}
If the user enters:

Alice
987-654-3210

456 Elm St
The updated contact_book should look like this:

{"Alice": {"phone": "987-654-3210", "email": "alice@example.com", "address": "456 Elm St"}}
If the user enters a name that does not exist:

Bob
The output should be:

Contact not found!
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
