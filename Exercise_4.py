#4.1
l = [20,19,100,1,2,3,4,5,6,7,8,9,10,12]

while l is True:
    l.pop(0)
    print(l)

#4.2
s = "0123456789"
ls = list(s)

while len(ls) >= 1:
    print(ls)
    ls.pop(0)

#first way with string
s = "0123456789"
ind = len(s)
while ind  >= 1:
  if ind == len(s):
    print(s)
    ind -= 1
  else:
    print(s.replace(s[ind:], " "))
    ind -= 1

#Second way with string
s = "0123456789"
ind = len(s)-1

print(s)
while ind  >= 1:
    print(s.replace(s[ind:], " "))
    ind -= 1


#4.3
new_list = [21,2,3,4,111,1111,98]

new_list_s = sorted(new_list)
while len(new_list_s) >= 1:
    print(new_list_s)
    new_list_s.pop(0)

#solution with min() func
new_list = [21,2,3,4,111,1111,98]

while len(new_list) >= 1:
    print(sorted(new_list))
    new_list.remove(min(new_list))

