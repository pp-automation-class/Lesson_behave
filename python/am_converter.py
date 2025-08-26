core_dictionary = [
    {
        "unit": "Area",
        "items": [
            {"unit": "Square Mile (mi²)", "value": 0.386102},
            {"unit": "Square Yard (yd²)", "value": 1195990},
            {"unit": "Square Foot (ft²)", "value": 10763910},
            {"unit": "Square Inch (in²)", "value": 1550003100},
            {"unit": "Square Kilometre (km²)", "value": 1},
            {"unit": "Hectare (ha)", "value": 100},
            {"unit": "Acre (ac)", "value": 247.105381},
            {"unit": "Square Metre (m²)", "value": 1000000},
            {"unit": "Square Centimetre (cm²)", "value": 10000000000},
        ],
    },
    {
        "unit": "Length",
        "items": [
            {"unit": "Metre (m)", "value": 1},
            {"unit": "Inch (in)", "value": 39.370079},
            {"unit": "Foot (ft)", "value": 3.28084},
            {"unit": "Yard (yd)", "value": 1.093613},
            {"unit": "Mile (mi)", "value": 0.000621371},
            {"unit": "Kilometre (km)", "value": 0.001},
            {"unit": "Centimetre (cm)", "value": 100},
            {"unit": "Millimetre (mm)", "value": 1000},
            {"unit": "Micrometre (µm)", "value": 1000000},
            {"unit": "Astronomical Unit (AU)", "value": 6.6845871088e-12},
            {"unit": "Light Year (ly)", "value": 1.05702341e-16},
            {"unit": "Parsec (pc)", "value": 3.240779282e-17},
        ],
    },
    {
        "unit": "Mass/Weight",
        "items": [
            {"unit": "Kilogram (kg)", "value": 1},
            {"unit": "Pound (lb)", "value": 2.204623},
            {"unit": "Ounce (oz)", "value": 35.273962},
            {"unit": "Milligram (mg)", "value": 1000000},
            {"unit": "Gram (g)", "value": 1000},
            {"unit": "Tonne (t)", "value": 0.001},
            {"unit": "Stone (st)", "value": 0.157473},
            {"unit": "Carat (ct)", "value": 5000},
        ],
    },
    {
        "unit": "Temperature",
        "items": [
            {"unit": "Celsius (°C)", "from": "quantity", "to": "universal"},
            {
                "unit": "Fahrenheit (°F)",
                "from": "(quantity - 32) * 5 / 9",
                "to": "(universal * 9 / 5) + 32",
            },
            {
                "unit": "Kelvin (K)",
                "from": "quantity - 273.15",
                "to": "universal + 273.15",
            },
            {
                "unit": "Rankine (°R)",
                "from": "(quantity - 491.67) * 5 / 9",
                "to": "(universal * 9 / 5) + 491.67",
            },
        ],
    },
    {
        "unit": "Volume and Liquid Capacity",
        "items": [
            {"unit": "Millilitre (ml)", "value": 1000},
            {"unit": "Litre (l)", "value": 1},
            {"unit": "Teaspoon US (tsp)", "value": 202.884136},
            {"unit": "Tablespoon US (tbsp)", "value": 67.628045},
            {"unit": "Cup US (c)", "value": 4.226753},
            {"unit": "Pint US (pt)", "value": 2.113376},
            {"unit": "Quart US (qt)", "value": 1.056688},
            {"unit": "Gallon US (gal)", "value": 0.264172},
            {"unit": "Fluid Ounce US (fl oz)", "value": 33.814023},
            {"unit": "Cubic Centimetre (cm³)", "value": 1000},
            {"unit": "Cubic Metre (m³)", "value": 0.001},
            {"unit": "Cubic Foot (ft³)", "value": 0.035315},
        ],
    },
]


def output_units(units_list):
    """
    Outputs a formatted list of units along with an option to exit.

    This function takes a list of units as input, displays them in an enumerated
    format, and appends an option to exit. It is intended for use cases where a user
    needs to select an option from a presented list.

    :param units_list: A list of dictionaries, where each dictionary contains
        information about a unit. It must include a 'unit' key with a string value.
    :return: None
    """
    count = 1
    print("Your choice:")
    for unit in units_list:
        print(f"{count}. {unit['unit']}")
        count += 1
    print("Q. Exit")


def select_unit(units_list):
    """
    Selects a unit from a given list by presenting options to the user and allowing
    them to make a choice. The function repeatedly prompts the user until they enter
    a valid number corresponding to the units in the list, or until they choose to
    exit by entering 'Q'. The selected unit's index is returned.

    :param units_list: A list of unit names or options presented for user selection.
    :type units_list: list
    :return: The index of the selected unit, or 0 if the user chooses to exit.
    :rtype: int
    """
    result = -1
    while result == -1:
        output_units(units_list)
        choiced_item = input("=>")
        if choiced_item.isdigit():
            result = int(choiced_item)
            if result < 0 or result > len(units_list):
                result = -1
        elif choiced_item.upper() == "Q":
            result = 0
        if result == -1:
            print("\nInvalid choice. Enter number of the unit or Q for exit.\n")
    return result


