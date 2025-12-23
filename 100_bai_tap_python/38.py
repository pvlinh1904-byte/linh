n = int(input("Nhập số nguyên dương n: "))
n = str(n)
#print(len(n))

k = 10
dem = 1
while n >= k:
    k *= 10
    dem += 1
print(dem)

dem = 0
while n != 0:
    n  = n // 10
    dem += 1
print(dem)