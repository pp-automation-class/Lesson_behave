"""Simple math calculator"""
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

def addition(num1, num2):
    print(f"Sum = {num1 + num2}")

def subtraction(num1, num2):
    print(f"Difference = {num1 - num2}")

def multiplication(num1, num2):
    print(f"Result of multiplication = {num1 * num2}")

def division(num1, num2):
    if num2 ==0:
        print("Can't divide by zero!")
    else:
        print(f"Result of division = {num1 / num2}")

def average(num1, num2):
    print(f"Average = {(num1 + num2) / 2}")

addition(num1, num2)
subtraction(num1, num2)
multiplication(num1, num2)
division(num1, num2)
average(num1, num2)