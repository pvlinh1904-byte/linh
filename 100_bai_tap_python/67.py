L = input("Nhập vào L: ")
L = L.split()
L = list(map(int, L))
L_chan = []
L_le = []
L_khong = []
for i in L:
    if i == 0:
        L_khong.append(i)
    elif i % 2 == 0:
        L_chan.append(i)
    else:
        L_le.append(i)
L_kq = L_chan + L_khong + L_le
print(L_kq)