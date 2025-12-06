def tinh_tong_tich(a, b):
    tong = a + b
    tich = a * b
    return tong, tich
a, b = map(int, input("a, b = ").split(", "))
tong, tich = tinh_tong_tich(a, b)
print(tong, tich)