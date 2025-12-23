n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    chan = 0
    le = 0
    temp = n

    while temp > 0:
        digit = temp % 10   # Lấy chữ số cuối
        if digit % 2 == 0:
            chan += 1       # Chữ số chẵn
        else:
            le += 1         # Chữ số lẻ
        temp //= 10         # Bỏ chữ số cuối

    print(f"{n} có {chan} chữ số chẵn và {le} chữ số lẻ.")
