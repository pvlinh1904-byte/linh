a = int(input("a = "))
tong = 0
for i in range(1, a):
    if a % i == 0:
        tong = tong + i
if tong == a:
    print(f"{a} là số hoàn hảo")
else:
    print(f"{a} không là số hoàn hảo")