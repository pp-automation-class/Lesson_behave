# def say_hello():
#     print("Hi there!")
# say_hello()
#
# def say_how_are_you():
#     print("How are you?")
# say_how_are_you()
#
# def say_goodbye():
#     print("Добрый вечер!")
# say_goodbye()
#
# def greet(name):
#     print (f"Hi, {name}!")
# greet("Lena")
#
# def say(name):
#     print (f"Hello, {name}!")
# say("Linda")
#
# def что_то(name):
#     print (f"Hi, {name}.")
# что_то("Santa")

# def сложение(a,b,c):
#     print(a+b-c)
# сложение(1,78,4)
# сложение(1,3,7)
#
# def add(a,b):
#     print(a+b)
# add(1,7)

# def add(a,b):
#     return a+b
# result = add(1,2)
# print(result)
#
# def minus(a,b,c):
#     return a-b-c
# result = minus(25, 1,0)
# print(result)
#
# def greet(name = "Гость"):
#     print(f"Hi, {name}!")
# greet()
# greet("Lena")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person("Lena", 37)
# print(p1.name, p1.age)
#
# c1 = Person("Santa", 4)
# print (c1.name)

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

class Cars:
    def __init__(self, years, car_type, doors):
        self.years = years
        self.car_type = car_type
        self.doors = doors

    def __str__(self):   # магический метод
        return f"Машина: {self.car_type}, год выпуска: {self.years}, дверей: {self.doors}"

c1 = Cars(2014, "Honda", 4)

print(c1)   # теперь сработает __str__