def listklan(L, k):
    L_kq = []
    for i in L:
        if L.count(i) > k:
            if i not in L_kq:
                L_kq.append(i)
    L_kq.sort()
    return L_kq

L = list(map(int, input("L = ").split()))
k = int(input("k = "))
print(listklan(L, k))