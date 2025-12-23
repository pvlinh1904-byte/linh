def trungbinh(L, a):
    tong = 0
    for i in range(0, a):
        tong += L[i]
    return tong/a
L = list(map(int, input("L = ").split()))
a = int(input("a = "))
print(trungbinh(L, a))