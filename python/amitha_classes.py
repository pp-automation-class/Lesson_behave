

class Amitha_cars:
    def __init__(self, model, make, year, condition: bool = True):
        self.model = model
        self.make = make
        self.year = year
        self.condition = condition


    def __str__(self):
        return f'{self.model} {self.make} {self.year} {self.condition}'


c1 = Amitha_cars("Ford", "Mustang", 1999, True)
print(c1)


class Amitha_person:
    def __init__(self, firstname, lastname, age, marital_status=None, address=None):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.marital_status = marital_status if marital_status else "single"
        self.address = address

    def __str__(self):
        return (f'{self.firstname} {self.lastname}, Age: {self.age}, '
                f'Marital Status: {self.marital_status}, Address: {self.address}')


# Creating an object
p1 = Amitha_person('Amitha', 'Ganesh', 30,
                   'single', 'Dublin, CA')

print(p1)