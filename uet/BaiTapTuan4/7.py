import math
n = int(input("n = "))
if n < 2:
    print("nhập sai r")
else:
    for i in range(n, 1, -1):
        rs = True
        for j in range(2, int(math.sqrt(n))+1):
            if i % j == 0:
                rs = False
                break
        if rs == True:
            break
    print(i)

