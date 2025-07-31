"""
Display Menu


Challenge

In this project, we will build a Contact Book application step by step by breaking it into small, manageable functions. The first step is to create a display_menu function.

Create a function named display_menu that prints the main menu options for the Contact Book.

The menu should include the following options:

Add Contact
View Contact
Edit Contact
Delete Contact
List All Contacts
Exit
This function will be the starting point of the program, helping users navigate through the options.

Check the test case for the output format!
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
