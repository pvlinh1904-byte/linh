# số nguyên tố: là số chia hết cho 1 và chính nó
# 1 không phải số nguyên tố
# mặc định n là số nguyên tố
# nếu tìm ước [2, n-1] mà n chia hết thì không phải sô nguyên tố
# 1 số nguyên n chỉ chia hết tối đa cho căn bậc 2 của chính nó
import math
n = int(input("n = "))
if (n < 1):
    print("Không hợp lệ")
elif (n == 1):
    print("1 không là số nguyên tố")
else:
    cb2 = int(math.sqrt(n))
    rs = True
    for i in range (2, cb2 + 1):
        if (n % i == 0):
            rs = False
            break
    if (rs == True):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải số nguyên tố")