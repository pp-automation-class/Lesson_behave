# HW by Laura Stark

# Miles/Kilometers
print("Hello! Miles to kilometers conversion program.")
type_of_conversion = input("Enter 'm' for miles to kilometers' or 'k' for kilometers to miles:")

if type_of_conversion == 'm':
    answer = float(input("Enter a number of miles:"))
    print(f"{answer} miles is {answer * 1.60934} kilometers")

elif type_of_conversion == 'k':
    answer = float(input("Enter a number of Kilometers:"))
    print(f"{answer} kilometers is {answer / 1.60934} miles")

else:
    print("Inavalid input, please enter 'm' or 'k'")
print("End of program")
print("\n")

# Kilo/Pounds

print("Helo! Kilograms to Pounds conversion program.")
while True:
    type_of_conversion = input("Enter 'k' for kilograms to pounds' or 'p' for pounds to kilograms:")

    if type_of_conversion == 'k':
        answer = float(input("Enter number of kilograms:"))
        print(f"{answer} kilograms is {answer * 2.20462} pounds")
        # print("\n")

    elif type_of_conversion == 'p':
        answer = float(input("Enter number of pounds:"))
        print(f"{answer} pounds is {answer / 2.20462} kilograms")
        #
    elif type_of_conversion == 'stop':
        print("Goodbye!")
        break
    else:
        print("Invalid input, please enter 'k' or 'p'")
