import time

print("Welcome to the Unit Converter!")

conv_rate = {'km_m': 1000, 'm_cm': 100, 'cm_mm': 10}
INVALID_MSG = "Ошибка ввода"

while True:
    type_of_calc = input("\nEnter '1' for kilometers to meters\n"
                         "\nEnter '2' for meters to centimeters\n"
                         "\nEnter '3' for centimeters to millimeters\n")
    if type_of_calc == "1":
        answer = float(input("Enter a number of kilometers:"))
        print(f"{answer} kilometers is {round(answer * conv_rate['km_m'], 2)} meters")
        time.sleep(3)

    elif type_of_calc == "2":
        answer = float(input("Enter a number of meters:"))
        print(f"{answer} meters is {round(answer * conv_rate['m_cm'], 2)} centimeters")
        time.sleep(3)

    elif type_of_calc == "3":
        answer = float(input("Enter a number of centimeters:"))
        print(f"{answer} centimeters is {round(answer * conv_rate['cm_mm'], 2)} millimeters")
        time.sleep(3)

    elif type_of_calc == "q":
        print("Go away!")
        break

    else:
        print(INVALID_MSG)
