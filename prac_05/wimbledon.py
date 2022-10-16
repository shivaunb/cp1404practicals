"""
CP1404 Practical
Wimbledon - Write a program to display information regarding Wimbledon Gentlemen Singles Champions
"""

FILENAME = "wimbledon.csv"


def main():
    records = get_information(FILENAME)
    print(records)


def get_information(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
