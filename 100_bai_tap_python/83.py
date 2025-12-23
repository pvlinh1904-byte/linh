def giatrikeydainhat(D):
    kq = None
    for i in D:
        if kq == None or len(i) > len(kq):
            kq = i
    return D[kq]
D = {"xin chao":1,"linh":2,"ngoc anh cute":3}
print(giatrikeydainhat(D))