import time

print("Welcome to the Length Calculator")

conv_rate = {'mi': 1.60934, 'ft': 0.3048, 'in': 2.54}
INVALID_MSG = "Invalid input"

while True:
    calc_directions = input("Enter '1' Empire to Metric units or '2' Metric to Empire units\n'q' to quit:")
    if calc_directions == "1":
        while True:
            type_of_calc = input("\nEnter '1' for miles --> kilometers;\n"
                                 "      '2' for feet --> meters;\n"
                                 "      '3' for inches --> centimeters;\n"
                                 "      'b' Previous menu\n"
                                 "Select an option: ")
            if type_of_calc == "1":
                answer = float(input("Enter a number of miles:"))
                print(f"{answer} miles is {round(answer * conv_rate['mi'], 2)} kilometers")
                time.sleep(2)

            elif type_of_calc == "2":
                answer = float(input("Enter a number of feet:"))
                print(f"{answer} miles is {round(answer * conv_rate["ft"], 2)} meters")
                time.sleep(2)

            elif type_of_calc == "3":
                answer = float(input("\nEnter a number of inches:"))
                print(f"{answer} inches is {round(answer * conv_rate["in"], 2)} centimeters")
                time.sleep(2)

            elif type_of_calc == "b":
                break

            else:
                print(INVALID_MSG)

    elif calc_directions == "2":
        while True:
            type_of_calc = input("Enter '1' for kilometers --> miles;\n"
                                 "      '2' for meters --> feet ;\n"
                                 "      '3' for  centimeters --> inches;\n"
                                 "      'b' Previous menu\n"
                                 "Select an option: ")
            if type_of_calc == "1":
                answer = float(input("Enter a number of kilometers:"))
                print(f"{answer} kilometers is {round(answer / conv_rate["mi"], 2)} miles")
                time.sleep(2)

            elif type_of_calc == "2":
                answer = float(input("Enter a number of meters:"))
                print(f"{answer} meters is {round(answer / conv_rate["ft"], 2)} feet")
                time.sleep(2)

            elif type_of_calc == "3":
                answer = float(input("Enter a number of centimeters:"))
                print(f"{answer} centimeters is {round(answer / conv_rate["in"], 2)} inches")
                time.sleep(2)

            elif type_of_calc == "b":
                break

            else:
                print(INVALID_MSG)

    elif calc_directions == "q":
        print("Goodbye!")
        break

    else:
        print(INVALID_MSG)
