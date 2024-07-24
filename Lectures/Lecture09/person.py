import datetime


class Person:
    """Create a person object."""

    def __init__(self, name: str, date_of_birth: datetime.date):
        """Initialise Person class."""
        self.name = name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        """Return the user's name and date of birth as a string."""
        date_string = datetime.datetime.strftime(self.date_of_birth, "%d/%m/%Y")
        return f"{self.name} ({date_string})"

    def calculate_age(self):
        """Calculate the age of the person."""
        today = datetime.date.today()

        # calculate the user's age first looking only at the year,
        # then compare (month,day) tuples and subtract the resulting 1 or 0 (True or False)
        age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age


if __name__ == "__main__":
    person = Person("Michael", datetime.datetime(1990, 9, 15))
    print(person)
    print(f"Age {person.calculate_age()}")
