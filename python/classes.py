# OOP
# Animal =============
# legs = 4
# tail = True
#
# def breath():
#     print("breathing")
#
# def run():
#     print("running")
#
# # ======================
# # Cat =============
# cat_legs = 4
# cat_tail = True
#
# def cat_breath():
#     print("breathing")
#
# def cat_run():
#     print("running")
#
# # ======================
#
# cat_breath()

class Animal:
    def __init__(self, legs_amount: int, tail: bool = True):
        self.legs = legs_amount
        self.tail = tail
        self.name = "Animal"

    def breath(self):
        print(f"breathing and has {self.legs} legs")

    def run(self):
        print("running")


class Cat(Animal):
    def meow(self):
        print("meow")

    def run(self):
        print("running and climbing tree")


class Dog(Animal):
    def bark(self):
        print("bark")


cat = Cat(4, False)
cat.meow()
cat.run()

print("++++++++++++")

dog = Dog(4)
dog.bark()
dog.run()
