def trung_binh_cong(a, b, c):
    return (a + b + c)/3
a, b, c = map(int, input("a, b, c =").split(", "))
tbc = trung_binh_cong(a, b, c)
print(tbc)