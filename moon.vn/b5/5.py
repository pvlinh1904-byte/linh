import math
a =float(input("a = "))
b =float(input("b = "))
c =float(input("c = "))
if (a == b == c == 0):
    print("Phương trình có vô số nghiệm")
elif (a != 0):
    delta = (b**2) - 4*a*c
    print(f"giải phương trình {a}x^2 + {b}x + {c} = 0 ")
    if (delta > 0):
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có 2 nghiệm: x1 = {x1}, X2 = {x2}")
    elif (delta == 0):
        x = -b/(2*a)
        print(f"Phương trình có nghiệm kép: x1 = x2 = {x}")
    else:
        print("Phương trình vô nghiệm")
else:
    print("Không phải phương trình bậc 2")