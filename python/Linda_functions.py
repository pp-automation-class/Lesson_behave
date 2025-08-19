# 1. Function without parameters
def say_goodbye():
    print("Goodbye, world!")
say_goodbye()



def say_hello():
    print("Hello, world!")

say_hello()

def tell_me_name():
    print("My name is Google.")
tell_me_name()

def как_я_зае_устала():
    print("Пора отдыхать!")
как_я_зае_устала()

def не_входить():
    print("Не входить!")
не_входить()

# 2. Function with parameters

def greet(name):
    print(f"Hello, {name}!")
greet("Linda")
greet("Santa")

def write_your_name(name):
    print(f"напишите ваше имя: {name}")
write_your_name("Linda")
write_your_name("Santa")

def write_your_name(name):
    print(f" {name}")
write_your_name("Linda")
write_your_name("Santa")

# 3. Function with a return value

def add(a, b):
    return a + b
result = add(5, 3)
print(result)

def grett(name):
    return f"Hello, {name}!"
greeting = grett("Linda")
print(greeting)

def get_info (name, age):
    return "Linda", 25
name, age = get_info("Linda", 25)
print(f"Name: {name}, Age: {age}")


# 4. Function with parameters and Return Value

def add(a,b):
    return a + b
sum_result = add(1,2)
print(sum_result)


