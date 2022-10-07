"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_period = int(input("How many months? "))

    for month in range(1, month_period + 1):
        income = float(input(f"Enter income for month {month}: $"))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print report based on incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
