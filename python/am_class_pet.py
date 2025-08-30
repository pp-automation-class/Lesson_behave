"""Simple OOP example for pets.

This module defines a small class hierarchy:
- Pet: a base class that encapsulates shared attributes/behavior
- Cat, Dog, Parrot: specific pet types that extend Pet with extra actions

Key details:
- Birthday must be a string in the format '%m/%d/%Y' (e.g., '12/25/2020').
- Pet.age is a read-only @property that returns an integer number of years or None if
  the birthday is missing or invalid.
- The bottom of the file contains a quick, runnable demonstration.
"""

import datetime


class Pet:
    """Base class for pets with common attributes and behaviors."""

    # Default "vocabulary" of the pet.
    # Subclasses typically override this to provide species-specific sounds.
    sounds = None

    # A short description of how this pet moves by default.
    # You can override this per-instance (as shown in the demo below).
    moves = "moving"

    # Default "anatomy" values; subclasses (e.g., Parrot) override as needed.
    legs = 4
    wings = 0

    def __init__(self, name: str, birthday=None, breed=None):
        """Initialize a new Pet.

        Parameters:
            name (str): The pet's display name.
            birthday (str | None): Birthday in '%m/%d/%Y' format (e.g., '07/04/2023').
                                   If None or invalid, age will be reported as None.
            breed (str | None): Optional breed information (mostly applies to dogs/cats).
        """
        self.name = name
        self.birthday = birthday
        self.breed = breed

    def __str__(self) -> str:
        """Return a human-readable summary of this pet."""
        result = f"{self.__class__.__name__} {self.name}, born on {self.birthday}"
        if self.breed:
            result += f", breed: {self.breed}"
        return result

    @property
    def age(self):
        """Compute the pet's integer age in years.

        Returns:
            int | None: Age in whole years, or None if birthday is not provided or
                        not in the expected '%m/%d/%Y' format.

        Notes:
            - The calculation subtracts 1 year if the pet hasn't yet had its birthday
              in the current year (standard "age in years" logic).
            - Invalid dates (e.g., '13/40/2020') are handled gracefully by returning None.
        """
        if self.birthday is None:
            return None
        try:
            # Parse the birthday string to a date object.
            birthday = datetime.datetime.strptime(self.birthday, "%m/%d/%Y").date()
            today = datetime.date.today()

            # Compute year difference and adjust if today's month/day is before the birthday.
            age = (
                today.year
                - birthday.year
                - ((today.month, today.day) < (birthday.month, birthday.day))
            )
            return age
        except ValueError:
            # Return None if the string can't be parsed as a valid date.
            return None

    def print_age(self, form: int = 1):
        """Print the age to stdout in one of two formats.

        Parameters:
            form (int): If 1, prints '<name> is N year(s) old'.
                        Otherwise, prints 'Age of <name>: N year(s)'.

        Notes:
            - If birthday is missing/invalid, nothing is printed.
            - Proper pluralization for 'year' is applied.
        """
        if self.birthday:
            age = self.age
            if isinstance(age, int):
                s = 's' if age > 1 else ''
                if form == 1:
                    print(f"{self.name} is {age} year{s} old")
                else:
                    print(f"Age of {self.name}: {age} year{s}")

    def sound(self):
        """Print a line describing the sounds this pet makes, if defined."""
        if self.sounds:
            print(f"{self.name} {self.sounds}")

    def move(self):
        """Print a line describing how this pet moves."""
        print(f"{self.name} {self.moves}")


class Cat(Pet):
    """Cat implementation with species-specific sounds and actions."""

    sounds = "meows, chirrups, hisses, purrs, chatters, and growls"
    moves = "running, jumping, climbing and sneaks"

    def purr(self):
        """Print that the cat is purring."""
        print(f"{self.name} purrs")

    def scratch(self):
        """Print that the cat is scratching."""
        print(f"{self.name} scratches")

    def meow(self):
        """Print that the cat is meowing."""
        print(f"{self.name} meows")


class Dog(Pet):
    """Dog implementation with species-specific sounds and actions."""

    sounds = "barks, woofs, arfs, ruffs, yips, and growls"
    moves = "running, jumping"

    def bark(self):
        """Print that the dog is barking."""
        print(f"{self.name} barks")

    def fetch(self, item: str):
        """Print that the dog fetches a given item."""
        print(f"{self.name} fetches the {item}")

    def guard(self):
        """Print that the dog is guarding."""
        print(f"{self.name} is guarding")


class Parrot(Pet):
    """Parrot implementation with wings, flight, and voice behavior."""

    sounds = "talks, gurgles, trills, whistles and squawks"
    moves = "flying, climbing"
    legs = 2
    wings = 2

    def fly(self):
        """Print that the parrot is flying."""
        print(f"{self.name} is flying")

    def talk(self):
        """Print that the parrot is talking."""
        print(f"{self.name} talks")


# --- Demonstration section below ---
# Create a generic Pet. Override 'moves' for this instance to show per-instance customization.
some = Pet("Sam", "12/4/2023")
some.moves = "crawls"
print(some)
some.print_age(form=2)  # Use alternate print format.
some.sound()            # No output expected because Pet.sounds is None by default.
some.move()

print()

# Create a Cat and demonstrate various behaviors and inherited functionality.
my_cat = Cat("Lucy", "4/22/2020")
print(my_cat)
my_cat.print_age(form=2)
my_cat.sound()   # Uses Cat.sounds override.
my_cat.purr()
my_cat.scratch()
my_cat.meow()
my_cat.move()

print()

# Create a Dog with a breed and demonstrate dog-specific behaviors.
my_dog = Dog("Beavis", "8/11/2017", "Chihuahua")
print(my_dog)
my_dog.print_age()
my_dog.sound()
my_dog.move()
my_dog.bark()
my_dog.fetch("toy")
my_dog.guard()

print()

# Create a Parrot and demonstrate special anatomy (wings) and actions (fly, talk).
my_bird = Parrot("Pikachu", "7/4/2023")
print(my_bird)
my_bird.print_age()
my_bird.sound()
my_bird.move()
my_bird.fly()
my_bird.talk()
