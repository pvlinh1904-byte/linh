def vt_cantim(L, k):
    
    for i in range(len(L)):
        if L[i] == k:
            return i
    return -1
L = input("L = ")
L = L.split()
L = list(map(int, L))
k = int(input("k = "))
print(vt_cantim(L, k))