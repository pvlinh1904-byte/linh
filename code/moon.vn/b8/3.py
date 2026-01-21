s = input("s = ")
d = dict()

for c in s:
    if(c in d.keys()):
        continue
    k = s.count(c)
    d[c] = k
    
print(d)