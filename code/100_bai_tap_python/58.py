L = input("Nhập vào L: ")
L = L.split(",")
L = list(map(int, L))
x = int(input("Nhập vào x: "))
kq = None
for i in L:
    if kq == None or abs(kq-x) < abs(i-x):
        kq = i
print(kq)