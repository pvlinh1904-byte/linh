import math
a, b = map(int, input("a, b = ").split(", "))
if a > b:
    print("không hợp lệ")
else:
    tong = 0
    for i in range(a, b+1):
        rs = True
        for j in range(2, int(math.sqrt(b)+1)):
            if i % j == 0:
                rs = False
                break
        if (rs == True):
            tong = tong + i
    print(tong)
