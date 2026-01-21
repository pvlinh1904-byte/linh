s1 = set()
input1 = input("s1 = ").split(",")

for i in input1:
    i = i.strip()
    if (i.isnumeric()):
        s1.add(int(i))
    elif(i.isdecimal()):
        s1.add(float(i))
    else:
        s1.add(i)

s2 = set()
input2 = input("s2 = ").split(",")

for i in input2:
    i = i.strip()
    if (i.isnumeric()):
        s2.add(int(i))
    elif(i.isdecimal()):
        s2.add(float(i))
    else:
        s2.add(i)

s = s1.copy()
s = s.intersection(s2)

rs = set()
for i in s:
    if(not isinstance(i, str)):
        rs.add(i)

print(rs)