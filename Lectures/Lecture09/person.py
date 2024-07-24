import datetime


class Person:
    def __init__(self, name="", date_of_birth="", age=0):
        """Initialise Person class."""
        self.name = name
        self.date_of_birth = date_of_birth
        self.age = age

    def get_date(self):
        """Get the user's date of birth."""
        date = input("What is your date of birth? (DD/MM/YYYY): ")
        self.date_of_birth = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        return self.date_of_birth

    def calculate_age(self):
        """Calculate the age of the person."""
        today = datetime.date.today()

        # calculate the user's age first looking only at the year,
        # then compare (month,day) tuples and subtract the resulting 1 or 0 (True or False)
        self.age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return self.age


if __name__ == "__main__":
    person = Person(name="John")
    person.get_date()
    person.calculate_age()
    print(f"{person.name}, you are {person.age} years old.")
