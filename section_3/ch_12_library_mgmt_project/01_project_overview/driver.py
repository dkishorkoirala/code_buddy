# TODO: Import the Library class from library.py
# Use format: from library import Library
from library import Library

# Comprehensive test case handler
test_case = input()

if test_case == "basic_library_creation":
    # TODO: Create a library with name "Test Library"
    # TODO: Print the library object (this will call the __str__ method)
    l1 = Library("Test Library")
    print(l1)

elif test_case == "library_attributes":
    # TODO: Create a library with name "Test Library"
    # TODO: Print the library's name attribute
    # TODO: Print the length of the books list
    # TODO: Print the length of the users list
    l2 = Library("Test Library")
    print("Name:", l2.name)
    print("Books:", len(l2.books))
    print("Users:", len(l2.users))

elif test_case == "multiple_libraries":
    # TODO: Create two different libraries with names "Library 1" and "Library 2"
    # TODO: Print both library objects
    l3 = Library("Library 1")
    l4 = Library("Library 2")
    print(l3)
    print(l4)

elif test_case == "empty_name":
    # TODO: Create a library with an empty string as the name
    # TODO: Print the library object
    l5 = Library("")
    print(l5)

elif test_case == "special_characters":
    # TODO: Create a library with the name "!@#$%^&*()"
    # TODO: Print the library object
    l6 = Library("!@#$%^&*()")
    print(l6)

elif test_case == "very_long_name":
    # TODO: Create a library with a name of exactly 100 'A' characters (use "A" * 100)
    # TODO: Print the library object
    name = "A" * 100
    l7 = Library(name)
    print(l7)

elif test_case == "add_books_users":
    # TODO: Create a library with name "Test Library"
    # TODO: Add these items to the books list: ["Book1", "Book2", "Book3"]
    # TODO: Add these items to the users list: ["User1", "User2"]
    # TODO: Print the library object (should show updated counts)
    l8 = Library("Test Library")
    l8.books = ["Book1", "Book2", "Book3"]
    l8.users = ["User1", "User2"]
    print(l8)

elif test_case == "empty_lists":
    # TODO: Create a library with name "Test Library"
    # TODO: Verify that books and users lists are empty by printing their lengths
    l9 = Library("Test Library")
    print("Books length:", len(l9.books))
    print("Users length:", len(l9.users))

elif test_case == "type_validation":
    # TODO: Create a library with the integer 123 as the name
    # TODO: Print the library object (should convert to string)
    l10 = Library(123)
    print(l10)
