from time import sleep
# print("Hello from functions_imports.py")

# sleep(10)
name = "Bob"

def calculate_sum(a, b):
    print(name)
    return a + b

def calculate_multiply(a, b):
    print(name)
    return a * b

def print_result(result):
    print(f"Result: {result}")

summ = calculate_sum(1, 2)
print_result(summ)

mult = calculate_multiply(1, 2)
print_result(mult)
