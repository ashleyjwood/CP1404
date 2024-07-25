from person import Person
from datetime import datetime


class Employee(Person):
    """Create a child class, Employee, of Person."""

    def __init__(self, name: str, date_of_birth: datetime.date, salary: float):
        """Initialise an Employee object, which also has a salary."""
        super().__init__(name, date_of_birth)
        self.salary = salary

    def __str__(self):
        """Return string representation of an Employee."""
        return f"{super().__str__()} ${self.salary:.2f}"
