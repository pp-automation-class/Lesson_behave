# Calculator 1
def summary(num1, num2):
    print(f"Sum: {num1 + num2}")
    print(f"Diff: {num1 - num2}")
    print(f"Product: {num1 * num2}")
    print(f"Product: {num1 / num2}")
a = 6
b = 2
summary(a,b)

a = 30
b = 15
summary(a,b)

a = 8
b = 10
summary(a,b)

# Calculater 2

def sum(x, y):
    return x + y
x=6
y=2
print(f'x={x}', f'y={y}', f'sum = {sum(x, y)}')

def sub(x, y):
    return x - y
print(f'x={x}', f'y={y}', f'sub = {sub(x, y)}')

def mul(x, y):
    return x * y
print(f'x={x}', f'y={y}', f'mul = {mul(x, y)}')

def div(x, y):
    return x / y
print(f'x={x}', f'y={y}', f'div = {div(x, y)}')