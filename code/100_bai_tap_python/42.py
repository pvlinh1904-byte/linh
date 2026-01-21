A = int(input("Nhập vào A: "))
a = 1
b = 1
c = a + b
while c <= A:
    a = b
    b = c
    c = a + b
print(b)