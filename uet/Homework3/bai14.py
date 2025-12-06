# Khởi tạo biến max và min là None để nhận giá trị đầu tiên nhập vào
max_val = None
min_val = None

while True:
    n = int(input("Nhập số nguyên (nhập -1 để dừng): "))

    if n == -1:
        break

    # Nếu là số đầu tiên
    if max_val is None or min_val is None:
        max_val = n
        min_val = n
    else:
        # Cập nhật max và min
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n

# Sau khi kết thúc nhập
if max_val is None:
    print("Không có số nào được nhập!")
else:
    print("Số lớn nhất:", max_val)
    print("Số nhỏ nhất:", min_val)
