def sln(L):
    if len(L) == 0:
        return -1
    
    vt_max = None
    for i in range(len(L)):
        if vt_max == None or L[vt_max] < L[i]:
            vt_max = i
    return vt_max
    
L = input("L = ")
L = L.split()
L = list(map(int, L))
print(sln(L))