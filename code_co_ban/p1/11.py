def tim_hai_chu_so_dau_va_cuoi(so):
    chuoi_so = str(so)
    hai_dau = int(chuoi_so[2:])
    hai_cuoi = so % 100
    return hai_dau, hai_cuoi
so = int(input("so = "))
dau, cuoi = tim_hai_chu_so_dau_va_cuoi(so)
print(dau, cuoi)