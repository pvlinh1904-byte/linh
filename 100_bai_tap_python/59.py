L = input("Nhập vào L: ")
L = L.split(",")
L = list(map(int, L))
tong = 0
dem = 0
for i in L:
    tong = tong + i
    dem = dem + 1
gttb = tong / dem
print(gttb)

tong = 0
for i in L:
    tong += i
print(tong/len(L))