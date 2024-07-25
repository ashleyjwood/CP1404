from student import Student
from person import Person
import datetime


def main():
    """Main function used for testing Parent/Child classes."""
    p1 = Person("Alex", datetime.date(1999, 12, 25))
    print(p1)
    print(p1.calculate_age())
    print()
    s1 = Student(name="Jane", date_of_birth=datetime.date(1998, 1, 1), student_id=12345678, course="AB0123")
    print(s1)
    print(s1.calculate_age())


main()
