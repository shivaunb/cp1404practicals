"""
CP1404 - Practical
Quick Pick Lottery Ticket Generator
Write program to generate a quick pick ticket depending on how many lines a user has purchased
"""
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Generates quick pick length of users choice using random numbers. """
    number_of_quick_picks = int(input("How many quick picks? "))

    while number_of_quick_picks < 0:
        print("Invalid number. Try again")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()

        print(" ".join(f"{number:2}" for number in quick_picks))


main()
