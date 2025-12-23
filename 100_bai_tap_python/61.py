L  = input("Nhập vào L: ")
L = L.split(",")
L = list(map(int, L))

L.sort()
print(L)

for i in range(len(L)):
    for j in range(i+1, len(L)):
        if L[i] > L[j]:
            L[i],L[j] = L[j],L[i]
print(L)