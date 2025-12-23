def xoa_nho_hon_x(L, x):
    i = 0
    while i < len(L):
        if L[i] < x:
            L.pop(i)
        else:
            i += 1
    return L
L = list(map(int, input("L = ").split()))
x = int(input("x = "))
print(xoa_nho_hon_x(L, x))