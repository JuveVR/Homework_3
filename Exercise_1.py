message = input("Enter any string with length more then 2 symbols: ")
try:
    print(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, sep="\n")
except Exception:
    print("String length error! Your string must consist of more then 2 symbols")


s1 = message[2]
s2 = message[-2]
s3 = message[0:5]
s4 = message[0:-2]
s5 = message[0::2]
s6 = message[1::2]
s7 = message[::-1]
s8 = message[-1::-2]
s9 = message[-2:0:-1]
s10 = len(message)

