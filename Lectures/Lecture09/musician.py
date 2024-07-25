from person import Person
from datetime import datetime


class Musician(Person, ):
    """Create a child class, Musician, of Person."""

    def __init__(self, name: str, date_of_birth: datetime.date, style: str, duration: int):
        """Initialise a Musician object."""
        super().__init__(name, date_of_birth)
        self.style = style
        self.duration = duration

    def play(self):
        """Return the duration of the musician."""
        return f"{self.duration}mins"

    def __str__(self):
        """Return string representation of Musician."""
        return f"{super().__str__()} {self.style} {self.play()}"
