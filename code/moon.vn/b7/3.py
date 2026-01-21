s = input("nhập dãy số: ")
if (s != ""):
    l = list(map(int, s.split(",")))
else:
    l = list()
t = 0
for n in l:
    t = t + n
print(t)