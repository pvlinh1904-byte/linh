L = input("Nhập vào L: ")
L = L.split(",")
chuoi_kq = None
vt_max = None
for i in L:
    kq = -1
    for j in range(len(i)):
        if i[j].isupper():
            kq = j
    if chuoi_kq == None or vt_max < kq:
        chuoi_kq = i
        vt_max = kq

print(chuoi_kq)