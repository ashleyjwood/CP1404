from person import Person


class Student(Person):
    """Create a child class, Student, of Person."""

    def __init__(self, student_id: int, course: str, **kwargs):
        """Initialise a Student object."""
        super().__init__(**kwargs)
        self.id = student_id
        self.course = course

    def __str__(self):
        """Return a string representation of a Student."""
        return f"{super().__str__()} [{self.id}] {self.course}"

    def __repr__(self):
        """Return a string representation of a Student."""
        return str(vars(self))
