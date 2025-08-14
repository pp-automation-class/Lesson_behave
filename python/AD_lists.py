from python.main import my_list

my_list = [1, 2, 3, 5, 7, 9, 10, 12, 5, 4, 12, 0, 36, 99]
print (my_list)
print(type(my_list))
print (my_list [0:8])
print(len(my_list))
print (my_list [-2])

my_list_2 = {'apple', 'ball', 'mountain', 'snow', 'sunshine'}
print(my_list_2)

my_dict = {'name': 'Alex', 'age': 5, 'id': 'd5d5d5'}
print (my_dict)

def my_function(x, y, z):
    return x + y + z + 1
x=0
y=0
z=0
print(my_function(x, y, z))

x=0
y=1
z=0
print(my_function(x, y, z))

x=0
y=1
z=1
print(my_function(x, y, z))

# calculator
# sum
def sum(x, y):
    return x + y
x=1
y=2
print(f'x={x}  '
      f'y={y}    '
      f'sum = {sum(x, y)}')

# subtraction
def minus (x, y):
    return x - y
x=1
y=2
print(f'x={x}  '
      f'y={y}    '
      f'subtraction = {minus(x, y)}')

# multiplication
def multiply (x, y):
    return x * y
x=1
y=2
print(f'x={x}  '
      f'y={y}    '
      f'multiplication = {multiply(x, y)}')

# division
def divide (x, y):
    return x / y
x=1
y=2
print(f'x={x}  '
      f'y={y}    '
      f'division = {divide(x, y)}')

# square root
def sqrt (x):
    return x ** 0.5
x=9
print(f'x={x}         '
      f'square root = {sqrt(x)}'   )

# exponent
def exp (x, y):
    return x ** y
x=2
y=3
print(f'x={x}  '
      f'y={y}    '
      f'exponent = {exp(x, y)}')