"""
CP1404 Practical
Wimbledon - Write a program to display information regarding Wimbledon Gentlemen Singles Champions

Estimated time: 45 minutes
Actual time: 62 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Display details regarding Wimbledon champions and countries by reading data file."""
    records = get_records(FILENAME)
    champion_to_amount, countries = process_records(records)
    display_records(champion_to_amount, countries)


def get_records(filename):
    """Get records from data file in a list of lists."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Create a dictionary of champions and a set of countries from records."""
    champion_to_amount = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_amount[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_amount[record[CHAMPION_INDEX]] = 1
    return champion_to_amount, countries


def display_records(champion_to_amount, countries):
    """Display champions with number of wins and display countries."""
    print(f"Wimbledon Champions:")
    for name, amount in champion_to_amount.items():
        print(f"{name} {amount}")

    print(f"These {len(countries)} countries have won Wimbledon: ")
    countries = sorted(countries)
    print(", ".join(countries))


main()
