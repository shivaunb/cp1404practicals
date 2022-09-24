"""
CP1404 - Practical 2
Get a password with minimum length and display asterisks
"""

MINIMUM_LENGTH = 5


def part_one():
    """Get eligible password and print asterisks."""
    password = input("Enter Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password not long enough. Try again")
        password = input("Enter Password: ")
    for i in range(len(password)):
        print("*", end="")


# part_one()

def main():
    """Get eligible password and print asterisks using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Enter Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password needs to be longer than {} characters. Try again".format(minimum_length))
        password = input("Enter Password: ")
    return password


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


main()
