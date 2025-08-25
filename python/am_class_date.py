import datetime


# Example of a class with a property that handles date input in multiple formats
class Person:
    def __init__(self, first_name: str, last_name: str, birthday=None):
        self.first_name = first_name
        self.last_name = last_name
        self._birthday = birthday

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        if isinstance(value, datetime.date):
            self._birthday = value
        else:
            try:
                self._birthday = datetime.datetime.strptime(value, "%m/%d/%Y")
            except ValueError:
                raise ValueError("Incorrect data format, should be MM/DD/YYYY")


p1 = Person("John", "Smith")
print(p1.first_name)
p1.birthday = "12/1/1990"
print(p1.birthday, type(p1.birthday))

p1.birthday = datetime.datetime(1990, 12, 1)
print(p1.birthday, type(p1.birthday))
