"""
CP1404 Practical 2
Program to get a valid score and print stars
"""


def main():
    """Menu style program to obtain user score with options to print score status or stars."""
    score = 0
    print("(G)et Score \n(P)rint Score \n(S)tars")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print("Your score of {} is {}".format(score, (determine_score_status(score))))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print("Menu: ")
        choice = input("> ").upper()
    print("Finished")


def get_valid_score():
    """Get a valid score."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Score: "))
    return score


def determine_score_status(score):
    """Determine score status of given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print number of stars as determined by user score"""
    print("*" * score)

main()
