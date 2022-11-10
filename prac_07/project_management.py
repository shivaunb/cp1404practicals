"""
CP1404 - Project Management Program
Estimated Time: 1.5 hours
Actual Time: incomplete.
"""
import datetime

from prac_07.project import Project

FILENAME = "projects.txt"
MENU_PROMPT = "Menu:\nL - Load Projects\nS - Save Projects\nD - Display Projects" \
              "\nF - Filter Projects\nA - Add New Project\nU - Update Project\nQ - Quit"
HEADER = "Name  Start Date  Priority    Cost Estimate   Completion Percentage"


def main():
    """Project management program."""
    projects = load_projects(FILENAME)
    print(projects)
    print(MENU_PROMPT)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("File to load from: ")
            projects = load_projects(filename)
            print(projects)
        elif choice == "S":
            filename = input("File to save to: ")
            save_projects(projects, filename)
        elif choice == "D":
            display(projects)
        elif choice == "F":
            pass
            # date = input("Enter date as dd/mm/YYYY: ")
            # filter_projects(date, projects)
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU_PROMPT)
        choice = input(">>> ").title()
    save_projects(projects, FILENAME)
    print("Thank you using.")


def load_projects(filename):
    """Read a file containing project details and create a list of projects."""
    projects = []
    with open(filename, encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], start_date, parts[2], parts[3], parts[4])
            projects.append(project)
        return projects


def save_projects(projects, filename):
    """Save projects to a text file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=out_file)


def display(projects):
    """Display in two groups: incomplete projects; completed projects, both sorted by priority."""
    print("Incomplete projects: ")
    incomplete_projects = [project for project in projects if not project.is_complete()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    print("Completed projects: ")
    complete_projects = [project for project in projects if project.is_complete()]
    complete_projects.sort()
    for project in complete_projects:
        print(" ", project)


#
# def filter_projects(date, projects):
#     """Display projects that start after the date entered by the user, sorted in date order."""


# def update(projects):
#     """Get project choice and updated based on user input."""
#     for i, project in enumerate(projects):
#


main()
