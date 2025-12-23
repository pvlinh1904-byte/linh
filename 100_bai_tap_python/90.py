m = int(input("Nhập vào m: "))

def collatz(n):
    kq = str(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n*3 +1
        kq += "," + str(n)
    return kq 
for i in range(1, m+1):
    print(collatz(i))