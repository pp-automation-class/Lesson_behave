var = 12
firstName = 'John'
lastName = "Doe"

value1 = float(input("Enter a number: "))
value2 = float(input("Enter another number: "))

def sum(value1, value2):
    print(f"Sum = {value1 + value2}")

def diffrence(value1, value2):
    print(f"diffrence = {value1 - value2}")

def multiply(value1, value2):
    print(f"multiply = {value1 * value2}")

def division(value1, value2):
    if 0 == value2:
        print(f"Cannot be divided by 0")
    else:
        print(f"division = {value1 / value2}")

sum(value1, value2)
diffrence(value1, value2)
multiply(value1, value2)
division(value1, value2)

type_converion = input("Type M for coverstion to miles or type K for coverstion to kilometers ")
covertion = float(input("Enter a number: "))
def conversion(covertion):
    if type_converion == "M":
        print(f"kilomters to miles = {covertion * 0.621371}")
    elif type_converion == "K":
        print(f"miles to kilometers = {covertion * 1.609344}")
    else:
        print("type the correct coverstion type")

conversion(covertion)
