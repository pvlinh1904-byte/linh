a = int(input("nhập vào a: "))
if a > 1:
    dem = 0
    for i in range(1, a+1):
        if a % i == 0:
            dem += 1
    if dem == 2:
        print(a, "là số nguyên tố")
    else:
        print(a, "không là số nguyên tố")

else:
    print(a, "không là số nguyên tố")