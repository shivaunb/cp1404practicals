"""
CP1404 - Taxi Test Program. Test Taxi Class
"""
from prac_09.taxi import Taxi


def main():
    """Test Taxi Class."""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
