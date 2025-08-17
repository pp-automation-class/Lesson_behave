
# answer = int(input("What is your age?"))

# if answer < 5:
#     print("Less than 5")

# if answer > 5:
#     print("Less or equal 5")
#
# if answer <= 5:
#     print("More than 5")

# if answer == 5:
#     print("Equal 5")

# if answer != 5:
#     print("Not Equal 5")

# and
# True and True  => True
# True and False  => False
# False and True  => False
# False and False  => False

# if answer <=5 and answer <= 10:
#     print("Between 5 and 10")

# or
# True or True  => True
# True or False  => True
# False or True  => True
# False or False  => False

#14
#    false     or       true      and     true
#       false        or          true    => true
# if answer <=5 or  answer >= 10 and answer != 15:
#     print(" 5")

#15
#    false     or       true      and     false
#       false        or          false   => false
# if answer <=5 or  answer >= 10 and answer != 15:
#     print(" 5")


# answer = int(input("What is your age?"))
# if True:
#     print("Not Equal 5")

# if not True:
#     print("Not Equal 5")

# if not False:
#     print("Not Equal 5")

# arr = [1, 2, 3, 4, 5]
# if arr:
#     print("Full array")

# arr = []
# if not arr:
#      print("Full array")

# name = "Alice"
# if name:
#      print("Full array")

# name = ""
# if name:
#      print("Full array")

# name = ""
# if not name:
#      print("Empty!")

answer = int(input("What is your age?"))

# if answer >= 5:
#     print("Greater than 5")
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


