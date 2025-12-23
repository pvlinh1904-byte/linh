L = input("Nhập vào L:")
L = L.split(",")
L = list(map(int, L))
kq = True
for i in range(1, len(L) - 1):
    if not(L[i-1] < L[i] > L[i+1] or L[i-1] > L[i] < L[i+1]):
        kq = False
        break
print(kq)