L = input("Nhập vào L: ")
L = L.split()
L = list(map(int, L))
vt_max = None
vt_min = None
for i in range(len(L)):
    if vt_max == None or L[vt_max] < L[i]:
        vt_max = i
    if vt_min == None or L[vt_min] > L[i]:
        vt_min = i
L[vt_max], L[vt_min] = L[vt_min], L[vt_max]
print(L)