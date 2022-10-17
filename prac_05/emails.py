"""
CP1404 Practical
Emails - store user email and name in a dictionary

Estimated time: 40 minutes
Actual time: 45 minutes
"""


def main():
    """Store user email and name in a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        validity = input(f"Is your name {name}? (Y/n) ").upper()
        if validity != "Y" and validity != "":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract potential user name from user email address."""
    prefix = email.split("@")
    parts = (prefix[0].split("."))
    name = " ".join(parts).title()
    return name


main()
