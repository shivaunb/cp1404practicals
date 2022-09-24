"""
CP1404 - Practical 2
Program to determine Score status
"""
import random


def main():
    """Get user score and generate random score and display both score status """
    score = float(input("Enter score: "))
    print("Your score is {}".format((determine_score_status(score))))
    random_score = random.randint(0, 100)
    print("The randomly chosen score is {} and it is {}".format(random_score, (determine_score_status(random_score))))


def determine_score_status(score):
    """Determine score status of given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
