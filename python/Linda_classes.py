
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Lena", 37)
print(p1.name, p1.age)


c1 = Person("Santa", 4)
print(c1.name)


class Cars:
    def __init__(self, years, car_type, doors):
        self.years = years
        self.car_type = car_type
        self.doors = doors

    def describe(self):

        print(f"Car:{self.car_type}, год выпуска: {self.years}, имеет дверей:{self.doors}")


c1 = Cars(2014, "Honda", 4)
print(c1.years, c1.car_type, c1.doors)
c2 = Cars(2020, "Audi", 2)
print(c2.years, c2.car_type, c2.doors)

c1.describe()
c2.describe()


class Dog:
    def __init__(self, name, age, hair_color, breed):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.breed = breed

    def bark(self):
        print(f"{self.name} говорит: Гав-гав!")
        print("Когда радуется виляет хвостом")

    def description(self):
        print(f"{self.name} -- {self.age} года, порода {self.breed} имеет окрас {self.hair_color}")


dog1 = Dog("Santa", 4, "ginger", "mini golden doodle")
dog1.bark()
dog1.description()


class Books:
    def __init__(self, Author: str, name: str, pages: int):
        self.Author = Author
        self.name = name
        self.pages = pages

    def read_themthelf(self):
        print("you can choose Author to read the book")

    def description(self):
        print(f"{self.name} написана {self.Author} имеет {self.pages} страниц.")


book1 = Books("J K Rowling", "Harry Potter", 636)
book2 = Books("A С Пушкин", "сказки", 222)

book1.description()
book2.read_themthelf()
print(book1.name)


class Math_book(Books):

    def algebra(self):
        print("вычитать и умножать")

    def __str__(self):
        return f"Книга по математике: {self.name} написана {self.Author} имеет {self.pages} страниц"


m1 = Math_book("Piphagor", "Theorem", 1)

print(m1)


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def authenticate(self):
        if self.password == "Hello":
            self.logged_in = True
            print(f"{self.username} logged in successfully.")
        else:
            print("Invalid credentials.")


user = Login("Lina", "Hello")
user.authenticate()
