"""
CP1404 Practical
Languages Class
Estimated time: 30 minutes
Actual time: 24 minutes
"""


class ProgrammingLanguage:
    """Represent a Programming Language."""

    def __init__(self, name, typing, reflection, year):
        """Build a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string of the ProgrammingLanguage"""
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine is typing is dynamic in language."""
        if self.typing == "Dynamic":
            return True
