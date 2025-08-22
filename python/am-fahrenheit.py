def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9 / 5 + 32


def fahrenheit_to_rankine(fahrenheit):
    """Convert Fahrenheit to Rankine."""
    return fahrenheit + 459.67


def rankine_to_fahrenheit(rankine):
    """Convert Rankine to Fahrenheit."""
    return rankine - 459.67

def rankine_to_celsius(rankine):
    """Convert Rankine to Celsius."""
    return (rankine - 491.67) * 5 / 9


def main():
    print("Temperature Conversion Tool")
    print("---------------------------")

    while True:
        print("\nSelect conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Fahrenheit to Kelvin")
        print("4. Kelvin to Fahrenheit")
        print("5. Fahrenheit to Rankine")
        print("6. Rankine to Fahrenheit")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            value = float(input("Enter the temperature value: "))

            if choice == "1":
                result = celsius_to_fahrenheit(value)
                print(f"{value} °C = {result:.2f} °F")
            elif choice == "2":
                result = fahrenheit_to_celsius(value)
                print(f"{value} °F = {result:.2f} °C")
            elif choice == "3":
                result = fahrenheit_to_kelvin(value)
                print(f"{value} °F = {result:.2f} K")
            elif choice == "4":
                result = kelvin_to_fahrenheit(value)
                print(f"{value} K = {result:.2f} °F")
            elif choice == "5":
                result = fahrenheit_to_rankine(value)
                print(f"{value} °F = {result:.2f} °R")
            elif choice == "6":
                result = rankine_to_fahrenheit(value)
                print(f"{value} °R = {result:.2f} °F")
        else:
            print("Invalid choice, please try again.")
