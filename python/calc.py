
print("Hello! Miles to kilometers calculator")

while True:
    type_of_calc = input("Enter 'm' for miles to kilometers or 'k' for kilometers to miles: ")

    if type_of_calc == "m":
        answer = float(input("Enter a number of miles:"))
        print(f"{answer} miles is {answer * 1.609} kilometers")
    elif type_of_calc == "k":
        answer = float(input("Enter a number of Kilometers:"))
        print(f"{answer} kilometers is {answer / 1.609} miles")
    elif type_of_calc == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid input")
