chuoi = input("Nhập vào chuỗi: ")
demhoa = demthuong = demso = 0
for i in chuoi:
    if i.isupper():
        demhoa += 1
    elif i.islower():
        demthuong += 1
    elif i.isnumeric():
        demso += 1
print("Số ký tự in hoa là: ", demhoa)
print("Số ký tự in thường là: ", demthuong)
print("Số ký tự số là: ", demso)