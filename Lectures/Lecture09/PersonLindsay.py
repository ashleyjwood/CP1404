from datetime import datetime


class PersonLindsay:
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.name = name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        date_string = datetime.strftime(self.date_of_birth, '%m/%d/%Y')
        return f"{self.name} ({date_string})"

    def age(self):
        return int((datetime.now() - self.date_of_birth).days) / 365.2425


p1 = PersonLindsay("Jane", datetime(1999, 2, 14))
print(p1)
print(p1.age())
