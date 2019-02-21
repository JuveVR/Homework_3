#4.1
l = [20,19,100,1,2,3,4,5,6,7,8,9,10,12]

while len(l) >= 1:
    print(l)
    l.pop(0)



#4.2
s = "0123456789"
ls = list(s)

while len(ls) >= 1:
    print(ls)
    ls.pop(0)

#4.3
new_list = [21,2,3,4,111,1111,98]

new_list_s = sorted(new_list, key=int)
while len(new_list_s) >= 1:
    print(new_list_s)
    new_list_s.pop(0)
