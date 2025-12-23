import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print(f"phuong trinh: {a}^2 + {b}x + {c} = 0")
if a == 0:
    if b == 0:
        if c == 0:
            print("phuong trinh co vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        print("phuong trinh co 1 nghiem", -c/b)
else:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"phuong trinh co 2 nghiem: {x1:.2f}, {x2:.2f}")
    elif delta == 0:
         x = -b / (2 * a)
         print(f"phuong trinh co nghiem duy nhat: {x:.2f}")
    else:
        print("phuong trinh vo nghiem")
