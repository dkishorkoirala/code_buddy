"""
Smart Contact Manager


Challenge

Create a function named organize_contacts that processes a list of contact dictionaries to create a clean contact database.

Each contact dictionary in the input list has these keys:

name: The person's name
email: The person's email address
phone: The person's phone number
Your function should:

Remove duplicate contacts (contacts with the same email or phone number)
Standardize all emails to lowercase
Filter out contacts with invalid email addresses
Filter out contacts with invalid phone numbers
Return a list of cleaned contact dictionaries
Validation rules:

Valid email: Must contain '@' and '.', and must not have spaces
Valid phone: Must contain exactly 10 digits (ignore non-digit characters like dashes or parentheses)
For cleaning phone numbers, you should use Python's str.isdigit() method to extract only the numeric digits from phone numbers. This method returns True if a character is a digit (0-9) and False otherwise, making it perfect for filtering out non-digit characters.

Example Input:
contacts = [
    {"name": "John Doe", "email": "john@email.com", "phone": "123-456-7890"}
]
Expected Output:
[
    {"name": "John Doe", "email": "john@email.com", "phone": "1234567890"}
]
"""


def organize_contacts(contact_list):
    # Helper: validate email
    def is_valid_email(email):
        return "@" in email and "." in email and " " not in email

    # Helper: clean phone (keep only digits)
    def clean_phone(phone):
        return "".join(ch for ch in phone if ch.isdigit())

    # Helper: validate phone
    def is_valid_phone(phone):
        return len(phone) == 10 and phone.isdigit()

    cleaned_contacts = []
    seen_emails = set()
    seen_phones = set()

    for contact in contact_list:
        # Standardize email
        email = contact["email"].strip().lower()

        # Clean phone number
        phone = clean_phone(contact["phone"])

        # Validate
        if not is_valid_email(email):
            continue
        if not is_valid_phone(phone):
            continue

        # Check for duplicates
        if email in seen_emails or phone in seen_phones:
            continue

        # Add to results
        seen_emails.add(email)
        seen_phones.add(phone)
        cleaned_contacts.append(
            {"name": contact["name"].strip(), "email": email, "phone": phone}
        )

    return cleaned_contacts
