def giai_thua(n):
    if(n < 0):
        return -1
    t = 1
    for i in range(1, n + 1):
            t = t * i
    return t
n = int(input("nhập n = "))
print(giai_thua(n))