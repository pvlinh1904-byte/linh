import math
rs = True
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        rs = False
        break
while True:
    n = int(input("n = "))
    if n > 0:
        print("hợp lệ")
    else:
        print("nhập lại")
    if rs == True:
        print("là sô nguyên tố")
    else:
        print("không là số nguyên tố")