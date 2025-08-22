ENTER_B = 'Enter next number: '
ENTER_A = 'Enter a number:'


AD_my_list = [1, 2, 3, 5, 7, 9, 10, 12, 5, 4, 12, 0, 36, 99]
print(AD_my_list)
print(type(AD_my_list))
print(AD_my_list[0:8])
print(len(AD_my_list))
print(AD_my_list[-2])

my_list_2 = {'apple', 'ball', 'mountain', 'snow', 'sunshine'}
print(my_list_2)

my_dict = {'name': 'Alex', 'age': 5, 'id': 'd5d5d5'}
print(my_dict)


def my_function(x, y, z):
    return x + y + z + 1


x = 0
y = 0
z = 0


print(my_function(x, y, z))

x = 0
y = 1
z = 0


print(my_function(x, y, z))

x = 0
y = 1
z = 1


print(my_function(x, y, z))

# calculator
# Addition


def sum(x, y):
    return x + y


x = 1
y = 2


print(f'x={x}   '
      f'y={y}\n'
      f'sum = {sum(x, y)}\n')


# Subtraction
def minus(x, y):
    return x - y


x = 1
y = 2


print(f'x={x}   '
      f'y={y}\n'
      f'subtraction = {minus(x, y)}')


# multiplication
def multiply(x, y):
    return x * y


x = 1
y = 2


print(f'x={x}   '
      f'y={y}\n'
      f'multiplication = {multiply(x, y)}')


# division
def divide(x, y):
    return x / y


x = 1
y = 2


print(f'x={x}   '
      f'y={y}\n'
      f'division = {divide(x, y)}')


# square root
def sqrt(x):
    return x ** 0.5


x = 9
print(f'x={x}\n'
      f'square root = {sqrt(x)}')


# exponent
def exp(x, y):
    return x ** y


x = 2
y = 3


print(f'x={x}   '
      f'y={y}\n'
      f'exponent = {exp(x, y)}\n')


# calculator 2.0
a = float(input('Addition:\n' + ENTER_A))
b = float(input(ENTER_B))


def sum(a, b):
    return a + b


print(f'sum = {sum(a, b)}\n')


a = float(input('Subtraction:\n' + ENTER_A))
b = float(input(ENTER_B))


def minus(a, b):
    return a - b


print(f'Subtraction = {minus(a, b)}\n')

a = float(input('Multiplication:\n' + ENTER_A))
b = float(input(ENTER_B))


def multiply(a, b):
    return a * b


print(f'Multiplication = {multiply(a, b)}\n')

a = float(input('Division:\n' + ENTER_A))
b = float(input(ENTER_B))


def divide(a, b):
    return a / b


print(f'Division = {divide(a, b)}\n')

a = float(input('Exponentiation:\n' + ENTER_A))
b = float(input('Enter b(exponent): '))


def exp(a, b):
    return a ** b


print(f'Exponentiation = {exp(a, b)}\n')

a = float(input('Percentage (a/b*100):\n' + ENTER_A))
b = float(input(ENTER_B))


def percent(a, b):
    return a / b * 100


print(f'Percentage = {percent(a, b)}\n')
