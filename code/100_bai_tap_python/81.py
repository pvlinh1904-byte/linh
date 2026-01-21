def giatrilonthua(L, a):
    for i in range(a):
        vt_max = None
        for j in range(len(L)):
            if L[j] != None:
                if vt_max == None or L[vt_max] < L[j]:
                    vt_max = j
        if i == a - 1:
            return L[vt_max]
        else:
            L[vt_max] = None

L = list(map(int, input("L = ").split()))
a = int(input("a = "))
print(giatrilonthua(L, a))