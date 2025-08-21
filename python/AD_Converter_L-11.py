print('Hello! Convert miles to km or km to miles')
while True:
    type_of_calc=input('Enter "m" for miles to km \n'
                       'enter "k" for km to miles \n'
                       'enter "q" to quit: ')

    if type_of_calc=='m':
        answer=float(input("Enter a number of miles: "))
        print(f'{answer} miles is {answer*1.609} km')
    elif type_of_calc=='k':
        answer=float(input("Enter a number of km: "))
        print(f'{answer} km is {answer*0.621371} miles')
    elif type_of_calc=='q':
        print('Goodbye\n')
        break
    else:
        print('Invalid input')



print('Hello! Convert Celsius to Fahrenheit or Fahrenheit to Celsius')
while True:
    type_of_calc = input('Enter "c" for Celsius to Fahrenheit \n'
                         'enter "f" for Fahrenheit to Celsius \n'
                         'enter "q" to quit: ')
    if type_of_calc == 'c':
        answer = float(input("Enter Celsius degrees: "))
        print(f'{answer} Celsius degrees = {answer * 1.8 + 32} Fahrenheit degrees')
    elif type_of_calc == 'f':
        answer = float(input("Enter Fahrenheit degrees: "))
        print(f'{answer} Fahrenheit degrees = {(answer - 32) * 5 / 9} Celsius degrees')
    elif type_of_calc == 'q':
        print('Goodbye\n')
        break
    else:
        print('Invalid input')



print('Hello! Welcome to calculator\n'
      'Enter "+" for Addition \n'
      'enter "-" for Subtraction \n'
      'enter "*" for Multiplication \n'
      'enter "/" for Division \n'
      'enter "e" for Exponent \n'
      'enter "p" for Percentage (a/b*100)\n'
      'enter "ac" for All clear \n'
      'enter "q" to quit: ')
a = float(input('Enter a: '))

while True:
    type_of_calc = input('Enter function \n')
    if type_of_calc == 'ac':
        print('All clear')
        a = float(input('Enter a: '))
        type_of_calc = input('Enter function \n')

    if type_of_calc == '+':
        b = float(input('Enter b: '))
        def sum(a, b):
            return a + b
        a=sum(a, b)
        print(f'Summary = {a}\n')

    elif type_of_calc == '-':
        b = float(input('Enter b: '))
        def minus(a, b):
            return a - b
        a=minus(a, b)
        print(f'Subtraction = {a}\n')
    elif type_of_calc == '*':
        b = float(input('Enter b: '))
        def multiply(a, b):
            return a * b
        a=multiply(a,b)
        print(f'Multiplication = {a}\n')
    elif type_of_calc == '/':
        b = float(input('Enter b: '))
        def divide(a, b):
            return a / b
        a=divide(a, b)
        print(f'Division = {a}\n')
    elif type_of_calc == 'e':
        b=float(input('Enter b: '))
        a={a ** b}
        print(f'Exponentiation = {a} \n')
    elif type_of_calc == 'p':
        b=float(input('Enter b: '))
        a={a/b*100}
        print(f'Percentage (a/b*100)= {a}\n')
    elif type_of_calc == 'q':
        print('Goodbye')
        break
    else:
        print('Invalid input')