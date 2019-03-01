#First way, using exceptions
value1 = input("Please input first value: ")
value2 = input("Please input second value: ")
try:
    if float(value1) and float(value2):
        print(float(value1) + float(value2))
except ValueError:
    print(value1+value2)

#Second way, that doesn't allow to sum up float numbers
value3 = input("Please input first value: ")
value4 = input("Please input second value: ")


if value3.isdigit() and value4.isdigit():
    print(int(value3) + int(value4))
else:
    print(value3+value4)
