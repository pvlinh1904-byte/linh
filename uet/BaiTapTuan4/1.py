n = int(input("Nhập n (n <= 1000): "))

if n < 1 or n > 1000:
    print("Vui lòng nhập n hợp lệ (1 <= n <= 1000)!")
else:
    tong = 0
    i = 1
    while i <= n:
        tong += i
        i += 1

    print(f"Tổng các số nguyên từ 1 đến {n} là: {tong}")
