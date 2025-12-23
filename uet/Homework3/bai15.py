n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    count = 0
    temp = n
    while temp > 0:
        temp //= 10     # Bỏ chữ số cuối
        count += 1

    print(f"{n} có {count} chữ số.")
