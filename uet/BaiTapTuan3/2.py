a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

print("Trước khi hoán đổi: a =", a, ", b =", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("Sau khi hoán đổi: a =", a, ", b =", b)
