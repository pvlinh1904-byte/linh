m = float(input("Nhập số m: "))
n = float(input("Nhập số n (khác 0): "))

if n == 0:
    print("Không thể chia cho 0!")
else:
    # Chia và làm tròn xuống
    ketqua = m // n
    print(f"Kết quả {m} chia {n} làm tròn xuống là: {ketqua}")
