def snt(n):
    for i in range(2, n//2 + 1):
        if n % 2 == 0:
            return False
    if n > 1:
        return True

def asnt(L, a):
    L_kq = []
    for i in L:
        if snt(i):
            L_kq.append(i)
            if len(L_kq) == a:
                return L_kq
    return L_kq
L = list(map(int, input("L = ").split()))
a = int(input("a = "))
print(asnt(L, a))