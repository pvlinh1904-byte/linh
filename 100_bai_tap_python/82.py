def timkeymax(D):
    kq = None
    for i in D:
        if kq == None or D[kq] < D[i]:
            kq = i
    return kq
D = {"hello":10,"linh":15,"anh":20}
print(timkeymax(D))