s = """We are not what we should be! 
We are not what we need to be.
But at least we are not what we used to be
(Football Coach)"""
s1 = s.split()
print(len(s.split()))

s2 = []
for i in s1:
    s2.append(i.strip('!.()'))

print(s2)

#print(s2.sort()) This function returns None, can't understand why
print(sorted(s2))

