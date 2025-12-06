n = int(input("n = "))
if n < 0:
    print("nhập sai r ^_^")
else:
    c = 0
    while n > 0:
        b = n % 10
        c += b
        n //= 10
    print(c)