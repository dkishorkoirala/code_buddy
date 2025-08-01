"""
Everything Together


Challenge

Now that you’ve built all the individual functions for the Contact Book, it’s time to put them together to create the full program!

Your Task:
Combine the functions you’ve created:
display_menu: Displays the menu options for the user.
add_contact: Adds a new contact to the Contact Book.
view_contact: Displays details for a specific contact.
edit_contact: Updates an existing contact’s information.
delete_contact: Removes a contact from the Contact Book.
list_all_contacts: Displays all the contacts in the Contact Book.
Create a dictionary called contact_book to store the contacts.
Write a loop that:
Displays the menu using display_menu.
Accepts user input for the menu choice.
Calls the appropriate function based on the user’s choice.
Continues until the user selects the option to exit the program.
Expected Behavior:
When you run the program, it should:

Show a menu of options for the user to choose from.
Allow the user to interact with the Contact Book by calling the appropriate function.
Exit the program cleanly when the user selects the "Exit" option.
This final step combines all the knowledge you’ve gained into a fully functioning Contact Book application. Enjoy seeing your hard work come together! 🎉
"""

MENU = """1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit"""


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


contact_book = {}

while True:
    display_menu()

    choice = input()

    if choice == "1":
        add_contact(contact_book)

    elif choice == "2":
        view_contact(contact_book)

    elif choice == "3":
        edit_contact(contact_book)

    elif choice == "4":
        delete_contact(contact_book)

    elif choice == "5":
        list_all_contacts(contact_book)

    elif choice == "6":
        break

    else:
        print("Invalid input")
