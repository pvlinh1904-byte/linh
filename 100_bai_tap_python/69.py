L = input("Nhập vào L: ")
L = L.split(",")
so_min = None
chuoi_max = None
for i in range(len(L)):
    if L[i].isnumeric():
        if so_min == None or so_min < L[i]:
            so_min = L[i]
    else:
        if chuoi_max == None or len(chuoi_max) < len(L[i]):
            chuoi_max = L[i]
print("Giá trị số nhỏ nhất trong List là: ", so_min)
print("Giá trị chuỗi có độ dài lớn nhất là:", chuoi_max)