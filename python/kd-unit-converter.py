"""Unit Converter"""

print("Welcome to Unit Converter.\nSelect units to convert:\n")
print("1. Miles to kilometers")
print("2. Kilometers to miles")
print("3. Fahrenheit to celsius")
print("4. Celsius to fahrenheit")
print("5. Quit")

while True:
    choice = input("Choose an option: ")
    if choice == "1":
        answer = float(input("Enter a number of miles: "))
        print(f"{answer} miles is {answer * 1.609} kilometers")
    elif choice == "2":
        answer = float(input("Enter a number of kilometers: "))
        print(f"{answer} kilometers is {answer / 1.609} miles")
    elif choice == "3":
        answer = float(input("Enter temperature in fahrenheit: "))
        print(f"{answer} fahrenheit is {(answer - 32) * 5/9} celsius")
    elif choice == "4":
        answer = float(input("Enter temperature in celsius: "))
        print(f"{answer} celsius is {(answer / 5/9) + 32} fahrenheit")
    elif choice == "5":
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid input, try again.")

