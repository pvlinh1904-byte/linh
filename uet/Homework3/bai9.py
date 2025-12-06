import math
a = int(input("a = "))
if a < 1:
    print("nhập sai dữ liệu r ^_^")
else:
    sqrt_a = math.isqrt(a)
    if sqrt_a * sqrt_a == a:
        print(f"{a} là số chính phương")
    else:
        print(f"{a} không là số chính phương")