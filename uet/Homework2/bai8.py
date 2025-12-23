# Giải hệ:
# a*x + b*y = m
# c*x + d*y = n

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
d = float(input("Nhập d: "))
m = float(input("Nhập m: "))
n = float(input("Nhập n: "))

# Định thức
D = a * d - b * c

if D != 0:
    x = (m * d - b * n) / D
    y = (a * n - m * c) / D
    print("Hệ có nghiệm duy nhất:")
    print("x =", x)
    print("y =", y)

else:
    # Kiểm tra vô số nghiệm hoặc vô nghiệm
    if a*n == m*c and b*n == m*d:
        print("Hệ có vô số nghiệm.")
    else:
        print("Hệ vô nghiệm.")
