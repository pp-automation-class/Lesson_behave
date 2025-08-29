import datetime


class Pet:
    sounds = None
    moves = "moving"
    legs = 4
    wings = 0

    def __init__(self, name: str, birthday=None):
        self.name = name
        self.birthday = birthday

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}, born on {self.birthday}"

    @property
    def age(self):
        if self.birthday is None:
            return None
        try:
            birth_date = datetime.datetime.strptime(self.birthday, "%m/%d/%Y").date()
            today = datetime.date.today()
            complement = (today.month, today.day) < (birth_date.month, birth_date.day)
            age = today.year - birth_date.year - complement
            return age
        except ValueError:
            return None

    def print_age(self):
        if self.birthday:
            print(f"Age of {self.name}: {self.age} year(s)")

    def sound(self):
        if self.sounds:
            print(f"{self.name} { self.sounds }")

    def move(self):
        print(f"{self.name} { self.moves }")


some = Pet("Sam", "12/4/2023")
print(some)
some.print_age()
some.sound()
some.move()

print("")


class Cat(Pet):
    sounds = "meows, chirrups, hisses, purrs, chatters, and growls"
    moves = "running, jumping, climbing and sneaks"


my_cat = Cat("Lucy", "4/22/2020")
print(my_cat)
my_cat.print_age()
my_cat.sound()
my_cat.move()

print("")


class Dog(Pet):
    sounds = "barks, woofs, arfs, ruffs, yips, and growls"
    moves = "running, jumping"


my_dog = Dog("Beavis", "8/11/2017")
print(my_dog)
my_dog.print_age()
my_dog.sound()
my_dog.move()

print("")


class Parrot(Pet):
    sounds = "gurgles, trills, whistles and squawks"
    moves = "flying, climbing"
    legs = 2
    wings = 2


my_bird = Parrot("Pikachu", "7/4/2023")
print(my_bird)
my_bird.print_age()
my_bird.sound()
my_bird.move()
