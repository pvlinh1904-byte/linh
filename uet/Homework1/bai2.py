import math
a, b = map(float, input("a, b =").split(", "))
s = a * b
if (a > b):
    dtht = math.pi * ((b/2) ** 2)
else:
    dtht = math.pi * ((a/2) ** 2)
dttc = s - dtht
print(f"diện tích còn lại để trồng cây là {dttc:.2f}")