L = input("Nhập vào L: ")
L = L.split(",")
max = None
kq_vt = None
for i in range(len(L)):
    x = L[i].count(" ") + 1
    if max == None or max < i:
        max = i
        kq_vt = i
print(kq_vt)