"""
CP1404 Practical
Guitar Class
Estimated time: 60 minutes
Actual time: 35 minutes
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar class that stores the details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the details of a guitar as a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get age of guitar based on current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine is a guitar is vintage based on its age."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year
