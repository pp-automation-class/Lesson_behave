print ("Hello! Inches to cm converter")

while True:
    type_of_conversion = input("Enter 'in' for inches to centimeters or 'cm' for centimeters to inches: ")

    if type_of_conversion == 'in':
        answer = float(input("Enter a number of inches:"))
        print(f"{answer} inches is in{answer * 2.54} cm")
    elif type_of_conversion == 'cm':
        answer = float(input("Enter a number of centimeters:"))
        print (f"{answer} centimeters is {answer / 2.54} inches")
    elif type_of_conversion == 'q':
        break
    else:
        print("Invalid input")