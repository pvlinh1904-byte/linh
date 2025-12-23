L = input("Nhập vào L: ")
L = L.split(",")
L = list(map(int, L))
kq = -1
for i in range(1, len(L)-1):
    if L[i] == L[i-1] * L[i+1]:
        kq = i
        break
print("Vị trí thỏa mãn yêu cầu là: ", i)