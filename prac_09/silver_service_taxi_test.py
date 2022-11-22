"""
CP1404 Practical
Silver Service Taxi cCass tests
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.calculate_fare())
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)

main()
