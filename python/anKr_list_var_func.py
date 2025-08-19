# 4 TYPE OF ARRAYS IN PYTHON
# 1 List
# value = [1, 2, 3, 4, 5]
#
# values = ["abcd", 2, 3.5, 8, True, [ 1, 2, 3]]
# print(values)
# print(type(values))
#
# values = [ 7, "abc", 9, True, 2]
# #          0    1    2   3    4
# print(values[0])
# print(type(values[0]))
#
# values = [ 7, "abc", 9, True, 2]
# #          0    1    2   3    4
# print(values[5])
# print(type(values[5]))
#
# values = [ 7, "abc", 9, True, 2]
# #         -5   -4   -3   -2   -1
# print(values[-4])
# print(type(values[-4]))
#
# name = "Alice"
# print(name [-2])
#
# name = "Alice"
# print(name [2:])
#
# name = "Alice"
# print(name [1:3])
#
# name = "Alice"
# print(name [:3])
#
# name = "Al ice"
# print(name [:5])
#
# 2 Tuple
# coordinates = ( 10.0, 20.0)
# print(coordinates)
# print(type(coordinates))
#
# coordinates = ( 7, "abc", 9, True, 2)
# print(coordinates [1])
# print(type(coordinates[1]))
#
# 3 Dictionary
# student = ["Alice", 20, "S12345"]
# student[0] = "Bob"
#
# student = ["Alice", 20, "S12345"]
# student.append("Smith")
# student.append("Smith")
#
# student = {"name": "Alice",
#            "age": 20,
#            "id": "S12345"}
#
# student = {"name": "Alice", "age": 20, "id": "S12345"}
# print(student)
# print(type(student))
#
# student = {"name": "Alice", "age": 20, "id": "S12345"}
# print(student["name"])
# print(type(student))
#
# student = {"name": "Alice", "age": 20, "id": "S12345"}
# print(student["age"])
# print(type(student))
#
# student = {"name": "Alice", "age": 20, "id": "S12345"}
# student["name"] = "Bob"
#
# student = {"name": "Alice", "age": 20, "id": "S12345"}
# student["address"] = "New York"
#
# student = {"age": 20, "id": "S12345", "name": "Alice"}
# student["name"] = "Bob"
# student["address"] = "New York"
#
# print(student)
# print(type(student))
#
# 4 Set
# values = [1, 2, 3, 3, 4, 5, 5]_
#
# values = (1, 2, 3, 3, 4, 5, 5)
#
# values = {1, 2, 3, 3, 4, 5, 5}
#
# values = [1, 2, 3 , 4, "apple", "banana", "apple"]
#
# values = set([1, 2, 3 , 4, "apple", "banana", "apple"])
#
# values = list(set([1, 2, 3 , 4, "apple", "banana", "apple"]))
# print(values)
# print(type(values))

# age = 6.2
# name = "Charlik"
#
# print(age)
# print(type(age))
#
# age = 6.2
# name = "Charlik"
#
# print(age, name)
# print(type(age), type(name))
# Variables can be reassigned
#
# age = 6.2
# name = "Charlik"
# size = 1.75
# last_name = 'Smith'
# middle_name = 'Charlik "Red" Smith'
# middle_name2 = "Charlik 'Red' Smith"
# middle_name3 = 'Charlik \'Red\' Smith'
# middle_name4 = "Charlik \"Red\" Smith"
# next_line = 'Charlik \n"Red" \n Smith'
#
# number_in_quotes = "12"
# number_in_quotes2 = '21.5'
#
# my_variable = input("Enter value:")
# print(my_variable)
# print(type(my_variable))
#
# a = 3
# b = 5
# c = a + b
#
# a = 3
# b = 5
# c = a - b
#
# a = 3
# b = 5
# c = a * b
#
# a = 3
# b = 5
# c = a / b
#
# a = 8
# b = 4
# c = a / b
#
# a = 6
# b = 3.0
# c = a + b
#
# a = 6
# b = "4"
# c = a + b
#
# a = "8"
# b = "4"
# c = a + b
# print(c)
# print(type(c))
#
# value_1 = input("Enter value1:")
# value_2 = input("Enter value2:")
# sum = value_1+ value_2
# print(sum)
# print(type(sum))
#
# value_1 = int(input("Enter value 1:"))
# value_2 = int(input("Enter value 2:"))
# sum = value_1+ value_2
# print(sum)
# print(type(sum))
#
# value_1 = float(input("Enter value 1:"))
# value_2 = float(input("Enter value 2:"))
# sum = value_1+ value_2
# print(sum)
# print(type(sum))
#
# a = True
# b = False
#
# print(a)
# print(type(a))5
#
#
# value_1 = float(input("Enter value 1:"))
# value_2 = float(input("Enter value 2:"))
# sum = value_1 == value_2
# print(sum)
# print(type(sum))

# Functions
#
# a = 22
# b = 5
# print(a + b)
#
# a = 34
# b = 6
# print(a + b)
#
#
# a = 22
# b = 5
# print(f"Sum: {a + b}")
#
# a = 34
# b = 6
# print(f"Sum: {a + b}")
#
# def summary(num1, num2):
#     print(num1 + num2)
# a = 6
# b = 2
# summary(a,b)
#
# def summary(num1, num2):
#     print(f"Sum: {num1 + num2}")
# a = 1
# b = 2
# summary(a,b)
# a = 15
# b = 22
# summary(a,b)
#
# def (num1, num2):
#     print(f"Sum = {num1 + num2}")
# a = 1
# b = 2
# summary(a,b)
# a = 15
# b = 22
# summary(a,b)
# a = 56
# b = 2
# summary(a,b)
# a = 22
# b = 2
# summary(a,b)
#
# print("End of program")

def remind_to_rest():
    print("I am tired!")
    print("Have a rest!")

remind_to_rest()
print("End of program")

