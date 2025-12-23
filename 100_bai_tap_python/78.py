def vitrichuoi(L):
    kq = None
    for i in L:
        if kq == None or len(kq) > len(i):
            kq = i
    return kq

L = input("L = ")
L = L.split(",")
print(vitrichuoi(L))