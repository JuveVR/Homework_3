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


print(part2+part1)
