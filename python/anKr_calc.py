# CALCULATOR 1

# def summary(num1, num2):
#     print(f"Sum: {num1 + num2}")
#     print(f"Diff: {num1 - num2}")
#     print(f"Product: {num1 * num2}")
#     print(f"Product: {num1 / num2}")
# a = 6
# b = 2
# summary(a,b)
#
# a = 30
# b = 15
# summary(a,b)
#
# a = 8
# b = 10
# summary(a,b)

#  CALCULATOR 2

# def sum(x, y):
#     return x + y
# x=6
# y=2
# print(f'x={x}', f'y={y}', f'sum={sum(x, y)}')
#
# def sub(x, y):
#     return x - y
# print(f'x={x}', f'y={y}', f'sub={sub(x, y)}')
#
# def mul(x, y):
#     return x * y
# print(f'x={x}', f'y={y}', f'mul={mul(x, y)}')
#
# def div(x, y):
#     return x / y
# print(f'x={x}', f'y={y}', f'div={div(x, y)}')


# CALCULATOR 3 Miles to kilometers calculator

# print("Hello! Miles to kilometers calculator")
# answer = float(input("Enter a number of miles: "))
# print(f"{answer} miles is {answer*1.609} kilometers")


# print("Hello! Miles to kilometers calculator")
# while True:
#     type_of_calc = input("Enter 'm' for miles, 'k' for kilometers or or 'q' to quit: ")
#
#     if type_of_calc == 'm':
#         answer = float(input("Enter a number of miles: "))
#         print(f"{answer} miles is {answer * 1.609} kilometers")
#     elif type_of_calc == 'k':
#         answer = float(input("Enter a number of kilometers: "))
#         print(f"{answer} kilometers is {answer / 1.609} miles ")
#     elif type_of_calc == 'q':
#         print("Goodbye")
#         break
#     else:
#         print("Invalid input")


#CALCULATOR 4  Miles to kilometers calculator with 2 decimal places

# print("Hello! Miles to kilometers calculator")
#
# while True:
#     type_of_calc = input("Enter 'm' for miles, 'k' for kilometers or or 'q' to quit: ")
#
#     if type_of_calc == 'm':
#         answer = float(input("Enter a number of miles: "))
#         result = answer * 1.609
#         print(f"{answer} miles is {result:.2f} kilometers")
#     elif type_of_calc == 'k':
#         answer = float(input("Enter a number of kilometers: "))
#         result = answer / 1.609
#         print(f"{answer} kilometers is {result:.2f} miles ")
#     elif type_of_calc == 'q':
#         print("Goodbye")
#         break
#     else:
#         print("Invalid input")


#CALCULATOR 5  Fahrenheit to Celsius

# print("Hello! Fahrenheit to Celsius calculator")
#
# while True:
#     type_of_calc = input("Enter 'f' for Fahrenheit, 'c' for Celsius or or 'q' to quit: ")
#
#     if type_of_calc == 'f':
#         temp_f = float(input("Enter temperature in Fahrenheit: "))
#         temp_c = (temp_f - 32) * 5 / 9
#         print(f"{temp_f:.1f}°F is {temp_c:.1f}°C")
#
#     elif type_of_calc == 'c':
#         temp_c = float(input("Enter temperature in Celsius: "))
#         temp_f = (temp_c * 9 / 5) + 32
#         print(f"{temp_c:.1f}°C is {temp_f:.1f}°F")
#
#     elif type_of_calc == 'q':
#         print("Goodbye")
#         break
#
#     else:
#         print("Invalid input")

# CALCULATOR 5  Fahrenheit to Celsius

print("Hello! Tip calculator")

while True:
    choice = input("Enter 't' to calculate tip or 'q' to quit: ")

    if choice == 't':
        bill = float(input("Enter the bill amount: $"))
        tip_percent = float(input("Enter the tip percentage (%): "))
        tip = bill * (tip_percent / 100)
        total = bill + tip
        print(f"Bill: ${bill:.2f}")
        print(f"Tip:  ${tip:.2f}")
        print(f"Total to pay: ${total:.2f}")
    elif choice == 'q':
        print("Goodbye")
        break
    else:
        print("Invalid input")

