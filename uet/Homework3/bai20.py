n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    dem = 0
    temp = n

    while temp > 0:
        digit = temp % 10   # Lấy chữ số cuối

        # Kiểm tra chữ số nguyên tố
        if digit in (2, 3, 5, 7):
            dem += 1

        temp //= 10         # Bỏ chữ số cuối

    print(f"{n} có {dem} chữ số là số nguyên tố.")
