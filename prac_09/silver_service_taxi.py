"""
CP1404 Practical - Silver Service Taxi Class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a Silver Service Taxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        Taxi.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def calculate_fare(self):
        """Calculate fare of Silver Service Taxi."""
        return self.flagfall + super().get_fare()
