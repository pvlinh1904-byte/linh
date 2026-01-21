def armstrong(a):
    sochuso = len(str(a))
    tong = 0
    a0 = a
    while a != 0:
        b = a % 10
        a = a // 10
        tong += b ** sochuso
    if tong == a0:
        return True
    return False

a = int(input("a = "))
print(armstrong(a))