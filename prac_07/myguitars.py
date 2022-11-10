"""
CP1404 Practical
More guitars!
"""

from prac_06.guitar import Guitar


def main():
    guitars = []

    in_file = open('guitars.csv', "r")
    for line in in_file:
        parts = line.strip().split(',')
        parts[1] = int(parts[1])
        parts[2] = float(parts[2])
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)

    in_file.close()
    print("Add Guitar to list or press enter to finish!")
    name = input("Name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.")
        name = input("Name: ").title()

    guitars.sort()
    print("Guitars in year order:")
    for guitar in guitars:
        print(f"{guitar.name:<25} from {guitar.year} is worth ${guitar.cost:.2f}")

    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
