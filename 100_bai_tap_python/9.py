import math
a = int(input("a = "))
if math.isqrt(a)*math.isqrt(a) == a:
    print(f"{a} la so chinh phuong")
else:
    print(f"{a} khong la so chinh phuong")