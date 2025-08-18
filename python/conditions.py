# <
# <=
# >
# >=
# ==
# !=

# answer = int(input("What is your age? "))

#  15
#   false           true              false
#   false                        false
# if answer <= 5 or answer >= 10 and answer != 15:
#     print("Not Equal 5")
#
# print("End of program")

# and
# True and True => True
# True and False => False
# False and True => False
# False and False => False

# or
# True or True => True
# True or False => True
# False or True => True
# False or False => False


# arr = []
# name = ""

# if not name:
#     print("Empty!")

answer = int(input("What is your age? "))

# if answer >= 5:
#     print("Greater than 5")
#
#     if answer >= 10:
#         print("Greater than 10")

if answer < 5:
    print("Less than 5")
elif answer < 10:
    print("Less than 10")
elif answer < 15:
    print("Less than 15")
else:
    print("Greater than 15")

print("End of program")