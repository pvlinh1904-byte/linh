chuoi = input("Nhập vào chuỗi: ")
chuoitam = ""
tong = 0
for i in chuoi:
    if i.isnumeric():
        chuoitam += i
    else:
        if chuoitam != "" :
            tong += int(chuoitam)
            chuoitam = ""
if chuoitam != "":
    tong += int(chuoitam)
print(tong)