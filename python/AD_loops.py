cars = ['Ford', 'BMW', 'Volvo','Audi', 'Mercedes', 'Tesla']
for i in cars:
    print(i)
print("\n")

name='Alice'
for i in name:
    print(i)
print("\n")

#for i in range(5, 11):
    #print(i)
    #print ('Hello')

for _ in range(2):
    print("Hello")
print("\n")

for i in range(7):
    if i == 5:
        continue
    if i!=3:
        print(i)
    else:
        print("skipping")
print("\n")

i=0
while i<4:
    print(i)
    i=i+1
print("\n")

i=0
result=True
while result:
    print(i)
    i=i+1
    if i==5:
        result=False
print("\n")

fruits = [["apple", "banana", "cherry"], ["mango", "orange"]]
for fruit in fruits:
    for f in fruit:
        print(f)





print("End of program")
