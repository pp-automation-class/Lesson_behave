# 4 TYPE OF ARRAYS IN PYTHON
# 1 List
# value = [1, 2, 3, 4, 5]

# values = ["abcd", 2, 3.5, 8, True, [ 1, 2, 3]]
# print(values)
# print(type(values))

# values = [ 7, "abc", 9, True, 2]
# #          0    1    2   3    4
# print(values[0])
# print(type(values[0]))

# values = [ 7, "abc", 9, True, 2]
# #          0    1    2   3    4
# print(values[5])
# print(type(values[5]))

# values = [ 7, "abc", 9, True, 2]
# #         -5   -4   -3   -2   -1
# print(values[-4])
# print(type(values[-4]))

# name = "Alice"
# print(name [-2])

# name = "Alice"
# print(name [2:])

# name = "Alice"
# print(name [1:3])

# name = "Alice"
# print(name [:3])

# name = "Al ice"
# print(name [:5])

# 2 Tuple
# coordinates = ( 10.0, 20.0)
# print(coordinates)
# print(type(coordinates))

# coordinates = ( 7, "abc", 9, True, 2)
# print(coordinates [1])
# print(type(coordinates[1]))

# 3 Dictionary
# student = ["Alice", 20, "S12345"]
# student[0] = "Bob"

# student = ["Alice", 20, "S12345"]
# student.append("Smith")
# student.append("Smith")

# student = {"name": "Alice",
#            "age": 20,
#            "id": "S12345"}

# student = {"name": "Alice", "age": 20, "id": "S12345"}
# print(student)
# print(type(student))

# student = {"name": "Alice", "age": 20, "id": "S12345"}
# print(student["name"])
# print(type(student))

# student = {"name": "Alice", "age": 20, "id": "S12345"}
# print(student["age"])
# print(type(student))

# student = {"name": "Alice", "age": 20, "id": "S12345"}
# student["name"] = "Bob"

# student = {"name": "Alice", "age": 20, "id": "S12345"}
# student["address"] = "New York"

# student = {"age": 20, "id": "S12345", "name": "Alice"}
# student["name"] = "Bob"
# student["address"] = "New York"

# print(student)
# print(type(student))

# 4 Set
# values = [1, 2, 3, 3, 4, 5, 5]

# values = (1, 2, 3, 3, 4, 5, 5)

# values = {1, 2, 3, 3, 4, 5, 5}

# values = [1, 2, 3 , 4, "apple", "banana", "apple"]

# values = set([1, 2, 3 , 4, "apple", "banana", "apple"])

values = list(set([1, 2, 3 , 4, "apple", "banana", "apple"]))
print(values)
print(type(values))
