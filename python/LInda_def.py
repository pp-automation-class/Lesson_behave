from python.conditions import answer

value1 = int(input("Enter a number: "))
value2 = int(input("Enter another number: "))


def add(value1, value2):
    print(f"add = {value1 + value2}")


def multiply(value1, value2):
    print(f"multiply = {value1 * value2}")


def divide(value1, value2):
    print(f"divide = {value1 / value2}")


add(value1, value2)
multiply(value1, value2)
divide(value1, value2)

age = int(input("What is your age?"))
if age < 5:
    pass
