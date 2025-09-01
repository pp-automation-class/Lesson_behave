import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG,
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )

print("Hello! Inches to cm converter")
logging.info("Starting the program")

while True:
    type_of_conversion = input("Enter 'in' for inches to centimeters "
                               "or 'cm' for centimeters to inches "
                               "or 'q' to quit: ")

    if type_of_conversion == 'in':
        logging.debug(f"type_of_conversion = {type_of_conversion}")
        answer = float(input("Enter a number of inches:"))
        print(f"{answer} inches is {answer * 2.54} cm")
        logging.info(f"{answer} inches is {answer * 2.54} cm")

    elif type_of_conversion == 'cm':
        logging.debug(f"type_of_conversion = {type_of_conversion}")
        answer = float(input("Enter a number of centimeters:"))
        print(f"{answer} centimeters is {answer / 2.54} inches")
        logging.info(f"{answer} centimeters is {answer / 2.54} inches")

    elif type_of_conversion == 'q':
        logging.debug(f"type_of_conversion = {type_of_conversion}")
        print("Goodbye")
        logging.info("Quitting the program")
        break

    else:
        logging.debug(f"type_of_conversion = {type_of_conversion}")
        logging.info(f"type_of_conversion = {'Invalid input'}")
        print("Invalid input")
