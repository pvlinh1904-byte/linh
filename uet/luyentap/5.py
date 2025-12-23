def tong(n):
    a = 0
    while n > 0:
        a += n % 10
        n //= 10
    return a
n = int(input("n = "))
b = tong(n)
print(b)