
result = None
try:
    answer_1 = int(input("Enter a number 1: "))
    answer_2 = int(input("Enter a number 2: "))

    result = answer_1 / answer_2

except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("You have entered a wrong value")
except Exception as e:
    print("Something went wrong")
    print(e)

print(result)

# if user provided valid input, it will ignore except and go to print(result) and print the result
# if user provided wrong input, it will go to except and print the corresponding message
# I can add it to my calculator file
# In Java: (try - catch); In Python it is (try - except) duo.