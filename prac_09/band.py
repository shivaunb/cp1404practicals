"""
CP1404 Practical
Band Class
"""
from prac_09.musician import Musician


class Band(Musician):
    """Band Class."""

    def __init__(self, name):
        """Construct a Band with a musician and empty instrument collection."""
        super().__init__()
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    # def __repr__(self):
    #     """Return a string representation of a Musician, showing the variables."""
    #     return str(vars(self))

    def add(self, musician):
        """Add a musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the band with the musician & instrument playing their first (or no) instrument."""
        playing_musicians = [musician.play() for musician in self.musicians]
        playing_musicians = "\n".join(playing_musicians)
        return playing_musicians
