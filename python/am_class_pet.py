import datetime


class Pet:
    sounds = None
    moves = "moving"
    legs = 4
    wings = 0

    def __init__(self, name: str, birthday=None, breed=None):
        self.name = name
        self.birthday = birthday
        self.breed = breed

    def __str__(self) -> str:
        result = f"{self.__class__.__name__} {self.name}, born on {self.birthday}"
        if self.breed:
            result += f", breed: {self.breed}"
        return result

    @property
    def age(self):
        if self.birthday is None:
            return None
        try:
            birthday = datetime.datetime.strptime(self.birthday, "%m/%d/%Y").date()
            today = datetime.date.today()
            age = (
                today.year
                - birthday.year
                - ((today.month, today.day) < (birthday.month, birthday.day))
            )
            return age
        except ValueError:
            return None

    def print_age(self):
        if self.birthday:
            print(f"Age of {self.name}: {self.age} year(s)")

    def sound(self):
        if self.sounds:
            print(f"{self.name} {self.sounds}")

    def move(self):
        print(f"{self.name} {self.moves}")


some = Pet("Sam", "12/4/2023")
print(some)
some.print_age()
some.sound()
some.move()

print("")


class Cat(Pet):
    sounds = "meows, chirrups, hisses, purrs, chatters, and growls"
    moves = "running, jumping, climbing and sneaks"

    def purr(self):
        print(f"{self.name} purrs")

    def scratch(self):
        print(f"{self.name} scratches")

    def meow(self):
        print(f"{self.name} meows")


my_cat = Cat("Lucy", "4/22/2020")
print(my_cat)
my_cat.print_age()
my_cat.sound()
my_cat.purr()
my_cat.scratch()
my_cat.meow()
my_cat.move()

print("")


class Dog(Pet):
    sounds = "barks, woofs, arfs, ruffs, yips, and growls"
    moves = "running, jumping"

    def bark(self):
        print(f"{self.name} barks")


my_dog = Dog("Beavis", "8/11/2017", "Chihuahua")
print(my_dog)
my_dog.print_age()
my_dog.sound()
my_dog.move()
my_dog.bark()

print("")


class Parrot(Pet):
    sounds = "talks, gurgles, trills, whistles and squawks"
    moves = "flying, climbing"
    legs = 2
    wings = 2

    def fly(self):
        print(f"{self.name} is flying")

    def talk(self):
        print(f"{self.name} talks")


my_bird = Parrot("Pikachu", "7/4/2023")
print(my_bird)
my_bird.print_age()
my_bird.sound()
my_bird.move()
my_bird.fly()
my_bird.talk()
