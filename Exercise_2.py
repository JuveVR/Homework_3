message = input("Enter any string: ")
length = len(message)

if length % 2 == 0:
    mediana = length/2
    part1 = message[0:int(mediana)]
    part2 = message[int(mediana):]


elif length % 2 != 0:
    mediana = length / 2 + 1
    part1 = message[0:int(mediana)]
    part2 = message[int(mediana):]

s = part2+part1
print(s)

#Easy way
message = input("Enter any string: ")
length = len(message)

part1 = message[:len(message)/2]
part2 = message[len(message)/2:]

s = part2+part1

print(s)
