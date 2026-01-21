chuoi = input("Nhập vào chuỗi: ")
tong = 0

for i in chuoi:
    if i.isnumeric():
        tong += int(i)
print(tong)
