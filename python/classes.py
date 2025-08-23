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
    legs = None
    name = None

    def breath():
        print("breathing")

    def run():
        print("running")

cat = Animal()
dog = Animal()


cat.legs = 4
dog.legs = 5
print(cat)
print(dog)


