import datetime


class Person:
    def __init__(self, first_name: str, last_name: str, birthday=None):
        self.birthday = birthday
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, born on {self.birthday}"

    def age(self):
        if self.birthday is None:
            return None
        birth_date = datetime.datetime.strptime(self.birthday, "%m/%d/%Y").date()
        today = datetime.date.today()
        age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
        return age


p1 = Person("John", "Smith", "12/1/1990")

print(p1.first_name)
print(p1.last_name)

print(p1.birthday)

print(p1.age())

print(p1)
