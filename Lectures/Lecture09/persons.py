from student import Student
from person import Person
from employee import Employee
from musician import Musician
from datetime import datetime


def main():
    """Main function used for testing Parent/Child classes."""
    p1 = Person("Alex", datetime(1999, 12, 25))

    s1 = Student(name="Jane", date_of_birth=datetime(1998, 1, 1), student_id=12345678, course="AB0123")

    e1 = Employee("Sarah", datetime(2005, 1, 19), 100.0)
    e1.address = "123 Home Street"

    m1 = Musician("Steve", datetime(1969, 8, 14), "Rock", 5)

    people = [p1, s1, e1, m1]
    for person in people:
        print(person)


main()
