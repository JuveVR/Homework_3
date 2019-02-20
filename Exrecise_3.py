#3.1
x = 0
while x in range(11):
    print(x)
    x +=1

#3.2
y = 20
while y in range(20,0,-1):
    print(y, end=" ")
    y -= 1
print()

#3.3
number = 15
dev = 0
while number % 2 == 0:
    number /= 2
    print(number)
    dev +=1
print(dev)