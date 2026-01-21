a , b = map(float,input("a, b = ").split())
if (a == b == 0):
    print("Phương trình có vô số nghiệm")
elif a != 0:
    x = -b/a
    print(f"Phương trình có 1 nghiệm x = {x}")
else:
    print("Phương trình vô nghiệm")