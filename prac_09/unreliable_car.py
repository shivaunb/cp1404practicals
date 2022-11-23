"""
CP1404 Practical
Unreliable Car Class
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the Unreliable Car based on random reliability."""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super(UnreliableCar, self).drive(distance)
        return distance_driven
