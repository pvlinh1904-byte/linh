n = int(input("Nhập số nguyên dương n: "))

if n > 0 and (n & (n - 1)) == 0:
    print(f"{n} là lũy thừa của 2.")
else:
    print(f"{n} không phải là lũy thừa của 2.")
