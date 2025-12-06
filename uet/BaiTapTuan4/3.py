while True:
    n = int(input("n = "))
    if 0 < n < 100:
        break
    else:
        print("nhập lại")
i = 1
tich = 1

while i <= n:
    tich = tich * i
    i = i + 1
print(tich)