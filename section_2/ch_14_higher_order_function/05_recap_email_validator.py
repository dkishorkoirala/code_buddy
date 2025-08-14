"""
Recap - Email Validator


Challenge

Create a function named clean_email_list that takes a list of email addresses and returns a list of valid, standardized email addresses.

Requirements:

    - Convert all emails to lowercase and strip all whitespace at the beginning or end

    - Only keep emails that:

        - Contain exactly one '@' symbol

        - Have at least one character before the '@'

        - Have at least one character after the ‘@’

Use map() and filter() to solve the problem.

"""


def clean_email_list(emails):
    # Write your code below
    standardized = map(lambda e: e.strip().lower(), emails)
    valid = filter(
        lambda e: e.count("@") == 1 and e.index("@") > 0 and e.index("@") < len(e) - 1,
        standardized,
    )

    valid_emails = valid
    return list(valid_emails)
