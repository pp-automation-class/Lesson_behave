var = 12
firstName = 'John'
lastName = "Doe"
# Basic calculator
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

#Coversion of Km to Miles and vise versa
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

#Printing a Fibonoci series till n

n = int(input("Enter the number for fibnoccci series: "))

def fibnoccci(firstNumber,secondNumber):
    i = 1
    fibSeries = [firstNumber, secondNumber]
    while i <=n:
        nextNumber = firstNumber + secondNumber
       # fibSeries = [firstNumber, secondNumber]
      #  print(f"Fibonnoccci = {firstNumber} , {secondNumber} , {nextNumber}")
        firstNumber = secondNumber
        secondNumber = nextNumber
        fibSeries.append(nextNumber)
        i = i + 1
    print(fibSeries)
fibnoccci(0,1)




