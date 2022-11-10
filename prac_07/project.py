"""
CP1404 - Project Class
Time Estimate: 1hr 15mins
"""
import datetime


class Project:
    """Represent information about a project."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        """Construct a project from the information provided."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        """Determine if project is complete."""
        return self.completion_percentage == 100
