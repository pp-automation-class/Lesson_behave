
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Lena", 37)
print(p1.name, p1.age)

c1 = Person("Santa", 4)
print (c1.name)

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