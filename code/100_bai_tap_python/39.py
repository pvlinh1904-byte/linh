n = int(input("Nhập vào n: "))

demchan = 0
demle  = 0
while n != 0:
    a = n % 10
    n = n // 10
    if a % 2 == 0:
        demchan += 1
    else:
        demle += 1

print("Số lượng chữ số chẵn", demchan)
print("Số lượng chữ số lẻ", demle)