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
            {"unit": "Acre", "value": 247.105381},
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
            {"unit": "Carat", "value": 5000},
        ],
    },
    {
        "unit": "Volume and Liquid Capacity",
        "items": [
            {"unit": "Millilitre (ml)", "value": 1000},
            {"unit": "Litre (l)", "value": 1},
            {"unit": "Teaspoon (US)", "value": 202.884136},
            {"unit": "Tablespoon (US)", "value": 67.628045},
            {"unit": "Cup (US)", "value": 4.226753},
            {"unit": "Pint (US)", "value": 2.113376},
            {"unit": "Quart (US)", "value": 1.056688},
            {"unit": "Gallon (US)", "value": 0.264172},
            {"unit": "Fluid Ounce (US)", "value": 33.814023},
            {"unit": "Cubic Centimetre (cm³)", "value": 1000},
            {"unit": "Cubic Metre (m³)", "value": 0.001},
            {"unit": "Cubic Foot (ft³)", "value": 0.035315},
        ],
    },
]


def output_units(units_list):
    count = 1
    print("Your choice:")
    for unit in units_list:
        print(f"{count}. {unit['unit']}")
        count += 1
    print("0. Exit")


def select_unit(units_list):
    result = -1
    while result == -1:
        output_units(units_list)
        choiced_item = input("=>")
        if choiced_item.isdigit():
            result = int(choiced_item)
            if result < 0 or result > len(units_list):
                result = -1
        if result == -1:
            print("\nInvalid choice. "
                  "Enter number of the unit or 0 for exit.\n")
    return result


def pretty_float(number):
    result = f"{number:,.6f}"
    if number < 0.001 or number > 999999999999:
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


def convert_units(item_index, units_list):
    quantity = -1
    while quantity:
        print(f"Enter the quantity of {units_list[item_index]['unit']}")
        print("0. choice the unit")
        quantity = input("=>")
        try:
            quantity = float(quantity)
            if not quantity:
                break
            if quantity < 0:
                continue
            #
            coefficient = 1 / units_list[item_index]["value"]
            for unit in units_list:
                result = pretty_float(unit["value"] * coefficient * quantity)
                print(f"{unit['unit']}: {result}")
            print("\n")
            #
        except ValueError:
            quantity = -1


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
                convert_units(choice_item - 1,
                              core_dictionary[choice - 1]["items"]
                              )

print("\nHave a nice day!")
