n = int(input("n = "))
if (n >= 1):
    t = 0
    for i in range (1, n + 1):
        if (i % 2 == 0):
            t = t + i
    print(t)
else:
    print("Không hợp lệ")