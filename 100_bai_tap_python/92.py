def phan_ngan(a):
    a = str(a)
    i = len(a) - 3
    while i > 0:
        a = a[:i] + "." + a[i:]
        i -= 3
    return a
a = int(input("a = "))
print(phan_ngan(a))