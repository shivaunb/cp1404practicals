"""
CP1404 Practical
Emails - store user email and name in a dictionary

Estimated time: 40 minutes
Actual time:
"""

email_to_name = {}
email = input("Email: ")
name = email.split("@")
print(name[0].split("."))

