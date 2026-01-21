n = int(input("Nhập vào n: "))
n0 = n
while n % 2 == 0:
    n = n / 2
if n == 1:
    print(n0, "là số dạng 2^k")
else:
    print(n0, "không là số dạng 2^k")