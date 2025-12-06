import math
n = int(input("n = "))
if (n <= 1):
    print("nhập sai ròiiiii ^_^")
else:
    count = 0
    for i in range (2, n + 1):
        rs = True  
        for j in range (2, int(math.sqrt(i)) + 1 ): 
            if (i % j == 0):
                rs = False
                break
        if (rs == True):
            count = count + 1
    print(f"có {count} số nguyên tố trong [1, {n}]")

