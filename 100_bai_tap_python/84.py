def mahoa(L):
    D_mahoa = {}
    L_mahoa = []
    dem = 0
    for i in L:
        if i not in D_mahoa:
            D_mahoa[i] = dem
            dem += 1
        L_mahoa.append(D_mahoa[i])
    print(L_mahoa)

L = ["đen","vàng","xanh","vàng","đỏ","xanh"]
mahoa(L)