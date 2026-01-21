def hoandoi_D(D):
    D_kq = {}
    for i in D:
        if D[i] not in D_kq:
            D_kq[D[i]] = i
        else:
            return None
    return D_kq

D = {"Tiếng Anh":"hello","Tiếng Việt":"Xin chào","Tiếng Việt":"chào"}
print(hoandoi_D(D))