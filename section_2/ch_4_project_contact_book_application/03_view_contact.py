"""
View Contact


Challenge

Create a function named view_contact that displays details of a specific contact.

Your function should:

Take a contact book dictionary as input
Ask the user to enter a contact name
Display the contact's details if found
Print "Contact not found!" if the contact doesn't exist
When displaying a contact, use this exact format:

Name: [name]
Phone: [phone]
Email: [email]
Address: [address]
Example:
If the contact book contains Alice's information and the user enters "Alice", output:

Name: Alice
Phone: 123-456-7890
Email: alice@example.com
Address: 123 Main St
If the user enters "Bob" (who doesn't exist), output:

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
