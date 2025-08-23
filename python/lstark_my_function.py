# HW function by LStark

def my_function(**food):

    print("My favorite food is " + food["option1"] + ".")
    print("What is your favorite food?")
    value_1 = input("Enter value 1: ")
    print("My favorite food is " + value_1 + ".")


my_function(option1="Chinese", option2="Italian", option3="Mexican")

print("End of program")
