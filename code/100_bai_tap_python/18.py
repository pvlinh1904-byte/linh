a = float(input("a = "))
b = float(input("b = "))
print(f"phuong trinh: {a}x + {b} = 0")
if a == 0:
    if b == 0:
        print("phuong trinh vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else:
    print("nghiem cua phuong trinh la: ", -b/a)