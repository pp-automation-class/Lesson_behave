# HW - Calculator by Laura Stark

print("Calculator")
print ("Type 'q' for operation to quit")

while True:
    value_1 = (float(input("Enter value 1: ")))
    operation = input("Enter type of operation:")
    value_2 = float(input("Enter value 2: "))

    if operation == "+":
        print(f"{value_1} + {value_2} = {value_1 + value_2}")

    elif operation == "-":
        print(f"{value_1} - {value_2} = {value_1 - value_2}")

    elif operation == "*":
        print(f"{value_1} * {value_2} = {value_1 * value_2}")

    elif operation == "/":
        if value_2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        else:
            print(f"{value_1} / {value_2} = {value_1 / value_2}")


