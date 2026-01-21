a = int(input("Nhập vào số nguyên: "))
a = str(a)
i = len(a) - 3
while i > 0:
    a = a[:i] + "." + a[i:]
    i -= 3
print(a)