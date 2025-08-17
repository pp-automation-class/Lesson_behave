
core_dictionary = [ {"unit":"Mass/Weight",
                     "items":[{"unit":"Kilogram (kg)","value":1},
                              {"unit":"Pound (lb)","value":2.204623},
                              {"unit":"Ounce (oz)","value":35.273962}
                              ]
                     },
                    {"unit": "Length",
                     "items": [{"unit": "Metre (m)", "value": 1},
                               {"unit": "Inch (in)", "value": 39.370079},
                               {"unit": "Foot (ft)", "value": 3.28084}
                               ]
                     }
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
        choice = input("=>")
        if choice.isdigit():
            result = int(choice)
            if not (result >= 0 and result <= len(units_list)): result = -1
        if result == -1: print("\nInvalid choice. Enter number of the unit or 0 for exit.\n")
    return result

def convert_units(item_index,units_list):
    quantity = -1
    while quantity:
        print(f"Enter the quantity of {units_list[item_index]['unit']}")
        print("0. choice the unit")
        quantity = input("=>")
        try:
            quantity = float(quantity)
            if not quantity: break
            #
            coefficient = 1/units_list[item_index]["value"]
            for unit in units_list:
                result = round(unit['value'] * coefficient * quantity, 4)
                print(f"{unit['unit']}: {result}")
            print("\n")
            #
        except ValueError:
            quantity = -1




#main code
print("Welcome to Unit Converter!")
choice = -1
while choice:
    choice = select_unit(core_dictionary)
    if choice :
            print(f"\n{core_dictionary[choice-1]['unit']}")
            choice_item = -1
            while choice_item:
                choice_item = select_unit(core_dictionary[choice-1]["items"])
                if choice_item: convert_units( choice_item-1, core_dictionary[choice-1]["items"] )

print("\nHave a nice day!")

