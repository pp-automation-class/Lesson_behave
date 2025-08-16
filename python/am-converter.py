
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

def select_unit(units_list):
    count = 1
    print("Select:")
    for unit in units_list:
        print(f"{count}.{unit['unit']}")
        count += 1
    print("0. Exit")
    choice = input("=>")
    if not choice.isdigit():
        result = -1
    else:
        result = int(choice)
        if not (result >= 0 and result <= len(units_list)):
            result = -1
    if result == -1:
        print("\nInvalid choice. Enter number of the unit or 0 for exit.\n")
    return result




while True:
    choice = select_unit(core_dictionary)
    match choice:
        case -1:
            pass
        case 0:
            break
        case _:
            print(f"\nYou have selected {core_dictionary[choice-1]['unit']}")
            while True:
                choice_item = select_unit(core_dictionary[choice-1]["items"])
                match choice_item:
                    case -1:
                        pass
                    case 0:
                        break
                    case _:
                        print(f"\nCalculations {core_dictionary[choice-1]['items'][choice_item-1]['unit']}")

print("\nHave a nice day!")

