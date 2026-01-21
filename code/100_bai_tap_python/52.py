a = input("Nhập vào chuỗi a: ")
b = input("Nhập vào chuỗi b: ")
vt_dau = 0
vt_cuoi = len(b)
while vt_cuoi <= len(a):
    if a[vt_dau:vt_cuoi] == b:
        a = a[:vt_dau] + a[vt_cuoi:]
    else:
        vt_dau += 1
        vt_cuoi += 1

print(a)
