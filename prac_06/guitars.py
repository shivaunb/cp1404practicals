"""
CP1404 Practical
Playing the Guitars
Expected time: 60 minutes
Actual time: 45 minutes
"""

from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        name = input("Name: ").title()

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>15} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")


main()