def pretty_float(number):
    """
    Format a numeric value into a neatly formatted string representation, adjusting the
    formatting based on the magnitude of the number for better readability.

    :param number: The numeric value to be formatted.
    :type number: float
    :return: A string representation of the number, formatted with different levels
        of precision and scientific notation depending on its magnitude.
    :rtype: str
    """
    result = f"{number:,.6f}"
    if number == 0:
        return "0"
    if abs(number) < 0.001 or abs(number) > 999999999999:
        result = f"{number:,.6e}"
    elif number > 99999:
        result = f"{number:,.0f}"
    elif number > 9999:
        result = f"{number:,.1f}"
    elif number > 999:
        result = f"{number:,.2f}"
    elif number > 99:
        result = f"{number:,.3f}"
    elif number > 9:
        result = f"{number:,.4f}"
    elif abs(number - round(number, 0)) < 0.001:
        result = f"{number:,.0f}"
    if result.find(".") != -1:
        result = result.rstrip("0").rstrip(".")
    return result


def convert_units_with_value(
    item_index: int, units_list: list, quantity: float
) -> None:
    """
    Convert a given quantity from a specific unit to all other units in the units_list.

    This function calculates the equivalent value of a given quantity in a specified
    base unit to all other units provided in the `units_list`. For each unit, the
    converted value is calculated based on the ratio of the base unit's value to
    the current unit's value, multiplied by the given quantity. The results are then
    printed in a formatted manner.

    :param item_index: Index of the base unit in the units_list from which the conversion
        is initiated.
    :type item_index: int
    :param units_list: A list of dictionaries where each dictionary represents a unit.
        Each dictionary must have keys "value" and "unit", where "value" is the
        conversion factor relative to a standard base and "unit" is the unit identifier.
    :type units_list: list
    :param quantity: The amount in the specified base unit to be converted into
        other units.
    :type quantity: float
    :return: None
    :rtype: None
    """
    coefficient = 1 / units_list[item_index]["value"]
    for unit in units_list:
        result = pretty_float(unit["value"] * coefficient * quantity)
        print(f"{unit['unit']}: {result}")
    print("\n")


def convert_units_with_to_and_from(
    item_index: int, units_list: list, quantity: float
) -> None:
    """
    Converts a given quantity from one unit to multiple target units using conversion
    formulas provided in the units list. The function evaluates conversion formulas
    for each unit, transforms the supplied quantity, and prints the results for all
    available units from the list.

    :param item_index: Index of the unit in the units_list to convert from.
    :type item_index: int
    :param units_list: A list of dictionaries where each dictionary contains keys:
        "from" (conversion formula to a universal unit), "to" (conversion formula
        from the universal unit), and "unit" (the name or symbol of the unit).
    :type units_list: list
    :param quantity: The numerical value to be converted from the specified unit.
    :type quantity: float
    :return: This function does not return any value; it prints converted quantities
        for all target units directly.
    :rtype: None
    """
    universal: float = eval(units_list[item_index]["from"], {"quantity": quantity})
    for unit in units_list:
        result = pretty_float(eval(unit["to"], {"universal": universal}))
        print(f"{unit['unit']}: {result}")
    print("\n")


def convert_units(item_index: int, units_list: list) -> None:
    """
    Converts units for a given item and updates its value or performs calculations based
    on the provided quantity. The function interacts dynamically through the console.

    :param item_index: The index of the unit within the units list to convert.
    :type item_index: int
    :param units_list: A list of dictionaries containing unit details. Each dictionary
        must have information necessary for the conversion such as 'unit', 'value',
        or 'to' and 'from' mapping for conversion.
    :type units_list: list
    :return: None
    """
    while True:
        print(f"Enter the quantity of {units_list[item_index]['unit']}")
        print("Q. choice the unit")
        quantity = input("=>")
        if quantity.upper() == "Q":
            return
        try:
            quantity = float(quantity)
            if "value" in units_list[item_index]:
                if quantity <= 0:
                    continue
                convert_units_with_value(item_index, units_list, quantity)
            elif "to" in units_list[item_index]:
                convert_units_with_to_and_from(item_index, units_list, quantity)
        except ValueError:
            pass


# main code
print("Welcome to Unit Converter!")
choice = -1
while choice:
    choice = select_unit(core_dictionary)
    if choice:
        print(f"\n{core_dictionary[choice-1]['unit']}")
        choice_item = -1
        while choice_item:
            choice_item = select_unit(core_dictionary[choice - 1]["items"])
            if choice_item:
                convert_units(choice_item - 1, core_dictionary[choice - 1]["items"])

print("\nHave a nice day!")
