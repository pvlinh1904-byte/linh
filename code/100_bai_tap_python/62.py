L = input("Nhập vào L: ")
L = L.split(",")
L = list(map(int, L))
kq = True
for i in range(len(L) - 1):
    if L[i+1] - L[i] != L[1] - L[0]:
        kq = False
        break
if kq:
    print("Là cấp số cộng với công sai: ", L[1] - L[0])
else:
    print("Không là cấp số cộng!")