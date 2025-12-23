L = input("Nhập vào L: ")
L = L.split(",")
L = list(map(int, L))
kq = True
for i in range(len(L)-1):
    if L[i] > L[i+1]:
        kq = False
        break
if kq:
    print("True")
else:
    print("False")