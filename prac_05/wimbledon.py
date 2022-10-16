"""
CP1404 Practical
Wimbledon - Write a program to display information regarding Wimbledon Gentlemen Singles Champions
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    records = get_information(FILENAME)
    champion_to_amount, countries = process_records(records)
    print(records)  # test list
    print(champion_to_amount)  # test dictionary
    print(countries)  # test list


def get_information(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    champion_to_amount = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_amount[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_amount[record[CHAMPION_INDEX]] = 1
    return champion_to_amount, countries


main()
